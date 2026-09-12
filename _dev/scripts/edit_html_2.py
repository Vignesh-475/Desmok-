import re
from bs4 import BeautifulSoup

with open('my-website.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace hardcoded orange colors in svgs or styles
html = html.replace('#F29A1C', '#007bff')
html = html.replace('#FA4721', '#0056b3')

soup = BeautifulSoup(html, 'html.parser')

# About section
about = soup.find('section', class_='about-two')
if about:
    title = about.find('h2', class_='sec-title__title')
    if title:
        title.string = "An end-to-end build partner, not a body shop."
    
    text = about.find('p', class_='about-two__text')
    if text:
        text.string = "We're a senior, cross-functional team — full-stack engineers, AI/ML specialists, automation architects, DevOps, and product designers — taking full ownership from first call to production. One team, one contract, zero hand-offs."

    list_items = about.find_all('li')
    serve_data = [
        "Founders with an idea: Validate and launch a real product, fast: a scoped MVP on clean architecture.",
        "Businesses running on manual work: We map your operations, then automate the repetitive load.",
        "Teams adding AI to a product: RAG, agents, and LLM features integrated into your existing stack."
    ]
    for i, li in enumerate(list_items):
        if i < len(serve_data):
            span = li.find('span')
            if span:
                span.string = serve_data[i]
            else:
                new_span = soup.new_tag("span")
                new_span.string = serve_data[i]
                li.append(new_span)

# Services section
services = soup.find('section', class_='services-two')
if services:
    tagline = services.find('p', class_='sec-title__tagline')
    if tagline:
        tagline.string = "CORE OFFERS"
    title = services.find('h2', class_='sec-title__title')
    if title:
        title.string = "Three ways to engage us."
    
    items = services.find_all('div', class_='services-two__item hover-item')
    offers = [
        {
            "title": "MVP-to-Launch",
            "tags": ["FIXED SCOPE", "FIXED QUOTE"],
            "desc": "For startups. Idea to a production-ready product in a typical 6-8 week build."
        },
        {
            "title": "AI Automation",
            "tags": ["AUDIT FIRST", "RETAINER AVAILABLE"],
            "desc": "For operators. We audit your workflows, then design and run automations."
        },
        {
            "title": "AI Integration",
            "tags": ["WORKS INSIDE YOUR EXISTING STACK"],
            "desc": "For product teams. Add intelligence to what you've already built."
        }
    ]
    
    for i, item in enumerate(items):
        if i < len(offers):
            # Update title
            h3 = item.find('h3', class_='services-two__item__title')
            if h3:
                a = h3.find('a')
                if a:
                    # Keep svgs inside
                    svgs = a.find_all('svg')
                    a.clear()
                    shape = soup.new_tag("span", **{'class': 'services-two__item__shape'})
                    for svg in svgs:
                        shape.append(svg)
                    a.append(shape)
                    a.append(" " + offers[i]["title"])
            
            # Update tags
            tags_div = item.find('div', class_='services-two__item__tags')
            if tags_div:
                tags_div.clear()
                for tag_text in offers[i]["tags"]:
                    new_tag = soup.new_tag("a", href="javascript:void(0)", **{'class': 'services-two__item__tag'})
                    new_tag.string = tag_text
                    tags_div.append(new_tag)
                    
            # We can use hover-item__box content to add description
            hover_box = item.find('div', class_='hover-item__box')
            if hover_box:
                p = soup.new_tag("p", style="color: white; padding: 20px;")
                p.string = offers[i]["desc"]
                hover_box.clear()
                hover_box.append(p)
        else:
            item.decompose()

with open('my-website.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
