# Multiplier website brief (v0.1 draft)

Status: draft for review. Wireframes: https://claude.ai/artifact/DRU4iJ8PFGAY7PExFfZT8d

## 1. Summary

Multiplier is a curated alternative-investments platform that brings together three groups: **investors**, **deal sponsors and asset managers**, and **financial advisers, wealth managers and distributors**. The platform is live. This project is a lean marketing site that explains the proposition to each audience in a calm, premium way, and moves them into registration or an application.

Reference points:
- **Structure and feel:** optoinvest.com. Clean, modern, minimal, product-led, with audience routing on the home page and product screens as proof.
- **Tone and proposition:** Moonfare. Classy, reassuring, investor-grade, transparent about fees and risk.
- **Look:** the Multiplier brand kit in this folder (light-first, white and light grey, one dark band per page, teal as a signal).

## 2. Goals

1. Make it obvious in under 10 seconds who Multiplier is for and what it does.
2. Give each audience a dedicated page that explains features and benefits and ends in one clear action.
3. Build trust: regulation, security, fee transparency, standards for sponsors.
4. Convert: registration requests (investors), applications (sponsors), partner sign-ups (advisers).
5. Stay lean: five core pages, one form, no content the team cannot maintain.

## 3. Audiences and jobs

| Audience | Wants | Primary action | Secondary action |
| --- | --- | --- | --- |
| Investors | Access to vetted private-market deals, clear terms, simple investing | Request access (register) | See how investing works |
| Sponsors and asset managers | Qualified capital, an efficient raise, brand safety | Submit your fund | See what we look for |
| Advisers, wealth managers, distributors | A vetted shelf for clients, disclosed economics, low admin | Become a partner | See the economics |

## 4. Sitemap (phase 1)

- Home
- For investors
- For sponsors
- For advisers
- Get started (one form, routed by user type; pre-selected from the page the visitor came from)
- About (short; team, principles, regulatory status)
- Legal: terms, privacy, risk warning, cookies, regional disclosures
- Log in: external link to the live platform app (not part of this build)

Phase 2 only if content is ready: Insights (market views, guides).

Global navigation: logo, For investors, For sponsors, For advisers, About, Log in (secondary button), Get started (primary button).

## 5. Page specifications

All three audience pages share one template. See the wireframes for layout.

**Home:** hero (positioning, two actions, visual); choose your path (three cards); proof strip (only real figures and logos); how it works (curate, connect, complete); platform features with product screens; principles accordion (curated, transparent, principled); trust and compliance; closing call to action (the single dark band); footer with regulatory disclosure.

**For investors:** hero with eligibility note; four benefits; how investing works (register and verify, explore, invest, track); illustrative example deal cards, clearly labelled as examples; our standards (full due diligence, compliance reviewed, clear terms per deal), with no fee table on the public page; eligibility and security; FAQ; call to action.

**For sponsors:** hero; four benefits (qualified reach, efficient raise, brand-safe, clear data); who we work with and what we look for; five-step process (apply, diligence, onboard, raise, manage); platform tools; distribution (direct investors and advisers); commercials; FAQ; call to action.

**For advisers:** four benefits of equal weight, none of them fees. Hero (private markets for your clients: vetted, simple and entirely digital); the four benefits (vetted deals, onboard once, entirely digital, bespoke experience); one compact "deals you can stand behind" section (five vetting gates plus the diligence pack, so compliance is a strong point but not the whole page); onboard once, invest many times (one verification and profile per client reused across every deal); entirely digital (documents, e-signature, subscriptions, live status, reporting, with a product screen); a bespoke experience (tailored to the practice, shortlists per client, a dedicated team; what we can actually tailor is to be confirmed); something unique for clients (example deal cards); three-step partner onboarding; FAQ balanced across the four benefits; call to action. Governance and regulatory status sit in About and the footer. No fee or referral-economics detail on the page.

**Get started:** user-type selector, form (name, work email, firm, country, one type-specific field, optional message, consent), what happens next.

## 6. Decisions so far

