import os
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from music.models import Lab, Generation
from music.forms import LabForm

from utils.midi import save_midi_file, parse_midi_file
from utils.algorithms import (
    fitness,
    initialize_population,
    mutate,
    one_point_crossover,
    two_point_crossover,
    roulette_wheel_selection
)


class LabCreateView(CreateView):
    model = Lab
    form_class = LabForm
    template_name = 'music/lab_form.html'

    def form_valid(self, form):
        lab = form.save()

        if self.request.user.is_authenticated:
            lab.user = self.request.user
            lab.save()

        directory = self.create_unique_directory(lab.id)

        best_sequence, best_fitness, generation_data, target_sequence = self.run_genetic_algorithm(
            lab.population_size,
            lab.target_sequence.path,
            lab.num_generations,
            lab.mutation_rate,
            directory,
        )

        lab.best_fitness = best_fitness
        lab.best_note.name = os.path.join(directory[6:], 'final_best.mid')
        lab.best_sequence_list = best_sequence
        lab.target_sequence_list = target_sequence
        lab.save()

        for gen_number, gen_data in generation_data.items():
            Generation.objects.create(
                lab=lab,
                number=gen_number,
                best_fitness=gen_data['fitness'],
                best_note=gen_data['file_path'][6:],
                best_sequence=gen_data['best_sequence'],
            )

        return super().form_valid(form)

    def create_unique_directory(self, lab_id):
        """Creates a unique directory for storing files for a specific lab."""
        dir_name = f"media/note/lab_{lab_id}_{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"
        os.makedirs(dir_name, exist_ok=True)
        return dir_name

    def run_genetic_algorithm(self, population_size, target_sequence_path, num_generations, mutation_rate, directory):
        """Runs the genetic algorithm and saves results to disk."""
        target_sequence = parse_midi_file(target_sequence_path)

        population = initialize_population(population_size, target_sequence)

        generation_data = {}
        for generation in range(num_generations):
            fitnesses = [fitness(seq, target_sequence) for seq in population]

            best_sequence = population[fitnesses.index(min(fitnesses))]
            best_fitness = min(fitnesses)

            file_path = os.path.join(directory, f"gen_{generation + 1}.mid")
            save_midi_file(best_sequence, file_path)

            generation_data[generation + 1] = {
                'fitness': best_fitness,
                'file_path': file_path,
                'best_sequence': best_sequence,
            }

            next_generation = []
            for _ in range(population_size // 2):
                parent1, parent2 = roulette_wheel_selection(population, fitnesses)
                child1 = one_point_crossover(parent1, parent2)
                child2 = two_point_crossover(parent1, parent2)
                next_generation.append(mutate(child1, mutation_rate))
                next_generation.append(mutate(child2, mutation_rate))

            population = next_generation

        fitnesses = [fitness(seq, target_sequence) for seq in population]
        best_sequence = population[fitnesses.index(min(fitnesses))]
        best_fitness = min(fitnesses)
        final_file_path = os.path.join(directory, 'final_best.mid')
        save_midi_file(best_sequence, final_file_path)

        return best_sequence, best_fitness, generation_data, target_sequence

    def get_success_url(self):
        return reverse_lazy('music:detail', kwargs={'pk': self.object.pk})


class LabDetailView(DetailView):
    model = Lab
    template_name = 'music/lab_detail.html'
    context_object_name = 'lab'


class LabHistoryView(LoginRequiredMixin, ListView):
    model = Lab
    template_name = 'music/history.html'
    context_object_name = 'labs'
    paginate_by = 5

    def get_queryset(self):
        return Lab.objects.filter(user=self.request.user).order_by('-created_at')
