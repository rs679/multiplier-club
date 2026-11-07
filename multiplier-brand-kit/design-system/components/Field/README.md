A labelled text input with an optional hint or error message.

- The consumer provides `label` (required, sentence case), and optionally `hint`, `placeholder`, `error`, `type`, and either `value` with `onChange` or `defaultValue`.
- Every input has a visible label; the placeholder is only an example, never the label.
- Errors replace the hint, render in `critical`, mark the input invalid and are linked with `aria-describedby`. Write errors that say how to fix the problem.
- 48px high, `radius-sm`, `border-control` border, `bg-raised` fill. Do not add shadows or floating labels.
