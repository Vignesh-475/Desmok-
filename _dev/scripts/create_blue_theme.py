import re

# Read original CSS
with open(r'd:\ZM\amoxi-html-package\amoxi-html-main\assets\css\amoxi.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace hex colors
css_content = re.sub(r'(?i)#f29a1c', '#007bff', css_content)
css_content = re.sub(r'(?i)#fa4721', '#0056b3', css_content)

# We should also check for any RGB variants if they exist, but normally they are defined in :root.
# Let's also check for other orange hex codes, like #ffA500 just in case.
# Wait, let's look at the :root variables again.

with open(r'd:\ZM\amoxi-html-package\amoxi-html-main\assets\css\amoxi-blue.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

# Update my-website.html to use amoxi-blue.css instead of amoxi.css
with open(r'd:\ZM\amoxi-html-package\amoxi-html-main\my-website.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('href="assets/css/amoxi.css"', 'href="assets/css/amoxi-blue.css"')

# Also replace any lingering orange colors in HTML if they were hardcoded
html = re.sub(r'(?i)#f29a1c', '#007bff', html)
html = re.sub(r'(?i)#fa4721', '#0056b3', html)

with open(r'd:\ZM\amoxi-html-package\amoxi-html-main\my-website.html', 'w', encoding='utf-8') as f:
    f.write(html)
