import os
import uuid

from django import forms
from django.core.exceptions import ValidationError

from utils.midi import save_midi_file
from .models import Lab


class LabForm(forms.ModelForm):
    target_sequence_list = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter a comma-separated list of MIDI notes (e.g., 60, 62, 64, 65, 67)',
            'class': 'form-control',
            'rows': 3,
        }),
        required=False,
        help_text='You can upload a MIDI file or enter a sequence of MIDI notes.',
    )

    class Meta:
        model = Lab
        fields = ['target_sequence', 'target_sequence_list', 'population_size', 'num_generations', 'mutation_rate']
        widgets = {
            'mutation_rate': forms.NumberInput(attrs={'step': '0.01'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        target_sequence = cleaned_data.get('target_sequence')
        target_sequence_list = cleaned_data.get('target_sequence_list')

        if not target_sequence and not target_sequence_list:
            raise ValidationError("You must provide either a MIDI file or a sequence of notes.")

        if target_sequence_list:
            try:
                notes = [int(n.strip()) for n in target_sequence_list.split(',')]
                if any(note < 0 or note > 127 for note in notes):
                    raise ValueError("MIDI notes must be between 0 and 127.")

                os.makedirs('media/generated', exist_ok=True)
                uuid_part = str(uuid.uuid4())[:8]
                save_midi_file(notes, os.path.join('media/generated', f'target_{uuid_part}.mid'))
                cleaned_data['target_sequence'] = os.path.join('generated', f'target_{uuid_part}.mid')

            except ValueError as e:
                raise ValidationError(f"Invalid note list: {str(e)}")

        return cleaned_data
