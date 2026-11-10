# Codex brief: legal documents, who signs what, and when

Paste everything below the line into Codex, inside the platform repository. It sits alongside `platform-next-build-brief.md`. The documents themselves are in this folder (`multiplier-brand-kit/legal/`), all marked "draft for legal review".

---

## How to read this brief

As with the main build brief: these are goals and suggestions. Confirm they fit the existing code, change them where you see a better way, and say what you decided. "Must" marks a guardrail.

Please reply first with a short design note (data model, gating engine, e-signature approach, migration of existing users) before building.

## The principle

**Easy to join, gated at the point of action.**

- Sign-up asks for as little as possible: name, email, password or passkey, role, country, and three click-through acceptances (Platform Terms, Privacy Notice, Electronic Signature and Communications Consent).
- Nothing else is asked until the user tries to do something that legally needs it. At that moment the platform shows a short checklist of what is missing ("To request access to this deal, complete 3 steps"), takes them through it, and then returns them to the action they started.
- Everything they complete is saved on their profile and reused. Nobody signs the same document twice unless the version changes materially or it expires.
- Until the checklist is complete, the action stays locked. Only then can an adviser share and sell deals, an investor see terms and subscribe, or a sponsor list.

## Document register

Each document has a fixed ID. The text lives in this folder; the platform must store each published version as a record (see data model).

Acceptance tiers:
- **T1 Click-through**: tick box, logged with version.
- **T2 Declaration**: the user answers questions and confirms; answers and version logged.
- **T3 E-signature**: signed through the e-signature provider; signed PDF stored.
- **T4 E-signature, countersigned**: as T3, then countersigned by a Multiplier signatory before it takes effect.

### Platform-wide

| ID | Document | Purpose | Who accepts | When | Tier | Unlocks | Re-accept |
|---|---|---|---|---|---|---|---|
| PLT-01 | Platform Terms of Use | Ground rules for using the technology platform: not advice, not regulated, no recourse to Multiplier for products | Every user | Sign-up | T1 | Account | Material change |
| PLT-02 | Privacy Notice (Platform) | How personal data is used and shared | Every user (acknowledge) | Sign-up | T1 | Account | Material change |
| PLT-03 | Electronic Signature and Communications Consent | Agreement that e-signatures and electronic notices are binding | Every user | Sign-up | T1 | Ability to sign later documents | Material change |
| PLT-04 | Data Sharing Schedule | Who sees what data (adviser, sponsor, administrator) and on what basis | Investor (per sharing event) | First time data would go to an adviser or sponsor | T1 | Data sharing to that party | Per new recipient |
| PLT-05 | Complaints Policy | How to complain | Published, not signed | Linked in footer and emails | None | None | None |
| PLT-06 | Content and Marketing Guidelines | What advisers and sponsors may say about products and Multiplier | Advisers and sponsors (incorporated into ADV-01 and SPN-02) | With those agreements | Part of T3/T4 | None separately | Material change |

### Investors

| ID | Document | Purpose | Who accepts | When | Tier | Unlocks | Re-accept |
|---|---|---|---|---|---|---|---|
| INV-01 | Investor Terms | Investor's relationship with Multiplier: technology platform only, no advice, no holding of money, own due diligence, no recourse, risks | Investor | First attempt to view product terms or a data room | T1 | Gated product area | Material change |
| INV-02 | Eligibility Declaration | Self-certification of investor category by country (country modules), including the optional genuine reverse-solicitation attestation | Investor | Same moment as INV-01 | T2 | Gated product area, filtered by eligibility | Every 12 months, or on change of country or category |
| INV-03 | AML, Tax and Status Declarations | Source of funds and wealth, tax residency and self-certification, PEP status, not a US person | Investor | First "indicate interest" or "subscribe" | T2 (plus identity verification) | Interest and subscription | Every 12 months or on change |
| INV-04 | Data Room Confidentiality Undertaking | Keeps product documents confidential | Investor, and any adviser user | Each product, first time opening its data room | T1 | That product's data room | New version of the product's documents only if the sponsor asks |
| INV-05 | Product Risk and Subscription Acknowledgement | Confirms the investor has read the documents and understands the specific risks of this product | Investor | Each product, before the sponsor's subscription pack | T2 | That product's subscription pack | Per subscription |

