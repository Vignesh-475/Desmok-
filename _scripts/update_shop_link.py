import os
import re

directory = r'd:\ZM\amoxi-html-package\amoxi-html-main'

# Replace the Shop dropdown link in all files
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        modified = False
        
        # We find `<a href="#">Shop</a>` or similar and change it to `<a href="my-shop.html">Shop</a>`
        # Or find the Shop link in the menu list.
        # Actually in `amoxi-html-main`, it's `<a href="#">Shop</a>`
        
        html_new = re.sub(r'<a href="#">Shop</a>', r'<a href="my-shop.html">Shop</a>', html)
        if html_new != html:
            html = html_new
            modified = True
            
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)

print("Updated Shop links in menu!")
