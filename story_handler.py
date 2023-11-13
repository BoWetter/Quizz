def read_latest_story():
    try:
        with open('latest_story.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Ingen ny berättelse hittades."
