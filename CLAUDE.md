# CLAUDE.md

Guidance for Claude Code (claude.ai/code) when working in this repository.

## What this is

A **static, multi-page HTML website** — the "Amoxi" creative-agency / portfolio HTML
template, customized into the **Desmok** brand (blue theme, reworked navigation, a custom
shop and services set). There is **no build step, no bundler, no `package.json`, no
Node/npm**. Pages are plain `.html` files that load CSS/JS directly via `<link>`/`<script>`.

- Git repo, branch `main`, remote `origin` → `https://github.com/Vignesh-475/Desmok-.git`.
- Note the trailing hyphen in the repo name (`Desmok-`) — it is part of the real name.

## Running it

It is a static site — serve the folder over HTTP (opening `file://` breaks some relative
paths and JS). From the repo root:

```bash
python -m http.server 8123 --bind 127.0.0.1   # then open http://127.0.0.1:8123/index.html
```

- **Entry page:** `index.html` (currently byte-identical to `my-website.html`, the
  customized Desmok homepage — the last commit set this as the default index).
- The contact form posts to `assets/inc/sendemail.php`, so **actually sending mail needs a
  PHP-capable server** (e.g. `php -S 127.0.0.1:8000`); the Python server above renders
  everything else but cannot execute the PHP.

## Layout

- **Root `*.html`** — every page of the site. Two kinds live side by side:
  - **Custom Desmok pages:** `my-website.html`, `my-services.html`, `my-shop.html`,
    `service-d-*.html` (six service detail pages).
  - **Original template demo pages** (`index-2..6`, `blog-*`, `portfolio*`, `team*`,
    `gallery*`, `products*`, `services*`, etc.) — kept as a reference/component library.
    Don't assume these are linked from the live nav; check before treating one as live.
- **`assets/css/`** — `amoxi.css` is the base template stylesheet; **`amoxi-blue.css` is
  the active Desmok theme** loaded by `index.html`. `color.css`, `amoxi-dark.css`, the
  `*-rtl.css` variants and `amoxi-landing.css` are alternate themes/layouts, mostly unused.
  `custom.css` holds small hand-written overrides layered on top of the theme.
- **`assets/js/`** — `amoxi.js` (main, jQuery-based), `amoxi-landing.js`.
- **`assets/vendors/`** — all third-party libs, vendored (not from a CDN): jQuery 3.7.1,
  Bootstrap 5, GSAP + ScrollSmoother/ScrollTrigger, Swiper, Owl Carousel, Slick, Isotope,
  AOS, Jarallax, Magnific Popup, Matter.js, and many jQuery plugins. **Do not upgrade or
  hand-edit vendor files.**
- **`assets/images/`** — image assets, organized by section. The large `1040X805` /
  `356X200` grey blocks visible on the homepage are the template's **intentional
  placeholder images**, not broken assets.
- **`assets/inc/sendemail.php`** — PHP contact-form handler.

## `_scripts/` — one-off customization scripts, NOT a build pipeline

Python scripts (`build_shop_page.py`, `apply_blue_everywhere.py`, `update_all_dropdowns.py`,
`fix_header.py`, …) that were run manually to mutate the HTML in bulk when the template was
Desmok-ified. They are **historical/ad-hoc tooling**, not part of any regular workflow, and
several are one-shot text rewrites that may not be safe to re-run against the current HTML.
Don't run them as a build; treat them as a record of how the customization was done. Prefer
editing the `.html` files directly.

## Editing conventions

- Edit `.html`, `.css`, and site `.js` by hand. Match the existing template markup and
  class names (Bootstrap + Amoxi custom classes) so styling and the JS initializers keep
  working.
- Keep the **blue theme** consistent — brand color changes live in `assets/css/amoxi-blue.css`.
- Because pages are independent files, a shared change (header, nav, footer) must be applied
  to **every** page it appears on; there is no template include/partial system.
- **Leave the backups alone:** `index.html.bak` and `index_old.html` are snapshots, not live
  pages — don't edit them and don't wire them into the site.
