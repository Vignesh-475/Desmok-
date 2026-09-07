import os

filepath = r'd:\ZM\amoxi-html-package\amoxi-html-main\assets\css\amoxi-blue.css'

with open(filepath, 'r', encoding='utf-8') as f:
    css = f.read()

# The exact string that was appended
correct_override = """
/* Dedicated header space override */
.main-header--two:not(.sticky-header--cloned) {
  position: relative !important;
  top: 0 !important;
  background-color: var(--amoxi-black2, #0E0F11) !important;
  border-bottom: 1px solid var(--amoxi-black3, #1b2748) !important;
  z-index: 99;
}
/* Reduce padding in menu items so header doesn't take too much space */
.main-header--two:not(.sticky-header--cloned) .main-menu .main-menu__list > li {
  padding-top: 15px !important;
  padding-bottom: 15px !important;
}
/* Make the logo slightly smaller to prevent huge vertical space */
.main-header--two .main-logo img {
  max-width: 180px;
  height: auto;
}
"""

# If it's there, remove it
if correct_override in css:
    css = css.replace(correct_override, "")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Reverted header changes.")
else:
    print("Could not find the exact string, trying a fallback split.")
    if "/* Dedicated header space override */" in css:
        css = css.split("/* Dedicated header space override */")[0]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(css)
        print("Reverted header changes using fallback split.")
