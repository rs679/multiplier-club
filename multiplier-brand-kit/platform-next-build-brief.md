# Codex brief: next platform build (suggestions, not a spec)

Paste everything below the line into Codex, inside the platform repository.

---

## How to read this brief

This is a set of **suggestions and goals**. You know the platform's code, data model and constraints better than we do. For every item: confirm it fits, change it where you see a better way, say what you decided and why, and flag anything that conflicts with what already exists. Where we say "must", it is a guardrail (legal, safety or an owner decision). Everything else is a suggestion.

Please start with a short design document and a phased plan, share it, and only then build.

## Context

Multiplier is a technology platform connecting regulated advisers, deal sponsors and eligible investors in private markets. The next build should strengthen a three-sided loop:

1. **Advisers bring clients.** One adviser invites many clients, so adviser tooling drives growth.
2. **Each client's verified profile is reused.** One onboarding, then every subscription is mostly pre-filled.
3. **Sponsors list where the advisers are,** with a digital subscription process that fits their own requirements.

Main audience for advisers: private bankers, wealth managers and asset managers, plus independent advisers. Test every idea against: does it bring a new person in, get them verified faster, or give them a reason to come back?

## Decisions already made (treat as fixed)

- **Not an aggregator.** No off-platform holdings. The client dashboard covers only products transacted through Multiplier.
- **No investor fees** at launch.
- **Multiplier controls distribution terms.** Sponsors pay Multiplier (a screening fee, a listing fee and a success fee on funded capital); Multiplier pays introducers, **paid-when-paid**, under firm-level distribution agreements. Fee schedules, entitlements and disclosures sit with Multiplier.
- **Screening wording:** use only: "We screen sponsors and issuers for regulatory status and track record before listing. We do not underwrite, recommend or endorse any individual product."
- **Terms stay behind registration and eligibility confirmation,** as on the website ("Terms: view after registration"). Nothing in an invite, QR code or wallet pass carries product terms or returns.
- No US persons, consistent with the Terms.

## Success looks like

- More advisers send invites in their first week, and more invitees reach verified status quickly.
- Fewer repeated forms: a returning client reaches "ready to subscribe" in minutes.
- Sponsors can launch a subscription with their own requirements without engineering help.
- Clients and advisers return for dates, notices and documents, not only for new deals.
- Every action involving a client and a product has an audit trail.

## Suggested scope

### Phase 1: the loop

**1. Adviser invites and tracking**
- Invite a client to one product, a hand-picked shortlist, or the adviser's whole shelf, through a unique tracked link.
- Channels (suggested): email, copy-link, SMS, and WhatsApp as a **click-to-chat link with a pre-filled message sent from the adviser's own number**. Do not build WhatsApp Business API automation yet.
- **QR codes:** one per event or campaign, so the adviser sees which events produced sign-ups.
- **Co-branded invite page:** adviser name, firm and logo, a short personal note, a clear path to register. Neutral content only.
- **"Bank mode" (per firm setting):** email and tracked links only, with WhatsApp and SMS disabled and a fuller audit log, because many banks restrict personal channels.
- Pipeline for the adviser: invited, opened, registered, verified, interested, subscribed, funded. Resend and reminder actions, notes, tags. Team view for a principal or desk head.

**2. Reusable client profile and standard subscription**
- One verified profile (identity, eligibility category, tax residency and self-certifications, source of funds, sanctions screening, consents) reused across products.
- A standard Multiplier subscription pack, pre-filled from the profile, with a clear "what is new for this product" step.
- Status triggers: compliance checks start automatically at a set subscription status.

**3. Sponsor module v1**
- A way for a sponsor to add its own requirements on top of the standard pack: extra questions (with conditional logic), extra documents, side-letter requests, signature blocks, payment instructions. Versioned templates, reusable across products. A builder UI is a suggestion; a configuration file with an admin review step may be enough for v1.
- A status tracker for every investor in a raise, and a simple closing flow: allocation, countersignature, confirmation certificate.
- **Distribution controls:** the sponsor can restrict which advisers, countries and investor categories see a product. Treat this as a compliance gate, not just a setting.

**4. Fee and entitlement ledger (record only)**
- Store the fee schedule per product and per adviser firm, and record entitlements when a subscription is funded and settled. Generate the **client remuneration disclosure** automatically for each product.
- Support a **waiver or rebate** option for the adviser share.
- Do not build automatic payouts yet. Make the data easy to export for finance.

### Phase 2: stickiness

**5. Client decision support**
- A one-screen **deal card**; a **key-terms table** in the same order for every product (fees, security, ranking, redemption, governing law); a structure view; the data room with versioned documents and "what changed" notes; sponsor Q&A; clearly sourced research.
- **AI helper (optional, careful):** explain jargon and summarise documents, labelled as generated, linked to the passage each statement comes from, never stating or implying suitability.

