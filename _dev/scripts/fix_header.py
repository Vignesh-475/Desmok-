import os

filepath = r'd:\ZM\amoxi-html-package\amoxi-html-main\assets\css\amoxi-blue.css'

with open(filepath, 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the previous override
css = css.replace(""".main-header--two {
  position: relative !important;
  top: 0 !important;
  background-color: var(--amoxi-black2, #0E0F11) !important;
  border-bottom: 1px solid var(--amoxi-black3, #1b2748) !important;
  z-index: 99;
}""", "")

# Add the correct override
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

css += correct_override

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed CSS overrides.")
