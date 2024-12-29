from mido import MidiFile, MidiTrack, Message

def save_midi_file(midi_notes, output_file="output.mid", duration=1):
    """
    Saves a MIDI file with the given MIDI notes.

    Parameters:
    - midi_notes: List of MIDI note numbers (e.g., [60, 61, 62]).
    - output_file: Name of the output MIDI file.
    - duration: Duration of each note in seconds.
    """
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    for note in midi_notes:
        track.append(Message('note_on', note=note, velocity=64, time=0))
        track.append(Message('note_off', note=note, velocity=64, time=int(duration * 480)))

    mid.save(output_file)

def parse_midi_file(file_path):
    try:
        midi = MidiFile(file_path)
        notes = []
        for track in midi.tracks:
            for msg in track:
                if msg.type == 'note_on' and msg.velocity > 0:
                    notes.append(msg.note)
        return notes

    except Exception as e:
        print(f"Error reading MIDI file: {e}")

    return None
