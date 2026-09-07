import re
from bs4 import BeautifulSoup
import shutil

# Copy base
shutil.copy('my-website.html', 'my-shop.html')

with open('my-shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Sections to remove
sections_to_remove = [
    'hero-two', 'social-media', 'about-two', 'funfact-two',
    'portfolio-two', 'team-two', 'video-two', 'testimonials-one',
    'blog-two', 'work-area'
]

for sec_class in sections_to_remove:
    sec = soup.find('section', class_=re.compile(sec_class))
    if sec:
        sec.decompose()
        
# The services-two section - remove it as well
srv_sec = soup.find('section', class_=re.compile(r'services-two'))
if srv_sec:
    srv_sec.decompose()

# The packages-one section (keep this, modify it)
packages_sec = soup.find('section', class_=re.compile(r'packages-one'))
if packages_sec:
    # Change Title
    tagline = packages_sec.find('p', class_='sec-title__tagline')
    if tagline: tagline.string = "MVP Service"
    title = packages_sec.find('h2', class_='sec-title__title')
    if title: title.string = "Choose Your MVP Pricing Plan"
    
    # Remove toggle switch
    switch = packages_sec.find('div', class_='packages-one__switch')
    if switch: switch.decompose()
    
    # Restructure cards container
    tabs = packages_sec.find('div', class_='packages-one__tabs')
    
    # We will build a new row with 2 cards
    new_cards_html = """
    <div class="row gutter-y-30" style="margin-top: 50px;">
        <div class="col-xl-6 col-lg-6">
            <div class="package-card">
                <div class="package-card__shape">
                    <div class="package-card__shape__bg" style="background-image: url(assets/images/shapes/package-card-bg-1-1.png);"></div>
                </div>
                <div class="package-card__content">
                    <div class="package-card__top">
                        <div class="package-card__top__left">
                            <h3 class="package-card__price" style="font-size: 32px;">$35 - $150</h3>
                            <p class="package-card__title">One Time Purchase <span class="package-card__title__shape"></span></p>
                        </div>
                        <p class="package-card__info">Based on project size</p>
                        <p style="margin-top: 20px; font-size: 15px;">Defined outcome, fixed quote, milestone billing. Best for MVPs and one-off builds.</p>
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
                            <h3 class="package-card__price" style="font-size: 32px;">$55 / mo</h3>
                            <p class="package-card__title">Retainer Business <span class="package-card__title__shape"></span></p>
                        </div>
                        <p class="package-card__info">Ongoing maintenance & scaling</p>
                        <p style="margin-top: 20px; font-size: 15px;">A standing team for automation, AI features, and continuous improvement at a predictable monthly cost.</p>
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
    """
    new_cards = BeautifulSoup(new_cards_html, 'html.parser')
    if tabs:
        tabs.replace_with(new_cards)


# Get Form from checkout.html
with open('checkout.html', 'r', encoding='utf-8') as f:
    checkout_html = f.read()

c_soup = BeautifulSoup(checkout_html, 'html.parser')
checkout_form = c_soup.find('div', class_='checkout-page__billing-address')

if checkout_form:
    # Let's wrap it in a nice section
    form_section_html = f"""
    <section class="checkout-page section-space" id="shop-form">
        <div class="container">
            <div class="sec-title sec-title--center">
                <h2 class="sec-title__title bw-split-text">Ready to start? Fill the details below.</h2>
            </div>
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="checkout-page__billing-address" style="background-color: var(--amoxi-black2, #0E0F11); border: 1px solid var(--amoxi-black3, #1b2748); padding: 40px; border-radius: 20px;">
                        {checkout_form.decode_contents()}
                        <div class="form-one__control" style="margin-top: 30px;">
                            <button type="submit" class="amoxi-btn amoxi-btn--two" style="width: 100%; border: none;">
                                <span class="amoxi-btn__text">Submit Request</span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """
    form_section = BeautifulSoup(form_section_html, 'html.parser')
    
    # insert before footer
    footer = soup.find('footer', class_='main-footer')
    if footer:
        footer.insert_before(form_section)

with open('my-shop.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
