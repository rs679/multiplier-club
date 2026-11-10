# Codex brief: transactional emails, adviser insights and owner controls

Paste everything below the line into Codex, inside the platform repository. It adds to `platform-next-build-brief.md`, `lifecycle-emails-brief.md` and `legal/CODEX-legal-documents-and-access-brief.md`.

---

## How to read this brief

You own the design and the build. This brief says what we want to achieve and the guardrails. How you do it, and in what order, is your call. Please reply with a short design note and say where you would do it differently.

The owner wants to run the platform **lean** and keep **control of the whole process**: few people, few tools, and a single place to see and act on everything.

## 1. Transactional emails triggered by actions

The lifecycle brief covers engagement emails. This covers emails that follow a specific action or status change. Suggested events, to adjust as you see fit:

**Everyone**
- Account created; email confirmation; sign-in from a new device; password or passkey change.
- A document they signed has been countersigned (with a link to their copy in the platform).
- A document they accepted has a new version that needs accepting before their next relevant action.
- Something on their checklist is waiting on them, or has been waiting a while.

**Investors**
- Identity check passed, or more information needed.
- Eligibility confirmed; eligibility due for renewal.
- Access granted to a product's details or data room.
- Interest registered; subscription pack ready; subscription submitted; accepted by the sponsor; funds received by the sponsor or administrator; confirmation certificate available.
- New document or "what changed" note in a data room they have opened.
- Upcoming date for a product they hold (notice period, capital call, distribution, maturity), once the monitoring features exist.

**Advisers**
- Firm agreement countersigned; firm checks complete; colleague joined.
- A client accepted their invitation, completed onboarding, opened a product, registered interest, subscribed, funded.
- A client has stalled at a step for a set number of days.
- Fee statement available; payout made; clawback applied.
- Referral: an introduced firm signed up, onboarded, or generated its first funded investment.

**Sponsors**
- Screening application received; more information needed; screening outcome.
- Listing agreement or product schedule countersigned; product live.
- New interest, subscription submitted, investor ready for countersignature.
- Representations certificate due for renewal (with reminders), and product suspended if it lapses.
- Invoice issued; payment received; quarterly certificate due.

**Multiplier admin**
- A daily summary of items needing action (see section 3) rather than one email per event.

Guardrails (must):
- Emails do not contain product names, terms, returns, fees or identifying details. They say something happened and link into the platform, where the gates apply.
- Wording follows the brand kit and avoids the banned words in the main brief.
- Security emails cannot be switched off. Everything else respects the user's notification settings and local consent rules.
- Each email that relates to a client, product, document or fee is recorded in the audit trail.

## 2. Engagement insights for advisers

Goal: give advisers useful information about their own clients' activity, so they know who to follow up with and when. This is a reason for advisers to come back to the platform every day.

Ideas (choose, combine or replace):
- Per client: last sign-in, onboarding progress and where they are stuck, products viewed, time spent on a product's page and documents, documents opened or downloaded, questions asked, interest registered.
- Per product on the adviser's shelf: how many of their clients viewed it, opened the data room, registered interest, subscribed.
- A simple "who to call today" list (for example, clients who spent time on a product but have not registered interest, or who are stuck on a step).
- A weekly digest by email, with the detail inside the platform.
- For a firm's team lead: the same view across the team.

For sponsors, consider aggregated, anonymised funnel data per product (views, data-room opens, interest, subscriptions), with no investor identity until the investor has consented to share with that sponsor.

Guardrails (must):
- Investors are told that their activity on products is shared with their linked adviser, and with the sponsor where they consent. The investor documents and privacy notice already cover this; check that your implementation matches them (`legal/PLT-02`, `legal/INV-04`).
- An adviser sees only their own clients; a sponsor sees only its own products.
- Insights are for follow-up, not product recommendations. Do not rank or label clients by likely investment size, or rank products by fee.
- Use only first-party analytics for this. No personal data goes to third-party analytics or advertising tools.
- Keep personal data out of application logs, and apply the retention periods in the privacy notice.

## 3. Owner controls (lean operations)

Goal: the owner can run day-to-day operations from one admin area, without other tools or engineering help. Suggestions:

- **One action queue:** documents to countersign, screening decisions, identity or firm checks needing review, sponsor event submissions, complaints, flagged content, and payouts ready to release.
- **Switches:** suspend or reinstate a user, a firm, a sponsor or a product instantly, with a reason recorded.
- **Document versions:** publish a new version of any legal document, mark it as a material change or not, and see who still needs to accept it.
- **Money view:** fees invoiced, received and outstanding from sponsors; adviser shares and overrides due, held back, paid and clawed back; an export for the accountant. Payouts stay manual (record only) for now.
- **Compliance calendar:** eligibility and declaration refreshes, sponsor certificate renewals, adviser regulatory status re-checks, periodic sanctions re-screening.
- **Owner dashboard:** registrations, onboarding completion, time to verified, active advisers, invitations sent and accepted, products live, interest, subscriptions, funded amounts, fees earned. Daily and weekly.
- **Exports:** audit trail per user, firm and product; signed documents; consents.
- **Roles for future staff:** least privilege, so the owner can later add an operations or compliance person with limited access.

## Deliverables

1. A short design note covering the three areas, with what you would build first.
2. The implementation behind feature flags, with tests using fictional data only.
3. A short walkthrough for the owner.
