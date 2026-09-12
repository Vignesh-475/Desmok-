import os
import re

directory = r'd:\ZM\amoxi-html-package\amoxi-html-main'

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        modified = False
        
        # We want to find:
        # <li><a href="product-details.html">Product details</a></li>
        # <li><a href="cart.html">Cart</a></li>
        # <li><a href="checkout.html">Checkout</a></li>
        # and replace them with:
        # <li><a href="packages.html">Pricing Plan</a></li>
        
        # Since formatting might vary (spaces/newlines), we can do it systematically:
        # 1. Remove the 3 unwanted links
        html_new = re.sub(r'<li[^>]*>\s*<a[^>]*href="product-details\.html"[^>]*>.*?</a>\s*</li>', '', html, flags=re.IGNORECASE|re.DOTALL)
        html_new = re.sub(r'<li[^>]*>\s*<a[^>]*href="cart\.html"[^>]*>.*?</a>\s*</li>', '', html_new, flags=re.IGNORECASE|re.DOTALL)
        html_new = re.sub(r'<li[^>]*>\s*<a[^>]*href="checkout\.html"[^>]*>.*?</a>\s*</li>', '', html_new, flags=re.IGNORECASE|re.DOTALL)
        
        # 2. Add Pricing Plan into the Shop dropdown.
        # Find where products-carousel.html is, and insert packages.html right after it.
        # If it's already there, don't add it again.
        if 'href="packages.html"' not in html_new and 'href="products-carousel.html"' in html_new:
            insertion = r'<li><a href="products-carousel.html">Products carousel</a></li>\n  <li><a href="packages.html">Pricing Plan</a></li>'
            html_new = re.sub(r'<li[^>]*>\s*<a[^>]*href="products-carousel\.html"[^>]*>.*?</a>\s*</li>', insertion, html_new, flags=re.IGNORECASE|re.DOTALL)
            
        if html_new != html:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_new)
            count += 1

print(f"Updated Shop dropdowns in {count} HTML files.")
