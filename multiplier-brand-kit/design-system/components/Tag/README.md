A small mono label for asset classes and deal status.

- Always contains a word: "Open", "Closing soon", "Fully subscribed", "Private equity". Colour alone never carries the meaning.
- `neutral` for categories; `accent` for open or positive states; `caution` for closing soon; `critical` for closed or failed states.
- Text is uppercase by style; type it in sentence case.
- Tags are labels, not controls: do not make them clickable. For filters, use `Button` with `variant="secondary"`.