### Advisers

| ID | Document | Purpose | Who accepts | When | Tier | Unlocks | Re-accept |
|---|---|---|---|---|---|---|---|
| ADV-01 | Adviser Firm Agreement | Firm-level agreement: introducer role, 70% Adviser Share of deal fees, paid-when-paid, clawback, non-circumvention and non-solicitation of sponsors and issuers, no advice or guarantees from Multiplier, adviser's own due diligence and suitability, regulatory responsibility stays with the firm | Firm signatory (firm admin) | First time anyone at the firm requests deal access, invites a client to a product, or shares a product | T4 | Firm can transact | Material change |
| ADV-02 | Adviser Fee Schedule | The fee split, payment timing, and any product-specific variations | Firm signatory | With ADV-01; again when the schedule changes | T3 (or T1 if Multiplier and counsel agree acceptance by firm admin is enough for updates) | Fee entitlement | Each new schedule version |
| ADV-03 | Referral Programme Rules | Multi-level override on introduced advisers, paid only from Multiplier's 30% share, with caps and a minimum retained share | Firm signatory | First time the firm generates or uses an adviser referral link | T3 | Referral links and override entitlement | Material change |
| ADV-04 | Points and Leaderboard Rules | How points and leagues work. Option A product-neutral (build first); Option B fee-linked (off until counsel review) | Each adviser user | Opting in to leaderboard visibility | T1 | Leaderboard participation | Each rules version |
| ADV-05 | Authorised User Terms | Individual user's obligations under the firm's agreement: confidentiality, permitted content, conduct | Each adviser user (and each sponsor user) | First gated action by that user | T1 | User can act under the firm | Material change |
| ADV-06 | Self-Billing Agreement | Lets Multiplier issue invoices on the firm's behalf for payouts, where tax rules allow | Firm signatory | When payout details are first added | T3 | Payouts | Material change, or tax change |

### Sponsors

| ID | Document | Purpose | Who accepts | When | Tier | Unlocks | Re-accept |
|---|---|---|---|---|---|---|---|
| SPN-01 | Screening Application and Consent | Consent to regulatory and track-record screening, screening fee, no guarantee of listing | Sponsor signatory | First product submitted | T3, plus screening fee paid | Screening starts | Each new application |
| SPN-02 | Sponsor Listing Agreement | Listing and success fees payable to Multiplier on all capital from Platform Investors (prior relationships irrelevant if processed through Multiplier), tail period, no circumvention or solicitation, sponsor's responsibility for products and documents | Sponsor signatory | Before first listing goes live | T4 | Listing | Material change |
| SPN-03 | Product Listing Schedule | Per-product commercial terms, distribution restrictions (countries, investor categories, advisers), fees | Sponsor signatory | Each product | T4 | That product goes live | Change of terms |
| SPN-04 | Sponsor Representations Certificate | Sponsor confirms documents are accurate, product lawfully offered, regulatory status, material changes notified | Sponsor signatory | Each product, and every 12 months while live | T3 | That product stays live | On any material change and every 12 months |

### Internal

| ID | Document | Purpose |
|---|---|---|
| INT-01 | Internal Policies Outline | Not user-facing. Lists the internal policies (AML, sanctions, data protection, conflicts, complaints handling, record keeping) the platform's controls must align with |

## Journeys and gates

The gate engine should evaluate **requirements per action**, not per page. Below are the actions and what each requires. Express these as data (a requirements table or config), not hard-coded `if` statements, so legal can change them without a release.

