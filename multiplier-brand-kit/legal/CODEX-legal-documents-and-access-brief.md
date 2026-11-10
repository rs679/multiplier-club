# Codex brief: legal documents, who signs what, and when

Paste everything below the line into Codex, inside the platform repository. It sits alongside `platform-next-build-brief.md`. The documents are in this folder (`multiplier-brand-kit/legal/`), all marked "draft for legal review".

---

## How to read this brief

You own the design and the implementation. This brief explains **what** the documents are, **who** accepts them and **when**, and the outcomes we need. **How** to build it (data model, gating mechanism, UI, providers, sequencing) is your call, based on what already exists in the platform.

Three kinds of content:
- **Owner decisions:** fixed commercial or product choices. Please build to them, and flag if you see a problem.
- **Legal requirements:** what the documents need in order to be effective (for example, who signs and what must be on record). Please meet them, in whatever way suits the platform.
- **Everything else:** context and ideas only. Change or ignore as you see fit, and tell us what you decided.

Please share a short design note before building.

## The principle (owner decision)

**Easy to join, gated at the point of action.**

- Sign-up should be as light as possible. The only documents at sign-up are the Platform Terms, the Privacy Notice and the Electronic Signature and Communications Consent.
- Everything else is asked for only when a user tries to do something that needs it: for example, an adviser requesting access to a deal, an investor viewing terms or subscribing, or a sponsor listing a product. At that point the user is guided to complete what is missing (agreements, identity checks, declarations, questions), and then gets on with what they were doing.
- What a user completes is kept on their profile and reused, so they do not repeat it.
- Until the required steps are complete, the action stays unavailable. Only then can an adviser share and sell deals, an investor see terms and subscribe, or a sponsor go live.

## The documents

| ID | Document | What it is for | Who accepts | When it comes up | How it is accepted |
|---|---|---|---|---|---|
| PLT-01 | Platform Terms of Use | Ground rules: what Multiplier does and does not do; no advice; products are the sponsor's responsibility | Every user | Sign-up | Click-through |
| PLT-02 | Privacy Notice | How personal data is used and shared | Every user | Sign-up | Acknowledged |
| PLT-03 | Electronic Signature and Communications Consent | Makes e-signatures and electronic notices binding | Every user | Sign-up | Click-through |
| PLT-04 | Data Sharing Schedule | Data terms between Multiplier, adviser firms and sponsors | Adviser firms and sponsors | Part of ADV-01 and SPN-02 | With those agreements |
| PLT-05 | Complaints Policy | How to complain | Nobody (published) | Always available | Not signed |
| PLT-06 | Content and Marketing Guidelines | What advisers and sponsors may say about products and Multiplier | Adviser firms and sponsors | Part of ADV-01 and SPN-02 | With those agreements |
| INV-01 | Investor Terms | Investor's relationship with Multiplier: no advice, no handling of investor money, own due diligence, limits on liability, risks | Investor | First time viewing product terms or a data room | Click-through |
| INV-02 | Eligibility Declaration | Investor category by country; optional reverse-solicitation statement | Investor | Same time as INV-01 | Form, confirmed by e-signature; renewed every 12 months or on change |
| INV-03 | AML, Tax and Status Declarations | Source of funds and wealth, tax residency, PEP status, not a US person | Investor | First "indicate interest" or "subscribe", with identity verification | Form, confirmed by e-signature; renewed periodically or on change |
| INV-04 | Data Room Confidentiality Undertaking | Keeps product documents confidential | Investor or adviser user | Each product, first time opening its data room | Click-through |
| INV-05 | Product Risk and Subscription Acknowledgement | Confirms the investor has read the documents and understands this product's risks | Investor | Each product, before the sponsor's subscription pack | E-signature |
| ADV-01 | Adviser Firm Agreement | Firm agreement: introducer role, 70% Adviser Share, paid-when-paid, clawback, non-circumvention, no advice from Multiplier, firm keeps its own regulatory responsibility | Firm's authorised signatory | First time anyone at the firm requests deal access, invites a client to a product, or shares a product | E-signature, countersigned by Multiplier |
| ADV-02 | Adviser Fee Schedule | Fee split, timing, product variations | Firm's authorised signatory | With ADV-01, and when the schedule changes | E-signature |
| ADV-03 | Referral Programme Rules | Overrides for introducing other adviser firms | Firm's authorised signatory | First time the firm uses an adviser referral link | E-signature |
| ADV-04 | Points and Leaderboard Rules | How points and leagues work | Each adviser user | Opting in to the leaderboard | Click-through |
| ADV-05 | Authorised User Terms | Individual obligations of each adviser or sponsor user | Each user at a firm or sponsor | Their first gated action | Click-through |
| ADV-06 | Self-Billing Agreement | Multiplier issues invoices for payouts on the firm's behalf, where tax rules allow | Firm's authorised signatory | When payout details are first added | E-signature |
| SPN-01 | Screening Application and Consent | Consent to screening; screening fee | Sponsor's authorised signatory | First product submitted | E-signature, plus fee |
| SPN-02 | Sponsor Listing Agreement | Listing and success fees, tail period, non-circumvention, sponsor's responsibility for its products | Sponsor's authorised signatory | Before the first listing goes live | E-signature, countersigned by Multiplier |
| SPN-03 | Product Listing Schedule | Per-product terms, fees, distribution restrictions, headline card | Sponsor's authorised signatory | Each product | E-signature, countersigned by Multiplier |
| SPN-04 | Sponsor Representations Certificate | Sponsor confirms documents are accurate and the product is lawfully offered | Sponsor's authorised signatory | Each product; every 12 months and on material change | E-signature |
| INT-01 | Internal Policies Outline | Internal only: the policies the platform's controls should line up with | Multiplier | Not shown to users | Not applicable |

