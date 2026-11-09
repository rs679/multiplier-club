# Codex brief: lifecycle engagement emails for registered platform users (via Brevo)

Paste everything below the line into Codex, inside the platform repository.

---

## Goal

New sign-ups to the Multiplier platform should keep coming back. Registered users of all three types (investors, sponsors and asset managers, advisers and intermediaries) should be gently guided to finish setting up, take the first useful actions, and discover key features, so that nobody signs up and then forgets about us.

You already built the transactional emails (verification, notifications, and so on). This brief is about a separate layer: automated **engagement (lifecycle) emails** sent through **Brevo**. You decide the exact emails, content, design, timing and technical set-up, within the goals and guardrails below. Where something is unclear, make a sensible choice, write down the decision, and carry on.

## What success means

- More new users complete their profile in their first 7 days.
- Shorter time to the first meaningful action for each type. Examples: investors finish verification and look at opportunities; sponsors complete their firm profile and add a raise; advisers onboard a first client and invite clients or colleagues.
- Users who go quiet are reminded once or twice, then left alone.
- Healthy sending: unsubscribes under about 0.5% per email, spam complaints under 0.1%.

## What we want you to design

1. **Journeys per user type.** For each of the three types, a short sequence over roughly the first 30 to 60 days that nudges the next most valuable step (finish profile, verify, add a deal or raise, invite clients, advisers or network, share a raise, view opportunities, discover a feature). Decide the steps, order and delays yourself, based on what the platform actually offers.
2. **Behaviour-aware.** Emails must reflect what the user has already done. Never ask someone to do something they have already done. A sequence stops as soon as its goal is reached; someone who completes the step should move on, not keep getting the nudge.
3. **Milestone emails** triggered by actions (for example verification complete, first deal added, first client invited, an invitation that has not been accepted after a few days, first document signed), where it helps.
4. **A light ongoing rhythm** after the onboarding window: an occasional product-updates email, and a final "still interested?" step for inactive users. Move people who never engage into a low-frequency state and eventually stop emailing them.
5. **Content ideas to use where relevant:** Insights articles on the public site (private equity, venture, real assets, private credit, secondaries, special situations, collectibles and fine art, litigation finance) can be linked for education.

## Data and technical expectations (you choose how)

- The platform must tell Brevo what users do. Decide and document the contract. At minimum we expect: contact attributes (user type, first name, sign-up date, profile completion, verification status, last login, counts of key actions such as deals added and clients invited) and events (account created, profile completed, verification started and completed, deal added, client invited and accepted, document signed, login).
- Use Brevo's contacts and events APIs and Brevo automations. Keep it server-side. Secrets only through the secure mechanism of the platform; never in code, logs or chat.
- Keep platform users separate from the **website subscriber lists** that already exist in Brevo (investor 6, sponsor 7, adviser 8). Do not mix them. A person can be in both; avoid duplicate sends if both apply (a registered user should not also get website-subscriber emails that duplicate lifecycle ones).
- Transactional emails stay transactional; do not send marketing content in them.
- Be idempotent and safe: retries without duplicate sends, no personal data in logs, no failure that blocks a normal platform action.
- Frequency guardrails: no more than one lifecycle email every few days per person, sensible local sending times, exclude people who unsubscribed or whom support has flagged, and stop all sequences for closed accounts.
- Provide a test mode: a way to run each journey on a dummy account per user type, with shortened delays, without emailing real users.

## Guardrails (must follow)

- **No deal specifics or returns in emails.** No names of opportunities, amounts, percentages, performance or terms. Deal-specific emails to investors can be financial promotions in some countries. Use "something new is available, sign in to see it", and keep specifics inside the platform.
- **No unapproved claims.** Never use "vetted", "verified deals", "approved", "guaranteed", "safe", "best", "AI due diligence". For the screening point, use only this wording: "We screen sponsors and issuers for regulatory status and track record before listing. We do not underwrite, recommend or endorse any individual product."
- **"Verified"** is only for a person's identity or status, never for a deal.
- Plain, calm, premium tone matching the brand: short, specific, one clear action per email, no hype, no exclamation marks, no urgency tricks.
- Every email: company name and postal address in the footer (use the details in the platform config; do not invent any), one-click unsubscribe and a link to manage preferences, a real reply-to address that is monitored, no tracking pixels beyond Brevo's standard open/click tracking if we choose to keep it, no images that carry meaning without alt text, text version included.
- Consent: confirm with the owner whether these are treated as service messages or require a separate opt-in at registration. Our recommendation is a clear, separate, unticked checkbox at registration for non-service emails, honoured in Brevo. Implement whichever the owner confirms; default to the recommendation and flag it.
- Accessibility and mobile first: single column, 600px max, 16px minimum body text, strong contrast, dark-mode safe, works in the main clients (Gmail, Apple Mail, Outlook).
- Brand: Multiplier brand kit (`multiplier-brand-kit/design-system/tokens.css`, logo solid black on light). Email-safe fonts (Geist will not load in most clients; use a clean system stack), teal only as a signal (the button), hairlines, no shadows or gradients.

## Sender setup assumptions

- The domain `multiplier.club` is authenticated in Brevo (DKIM, SPF, DMARC), and a separate sender for lifecycle mail exists (for example `updates@multiplier.club`, name "Multiplier"). The existing `access@multiplier.club` is used by internal alert emails; do not use it for lifecycle emails. If something is missing, say exactly what the owner has to do.

## Deliverables

1. A short design document (one or two pages): journeys per user type with triggers, delays, exit conditions and the goal of each email; the attribute and event contract; list and segment structure in Brevo; frequency rules.
2. The implementation: events and attributes sent from the platform, Brevo automations and templates set up (via API or scripts we can re-run), test mode, and tests.
3. All email copy in one place (subject, preview text, body, button label, per user type), reviewed against the guardrails above.
4. A QA checklist and a send-to-yourself walkthrough for the owner (one dummy account per type), including how to check results in Brevo.
5. A measurement plan: which Brevo reports and which platform metrics tell us if activation improved, and a simple weekly view.
6. A list of anything you could not decide or do, plus decisions that need the owner (consent model, missing sender, missing company details).

Do not send to real users until the owner approves after the test walkthrough. Launch to **new sign-ups only** (no backfill of existing accounts) unless the owner says otherwise.