| Topic | Decision |
| --- | --- |
| Existing UAE M&A marketplace | Moves to a subdomain and is hidden from the new site. Needs 301 redirects for old URLs that still matter and a no-index decision. |
| Deal visibility | Deals, names, terms and fees are visible only after registration. Public pages show illustrative example cards only, labelled "Example". |
| Regulatory setting | Global, multiple regions. Region-aware disclosures and eligibility notices; every claim reviewed by compliance. |
| Product status | The platform is live. Show real screens (with sensitive data removed) and link Log in to the platform app. |
| Fees and referral terms | Not detailed on the public site, because advisers' clients read it. Partner terms are shared in the partner agreement after sign-up; deal-level costs are shown to registered investors. Public pages say only that terms are clear and shared after registration or sign-up. |
| Adviser message | Four equal benefits: vetted deals (full diligence, compliance reviewed), onboard your client once, everything digital, and a bespoke experience, plus something unique to offer clients. Compliance is one pillar, not the whole story. |

## 7. Functional requirements

- Static, fast marketing pages with a CMS for copy, FAQs, stats and legal text (no code changes for edits).
- Get started form posts to the CRM or inbox with the user type and source page; sends a confirmation email; spam protection; clear error and success states.
- Log in links to the platform app. Registration happens in the platform; the site only captures the request.
- Region handling: detect or select region, show the correct risk warning and eligibility text in the footer and on investor pages; keep a record of which disclosure version was shown (to confirm with compliance).
- Cookie consent, privacy-friendly analytics, events for each primary action and the form funnel.
- SEO basics: titles, descriptions, Open Graph images, sitemap, structured data for the organisation.
- Accessibility to WCAG 2.2 AA, keyboard and screen reader support, reduced-motion support.
- Performance targets: Lighthouse 90 or better on mobile for Performance, Accessibility, SEO.

## 8. Design direction

- Use the brand kit: `design-system/tokens.css`, the logo files, Geist and Geist Mono, 4 px corners, hairline borders, no shadows.
- Light-first: white and light grey grounds, with a single dark band per page (the closing call to action). The logo is only ever black or white.
- Product screens are the proof. Use real screens, framed with a 1 px border and an 8 px radius.
- Imagery: dark, macro, organic, teal and deep green. No stock handshakes, skylines or office photos.
- Motion: slow fades only.

## 9. Content requirements

- Brand name is **Multiplier** (never "Multiplier Club"); multiplier.club is only the web address.
- Voice: calm, specific, respectful of professional readers. No hype, no promised returns, no urgency language. See `guidelines/voice.md`.
- Needed from the team: positioning statement, one-line benefits per audience, process steps, FAQ answers, fee and commercial explanations, regulatory status per region, security and custody facts, team bios, real metrics and logos (only if approved), product screens.
- Anything unconfirmed stays a bracketed placeholder until supplied.

## 10. Compliance and risk (to be confirmed with legal)

- Financial-promotion rules differ by region. The site must not be the only gate: eligibility and suitability checks happen in the platform.
- Referral fees paid to advisers must still be disclosed to clients where the rules require it. Confirm with compliance where and how that disclosure appears (for example in the platform and partner agreement) so the public site can stay light on fees.
- Risk warning and regulatory disclosure text per region comes from compliance and is rendered from one editable source.
- This brief is not legal advice. Compliance and counsel must review all copy before launch.

## 11. Suggested technical approach

- Next.js (App Router), TypeScript, Tailwind using `design-system/tailwind.preset.js`, deployed on a managed host with preview URLs.
- Headless CMS (for example Sanity or Contentful) for page content and legal text.
- Form handling to CRM (for example HubSpot or Attio) via a server route.
- i18n-ready routing, English only at launch.
- Subdomain set-up and redirects for the legacy M&A marketplace.

## 12. Out of scope for phase 1

Blog or Insights hub, deal listings or search on the public site, investor dashboards, multi-language content, live chat, gated resource library.

## 13. Success measures

- Qualified Get started submissions per month, by audience.
- Share of visitors who reach an audience page from Home.
- Form conversion rate and drop-off step.
- Time to first useful content (LCP under 2.5 s) and accessibility audit pass.

## 14. Open questions

1. Regulatory status and licences in each target region, and who is the regulated entity.
2. How Multiplier is paid, and exactly how adviser referral fees work.
3. Proof available at launch: figures, sponsor and partner logos, testimonials.
4. Languages beyond English.
5. Who owns imagery, screens and copy; who approves compliance wording.
6. Timeline, budget and launch date; whether the CMS must be Lovable-compatible or standalone.

## 15. Suggested milestones

1. Brief and sitemap sign-off.
2. Wireframe review and content plan.
3. Visual design of Home and one audience page.
4. Build of all pages in the CMS.
5. Compliance review, accessibility and performance pass.
6. Subdomain migration, redirects, launch.
