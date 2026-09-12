import re
from bs4 import BeautifulSoup

# Data for 8 services
services_data = [
    {
        "name": "MVP system", 
        "id": "mvp-system", 
        "img": "assets/images/services/service-1-1.jpg",
        "desc": "We build your Minimum Viable Product from scratch, enabling you to test the market quickly. We handle everything from scope, prototyping, UI/UX, backend architecture to the final launch, ensuring a seamless early-stage deployment."
    },
    {
        "name": "Ai automations", 
        "id": "ai-automations", 
        "img": "assets/images/services/service-1-2.jpg",
        "desc": "Streamline your internal processes with cutting-edge AI-driven workflow automations. Say goodbye to manual, repetitive tasks. We deploy custom scripts and intelligent agents to handle data entry, customer support routing, and internal reporting."
    },
    {
        "name": "Performance Marketing", 
        "id": "performance-marketing", 
        "img": "assets/images/services/service-1-3.jpg",
        "desc": "Data-backed marketing campaigns designed to convert clicks into paying customers. Through advanced analytics and A/B testing, our targeted ads guarantee a higher return on investment and a steadily growing user base."
    },
    {
        "name": "Social Media Management", 
        "id": "social-media-management", 
        "img": "assets/images/services/service-1-4.jpg",
        "desc": "Grow your online presence with tailored content strategies and community management. We design engaging posts, plan content calendars, and actively manage your brand's voice across major social platforms."
    },
    {
        "name": "Ai integration", 
        "id": "ai-integration", 
        "img": "assets/images/services/service-1-5.jpg",
        "desc": "Seamlessly integrate Large Language Models and AI capabilities into your existing products. Whether you need semantic search, RAG pipelines, or autonomous copilots, we build secure and scalable AI layers into your stack."
    },
    {
        "name": "lead generation", 
        "id": "lead-generation", 
        "img": "assets/images/services/service-1-6.jpg",
        "desc": "Targeted outreach and lead capture systems to fill your sales pipeline with high-quality prospects. We deploy strategic landing pages, highly optimized funnels, and automated follow-ups to maximize conversions."
    },
    {
        "name": "Website Design", 
        "id": "website-design", 
        "img": "assets/images/portfolio/portfolio-2-1.jpg",
        "desc": "Beautiful, responsive, and conversion-optimized websites that represent your brand perfectly. Our design team focuses on modern aesthetics, lightning-fast load times, and intuitive user experiences."
    },
    {
        "name": "personalised system creation and management", 
        "id": "personalised-system", 
        "img": "assets/images/portfolio/portfolio-2-2.jpg",
        "desc": "End-to-end custom software architecture, tailored specifically to your unique business needs. We plan, build, and continuously manage sophisticated internal tools, dashboards, and enterprise systems."
    },
]

# Read my-services.html
with open('my-services.html', 'r', encoding='utf-8') as f:
    services_html = f.read()

soup = BeautifulSoup(services_html, 'html.parser')

# Find services section
services_sec = soup.find('section', class_=re.compile(r'services-two'))

if services_sec:
    # Find container
    container = services_sec.find('div', class_='container')
    
    # We will remove the old row and create our own
    old_row = container.find('div', class_='services-two__row')
    if old_row:
        old_row.decompose()
        
    # Create new container for our cards
    cards_container = soup.new_tag('div', **{'class': 'services-cards-container'})
    
    for idx, srv in enumerate(services_data):
        # Alternate image position
        img_order = "order-1 order-xl-0" if idx % 2 == 0 else "order-1 order-xl-1"
        text_order = "order-2 order-xl-1" if idx % 2 == 0 else "order-2 order-xl-0"
        
        card_html = f"""
        <div class="blog-two__item" id="{srv['id']}" style="background-color: var(--amoxi-black2, #0E0F11); border: 1px solid var(--amoxi-black3, #1b2748); border-radius: 20px; margin-bottom: 50px; padding: 30px; transition: all 0.3s ease;" data-aos="fade-up" data-aos-duration="1300">
            <div class="row gutter-y-30 align-items-center">
                <div class="col-xl-5 {img_order}">
                    <div class="blog-two__item__image" style="overflow: hidden; border-radius: 15px;">
                        <img alt="{srv['name']}" src="{srv['img']}" style="width: 100%; height: 350px; object-fit: cover; transition: transform 0.5s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'"/>
                    </div>
                </div>
                <div class="col-xl-7 {text_order}">
                    <div class="blog-two__item__content" style="padding: 20px;">
                        <h3 class="blog-two__item__title" style="font-size: 32px; margin-bottom: 20px; color: var(--amoxi-white);">
                            {srv['name']}
                        </h3>
                        <p class="blog-two__item__text" style="font-size: 18px; line-height: 1.8; margin-bottom: 35px; color: var(--amoxi-text);">
                            {srv['desc']}
                        </p>
                        <a class="amoxi-btn amoxi-btn--two" href="#contact-form">
                            <span class="amoxi-btn__text">Get Now</span>
                            <span class="amoxi-btn__icon-box">
                                <span class="amoxi-btn__icon"><span><i class="icon-arrow-right-2"></i></span></span>
                            </span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        """
        card_soup = BeautifulSoup(card_html, 'html.parser')
        cards_container.append(card_soup)
        
    container.append(cards_container)

# Now extract contact form from contact.html
with open('contact.html', 'r', encoding='utf-8') as f:
    contact_html = f.read()

contact_soup = BeautifulSoup(contact_html, 'html.parser')
contact_section = contact_soup.find('div', class_=re.compile(r'contact-one section-space-t'))

# Ensure we found it
if contact_section:
    # Convert it into a section with id="contact-form"
    contact_section.name = 'section'
    contact_section['id'] = 'contact-form'
    contact_section['class'] = ['contact-one', 'section-space']
    
    # Remove google map to keep it clean, or keep it. Let's keep it but remove the extra top margin
    
    # Append right before footer
    footer = soup.find('footer', class_='main-footer')
    if footer:
        footer.insert_before(contact_section)

with open('my-services.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully rebuilt services with full sized cards and added contact form!")
