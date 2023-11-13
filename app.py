from flask import Flask, request, render_template
import story  # Fortsätt att importera story-modulen
from story_handler import read_latest_story  # Importera den nya funktionen
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    story_text = ""
    chosen_adventure = ""  # För att hålla den genererade berättelsen
    if request.method == 'POST':
        chosen_adventure = request.form['adventure']
        save_choice(chosen_adventure)
        # Kör story.py's huvudprocess efter att valet har sparats
        story.main()

         # Läs in den senaste berättelsen
        story_text = read_latest_story()

        # Efter att story.py har körts, kan du till exempel hämta den genererade texten
        # och skicka den tillbaka till din webbsida, om så önskas.
    return render_template('index.html', choice=chosen_adventure, story=story_text, background_image='background_image.png')

def save_choice(adventure_id):
    with open('adventure.txt', 'w') as file:
        file.write(adventure_id)

# Test function to create a file when the app runs
def create_test_file():
    with open('test_file.txt', 'w') as file:
        file.write('Test file created')

create_test_file()

if __name__ == '__main__':
    app.run(debug=True)
