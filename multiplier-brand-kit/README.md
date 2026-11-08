# Multiplier brand kit

Everything needed to build the Multiplier website and keep it on brand. Hand this whole folder to Codex.

Multiplier is a curated alternative-assets deal platform. Advisers introduce vetted private-market opportunities to clients and earn a disclosed referral fee. The brand name is **Multiplier** (never "Multiplier Club"); `multiplier.club` is only the web address.

## What is in the folder

| Path | What |
| --- | --- |
| `logos/svg/` | Master logo files: mark and full logo in white and black, plus the app icon. The wordmark is outlined, so no font is needed. |
| `logos/png/` | High-resolution transparent PNGs: marks 4096×4096, logos about 6000 px wide, app icon 1024×1024. |
| `design-system/tokens.json` | The source of truth for colour (dark and light themes), type, spacing and radius, with a usage note on every token. |
| `design-system/tokens.css` | The same tokens as CSS variables. Dark is the default; set `data-theme="light"` for light. |
| `design-system/tailwind.preset.js` | Tailwind preset that maps the tokens to utilities. |
| `design-system/components/` | React components (`Logo`, `Button`, `Tag`, `Field`, `Card`, `Nav`, `DealCard`) as a plain browser bundle, with CSS, TypeScript types, a README and a preview for each. |
| `design-system/demo.html` | Open in a browser to see the components together on a sample page. |
| `website-brief.md` | The website brief: goals, audiences, sitemap, page specs, decisions, requirements and open questions. |
| `go-live-runbook.md` | Launch-day steps, blockers, rollback and what is still open. |
| `platform-ui-snippets-brief.md` | Brief for Codex: marketing-safe platform screenshots from a demo mode. |
| `guidelines/` | Brand guidelines: `brand-guidelines.md` (start here), `logo.md`, `voice.md`, `imagery.md`, `accessibility.md`. |

## Rules that must not be broken

1. **The logo is only ever solid white or solid black.** Never teal, two-tone, outlined or with a filled centre. White on dark and mid-tone grounds, black on light grounds.
2. **Dark first.** Page ground is `--bg` (#060809). Text is `--ink`, `--ink-muted`, `--ink-subtle`.
3. **Teal is a signal, not a theme.** `--accent` for links and eyebrows, `--action` for primary button fills, `--teal` for decorative blocks only.
4. **Light type.** Geist at weight 300 for headlines and body, tight tracking at large sizes. Geist Mono, uppercase and tracked, for small labels. Load both from Google Fonts. Never bold a headline.
5. **Borders, not shadows.** 1px hairlines, 4px corners (`--radius-sm`). No drop shadows, no pills, no gradients except one dark-to-teal radial glow behind a hero.
6. **Always disclose.** Show the referral fee beside the minimum on every deal. Never invent figures, returns or regulatory wording. Use bracketed placeholders (`[amount]`, `[x]%`) until real values exist.
7. **Accessibility.** Keep the token pairings (they meet WCAG 2.2 AA in both themes), 44px minimum targets, visible focus (`--focus`), real `button`/`a`/`label` elements.

## Using the tokens

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500&family=Geist+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="design-system/tokens.css">
<html data-theme="dark"> ...
```

Type classes from the tokens: `.display`, `.display-sm`, `.heading-1`, `.heading-2`, `.heading-3`, `.body-lg`, `.body`, `.body-sm`, `.caption`, `.label`.

In a Next.js and Tailwind build: import `tokens.css` in the root layout, add `presets: [require('./design-system/tailwind.preset.js')]` to the Tailwind config, and load Geist and Geist Mono with `next/font/google`. Port the components in `design-system/components/bundle.js` to TypeScript React components in the project, keeping the class names and styles in `bundle.css`.

## Suggested build brief

Build the Multiplier marketing and adviser site as a Next.js (App Router), TypeScript and Tailwind app that follows the rules above.

**Pages**
1. **Home:** dark hero with the display headline "Access, curated." (or similar), a primary "Become a partner" and secondary "Browse deals"; a four-figure trust strip using placeholders; "How it works" in three steps (we curate, you introduce, you earn a disclosed fee); current opportunities (three `DealCard`s); adviser benefits; closing call to action; footer with the regulatory and risk-warning placeholder.
2. **Deals:** header, filter chips by asset class (private equity, venture, real assets, private credit), one featured deal, grid of `DealCard`s with status words.
3. **Deal detail:** thesis, key terms, referral fee, documents list, "Share with a client" action.
4. **Partner sign-up and log-in:** `Field`-based forms with validation and clear error messages.
5. **Partner dashboard:** introductions and their status, referral fees earned and pending.

**Engineering notes**
- Deals come from a typed data source (start with a local JSON or database table), not hard-coded markup.
- Referral fee and minimum are required fields on every deal.
- Gate deal detail and sharing behind partner authentication.
- Keep copy in plain, calm sentence case as described in `guidelines/voice.md`.
- Regulatory disclosure text is supplied by compliance; render it from a single editable source.
- Check both themes and phone width (about 400 px) before finishing.

## Open items for the owner

- Real deal data, fee terms and regulatory wording (all placeholders now).
- Confirm Geist and Geist Mono licensing and hosting preference (they are open-source and currently loaded from Google Fonts).
- Photography or generated artwork for heroes (dark, macro, organic, in teal and deep green).
