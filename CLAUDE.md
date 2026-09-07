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

- **Local-dev cache gotcha:** the Python server sends no `Cache-Control`, so Chrome
  heuristically caches `assets/js/*.js` and `assets/css/*.css`. After editing JS/CSS,
  hard-refresh (`Ctrl+Shift+R`) or you will be testing stale code. Vercel is unaffected
  (it sends `must-revalidate` + ETags).
- **Entry page:** `index.html` at the repo root (byte-identical to `pages/desmok/my-website.html`,
  the customized Desmok homepage). `index.html` and `404.html` are the **only** HTML at the
  root — everything else lives under `pages/` (see Layout).
- **Forms (contact/enquiry + newsletter) submit to Web3Forms** — no server code. The
  handlers live in `assets/js/amoxi.js` (search `WEB3FORMS_ACCESS_KEY`): paste the free
  access key from https://web3forms.com there, in that **one** place. Until it is set, the
  forms show a "not configured" message instead of failing silently. Submissions go to the
  email the key was issued to. The old PHP mailer (`assets/inc/sendemail.php`) was removed —
  it was never configured (recipient `mail@mail.com`) and cannot run on Vercel.
- **Deployment:** Vercel project `desmok` (team `akashs-projects-c931fb4b`), live at
  `https://desmok-five.vercel.app`. Not Git-connected (the GitHub repo is under another
  account), so redeploy from this folder with `vercel --prod`. `.vercelignore` keeps `_dev/`
  and `CLAUDE.md` out of the deploy. `vercel.json` adds security headers
  (`X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`);
  Vercel adds HSTS itself. No CSP yet — the template relies on inline scripts/styles.

## Paths — root-absolute

**All internal references are root-absolute** (`/assets/...`, `/pages/blog/x.html`), so a
page works regardless of which folder it sits in. When adding/editing links or assets, use a
leading `/` — do **not** use bare (`assets/…`) or `../` relative paths. This resolves
correctly on Vercel and on `python -m http.server` run from the repo root; it only breaks
under `file://` (which was already unsupported).

## Page metadata — brand-first

- **`<title>`** on every page is brand-first: `Desmok AI | <Page name>` (homepage:
  `Desmok AI | Product Engineering & Automation Studio`). Keep this order so "Desmok AI"
  shows beside the favicon in the browser tab. Don't reintroduce the template's
  `|| Creative Agency and Portfolio HTML Template` suffix.
- **`<meta name="description">`** is one site-wide Desmok description shared by all pages
  (the theme vendor's boilerplate was removed). If you change it, change it on every page.
- **Favicons** are the Desmok "D" mark on a white circle with transparent corners,
  generated from the source logo. Three dirs exist (`assets/images/favicons`, `favicons-2`,
  `favicons-3`) because different pages reference each — keep all three in sync.

## Layout

- **Root:** only `index.html` (homepage, served at `/`) and `404.html` (Vercel error page).
- **`pages/`** — every other page, grouped by kind:
  - `pages/desmok/` — the **custom Desmok pages**: `my-website.html`, `my-services.html`,
    `my-shop.html`, `service-d-*.html` (six service detail pages).
  - `pages/blog/`, `pages/shop/`, `pages/portfolio/`, `pages/team/`, `pages/gallery/`,
    `pages/services/`, `pages/testimonials/`, `pages/company/` (about/contact/faq), and
    `pages/home-demos/` (`index-2..6`, `index-boxed`, `index-one-page`) — **original template
    demo pages** kept as a reference/component library. Most are wired into the live nav
    dropdowns; check links before treating one as dead.
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
- **`robots.txt`** — allows crawling; disallows `/_dev/` and the unlinked
  `/pages/home-demos/`. **`.gitignore`** keeps OS junk and `*.bak`/`*_old.*` backups out
  of the repo. **`vercel.json`** — security headers only (no build config).

## `_dev/scripts/` — one-off customization scripts, NOT a build pipeline

Python scripts (`build_shop_page.py`, `apply_blue_everywhere.py`, `update_all_dropdowns.py`,
`fix_header.py`, …) that were run manually to mutate the HTML in bulk when the template was
Desmok-ified. They live under `_dev/` (outside the served page tree) as **historical/ad-hoc
tooling**, not part of any regular workflow, and several are one-shot text rewrites that may
not be safe to re-run against the current HTML. Don't run them as a build; treat them as a
record of how the customization was done. Prefer editing the `.html` files directly.

## Editing conventions

- Edit `.html`, `.css`, and site `.js` by hand. Match the existing template markup and
  class names (Bootstrap + Amoxi custom classes) so styling and the JS initializers keep
  working.
- Keep the **blue theme** consistent — brand color changes live in `assets/css/amoxi-blue.css`.
- Because pages are independent files, a shared change (header, nav, footer) must be applied
  to **every** page it appears on; there is no template include/partial system.
- **No backup files in the tree:** old `*.bak` / `*_old.*` snapshots were removed and are now
  git-ignored — rely on git history instead of leaving snapshot copies beside live pages.
