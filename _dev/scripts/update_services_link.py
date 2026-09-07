import os
import re

directory = r'd:\ZM\amoxi-html-package\amoxi-html-main'

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        # Target <a href="#">Services</a>
        html_new = re.sub(r'<a[^>]*href="#"[^>]*>\s*Services\s*</a>', r'<a href="my-services.html">Services</a>', html, flags=re.IGNORECASE)
        
        # We should also check for <a href="services.html">Services</a> just in case some templates used that natively
        html_new = re.sub(r'<a[^>]*href="services\.html"[^>]*>\s*Services\s*</a>', r'<a href="my-services.html">Services</a>', html_new, flags=re.IGNORECASE)
        
        # And <a href="services-2.html">Services</a>
        html_new = re.sub(r'<a[^>]*href="services-2\.html"[^>]*>\s*Services\s*</a>', r'<a href="my-services.html">Services</a>', html_new, flags=re.IGNORECASE)

        if html_new != html:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_new)
            count += 1

print(f"Updated Services parent link in {count} HTML files.")
