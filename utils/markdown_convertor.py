import requests
from bs4 import BeautifulSoup
import re

def medium_to_markdown(url):
    # Send a GET request to the Medium article
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the article title
    title = soup.find('h1').text.strip()

    # Extract the article content
    content = soup.find('article').find("section")

    allowed_to_go = False

    # Extract text content and structure
    markdown_content = f"# {title}\n\n"
    for element in content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'pre', 'blockquote']):
        if element.text.strip().lower() != "share" and not allowed_to_go:
            continue
        else:
            allowed_to_go = True
            if element.text.strip().lower() == "share":
                continue
        if element.name.startswith('h'):
            level = int(element.name[1])
            markdown_content += '#' * level + ' ' + element.text.strip() + '\n\n'
        elif element.name == 'p':
            markdown_content += element.text.strip() + '\n\n'
        elif element.name == 'pre':
            markdown_content += '```\n' + element.text.strip() + '\n```\n\n'
        elif element.name == 'blockquote':
            markdown_content += '> ' + element.text.strip() + '\n\n'

    # Clean up extra whitespace
    markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content).strip()

    return markdown_content

# Example usage
url = "https://medium.com/@heshanhfernando/pii-masking-with-python-using-ai4privacy-12279bf7312a"
result = medium_to_markdown(url)
print(result)