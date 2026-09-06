import re
import shutil
from bs4 import BeautifulSoup

# Step 1: Copy my-website.html to my-services.html
shutil.copy('my-website.html', 'my-services.html')

def update_dropdowns(html):
    soup = BeautifulSoup(html, 'html.parser')
    
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
    
    new_ul = soup.new_tag("ul")
    for name, cid in services_data:
        li = soup.new_tag("li")
        a = soup.new_tag("a", href=f"my-services.html#{cid}")
        a.string = name
        li.append(a)
        new_ul.append(li)

    # Find all dropdowns that have 'Services' text link
    nav_links = soup.find_all('a', href=re.compile(r'#|services\.html'))
    for link in nav_links:
        if link.string and link.string.strip() == "Services":
            parent_li = link.parent
            if parent_li and parent_li.name == "li" and "dropdown" in parent_li.get("class", []):
                old_ul = parent_li.find("ul")
                if old_ul:
                    old_ul.replace_with(BeautifulSoup(str(new_ul), 'html.parser'))

    return str(soup)


# Update my-website.html
with open('my-website.html', 'r', encoding='utf-8') as f:
    website_html = f.read()

website_html = update_dropdowns(website_html)

with open('my-website.html', 'w', encoding='utf-8') as f:
    f.write(website_html)


# Update my-services.html
with open('my-services.html', 'r', encoding='utf-8') as f:
    services_html = f.read()

# 1. Update dropdowns
services_html = update_dropdowns(services_html)

soup = BeautifulSoup(services_html, 'html.parser')

# 2. Remove all sections except services-two
sections_to_remove = [
    'hero-two', 'social-media', 'about-two', 'funfact-two',
    'portfolio-two', 'team-two', 'video-two', 'testimonials-one',
    'packages-one', 'blog-two', 'work-area'
]

for sec_class in sections_to_remove:
    sec = soup.find('section', class_=sec_class)
    if sec:
        sec.decompose()

# 3. Modify services-two
services_sec = soup.find('section', class_=re.compile(r'services-two'))
if services_sec:
    # Update titles
    tagline = services_sec.find('p', class_='sec-title__tagline')
    if tagline: tagline.string = "OUR SERVICES"
    
    title = services_sec.find('h2', class_='sec-title__title')
    if title: title.string = "Everything we offer."
    
    # We'll use the first item as a template
    row_container = services_sec.find('div', class_='services-two__row')
    if row_container:
        items = row_container.find_all('div', class_='services-two__item')
        if items:
            template_item = items[0]
            
            # Clear row container
            row_container.clear()
            
            services_data = [
                {"name": "MVP system", "id": "mvp-system", "tags": ["FAST LAUNCH", "SCALABLE"], "desc": "We build your Minimum Viable Product from scratch, enabling you to test the market quickly."},
                {"name": "Ai automations", "id": "ai-automations", "tags": ["EFFICIENCY", "WORKFLOW"], "desc": "Streamline your internal processes with cutting-edge AI-driven workflow automations."},
                {"name": "Performance Marketing", "id": "performance-marketing", "tags": ["ROI DRIVEN", "ADS"], "desc": "Data-backed marketing campaigns designed to convert clicks into paying customers."},
                {"name": "Social Media Management", "id": "social-media-management", "tags": ["ENGAGEMENT", "BRANDING"], "desc": "Grow your online presence with tailored content strategies and community management."},
                {"name": "Ai integration", "id": "ai-integration", "tags": ["SMART TECH", "API"], "desc": "Seamlessly integrate Large Language Models and AI capabilities into your existing products."},
                {"name": "lead generation", "id": "lead-generation", "tags": ["B2B", "SALES"], "desc": "Targeted outreach and lead capture systems to fill your sales pipeline with high-quality prospects."},
                {"name": "Website Design", "id": "website-design", "tags": ["UI/UX", "RESPONSIVE"], "desc": "Beautiful, responsive, and conversion-optimized websites that represent your brand."},
                {"name": "personalised system creation and management", "id": "personalised-system", "tags": ["CUSTOM", "MAINTENANCE"], "desc": "End-to-end custom software architecture, tailored specifically to your unique business needs."},
            ]
            
            for idx, srv in enumerate(services_data):
                new_item = BeautifulSoup(str(template_item), 'html.parser').find('div', class_='services-two__item')
                new_item['id'] = srv['id']
                
                # Serial
                serial = new_item.find('p', class_='services-two__item__serial')
                if serial: serial.string = f"0{idx + 1}"
                
                # Title
                h3 = new_item.find('h3', class_='services-two__item__title')
                if h3:
                    a = h3.find('a')
                    if a:
                        a['href'] = f"my-services.html#{srv['id']}"
                        # Preserve SVG shape
                        shape = a.find('span', class_='services-two__item__shape')
                        a.clear()
                        if shape: a.append(shape)
                        a.append(" " + srv['name'])
                
                # Tags
                tags_div = new_item.find('div', class_='services-two__item__tags')
                if tags_div:
                    tags_div.clear()
                    for tag in srv['tags']:
                        t = soup.new_tag('a', href='javascript:void(0)', **{'class': 'services-two__item__tag'})
                        t.string = tag
                        tags_div.append(t)
                        
                # Link
                btn = new_item.find('a', class_='services-two__item__btn')
                if btn: btn['href'] = f"my-services.html#{srv['id']}"
                
                # Desc
                hover_box = new_item.find('div', class_='hover-item__box')
                if hover_box:
                    p = hover_box.find('p')
                    if not p:
                        p = soup.new_tag('p', style="color: white; padding: 20px;")
                        hover_box.append(p)
                    p.string = srv['desc']
                    
                row_container.append(new_item)

with open('my-services.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Done building services page!")
