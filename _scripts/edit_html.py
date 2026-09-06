import re
from bs4 import BeautifulSoup

with open('my-website.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Hero section (hero-two)
hero_section = soup.find('section', class_='hero-two')
if hero_section:
    text_p = hero_section.find('p', class_='hero-two__text')
    if text_p:
        text_p.string = "We take startups from idea to production-ready product — and help businesses automate the work that slows them down. Strategy, design, engineering, and AI under one roof."
    
    title_h1 = hero_section.find('h1', class_='hero-two__title')
    if title_h1:
        title_h1.clear()
        title_h1.append("AI-powered ")
        span1 = soup.new_tag("span")
        span1.string = "product engineering"
        title_h1.append(span1)
        title_h1.append(" & ")
        span2 = soup.new_tag("span")
        span2.string = "automation."
        title_h1.append(span2)

# Social Media section (social-media) - change to domains
social_media = soup.find('section', class_='social-media')
if social_media:
    items = social_media.find_all('a', class_='social-media__item')
    domains = ["AI AGENTS", "SAAS & MVPS", "WEB & MOBILE", "AUTOMATION", "DATA", "CLOUD & DEVOPS"]
    for i, item in enumerate(items):
        if i < len(domains):
            h2 = item.find('h2', class_='social-media__title')
            if h2:
                span = h2.find('span')
                if span:
                    span.string = domains[i]
                h2['data-hover'] = domains[i]

with open('my-website.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
