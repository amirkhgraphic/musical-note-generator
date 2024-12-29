from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

User = get_user_model()


class Lab(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='labs')
    target_sequence = models.FileField(upload_to='note/target/', blank=True)
    population_size = models.IntegerField(
        validators=[
            MinValueValidator(10),
        ],
    )
    num_generations = models.IntegerField(
        validators=[
            MinValueValidator(1),
        ],
    )
    mutation_rate = models.FloatField(
        validators=[
            MinValueValidator(0.01),
            MaxValueValidator(0.1),
        ],
    )
    best_note = models.FileField(upload_to='note/')
    best_fitness = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Generation(models.Model):
    best_note = models.FileField(upload_to='note/')
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name='generations')
    number = models.IntegerField(
        validators=[
            MinValueValidator(1),
        ],
    )
    best_fitness = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['lab', 'number'], name='unique_lab_number')
        ]
