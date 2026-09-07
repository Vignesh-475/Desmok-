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
        
        # Find the 'Home' link in the main menu
        # It's usually inside <ul class="main-menu__list">
        menu_lists = soup.find_all('ul', class_=lambda c: c and 'main-menu__list' in c)
        
        for menu_list in menu_lists:
            # Find all <a> tags that say exactly "Home"
            home_links = menu_list.find_all('a', string=lambda s: s and s.strip() == "Home")
            for a_tag in home_links:
                parent_li = a_tag.parent
                if parent_li and parent_li.name == 'li':
                    # Remove the 'dropdown' class if it exists
                    classes = parent_li.get('class', [])
                    if 'dropdown' in classes:
                        classes.remove('dropdown')
                        parent_li['class'] = classes
                        modified = True
                        
                    # Remove any nested <ul> inside this <li>
                    nested_uls = parent_li.find_all('ul', recursive=False)
                    for ul in nested_uls:
                        ul.decompose()
                        modified = True
                        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            count += 1

print(f"Removed Home dropdown in {count} HTML files.")
