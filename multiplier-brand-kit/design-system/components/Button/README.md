The Multiplier action control, available as a solid `primary`, an outlined `secondary` or a text-only `ghost`.

- One `primary` per view, for the main action ("Become a partner", "Start a conversation"). Use `secondary` for the alternative ("Log in", "View deals") and `ghost` for tertiary links.
- Labels are sentence case and say what happens. No icons are required; if you add one, keep it 16px, 1.5px stroke.
- `size="lg"` (56px) is for hero actions. The default is 48px, above the 44px touch minimum.
- Pass `href` for navigation (renders an anchor); use `onClick` for in-page actions. The consumer provides the label and handler.
- Corners are always `radius-sm`. Do not make pill buttons or add shadows.
- Disabled buttons drop their fill; always explain why next to the control.
