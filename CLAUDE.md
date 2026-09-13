# CLAUDE.md

Guidance for Claude Code (claude.ai/code) when working in this repository.

## What this is

A **static, multi-page HTML website** — the "Amoxi" creative-agency / portfolio HTML
template, customized into the **Desmok** brand (blue theme, reworked navigation, a custom
shop and services set). There is **no build step, no bundler, no `package.json`, no
Node/npm**. Pages are plain `.html` files that load CSS/JS directly via `<link>`/`<script>`.

- Git repo with **two remotes**:
  - `origin` → `https://github.com/Vignesh-475/Desmok-.git` (note the trailing hyphen — it is
    part of the real name); default branch `main`.
  - `aidesmok` → `https://github.com/aidesmok/Desmok-Website.git`, the production
    `www.desmok.com` repo (branches `master`, `static-site`).
- Local branch `static-site-desmokai` tracks `aidesmok/static-site`. `main` was rewritten, so
  the same commits have **different hashes** on `main` and on `aidesmok/*`. Don't merge or
  cherry-pick between the two lines without checking `git log` on both.
  `backup-before-trailer-removal` / `rewritten-no-trailers` are leftovers from that rewrite.
  Leave them alone.

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
- **Entry page:** `index.html` at the repo root, served at `/`. The old duplicate
  `pages/desmok/my-website.html` was byte-identical to it and has been deleted; `/` is the
  single homepage and the legacy path 301s to it.
- **Forms (contact/enquiry + newsletter) submit to Web3Forms** — no server code. The
  handlers live in `assets/js/amoxi.js` (search `WEB3FORMS_ACCESS_KEY`): paste the free
  access key from https://web3forms.com there, in that **one** place. Until it is set, the
  forms show a "not configured" message instead of failing silently. Submissions go to the
  email the key was issued to. The old PHP mailer (`assets/inc/sendemail.php`) was removed —
  it was never configured (recipient `mail@mail.com`) and cannot run on Vercel.
- **Deployment:** Vercel project `desmok` (team `akashs-projects-c931fb4b`), live at
  `https://desmok-five.vercel.app`. Not Git-connected (the GitHub repo is under another
  account), so redeploy from this folder with `vercel --prod`. `.vercelignore` keeps `_dev/`
  and `CLAUDE.md` out of the deploy. `vercel.json` serves the repo root as-is
  (`outputDirectory: "."`, no build), and a `.vercelignore` replaces `.gitignore` for CLI
  uploads, so treat **any root file not in `.vercelignore` as public**. `.env*` (the
  `.env.local` holds a `VERCEL_OIDC_TOKEN`) and `.vercel/` are listed there as a safeguard
  (they currently 404 on the live site). Keep them listed.
  The Web3Forms key in `amoxi.js` is still the `YOUR_WEB3FORMS_ACCESS_KEY` placeholder.
  `vercel.json` also adds security headers
  (`X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`);
  Vercel adds HSTS itself. No CSP yet — the template relies on inline scripts/styles.

## URLs — clean, and the file tree mirrors them

`vercel.json` sets `cleanUrls: true` + `trailingSlash: false`, and **the filesystem layout
matches the public URL exactly**: `about.html` → `/about`, `services/ui-ux.html` →
`/services/ui-ux`, `blog/post.html` → `/blog/post`. To add a page, create the file at the
path you want the URL to be — no route config needed.

**Do not reintroduce Vercel `rewrites` to map pretty URLs onto `.html` files.** That was
tried and every short URL 404'd: `cleanUrls` removes the `.html` routes, so a rewrite whose
destination is `/x.html` points at a path that no longer resolves.

`vercel.json` carries 122 `redirects` (301) covering every pre-flattening path — both
`/pages/x` and `/pages/x.html` — so old links and indexed results still land correctly.
Keep them; add a new pair whenever you rename a page.

**All internal references are root-absolute** (`/assets/...`, `/services`), so a page works
regardless of which folder it sits in. Use a leading `/` — never bare (`assets/…`) or `../`
relative paths. Link to the **clean URL** (`/about`), never to a file (`/about.html`);
asset URLs keep their extensions. Note `python -m http.server` does **not** implement
`cleanUrls`, so extensionless links 404 locally — verify routing on a Vercel preview
deployment instead.

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

- **Root:** `index.html` (`/`), `404.html` (Vercel error page), and one file per top-level
  page: `about`, `contact`, `faq`, `services`, `shop`, `cart`, `checkout`, `packages`,
  `blog`, `portfolio`, `team`, `gallery`, `testimonials`.
- **Section folders** hold the sub-pages of the same-named page:
  - `services/` — the six Desmok service detail pages (`ui-ux`, `web-development`,
    `creative-design`, `digital-branding`, `marketing-growth`, `startup-launch`) plus
    `overview` (the template's generic services layout).
  - `blog/`, `shop/`, `portfolio/`, `team/`, `gallery/`, `testimonials/` — **original
    template pages** kept as a reference/component library. Most are wired into the live nav
    dropdowns; check links before treating one as dead.
  - `demos/` (`home-2..6`, `home-boxed`, `home-one-page`, `home-*-one-page`) — template demo
    homepages, unlinked and `Disallow`ed in `robots.txt`.
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
- **`robots.txt`** — allows crawling; disallows `/_dev/`, the unlinked `/demos/`, and the
  legacy `/pages/home-demos/`. **`.gitignore`** keeps OS junk and `*.bak`/`*_old.*` backups
  out of the repo. **`vercel.json`** — `cleanUrls`, the 122 legacy 301s, and security
  headers (no build config).

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
