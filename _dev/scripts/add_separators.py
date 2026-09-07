import re
from bs4 import BeautifulSoup

with open('my-shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find all the wrappers we added. They have a specific style string.
wrappers = soup.find_all('div', style=lambda value: value and 'border-top: 1px solid' in value)

for wrapper in wrappers:
    # Update style to remove the border-top
    wrapper['style'] = "margin-top: 20px;"
    
    # Create the prominent gradient separator
    separator_html = """
    <div class="service-separator" style="height: 2px; background: linear-gradient(90deg, rgba(0, 123, 255, 0), rgba(0, 123, 255, 1), rgba(0, 123, 255, 0)); margin: 100px 0; opacity: 0.6; box-shadow: 0 0 10px rgba(0, 123, 255, 0.5);"></div>
    """
    separator = BeautifulSoup(separator_html, 'html.parser')
    
    # Insert separator before the wrapper
    wrapper.insert_before(separator)

with open('my-shop.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Separators added!")
