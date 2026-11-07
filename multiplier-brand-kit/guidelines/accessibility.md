# Accessibility

The system targets WCAG 2.2 AA in both themes.

## Contrast

- Text meets 4.5:1 (3:1 at 24px or larger) on the surfaces named in its token's usage note, in both themes. Examples: `ink`, `ink-muted` and `ink-subtle` on `bg`, `bg-raised`, `bg-pine` and `bg-navy`; `on-action` on `action`.
- Meaningful non-text marks (input borders, focus rings, icons, chart series) meet 3:1: `border-control`, `focus`, `chart-teal`, `chart-navy`, `chart-slate`.
- `border` is decorative only. A control must never be identified by `border` alone.
- `teal` is a decorative fill. Do not set text in it on light surfaces.

## Status

- `positive`, `caution` and `critical` are never used alone: each comes with a word (for example "Open", "Closing soon", "Closed") and, where space allows, an icon.
- Teal and coral are separated in hue and by a word, not by hue alone.

## Interaction

- Interactive targets are at least 44px high. Buttons are 48px by default.
- Focus is always visible: a 2px solid `focus` ring, 2px offset.
- Use real `button`, `a`, `input` and `label` elements. Do not put click handlers on `div` or `span`.
- Every input has a visible label; errors are linked with `aria-describedby` and `aria-invalid`.
- The logo mark is decorative when beside the wordmark; as a standalone mark it has the accessible name "Multiplier".

## Motion and themes

- Respect `prefers-reduced-motion`.
- Respect the viewer's theme. Dark is the default; offer light for documents and print.
