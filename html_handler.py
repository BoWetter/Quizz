def create_html():
    with open('templates/index.html', 'w') as file:
        file.write('<html><head><title>Drakar och Demoner Spel</title></head><body>')
        file.write('<h1>Drakar och Demoner</h1>')
        file.write('</body></html>')

def update_html(content):
    with open('templates/index.html', 'r') as file:
        html_content = file.read()

    # Assume there is a marked section in the HTML for content updates
    updated_content = html_content.replace("<!-- CONTENT_PLACEHOLDER -->", content)

    with open('templates/index.html', 'w') as file:
        file.write(updated_content)
