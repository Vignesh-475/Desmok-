import os
from bs4 import BeautifulSoup

directory = r'd:\ZM\amoxi-html-package\amoxi-html-main'

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        modified = False
        
        # Check for side logo
        side_logo = soup.find('div', class_=lambda c: c and 'main-header__logo' in c)
        
        # Find all middle logos
        middle_logos = soup.find_all('li', class_=lambda c: c and 'main-logo' in c)
        
        if side_logo and middle_logos:
            for ml in middle_logos:
                ml.decompose()
                modified = True
                
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            count += 1

print(f"Removed duplicate middle logos in {count} HTML files.")
