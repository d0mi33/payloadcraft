# payloadcraft.com — Hugo site

Hand-rolled Hugo theme, **"field manual" design system** — engineering-print aesthetic:
blueprint grid, registration marks, document-control blocks, a ledger, ink stamps and a
barcode. Two type voices: **Fraunces** (the engraver) + **IBM Plex Mono** (the engineer).
No framework, no trackers, effectively no JS (one line for theme persist + one for the
toggle), deployed free on GitHub Pages.

## The design system (what makes it look this way)

| Piece | Where |
|-------|-------|
| All colors / type / spacing tokens | `themes/payloadcraft/assets/css/main.css` → the two `:root` blocks (light "paper" + dark "carbon") |
| Blueprint grid + paper grain + registration marks | `.grid-overlay` / `.paper-grain` in `baseof.html` + CSS (pure CSS, zero requests) |
| Document-control masthead (DOC / REV / CLASS) | `layouts/partials/header.html`, values from `hugo.toml` → `[params] docNo` |
| Hero poster + SPEC/STATUS panel + barcode | `layouts/index.html` |
| Ledger rows, year bands, section bands | `list.html`, `index.html` |
| Syntax colors (custom chroma palette) | `main.css` → "chroma" section; enabled by `noClasses = false` in `hugo.toml` |
| Dark mode | auto via `prefers-color-scheme`, manual via the LIGHT/DARK button (persists in localStorage) |
| Social card | `static/og.png` — regenerate with `python3 scripts/make_og.py` |
| Fonts (self-hosted, no external requests) | `static/fonts/` — Fraunces variable + IBM Plex Mono (Fontsource builds) |

## 0. Install Hugo (once)

```bash
# macOS
brew install hugo

# Windows
choco install hugo-extended

# Linux (debian/ubuntu)
wget https://github.com/gohugoio/hugo/releases/download/v0.148.2/hugo_extended_0.148.2_linux-amd64.deb
sudo dpkg -i hugo_extended_0.148.2_linux-amd64.deb

hugo version   # verify
```

## 1. Preview locally

```bash
cd payloadcraft
hugo server -D          # -D includes drafts
# → open http://localhost:1313
```

## 2. Push to GitHub

```bash
git init
git add .
git commit -m "payloadcraft v1 — field manual"
git branch -M main
git remote add origin https://github.com/YOURHANDLE/payloadcraft.git
git push -u origin main
```

## 3. Turn on GitHub Pages (2 clicks)

Repo → **Settings → Pages** → *Build and deployment → Source* → **GitHub Actions**.
Push (or re-run the workflow) → site live at `https://YOURHANDLE.github.io/payloadcraft/`.

## 4. Point the domain (Spaceship DNS panel)

| Type  | Host | Value                 | TTL  |
|-------|------|-----------------------|------|
| A     | @    | 185.199.108.153       | auto |
| A     | @    | 185.199.109.153       | auto |
| A     | @    | 185.199.110.153       | auto |
| A     | @    | 185.199.111.153       | auto |
| CNAME | www  | YOURHANDLE.github.io. | auto |

Then repo → **Settings → Pages → Custom domain** → `payloadcraft.com` → Save.
Wait for DNS (minutes–hours), then toggle **Enforce HTTPS**.

DNS check before switching: `dig +short payloadcraft.com A` should return those four IPs.

## 5. Write

```bash
hugo new content blog/my-post.md    # creates draft
hugo server -D                      # preview it
# flip `draft: true` → `false` in the file, then:
git add . && git commit -m "post: my-post" && git push   # auto-deploys
```

## File map (what to edit)

| Path | Controls |
|------|----------|
| `hugo.toml` | title, description, author, nav menu, doc number, motto, code palette flag |
| `themes/payloadcraft/assets/css/main.css` | **the entire design system** — edit the `:root` token blocks |
| `themes/payloadcraft/layouts/` | HTML structure per page type |
| `content/_index.md` | homepage intro text (feeds the hero brief) |
| `content/blog/` | posts (`.md` files) |
| `content/about/index.md` | about page |
| `content/projects/index.md` | projects page |
| `content/uses/index.md` | uses page |
| `static/favicon.svg` | favicon (the reticle mark) |
| `static/og.png` | social card (regenerate: `python3 scripts/make_og.py`) |
| `.github/workflows/hugo.yml` | deploy pipeline |

## Gotchas

- **Post not showing up?** Check `draft: false` is set AND the `date:` isn't in the future (Hugo skips future-dated pages by default). Set `slug:` in front matter for clean URLs.
- **After renaming menu items**, edit them in `hugo.toml` under `[[menus.main]]`, not in the theme.
- **Changing the accent red?** It lives in 2 token blocks (light + dark) at the top of `main.css`, plus the `mk-dot`/favicon/og script if you want full consistency.
- **Dates in copy** use Go layout tokens — they're case-sensitive (`Jan` works, `JAN` prints literally).
- **Hosting anywhere**: self-hosted fonts use relative paths, so the site works at a domain root *or* a subpath (`user.github.io/repo/`) out of the box.

## Design rules baked in (keep them)

1. Two voices only: Fraunces for display, IBM Plex Mono for everything else
2. One accent (signal red) on warm paper / carbon — no gradients, no rounded-glass cards
3. Blueprint grid, grain and registration marks are CSS-only — zero image requests
4. Auto dark mode + manual toggle, ~1 line of JS each, site fully readable with JS off
5. Full-text RSS at `/blog/index.xml`
6. No trackers, no cookie banner, no external requests (fonts self-hosted)
7. Every post reproducible: commands, configs, or verifiable results
