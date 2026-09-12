import os

script = """
<script>
document.addEventListener("DOMContentLoaded", function() {
    function scrollToHash(hash) {
        var target = $(hash);
        if (target.length) {
            $("html, body").stop().animate({
                scrollTop: target.offset().top - 100
            }, 800);
        }
    }

    // Handle hash on page load
    if (window.location.hash) {
        setTimeout(function() {
            scrollToHash(window.location.hash);
        }, 500); // 500ms allows preloader to vanish
    }

    // Intercept clicks to anchor links
    $('a[href*="#"]').not('[href="#"]').on("click", function(event) {
        var href = $(this).attr("href");
        var hash = href.substring(href.indexOf('#'));
        var path = href.substring(0, href.indexOf('#'));
        
        var currentPath = window.location.pathname.split('/').pop();
        if (path === "" || path === currentPath) {
            var target = $(hash);
            if (target.length) {
                event.preventDefault();
                scrollToHash(hash);
                // Remove locking classes from mobile nav / megamenu
                $("body").removeClass("locked megamenu-popup-active");
                $(".mobile-nav__wrapper").removeClass("expanded");
            }
        }
    });
});
</script>
"""

def inject(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # avoid double injection
    if "function scrollToHash(hash)" not in html:
        html = html.replace('</body>', script + '\n</body>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

inject('d:\\ZM\\amoxi-html-package\\amoxi-html-main\\my-services.html')
inject('d:\\ZM\\amoxi-html-package\\amoxi-html-main\\my-website.html')
print("Successfully injected JS fix.")
