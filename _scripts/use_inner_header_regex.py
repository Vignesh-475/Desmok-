import os
import re

directory = r'd:\ZM\amoxi-html-package\amoxi-html-main'

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        # Match main-header--something, but NOT main-header--inner-page
        html_new = re.sub(r'main-header--(?!(inner-page|cloned))[a-z0-9\-]+', 'main-header--inner-page', html)
        
        if html_new != html:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_new)
            count += 1

print(f"Updated {count} HTML files to use inner-page header.")
