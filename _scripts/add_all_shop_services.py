import re
from bs4 import BeautifulSoup

# Define data for the remaining 7 services
services_data = [
    {
        "tagline": "Ai Automations",
        "title": "Ai Automations Pricing",
        "c1_price": "$500 - $2500",
        "c1_title": "One Time Setup",
        "c1_info": "Based on workflow complexity",
        "c1_desc": "Custom scripts and smart agent deployment to automate repetitive tasks.",
        "c2_price": "$150 / mo",
        "c2_title": "Retainer Business",
        "c2_info": "Ongoing monitoring & updates",
        "c2_desc": "Ensuring your AI automations run smoothly 24/7 with dedicated support."
    },
    {
        "tagline": "Performance Marketing",
        "title": "Performance Marketing Pricing",
        "c1_price": "$300 - $800",
        "c1_title": "Campaign Build",
        "c1_info": "One time strategy & setup",
        "c1_desc": "Deep audience research, ad creatives, and tracking integration.",
        "c2_price": "$250 / mo",
        "c2_title": "Retainer Business",
        "c2_info": "Active ad management",
        "c2_desc": "Continuous A/B testing and optimization to guarantee maximum ROI."
    },
    {
        "tagline": "Social Media Management",
        "title": "Social Media Pricing",
        "c1_price": "$200 - $500",
        "c1_title": "Profile Makeover",
        "c1_info": "One time branding",
        "c1_desc": "Complete overhaul of your social profiles with bespoke branding assets.",
        "c2_price": "$300 / mo",
        "c2_title": "Retainer Business",
        "c2_info": "Content calendar & posting",
        "c2_desc": "Weekly posts, community engagement, and growth analytics."
    },
    {
        "tagline": "Ai Integration",
        "title": "Ai Integration Pricing",
        "c1_price": "$1000 - $5000",
        "c1_title": "Custom Integration",
        "c1_info": "Based on system scale",
        "c1_desc": "Seamlessly wire LLMs and advanced AI features into your existing software.",
        "c2_price": "$350 / mo",
        "c2_title": "Retainer Business",
        "c2_info": "Maintenance & Scaling",
        "c2_desc": "Continuous optimization of API calls and system scaling as you grow."
    },
    {
        "tagline": "Lead Generation",
        "title": "Lead Generation Pricing",
        "c1_price": "$400 - $1200",
        "c1_title": "Funnel Architecture",
        "c1_info": "One time build",
        "c1_desc": "Strategic landing pages and automated email capture sequences.",
        "c2_price": "$200 / mo",
        "c2_title": "Retainer Business",
        "c2_info": "Active lead sourcing",
        "c2_desc": "Ongoing outbound campaigns and pipeline management."
    },
    {
        "tagline": "Website Design",
        "title": "Website Design Pricing",
        "c1_price": "$600 - $3500",
        "c1_title": "Full Website Build",
        "c1_info": "Based on page count",
        "c1_desc": "Responsive, high-converting, and beautifully designed web experience.",
        "c2_price": "$55 / mo",
        "c2_title": "Retainer Business",
        "c2_info": "Hosting & Edits",
        "c2_desc": "Premium hosting, security updates, and monthly content edits."
    },
    {
        "tagline": "System Creation",
        "title": "Personalised System Pricing",
        "c1_price": "$1500 - $10k+",
        "c1_title": "System Architecture",
        "c1_info": "One time development",
        "c1_desc": "End-to-end bespoke software tailored entirely to your business needs.",
        "c2_price": "$600 / mo",
        "c2_title": "Retainer Business",
        "c2_info": "System Administration",
        "c2_desc": "Dedicated server management, security patching, and scaling support."
    }
]

def generate_panel(soup, data):
    # Construct the raw HTML for one service panel block
    html = f"""
    <div style="margin-top: 100px; padding-top: 50px; border-top: 1px solid var(--amoxi-black3, #1b2748);">
        <div class="packages-one__top">
            <div class="row gutter-y-50 align-items-center">
                <div class="col-xl-7">
                    <div class="sec-title sec-title--two">
                        <div class="sec-title__top">
                            <div class="sec-title__shape sec-title__shape--1"></div>
                            <p class="sec-title__tagline bw-split-text">{data['tagline']}</p>
                        </div>
                        <h2 class="sec-title__title bw-split-text">{data['title']}</h2>
                    </div>
                </div>
            </div>
        </div>
        <div class="row gutter-y-30" style="margin-top: 50px;">
            <div class="col-xl-6 col-lg-6">
                <div class="package-card">
                    <div class="package-card__shape">
                        <div class="package-card__shape__bg" style="background-image: url(assets/images/shapes/package-card-bg-1-1.png);"></div>
                    </div>
                    <div class="package-card__content">
                        <div class="package-card__top">
                            <div class="package-card__top__left">
                                <h3 class="package-card__price" style="font-size: 32px;">{data['c1_price']}</h3>
                                <p class="package-card__title">{data['c1_title']} <span class="package-card__title__shape"></span></p>
                            </div>
                            <p class="package-card__info">{data['c1_info']}</p>
                            <p style="margin-top: 20px; font-size: 15px;">{data['c1_desc']}</p>
                        </div>
                        <div class="package-card__bottom">
                            <div class="package-card__button">
                                <a class="amoxi-btn amoxi-btn--two" href="#shop-form">
                                    <span class="amoxi-btn__text">Contact Now</span>
                                    <span class="amoxi-btn__icon-box">
                                        <span class="amoxi-btn__icon"><span><i class="icon-arrow-right-4"></i></span></span>
                                    </span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-xl-6 col-lg-6">
                <div class="package-card active">
                    <div class="package-card__shape">
                        <div class="package-card__shape__bg" style="background-image: url(assets/images/shapes/package-card-bg-1-1.png);"></div>
                    </div>
                    <div class="package-card__content">
                        <div class="package-card__top">
                            <div class="package-card__top__left">
                                <h3 class="package-card__price" style="font-size: 32px;">{data['c2_price']}</h3>
                                <p class="package-card__title">{data['c2_title']} <span class="package-card__title__shape"></span></p>
                            </div>
                            <p class="package-card__info">{data['c2_info']}</p>
                            <p style="margin-top: 20px; font-size: 15px;">{data['c2_desc']}</p>
                        </div>
                        <div class="package-card__bottom">
                            <div class="package-card__button">
                                <a class="amoxi-btn amoxi-btn--two" href="#shop-form">
                                    <span class="amoxi-btn__text">Contact Now</span>
                                    <span class="amoxi-btn__icon-box">
                                        <span class="amoxi-btn__icon"><span><i class="icon-arrow-right-4"></i></span></span>
                                    </span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    return BeautifulSoup(html, 'html.parser')

with open('my-shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the main container holding the packages
packages_sec = soup.find('section', class_=re.compile(r'packages-one'))
if packages_sec:
    container = packages_sec.find('div', class_='container')
    
    if container:
        # Append the 7 new panels
        for data in services_data:
            panel_soup = generate_panel(soup, data)
            container.append(panel_soup)

with open('my-shop.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
    
print("Successfully added all 7 extra service panels.")
