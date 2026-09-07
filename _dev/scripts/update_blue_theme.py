import re

with open(r'd:\ZM\amoxi-html-package\amoxi-html-main\assets\css\amoxi.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace hex colors
css_content = re.sub(r'(?i)#f29a1c', '#007bff', css_content)
css_content = re.sub(r'(?i)#fa4721', '#0056b3', css_content)

# Replace rgba variants
css_content = css_content.replace('242, 154, 28', '0, 123, 255')
css_content = css_content.replace('250, 71, 33', '0, 86, 179')

with open(r'd:\ZM\amoxi-html-package\amoxi-html-main\assets\css\amoxi-blue.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

# Also check my-website.html
with open(r'd:\ZM\amoxi-html-package\amoxi-html-main\my-website.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(?i)#f29a1c', '#007bff', html)
html = re.sub(r'(?i)#fa4721', '#0056b3', html)
html = html.replace('242, 154, 28', '0, 123, 255')
html = html.replace('250, 71, 33', '0, 86, 179')

# Also, wait. Is there any orange in amoxi-icons/style.css?
with open(r'd:\ZM\amoxi-html-package\amoxi-html-main\my-website.html', 'w', encoding='utf-8') as f:
    f.write(html)
