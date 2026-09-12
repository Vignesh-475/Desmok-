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
        
        # Remove packages.html link
        new_html = re.sub(r'<li[^>]*>\s*<a[^>]*href="packages\.html"[^>]*>.*?</a>\s*</li>', '', html, flags=re.IGNORECASE|re.DOTALL)
        if new_html != html:
            html = new_html
            modified = True
            
        # Remove 404.html link
        new_html = re.sub(r'<li[^>]*>\s*<a[^>]*href="404\.html"[^>]*>.*?</a>\s*</li>', '', html, flags=re.IGNORECASE|re.DOTALL)
        if new_html != html:
            html = new_html
            modified = True
            
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            count += 1

print(f"Removed pricing and 404 links from {count} HTML files.")
