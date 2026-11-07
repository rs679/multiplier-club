Multiplier is a curated private-markets platform. Advisers introduce vetted alternative investments to their clients and earn a disclosed referral fee. The identity is dark-first, quiet and precise: premium through restraint, never through decoration.

## Principles

- **Considered.** Every element earns its place. If it does not help the reader decide, remove it.
- **Quiet.** Confidence without volume: light type, deep grounds, one teal signal.
- **Precise.** Exact geometry, exact spacing, exact words. Detail is the premium signal.

## Name

- The brand is **Multiplier**. Never "Multiplier Club". `multiplier.club` is only the web address and may appear in URLs, email addresses and footers.
- In running text, write "Multiplier" with a capital M. The logo wordmark is set in lowercase, "multiplier".

## Content fundamentals

- Speak to the adviser as a peer: "you" for the reader, "we" for Multiplier. Plain, specific and calm.
- Sentence case everywhere, including buttons and headings. Uppercase is only for mono labels (`label`).
- No exclamation marks, emoji, superlatives or urgency language. Never promise returns.
- Name things by what the adviser recognises: "referral fee", "minimum investment", "diligence summary".
- Real examples: "Become a partner", "Start a conversation", "Referral terms are shown on each deal.", "Capital at risk."
- Every deal and fee figure must be disclosed where it is shown. Regulatory wording is supplied by compliance; do not paraphrase it.
- More in `voice.md`.

## Visual foundations

- **Dark first.** The page is `bg`. Raised surfaces use `bg-raised`; quiet bands use `bg-pine` and `bg-navy`. The light theme swaps these values and is for documents and long reading.
- **Text.** Headings and key text in `ink`; body copy in `ink-muted`; mono labels, captions and placeholders in `ink-subtle`.
- **Teal is a signal.** Use `accent` for links, eyebrows and current state; `action` for primary button fills; `teal` for decorative blocks. Roughly 60% neutral grounds, 30% dark surfaces, 10% teal. Teal never appears in the logo.
- **Type.** Geist in light weights (300 for display and headings, 300 to 400 for text) with tight tracking at large sizes; Geist Mono, uppercase and tracked, for labels. Set headlines with `display`, `display-sm`, `heading-1`, `heading-2`; body with `body`; interface text with `body-sm`; eyebrows with `label`. Never bold a headline; never italicise.
- **Spacing.** Use the `space-*` scale. Sections are at least `space-9` apart; cards pad with `space-6`; grid gutters are `space-5`.
- **Corners.** `radius-sm` (4px) for buttons, inputs, tags, cards and tables. `radius-md` for large panels. No pills, no fully rounded buttons.
- **Borders, not shadows.** Separate surfaces with 1px `border` hairlines. Controls use `border-control`. No drop shadows, no glows, no gradients except an atmospheric dark-to-teal radial behind a hero image.
- **Motion.** Slow fades and colour changes only, 200ms ease. No bounces, parallax or looping animation. Respect `prefers-reduced-motion`.
- **Focus.** A 2px solid `focus` ring with 2px offset on every interactive element.
- Imagery, layout and charts: `imagery.md`. Accessibility: `accessibility.md`.

## Logo

- The mark is two vesica lenses crossed at 90° with the overlap removed: four identical tips around an empty diamond. It is only ever solid white or solid black.
- White on dark and mid-tone grounds (`logo-white`), black on light grounds (`logo-black`). Use `logo` to follow the theme automatically.
- Use the `Logo` component in interfaces and the files under Assets for everything else. Full rules: `logo.md`.

## Iconography

- No icon set is bundled. Use simple 1.5px stroke icons, square caps, drawn on a 24px grid, in `ink-muted` or `accent`.
- Status always has a word or icon as well as colour.
- Never use emoji, filled pictograms or illustrated icons.

## Components

- Build interfaces from the `Multiplier` bundle: `Logo`, `Button`, `Tag`, `Field`, `Card`, `Nav` and `DealCard`. Wrap pages in an element with `data-theme="dark"` or `data-theme="light"`.
- Load Geist and Geist Mono from Google Fonts: `https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500&family=Geist+Mono:wght@400;500&display=swap`.
- The consumer supplies data, copy and links. Components never invent fees, returns or deal facts.
