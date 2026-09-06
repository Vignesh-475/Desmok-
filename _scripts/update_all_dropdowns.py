import os
import re
from bs4 import BeautifulSoup

directory = r'd:\ZM\amoxi-html-package\amoxi-html-main'

# Define the new dropdown items
services_data = [
    ("MVP system", "mvp-system"),
    ("Ai automations", "ai-automations"),
    ("Performance Marketing", "performance-marketing"),
    ("Social Media Management", "social-media-management"),
    ("Ai integration", "ai-integration"),
    ("lead generation", "lead-generation"),
    ("Website Design", "website-design"),
    ("personalised system creation and management", "personalised-system"),
]

def get_new_ul(soup):
    new_ul = soup.new_tag("ul")
    for name, cid in services_data:
        li = soup.new_tag("li")
        a = soup.new_tag("a", href=f"my-services.html#{cid}")
        a.string = name
        li.append(a)
        new_ul.append(li)
    return new_ul

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        modified = False
        
        nav_links = soup.find_all('a', href=re.compile(r'#|services\.html'))
        for link in nav_links:
            if link.string and link.string.strip() == "Services":
                parent_li = link.parent
                if parent_li and parent_li.name == "li" and "dropdown" in parent_li.get("class", []):
                    old_ul = parent_li.find("ul")
                    if old_ul:
                        old_ul.replace_with(get_new_ul(soup))
                        modified = True
                        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            count += 1

print(f"Updated dropdowns in {count} HTML files.")
