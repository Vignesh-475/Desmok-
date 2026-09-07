import os
import re

directory = r'd:\ZM\amoxi-html-package\amoxi-html-main'

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        modified = False
        
        # Replace main-header--two with main-header--inner-page
        if "main-header--two" in html:
            html = html.replace("main-header--two", "main-header--inner-page")
            modified = True
            
        # Also replace main-header--one just in case they visit other templates
        if "main-header--one" in html:
            html = html.replace("main-header--one", "main-header--inner-page")
            modified = True
            
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            count += 1

print(f"Updated {count} HTML files to use inner-page header.")
