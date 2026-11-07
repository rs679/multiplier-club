# Imagery, layout and charts

## Imagery

- Dark, macro and organic: fine textures, filaments, cells and water in deep teal and green on near-black, in the spirit of scientific photography. No people, handshakes, skylines, stock offices or illustrated scenes.
- Photography sits on `bg` or `bg-navy`; crop tight and let it bleed off an edge. Corners: `radius-none`, or `radius-md` when framed.
- A single dark-to-teal radial glow may sit behind a hero. No other gradients.
- Overlay text only on the darkest part of an image, in `ink`, with at least 4.5:1 contrast.
- Generated or abstract graphics use the mark's construction: four equal circles, thin 1px lines in `teal` at low opacity, and the mark as a large ghost shape.

## Layout

- 12-column grid, 24px gutters (`space-5`), content max width 1280px, page side gutter 96px on desktop (`space-9`), 16px minimum on phones.
- Sections are at least `space-9` apart. A hero has `space-10` above and below.
- Alternate dark bands (`bg`, `bg-navy`, `bg-pine`) with, occasionally, one light band for relief. Do not stack more than three light surfaces.
- Left-align text. Keep running text under 65 characters wide. Use generous negative space; prefer one idea per band.
- Group with hairlines (`border`) and spacing, not boxes. Use a card (`bg-raised` with a 1px `border`) only for an object a user acts on, such as a deal.
- Tables: hairline row dividers, `body-sm`, numerals tabular, right-aligned numbers, mono labels as column headers.

## Charts

- Series colours in order: `chart-teal`, `chart-navy`, `chart-slate`. Never more than three series; group the rest as "Other" in `chart-slate`.
- Gridlines in `border`, axis text in `ink-subtle`, values in `ink`. Mark the highlighted value in `chart-teal` and label it directly.
- Never rely on colour alone: label lines and bars directly, or add markers and patterns.

## Motion

- 200ms ease for colour and opacity changes; 400ms for fades on entry. No movement over distance, no looping animation, no parallax.
- Honour `prefers-reduced-motion` by removing all non-essential transitions.
