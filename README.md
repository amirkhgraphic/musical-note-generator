# MIDI Genetic Algorithm Lab

This Django-based project uses a genetic algorithm to generate optimized MIDI note sequences. Users can create labs to explore the algorithm's performance and view the history of their labs and generations.

---

## Features

- **User Authentication**:
  - Login, signup, and password reset functionalities.

- **Lab Management**:
  - Create labs by uploading MIDI files or entering note sequences directly.
  - View lab details, including the best note sequence and generations.

- **Generations**:
  - Track the progress of the genetic algorithm across generations.
  - View playable MIDI files for target sequences, best sequences, and each generation's best sequence.

- **Admin Panel**:
  - Manage users, labs, and generations with a fully customized admin interface.

---

## Requirements

- Python 3.8+
- Django 4.0+
- MIDI.js (for playing MIDI files in the browser)
- SQLite (default, but configurable)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/amirkhgraphic/musical-note-generator
   cd musical-note-generator
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Visit `http://127.0.0.1:8000` in your browser.

---

## Usage

### Create a Lab
1. Log in or sign up.
2. Go to the "Create Lab" page.
3. Upload a MIDI file or enter a comma-separated list of MIDI notes.
4. Configure the population size, number of generations, and mutation rate.
5. Submit the form to start the genetic algorithm.

### View Labs
- Access the "Lab History" page to view a list of labs you've created.
- Click on a lab to see its details, including target and best sequences and playable MIDI files for each generation.

---

## Development

### Email Backend
For development purposes, emails are displayed in the console. Configure the email backend in `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

### Admin Panel
Access the admin panel at `http://127.0.0.1:8000/admin` to manage users, labs, and generations.

---

## Customization

### Settings
Modify `settings.py` to configure:
- Database (default is SQLite)
- Static and media files
- Email backend for production

### Genetic Algorithm
The genetic algorithm implementation can be found in the `algorithms/` module. Key features include:
- Fitness calculation
- Population initialization
- One-point and two-point crossover
- Mutation

---

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for suggestions or bug reports.

---

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

## Acknowledgments

- **[MIDI.js](https://github.com/mudcube/MIDI.js)**: For enabling MIDI playback in the browser.
- **Django Documentation**: For the framework and guidance.