The `README.md` in this folder has more detail on each.

## What each type of user needs before key actions

This is the legal position, not a design. How you group, sequence and present these steps is up to you.

**Everyone at sign-up:** PLT-01, PLT-02, PLT-03. No US persons.

**Investors**
- To see product terms or a data room: INV-01 and INV-02, with their category and country allowed for that product; INV-04 per product for the data room.
- To indicate interest or subscribe: identity verification and INV-03; then INV-05 per product before the sponsor's subscription pack.
- Their data goes to an adviser or sponsor only with their clear permission, naming the recipient, and they can withdraw it.

**Advisers**
- To request deal access, invite clients to products or share products: their firm has signed ADV-01 (countersigned) and ADV-02, the firm and the individual have passed checks, the individual has accepted ADV-05, and INV-04 is accepted per product.
- Owner decision: firms are the core intermediary. Agreements are at firm level: once a firm has signed, its other users only need their own checks and ADV-05. If the person acting cannot sign for their firm, the firm's signatory needs a way to sign.
- Owner decision: an individual who works alone may also onboard. They sign ADV-01 personally and give the Sole Adviser Certification (ADV-01 Schedule 3), confirming they are authorised to act alone. They are the only user under that agreement.
- Referral links need ADV-03; leaderboard opt-in needs ADV-04; payouts need ADV-06 where it applies.

**Sponsors**
- To submit a product: SPN-01 and the screening fee.
- To go live: screening passed, sponsor checks passed, SPN-02 and SPN-03 countersigned, SPN-04 signed, and ADV-05 accepted by each sponsor user.
- To stay live: SPN-04 renewed every 12 months and on material change.

Documents countersigned by Multiplier only take effect once countersigned. When a document changes materially, users accept the new version before their next relevant action.

## Owner decisions

- **On-platform only.** Documents, including signed copies, are viewed on the platform. No download or print is offered for now.
- **Headline cards before gating.** Before a user has completed a product's steps, they see only anonymised headline details: for example a reference code, asset class, broad sector, broad region, type of instrument, currency and status. Nothing that names or could identify the product, issuer, sponsor or underlying investment, and no terms, returns or fees. The sponsor proposes these details in SPN-03 and Multiplier can edit them. Full details appear only after the steps are complete.
- **Adviser Share:** 70% of the deal fees Multiplier receives for a product, paid when Multiplier is paid, unless the firm's fee schedule says otherwise.
- **Overrides:** individual advisers only, one level only. An individual adviser earns an override on other individual advisers they introduced directly; firms neither earn nor generate overrides. The rate is set by the introducing adviser's tier: 3%, 5% or 10% of deal fees. Tiers do not stack, so the most paid on any fee is 10%. Paid only from Multiplier's 30%, so the introduced adviser's 70% is never reduced and Multiplier keeps at least 20%. Tier qualification rules are not yet settled. Rates and tiers may change, so please do not fix them in code.
- **Clawback** of the Adviser Share and overrides when Multiplier refunds or loses a fee. Firms can **waive or rebate** their share.
- **Sponsor fees:** screening, listing and success fees. Success fees apply to capital from Platform Investors until 24 months after the later of their introduction and the end of the sponsor's agreement. A Platform Investor is one who was eligible to view that sponsor's products, was invited to or viewed one through the platform, or was introduced by a platform adviser. The platform needs to be able to evidence this.
- **No investor fees.**
- **Points:** build the product-neutral version first. The fee-linked version stays off until counsel has reviewed it.

## Legal requirements on records

- We need to be able to show, for any user, firm or product: which version of each document was accepted or signed, by whom, when, and how; their declarations; their check results; and the signed PDFs for e-signed documents.
- These records should be exportable and kept for the retention periods in PLT-02 and INT-01 (still to be confirmed by counsel).
- Access to product details and data rooms is logged.
- No personal data in application logs. Fictional data only in tests.

## Open items

1. Placeholders in the documents (see `PLACEHOLDERS-checklist.md`).
2. Counsel review, in particular: referral overrides, the fee-linked points score, eligibility wording by country, non-circumvention scope, and statements about Multiplier's regulatory position.
3. Your recommendation for e-signature and identity providers, if the platform does not already have them.
4. Who at Multiplier countersigns.

Please do not switch these gates on for real users until counsel has reviewed the documents and the owner has approved the walkthrough.
