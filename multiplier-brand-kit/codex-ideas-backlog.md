# Codex: ideas backlog for the Multiplier platform

Paste everything below the line into Codex, inside the platform repository.

---

## How to use this

These are ideas, not instructions. You decide what to build, in what order, and how. Please reply with:
1. a ranked shortlist, with rough effort, dependencies and what you would leave out;
2. anything here that conflicts with the existing code or another brief;
3. better ideas of your own.

Test every idea against four questions. Does it:
- **bring a new person in** (adviser, investor or sponsor)?
- **get them through onboarding faster**?
- **give them a reason to come back**?
- **give the owner more control with less effort**?

The owner wants to run the platform lean, with few people and few external tools, and keep control of the whole process.

Several ideas are already covered in other briefs in this repository. They are listed at the end so nothing is duplicated.

**Fixed points:**
- Owner decisions and the legal guardrails in `platform-next-build-brief.md` and `legal/CODEX-legal-documents-and-access-brief.md` stand: anonymised headline cards before gating, no product details in channels, consent before sharing data, a full audit trail, no investor fees, no off-platform holdings.
- Nothing may imply advice, suitability, a rating or endorsement of a product.

## Bringing people in

- **Shareable educational content with the adviser's tracking link.** Advisers share Insights articles, co-branded, with their invite link attached. The content is educational, so it is not a product promotion, and it gives advisers a reason to post every week. A new article is published every Thursday.
- **Client invites their adviser ("add my adviser").** An investor who arrives directly can invite their own adviser, which brings in new advisers.
- **Sponsor brings its distributors.** A sponsor can invite the advisers it already works with. They join as platform advisers under the normal agreements, and the sponsor gets one place to manage distribution.
- **Firm roll-out tools.** Once a firm is onboarded, the firm admin can invite colleagues in bulk and see who is set up.
- **Event mode.** A QR code for each event, a sign-up page for that event, and a follow-up list for the adviser afterwards.
- **Watchlists on headline cards.** Without registering interest, a user can ask to "notify me about new products like this" by asset class, sector and region. Matching works on the anonymised headline fields only.

## Getting through onboarding faster

- **Start on desktop, verify on phone.** A QR code hands the identity check over to the phone camera, then returns the user to their desktop session.
- **Adviser-assisted onboarding.** With the client's consent, the adviser pre-fills parts of the client's profile and the client confirms each item. The client always makes the declarations themselves.
- **Reuse for entity investors.** Company, trust and family-office investors keep their ownership structure, authorised signatories and documents on file. They are reused for every subscription and only updated when something changes.
- **Save and resume everywhere,** with a single progress indicator and a reminder if someone stalls.
- **Pre-fill from documents.** Read details from an uploaded ID or company document for the user to confirm, rather than typing them.

## Reasons to come back

- **Anonymised demand signals for sponsors.** Aggregated, consented interest data, for example "eligible investors in the GCC watching private credit". This helps sponsors decide to list. Never shows individuals.
- **Testing demand before a full listing.** A sponsor can publish a headline card to measure interest before the full listing goes live. This needs a compliance check by country first.
- **Sponsor Q&A** with shared answers visible to everyone who has access to that product.
- **Annual statement and tax pack** for each investor, covering Multiplier products only.
- **Closing reminders** for gated users who have shown interest.
- **Adviser meeting pack** built from the deal card for a client meeting, inside the gated area only.

## Control for the owner

- **Country and role switches.** Turn a country, an investor category or a role on or off without a release.
- **Pre-send checks on adviser messages and notes.** Messages sent through the platform are checked for banned words, product terms and identifying details, and blocked or flagged before they are sent.
- **Watermarked data-room documents.** Each viewer sees their name and the date on documents, with view-only or download controls set per product. This supports confidentiality and helps trace any leak.
- **AI-assisted listing.** Draft the standard key-terms table and headline card from the sponsor's information memorandum. The sponsor confirms and Multiplier reviews. AI output is labelled and linked to its source passage.
- **Tail tracking.** A register of Platform Investors for each sponsor, with the qualifying events and dates (eligible to view, invited, viewed, introduced), to support success fees during the 24-month tail.
- **Fees from the ledger to invoices.** Success fees calculated from closing reports, sponsor invoices issued, and adviser statements generated, all from one ledger, with exports for the accountant.
- **Status page and incident switch.** A simple way to show service status and pause sensitive actions during an incident.

## Trust and security

- **Passkeys,** device management, session time-outs, and alerts for new sign-ins.
- **Separation between sponsors** in data, documents and analytics, tested.
- **A periodic review of who has admin access.**

## Later (planning only)

- An Arabic interface, followed by other languages.
- Single sign-on for banks.
- CRM integrations.
- A secondary bulletin board for existing holdings (needs a regulatory view first).
- Workflows for discretionary managers.

## Already covered in other briefs

- `platform-next-build-brief.md`:
  - adviser invites and tracking, bank mode, the reusable profile and standard subscription
  - the sponsor module, distribution controls and fee ledger
  - the deal card and key-terms table, the AI helper and monitoring dashboard
  - the adviser workbench, wallet card, and points and leagues
- `lifecycle-emails-brief.md`: engagement emails.
- `operations-emails-and-adviser-insights-brief.md`: transactional emails, engagement insights for advisers, and the owner's admin area.
- `legal/CODEX-legal-documents-and-access-brief.md`: the legal documents and the gates at the point of action.
