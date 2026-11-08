# Codex brief: platform UI snippets for the Multiplier website

Paste everything below the line into Codex, inside the platform repository.

---

## Goal

Produce six marketing-safe screenshots of the Multiplier platform, shot from a demo mode that runs on fictional data. They replace the "Example" placeholder mock-ups on the public website (Home, For investors, For sponsors, For advisers). Nothing in this task may touch, read or expose real data.

## Rules (must not be broken)

1. **Demo mode only.** Add a demo mode that is switched on by a build-time flag (for example `VITE_DEMO=1` or `NEXT_PUBLIC_DEMO=1`) and is **compiled out of production builds**. It reads only from a local seed file (`demo/seed.ts`). It must make no calls to the real API, database, auth, Brevo or any third party. Add a test that fails if the demo route or seed is present in a production build.
2. **Fictional everything.** People: obviously fictional names such as "Alex Example" or "Sam Sample". Firms: "Example Capital", "Sample Advisory". Deals: "Example Growth Fund I", "Example Solar Portfolio", "Example Private Credit Note". No real companies, funds, banks, people, emails, phone numbers or addresses.
3. **No fees anywhere.** Hide every fee, referral fee, commission and platform-fee field and column in the demo views.
4. **No returns and no performance.** No percentages, IRR, yield, target return, multiple, or "performance" chart. Counts (for example "12 investors") and clearly round sample amounts (for example "$100,000 minimum") are allowed only when a small "Sample data" tag is visible in the screenshot.
5. **No unapproved claims.** Do not show "AI due diligence", "vetted", "verified deal", "approved by compliance" or similar. Status words allowed: Open, Closing soon, Fully subscribed, In review, Invited, Verified (this last one only for **client identity or status verification**, never for a deal).
6. **Brand.** Light theme (`data-theme="light"`), Geist (weights 300, 400, 500) and Geist Mono for small labels, 4px corners, 1px hairline borders, no drop shadows, no gradients, teal used as a signal only (`--accent`, `--action`). Use the real Multiplier logo (solid black on light). Follow `multiplier-brand-kit/design-system/tokens.css`.
7. **Clean capture.** No browser chrome, no dev tools, no cookie banner, no toasts, no cursor, no scrollbars, no real URL in view.

## The six screens

Each must look like a real, calm, premium product screen, not a template. Use realistic layout density.

1. **Investor: Opportunities.** A list or card grid of 4 fictional deals. Each shows name, asset-class tag (Private equity, Real assets, Private credit, Venture), region, status word, and "Terms: view after registration" or a clearly round sample minimum with the Sample data tag. One filter row by asset class.
2. **Investor: Portfolio overview.** A summary of 3 fictional commitments with status, a documents list (Subscription agreement, Information pack, Statement) and a simple status timeline. No chart of performance.
3. **Sponsor: Raise overview.** A fictional raise with a list of interested investors by stage (Invited, In review, Committed), a count of each stage, a documents area, and a "Share with advisers" action. No fee fields.
4. **Adviser: Clients.** A table of 6 fictional clients with status (Verified, In review, Invited), country, and the number of opportunities each is reviewing. A side panel shows one client's checklist ("Onboarded once", documents received, status). This screen must visually communicate "one verification, reused across every opportunity".
5. **Subscription document.** A document view with a short page preview, a signature box with a fictional signature, and a step indicator (Review, Sign, Fund, Confirmed).
6. **Onboarding.** A step-by-step verification flow on step 2 of 4 (Your details, Verify status, Documents, Done), with a progress indicator and one clear primary button.

## Output

- Use Playwright. Viewport **1600 x 1000**, `deviceScaleFactor: 2`, light theme. Wait for fonts to load. Disable animations.
- Export to `exports/website-snippets/`:
  - `01-investor-opportunities.png` through `06-onboarding.png` (desktop).
  - Mobile versions at **390 x 844**, scale 2, for screens 1, 4 and 6: `01-...-mobile.png`, `04-...-mobile.png`, `06-...-mobile.png`.
  - `manifest.json` with, for each file: filename, one-sentence alt text, the website page it is meant for (Home, Investors, Sponsors, Advisers), and the pixel size.
- Optimise PNGs so each desktop file is under 700 KB and each mobile file under 350 KB, without visible loss.
- Round the screen corners by 8px and leave a transparent margin of 0 (the website adds its own frame).

## Acceptance checklist (print this at the end, with pass or fail for each)

- [ ] Demo mode is off and absent in the production build (test included).
- [ ] No network request leaves the machine during capture.
- [ ] No fee, percentage, return, IRR, yield or performance chart is visible in any image.
- [ ] No real names, companies, emails or numbers.
- [ ] Every image with an amount shows the Sample data tag.
- [ ] No "AI", "vetted" or compliance-approval wording.
- [ ] Fonts, corners, hairlines and colours match the brand tokens; no shadows or gradients.
- [ ] File sizes and count are as specified, and `manifest.json` is complete.

When finished, commit the demo mode and the export script on a new branch named `demo-ui-snippets` (do not merge to main), and tell me the path of the `exports/website-snippets/` folder.
