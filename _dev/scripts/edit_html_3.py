import re
from bs4 import BeautifulSoup

with open('my-website.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# 1. Representative builds (portfolio-two)
portfolio = soup.find('section', class_='portfolio-two')
if portfolio:
    tagline = portfolio.find('p', class_='sec-title__tagline')
    if tagline: tagline.string = "WHAT WE BUILD"
    title = portfolio.find('h2', class_='sec-title__title')
    if title: title.string = "Representative builds."
    
    # We will just change the title/category inside the cards
    cards = portfolio.find_all('div', class_='portfolio-two__card')
    builds = [
        {"title": "AI Support Agent", "cat": "LLM APIS · RAG · VECTOR DB", "desc": "A customer-facing agent trained on your docs and policies. It answers on web and WhatsApp, hands off to a human when it should."},
        {"title": "Back-Office Autopilot", "cat": "OCR · N8N · CRM", "desc": "Invoices, forms, and emails read by AI, routed to the right system, and summarized for your team every morning."},
        {"title": "SaaS MVP", "cat": "REACT / NEXT.JS · NODE", "desc": "A launch-ready product: authentication, payments, admin dashboard, responsive UI — deployed on scalable cloud infrastructure."},
        {"title": "AI Support Agent", "cat": "LLM APIS · RAG · VECTOR DB", "desc": "A customer-facing agent trained on your docs and policies. It answers on web and WhatsApp, hands off to a human when it should."}
    ]
    for i, card in enumerate(cards):
        if i < len(builds):
            h3 = card.find('h3', class_='portfolio-two__card__title')
            if h3: 
                a = h3.find('a')
                if a: a.string = builds[i]["title"]
            cat = card.find('p', class_='portfolio-two__card__category')
            if cat: cat.string = builds[i]["cat"]
            
            # add desc
            content = card.find('div', class_='portfolio-two__card__content')
            if content:
                p = soup.new_tag('p')
                p.string = builds[i]["desc"]
                p['style'] = "color: white; margin-top: 10px;"
                content.append(p)
                
# 2. Capability Map (team-two)
team = soup.find('section', class_='team-two')
if team:
    tagline = team.find('p', class_='sec-title__tagline')
    if tagline: tagline.string = "CAPABILITY MAP"
    title = team.find('h2', class_='sec-title__title')
    if title: title.string = "Everything under one roof."
    
    items = team.find_all('div', class_='item')
    caps = [
        {"title": "AI & MACHINE LEARNING", "list": ["AI agents & multi-agent systems", "Chatbots & voice AI assistants", "RAG & semantic search"]},
        {"title": "PRODUCT ENGINEERING", "list": ["SaaS platforms & multi-tenant apps", "Web apps & PWAs", "iOS & Android apps"]},
        {"title": "AUTOMATION & INTEGRATIONS", "list": ["Business process automation", "n8n · Make · Zapier workflows", "MCP servers & agent orchestration"]},
        {"title": "DATA & ANALYTICS", "list": ["Dashboards & business intelligence", "ETL / ELT pipelines", "Predictive modeling"]},
        {"title": "CLOUD & DEVOPS", "list": ["AWS · Azure · GCP · DigitalOcean", "Docker & Kubernetes", "CI/CD pipelines"]},
        {"title": "DESIGN & SECURITY", "list": ["UI/UX design & design systems", "Landing pages & company sites", "OAuth · SSO · MFA · RBAC"]}
    ]
    for i, item in enumerate(items):
        if i < len(caps):
            h3 = item.find('h3', class_='team-card__title')
            if h3:
                a = h3.find('a')
                if a: a.string = caps[i]["title"]
            desig = item.find('p', class_='team-card__designation')
            if desig: desig.string = "Capability"
            
            content = item.find('div', class_='team-card__content')
            if content:
                # Add list
                ul = soup.new_tag('ul', style='list-style: none; padding: 0; text-align: left; margin-top: 15px;')
                for li_text in caps[i]["list"]:
                    li = soup.new_tag('li', style='color: white; margin-bottom: 5px; font-size: 14px;')
                    li.string = "- " + li_text
                    ul.append(li)
                content.append(ul)

# 3. Packages (packages-one)
packages = soup.find('section', class_='packages-one')
if packages:
    tagline = packages.find('p', class_='sec-title__tagline')
    if tagline: tagline.string = "WORKING TOGETHER"
    title = packages.find('h2', class_='sec-title__title')
    if title:
        title.clear()
        title.string = "Pick the shape that fits."
        
    # hide switch
    switch = packages.find('div', class_='packages-one__switch')
    if switch: switch.decompose()
    
    tables = packages.find_all('div', class_='package-card')
    plans = [
        {"name": "Fixed-scope project", "price": "Model 01", "desc": "Defined outcome, fixed quote, milestone billing. Best for MVPs and one-off builds."},
        {"name": "Monthly retainer", "price": "Model 02", "desc": "A standing team for automation, AI features, and continuous improvement at a predictable monthly cost."},
        {"name": "Dedicated team", "price": "Model 03", "desc": "Your own engineers and designers, managed by us, embedded with your team. Scale up or down monthly."}
    ]
    for i, table in enumerate(tables):
        if i < len(plans):
            name = table.find('h3', class_='package-card__title')
            if name: name.string = plans[i]["name"]
            price = table.find('h3', class_='package-card__price')
            if price:
                price.clear()
                price.string = plans[i]["price"]
            # add desc
            content = table.find('div', class_='package-card__top')
            if content:
                p = soup.new_tag('p', style="margin-top: 20px; font-size: 15px;")
                p.string = plans[i]["desc"]
                content.append(p)
                
            ul = table.find('ul', class_='package-card__list')
            if ul: ul.decompose() # remove the features list as it's not needed

# 4. Work Process (work-area)
work = soup.find('section', class_='work-area')
if work:
    tagline = work.find('p', class_='sec-title__tagline')
    if tagline: tagline.string = "HOW WE WORK"
    title = work.find('h2', class_='sec-title__title')
    if title: title.string = "A process you can see."
    
    items = work.find_all('div', class_='work-area__item')
    steps = [
        {"title": "Discover", "desc": "A working session on your goals, users, and constraints. We leave with a shared definition."},
        {"title": "Scope", "desc": "A fixed proposal: features, architecture, timeline, and price. No open-ended billing."},
        {"title": "Build", "desc": "Weekly demos of working software, direct access to the engineers, milestones you sign off on."},
        {"title": "Launch", "desc": "Production deployment, QA, documentation, and a clean handover. You own the IP."},
        {"title": "Support", "desc": "Maintenance, monitoring, and a roadmap for what's next."}
    ]
    for i, item in enumerate(items):
        if i < len(steps):
            h3 = item.find('h3', class_='work-area__item__title')
            if h3:
                a = h3.find('a')
                if a: a.string = steps[i]["title"]
            text = item.find('p', class_='work-area__item__text')
            if text: text.string = steps[i]["desc"]

with open('my-website.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
