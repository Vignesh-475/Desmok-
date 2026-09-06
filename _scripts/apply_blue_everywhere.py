import os

directory = r'd:\ZM\amoxi-html-package\amoxi-html-main'

count_css = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        modified = False
        if "assets/css/amoxi.css" in html:
            html = html.replace("assets/css/amoxi.css", "assets/css/amoxi-blue.css")
            modified = True
            
        # also replace 'index.html' with 'my-website.html' in the main navigation for Home
        if 'href="index.html">Home<' in html:
            html = html.replace('href="index.html">Home<', 'href="my-website.html">Home<')
            modified = True
            
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            count_css += 1

print(f"Turned {count_css} pages back to blue!")
