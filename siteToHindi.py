from yandex_tracker_client import TrackerClient
from bs4 import BeautifulSoup
import os
import requests
import fnmatch


API_KEY = 'xxxxxxxxx'
API_URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


CARPETA_ORIGEN = 'C:\\Users\\Downloads\\websites\\www.classcentral.com1'

def translate_text(text, target_lang='hi'):
    """
    Translates the given text to the target language using Yandex API.
    Returns the translated text.
    """
   
    response = requests.get(API_URL, params={
        'key': API_KEY,
        'text': text,
        'lang': target_lang
    })
    
    if response.status_code == 200:
        translated_text = response.json()['text'][0]
        return translated_text
    else:
        return f"Error: {response.status_code}"


def toTheSoup(file):
    """
    Read the HTML file, parser it with Beautifulsoup finding visible text and translate it
    """
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Parser the HTML with Beautifulsoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # find all visible text and translate it
    for tag in soup.find_all(text=True):
        if tag.parent.name not in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            # exclude certain elements that should not be translated
            if tag.strip() != "":
                translated_text = translate_text(tag)
                tag.replace_with(translated_text)
            

    # Save the HTML translated
    new_file_name = os.path.splitext(file)[0] + '_new.html'
    print(new_file_name)
    with open(new_file_name, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    # Delete the original HTML file and replace it with the new one
    if os.path.exists(file):
        os.remove(file)
    os.rename(new_file_name, file)


def find_html_files(folder_path):
    """
    Finds all HTML files in the given folder and its subfolders.
    Returns a list of file paths.
    """
    html_files = []
    for root, dirs, files in os.walk(folder_path):
        for filename in fnmatch.filter(files, '*.html'):
            file_path = os.path.join(root, filename)
            html_files.append(file_path)
    return html_files

# main

# Go to the folder with the web mirror
os.chdir(CARPETA_ORIGEN)

file_count = 0

html_files = find_html_files(CARPETA_ORIGEN)

for HtmlFile in html_files:
    print(f'Working on: {HtmlFile}')
    file_count += 1
    toTheSoup(HtmlFile)
    

print(f'========================= D O N E [Files: {file_count}]===============================')