### Everyone: sign-up
Requires: PLT-01, PLT-02, PLT-03. Email verified. Country declared. If country or answers indicate a US person, stop and show the "not available" screen.
Allows: profile, public insights, neutral deal cards (product name, sponsor, asset class, status; no terms, returns or fees), notifications settings.

### Investor

| Action | Requires (if not already complete) |
|---|---|
| View product terms, deal card details or key-terms table | INV-01, INV-02 (category must match the product's allowed categories and country) |
| Open a product's data room | The above, plus INV-04 for that product, plus product's distribution restrictions satisfied |
| Indicate interest | The above, plus identity verification (KYC), INV-03, sanctions screening clear |
| Subscribe | The above, plus INV-05 for that product, plus PLT-04 consent for the sponsor (and adviser, if any), then the sponsor's subscription pack pre-filled from the profile |
| Share their profile with an adviser | PLT-04 for that adviser |

An investor invited by an adviser goes through the same gates. The adviser's invite page only explains Multiplier and how to register.

### Adviser

An adviser can sign up and browse neutral deal cards straight away. The first time they try any of the actions below, they get the checklist.

| Action | Requires (if not already complete) |
|---|---|
| Request access to a deal (terms, data room) | Firm onboarded (ADV-01 countersigned, ADV-02 accepted, firm KYB passed, regulatory status recorded), user KYC passed, ADV-05, INV-04 for that product, product's adviser and country restrictions satisfied |
| Invite a client to a product or shortlist | As above |
| Share a product with a client, or create a fact sheet | As above, plus the product is on the adviser's shelf |
| Generate an adviser referral link | ADV-03 |
| Opt in to the leaderboard | ADV-04 |
| Add payout bank details | ADV-06 where applicable, plus firm bank account verification |
| Invite colleagues to the firm | Firm admin role |

**Firm logic.** Agreements are at firm level.
- If the adviser's firm is not on the platform, the checklist asks: "Are you authorised to sign for your firm?" If yes, they become firm admin and sign. If no, they enter the signatory's details, the platform sends the signatory an invitation, and the adviser sees a "waiting for your firm" state.
- An independent adviser is a firm of one and signs as their own firm admin.
- Once the firm is onboarded, each new user at that firm only needs KYC and ADV-05.

### Sponsor

| Action | Requires (if not already complete) |
|---|---|
| Submit a product for screening | SPN-01, screening fee paid, sponsor KYB started |
| List a product (go live) | Screening passed (Multiplier admin decision), sponsor KYB passed, SPN-02 countersigned, SPN-03 countersigned for that product, SPN-04 for that product, ADV-05 accepted by each sponsor user |
| Keep a product live | SPN-04 renewed every 12 months, and on material change |
| See investor data for a raise | Investor's PLT-04 consent for that sponsor, data scoped to that sponsor only |

### Multiplier admin
Countersigns T4 documents, decides screening, publishes document versions, and can see the full gate status of any user. Every admin action is audit-logged.

## What the user sees

Suggested pattern (adjust to the existing UI):

1. User clicks the action (for example "Request access").
2. A panel shows "To request access, complete these steps", with each step's status: done, to do, waiting (for example "Waiting for Multiplier countersignature" or "Waiting for your firm's signatory").
3. Each step opens in place: a document to read and accept, a short form, an identity check, or an e-signature.
4. Answers save to the profile as they go. A user can leave and come back.
5. When all steps are done, the user returns to the original action automatically.
6. A **Profile: Agreements and verification** page lists every document they have accepted (with version and date, and a PDF download), every declaration, and what is due for renewal.

Keep copy neutral and short. Do not use the words listed in the main brief's guardrails.

## Data model (suggested)

- `legal_document`: id (for example `ADV-01`), title, audience, tier, owner (Multiplier or sponsor).
- `legal_document_version`: document id, version number, effective date, content hash, rendered PDF, `is_material_change`, `supersedes`, status (draft, published, retired).
- `acceptance`: version id, user id, firm id (if any), product id (if per product), method (tier), timestamp, IP, user agent, e-signature envelope id, signed PDF reference, countersigned by and at, status (pending, active, superseded, expired, revoked).
- `declaration`: user id, type (eligibility, AML, tax, PEP), answers (structured), country module version, valid until.
- `verification`: user or firm id, type (KYC, KYB, sanctions, regulatory status), provider reference, result, checked at, valid until. Store references and results only, not raw ID images, unless the provider requires otherwise.
- `gate_requirement`: action key, requirement type (document, declaration, verification, role, product restriction), parameters, applies to role. This is the editable rules table.
- `gate_check_log`: user, action, product, result (allowed or blocked), missing requirements, timestamp.

Rules:
- An acceptance stays valid until the document version is superseded **with** `is_material_change = true`, it expires, or it is revoked. Non-material updates do not trigger re-acceptance; users are notified.
- T4 documents are not active until countersigned. Show "waiting" in the checklist.
- Per-product documents (INV-04, INV-05, SPN-03, SPN-04) are keyed to the product.
- Firm-level documents (ADV-01, ADV-02, ADV-03, ADV-06) are keyed to the firm, and satisfy the requirement for every user at that firm.

## E-signature and identity

- Choose an e-signature provider that produces a signed PDF and an audit certificate, supports embedded signing and countersignature, and has an API. Say which you recommend and why.
- Use the platform's existing identity and KYB provider if there is one. Otherwise recommend one that covers the UAE, UK, GCC and Asia, with sanctions and PEP screening.
- Fill document placeholders (party names, firm details, fee schedule figures) from the database at the moment of signing, and store the filled PDF.

## Audit and records

- Every acceptance, declaration, verification, gate check, countersignature and admin override is logged with who, what, when and which version.
- Exportable per user, per firm and per product.
- Signed PDFs are stored for at least the record-keeping period in INT-01 (placeholder; legal to confirm).
- No personal data in application logs.

## Commercial items the ledger needs from these documents

- **Adviser Share:** 70% of total deal fees Multiplier receives from the sponsor for that product, unless the firm's fee schedule (ADV-02) says otherwise. Paid when Multiplier has been paid.
- **Overrides:** multi-level, as set out in ADV-03, paid only from Multiplier's 30% share, with the caps and the minimum Multiplier retained share stated in ADV-03. The ledger must stop paying overrides once the cap or the retained-share floor is reached. Keep the levels and percentages in configuration, not code.
- **Clawback:** if Multiplier refunds or loses a fee, the related Adviser Share and overrides are reversed against future payouts.
- **Waiver or rebate:** a firm can waive or rebate its share; the ledger records this and the client disclosure reflects it.
- **Sponsor fees:** screening, listing and success fees from SPN-01, SPN-02 and SPN-03. Success fees apply to all capital from Platform Investors during the tail period in SPN-02.

## Tests (must)

Use fictional data only.
- Each action is blocked when any requirement is missing, and allowed when all are met.
- Superseding a version with a material change re-blocks the action; a non-material change does not.
- T4 documents do not satisfy requirements until countersigned.
- A firm-level agreement satisfies the requirement for every user at that firm, and only that firm.
- Product restrictions (country, category, adviser list) block access even when all documents are signed.
- US-person declaration blocks every gated action.
- Override calculation respects levels, caps and the retained-share floor; clawback reverses correctly.
- Every gate check, acceptance and override is in the audit log.

## Open items before launch

1. All `[PLACEHOLDER]` fields in the documents (company details, jurisdiction, governing law and arbitration seat, fee figures, override levels and caps, tail period, record retention).
2. Counsel review of every document, in particular: multi-level overrides (inducement and pyramid concerns), the Option B fee-linked points score, eligibility wording per country, non-circumvention scope, and the statements about Multiplier's regulatory position.
3. Choice of e-signature and identity providers.
4. Who at Multiplier countersigns T4 documents.

Do not switch on gated actions for real users until the documents have been reviewed by counsel and the owner has approved the walkthrough.