**6. Client monitoring dashboard**
- Calendar and timeline for Multiplier products only: coupons or interest dates, capital calls, distributions, redemption windows and notice periods, maturities, lock-up ends, document deadlines. Cash-flow forecast by month and currency. Latest reported value with its date and source, labelled "estimate" where it is not a market price.
- Alerts by email and in-app, a **calendar feed (ICS)**, and a document vault. With the client's consent, the adviser sees the same view.
- Sponsors submit events in a standard format (type, date, amount, currency, status) by form, upload or API. Fund-administrator feeds can come later.

**7. Adviser workbench**
- Shelf curation (clients see only what the adviser shares), side-by-side comparison on the standard fields, and a branded fact sheet or meeting pack built from the deal card.
- **Compliance file, auto-built:** what was shown to which client, when, with which consent and document versions.
- Alerts for new listings matching the adviser's criteria, terms changes and closing windows.

**8. Wallet invite card (small)**
- An Apple Wallet and Google Wallet pass holding the adviser's QR code to their invite page, updateable remotely. Also usable as an event pass. Identity and a link only; no product content. Choose between direct integration (Apple pass certificate, Google Wallet issuer account) and a third-party pass service.

**9. Adviser points and leagues (feature-flagged)**
- Points, leagues and badges for advisers. **Important: build the scoring as a separate, configurable rule set behind a feature flag.**
- **Our recommendation (and what we ask you to build first):** product-neutral points. The same points for the same action on any product regardless of the fee it pays: verified client onboarded, client active in the last 30 days, completed onboarding rate, advisers or colleagues invited, compliance file completeness, response time. Cap points from any single sponsor or product. Publish the rules. Opt-in visibility with percentile bands instead of exact client counts. Time-boxed leagues, plus team and firm boards (firm boards stay inside the firm). Rewards that are not cash and not product-linked (earlier access to listings, events, co-marketing, a verified-adviser badge).
- **Owner preference to be aware of:** the owner would like the score to reflect commission generated, shown as an opaque points score. We advised against it: the regulatory concern is the incentive, not the display, and it would favour higher-fee products. **Do not ship a commission-linked score until counsel has reviewed it for each jurisdiction.** Please keep the scoring rules isolated so either version can be switched on after review, and flag the risks you see.

### Phase 3: scale (for planning only, do not build yet)
Fund-administrator feeds, capital call and distribution notice builder, sponsor funnel analytics, indications of interest by adviser, WhatsApp Business automation, API and CRM integrations (HubSpot, Salesforce), single sign-on for banks, multi-language and right-to-left support (Arabic, Portuguese, Spanish, Thai, Malay), mobile-first progressive web app, discretionary-manager workflow (authorised signatory or power of attorney, with each client's eligibility still checked), recognised security certification.

## Guardrails (must)

- **No promotions in channels.** Invites, QR codes, wallet passes, WhatsApp text and emails carry neutral content only: who is inviting, what Multiplier is, how to register. No terms, returns, fees or performance.
- **No unapproved claims.** Never use "vetted", "verified deals", "approved", "guaranteed", "safe", "best" or "AI due diligence". "Verified" applies only to a person's identity or status.
- **Gating:** product terms and documents only after registration, eligibility confirmation and any sponsor or jurisdiction restriction are satisfied. Log every access.
- **Consent and data separation:** a client's data goes to an adviser or sponsor only with clear permission, and is kept separate between sponsors. WhatsApp, SMS and marketing messages need opt-in and an easy opt-out.
- **Audit trail:** every action touching a client, product, document or fee is logged and exportable.
- **Roles and permissions:** adviser, team lead, firm admin, sponsor, sponsor admin, Multiplier admin, client. Firm-level agreements and payments, not only individual.
- **Security:** passkeys or two-factor, least privilege, no secrets in code, logs or chat, no personal data in logs.
- **Accessibility and mobile first.** Match the brand kit (`multiplier-brand-kit`).
- **Do not use any customer data in tests;** use fictional data only.

## Non-goals
Off-platform holdings or any aggregation; investor fees; automated adviser payouts (record only for now); public rankings by sales, fees or any single product; product recommendations or suitability statements; any content that works as a financial promotion outside the gated area.

## Deliverables

1. A short design document: architecture changes, data model, roles and permissions, the invite flow, the subscription-module approach, the ledger, and the points scoring isolation. Include your decisions where you disagree with a suggestion.
2. A phased delivery plan with estimates and dependencies, plus the open questions you need answered.
3. The implementation per phase, with tests (unit, permissions and gating, audit trail), and a feature-flag setup.
4. A QA walkthrough for the owner using dummy advisers, clients and sponsors, and a security and privacy checklist.
5. A list of anything you could not do, and decisions needed from the owner or from counsel.

Do not release to real users until the owner approves after the walkthrough. Launch Phase 1 to a small group of advisers first.
