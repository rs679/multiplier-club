# Multiplier go-live runbook

Prepared for launch day. Nothing has been published and no domain has been changed. Every step that makes something public or changes DNS is for the owner to do, in the order below.

## What exists

| Piece | Where | State |
| --- | --- | --- |
| New site (final build) | Lovable project `73e4f557-913c-4cac-b144-17265e04c105`. Preview: https://id-preview--73e4f557-913c-4cac-b144-17265e04c105.lovable.app | Unpublished. Multi-page build in progress, see "Build status". |
| Legacy marketplace | Lovable project `929dcce9-259b-418d-9f9e-fb3c5c0c0952`. Preview: https://id-preview--929dcce9-259b-418d-9f9e-fb3c5c0c0952.lovable.app | The published version is still the original site on multiplier.club. A light-first restyle and a subdomain-ready router are prepared but unpublished. |
| Design reference | https://claude.ai/artifact/9UiAr58w9Cpu4dKsDtPZMt | Five pages with UI placeholders. |
| Brief and brand kit | `multiplier-brand-kit/` in this repo | Current. |

## Before you flip anything (blockers)

0. **Entry confirmation and Insights (added 8 Nov).** The new site now shows a first-visit confirmation dialog (investor, sponsor or adviser, country, terms tick) and a cookie notice. Wording is in `src/content/gate.ts` and is a draft for counsel; confirmations are saved to the `visitor_records` table (insert only, not readable from the website). Insights lives at `/insights`; the three seeded articles are drafts with `published = false`, so the section is empty until you review them and set them to published (preview with `?preview=1`). The sitemap and `llms.txt` need regenerating after an article is published. Lovable's built-in visitor analytics is unchanged: decide whether to keep it on.

1. **Counsel sign-off.** The footer disclosure, the draft Terms, Privacy, Risk warning and Cookies pages, and the regional notices for the UAE, Malaysia and Mexico must be reviewed. Replace the "to be confirmed by counsel" wording once approved.
2. **Claims switch.** `src/config.ts` has `CLAIMS_APPROVED = false`. With false, the site shows launch-safe wording and hides the "AI-powered due diligence" and "vetted deals" sections. After counsel approves the exact wording, change it to `true` and republish. Do not flip it earlier.
3. **Log in link.** Connected (8 Nov): `LOGIN_URL` in `src/config.ts` is `https://app.multiplier.club/access`, and Log in shows in the header, mobile menu and footer.
4. **Where requests go.** Form submissions are saved to the `requests` table in Lovable Cloud. There are no email alerts yet. Until alerts are set up, someone must check the table (Lovable project, Cloud, Database, `requests`) at least twice a day. Setting up alerts needs a sending domain.
5. **Test submission.** Submit one test request on the preview, confirm it appears in the table, then delete the row.
6. **Photo licensing.** Images are hotlinked from Unsplash and credited in the footer. Keep the credit line.

Verified today: the `requests` table allows anonymous inserts only when consent is ticked, and has no read policy, so submissions cannot be read through the website.

## Go-live sequence (about 45 minutes)

The legacy app is built to work on both hosts, so you can do steps 1 to 4 without breaking the current site.

1. **Review both previews.** Open the new site preview at 1440 px and on a phone: Home, For investors, For sponsors, For advisers, Request access, and the four legal pages. Check the footer disclosure on every page and that no `[bracketed placeholder]` text is visible.
2. **Publish the legacy project** (Lovable, project 929dcce9, Publish). It keeps serving multiplier.club as before and now also understands the `ma.` host.
3. **Add the subdomain to the legacy project.** Lovable, project 929dcce9, Settings, Domains, add `ma.multiplier.club`. Add the DNS record shown there at your registrar and wait for it to verify and for the certificate to issue.
4. **Check** https://ma.multiplier.club/uae loads, and that /uae/browse and /uae/valuation work. The top notice bar should link back to multiplier.club.
5. **Move the main domain.**
   1. In the legacy project, remove `multiplier.club` and `www.multiplier.club` from Domains.
   2. In the new project (73e4f557), publish, then add `multiplier.club` and `www.multiplier.club` under Domains. Update DNS at your registrar to the records Lovable shows for this project.
   3. Wait for verification. Expect a short gap (minutes) while DNS and certificates switch.
6. **Verify on the live domain.** Home and each audience page; Request access form (test submission, then delete it); /browse should redirect to https://ma.multiplier.club/uae/browse; robots.txt and sitemap.xml; favicon; the page title on each page; link preview for https://multiplier.club in a messaging app.
7. **After launch.** Submit https://multiplier.club/sitemap.xml and the new ma.multiplier.club sitemap in Search Console; set up email alerts for new requests; delete test rows.

## Rollback

If anything is wrong after step 5: in the new project remove `multiplier.club` and `www`, re-add them to the legacy project and restore the DNS records Lovable gave you for it. The legacy app still serves normally on the main domain, so rollback takes minutes. Do not unpublish the new project; just detach the domain.

## Redirects

The new site client-side redirects these old paths to the same path on https://ma.multiplier.club/uae: /browse, /valuation, /how-it-works, /list-your-business, /resources, /listing, /listings, /sign-in, /auth, /dashboard, /admin. These are not permanent (301) server redirects. If search ranking of old pages matters, set real 301 redirects at your DNS or CDN layer later.

## What I could not do

- Publish anything, change DNS or connect domains (these are yours to approve).
- Provide the platform Log in URL, the sending domain for email alerts, or counsel-approved wording.
- Visually check the finished Lovable build: Lovable's preview could not be opened from my environment. Please review the previews yourself in step 1.

## Build status (updated 2026-11-08, evening)

**New site (project 73e4f557). Live on multiplier.club. Published after each batch below.**
- Pages: Home, For investors, For sponsors, For advisers, Insights (15 published articles), About, FAQ, Regional notices, Request access, Terms of use, Privacy policy, Risk warning, Cookie policy, Not eligible, plus the legacy-path catch-all (old marketplace paths now go to Home; flip `LEGACY_MARKETPLACE_LIVE` to restore the marketplace redirect).
- Entry confirmation (status, country, tick), cookie notice and preferences. Records go to `visitor_records` (insert only). One native country select with UAE, Malaysia and Mexico first.
- Request form: asks a few questions that depend on type; answers are stored in `requests.details` (jsonb). Access rules unchanged (insert only with consent; no read policy).
- Insights: each article has a summary, question headings, visible FAQ, FAQPage, Article and Breadcrumb data, plus RSS, sitemap and llms.txt. Sitemap and llms.txt are static files: after adding or unpublishing an article, regenerate them with `scripts/update-insight-feeds.ts`.
- Photo credits and internal "draft/counsel" wording removed from public pages. Legal pages and Regional notices stay `noindex`.
- 101 automated tests passed on the last build.

**Added later on 8 Nov**
- Real platform screenshots (fictional sample data) replace the "Example" mock-ups on Home, For investors, For sponsors and For advisers.
- Company name set to Multiplier Private Markets Limited (Terms, Privacy policy, Organization data).
- Email alerts for new requests via Brevo are built and published. Each new request triggers a server-side email with the answers and Reply-To set to the visitor. The database trigger posts to `https://multiplier.club/api/public/request-alert`; if the primary domain ever changes, update `queue_request_alert()` with a new migration (the database cannot follow redirects). `BREVO_SENDER_NAME` is saved. The four Brevo secrets are saved and a test email was received (9 Nov). If an email ever fails, the request is still saved: check the `requests` table.

- **Design (8 Nov, late):** the platform screenshots were replaced by drawn, abstract interface fragments and brand-geometry illustrations (inline SVG, `src/components/site/ui-art.tsx`): no names, numbers, money or percentages, so nothing reads as a product claim. The Codex screenshots and brief remain in this kit but are not used on the site.
- **Request form:** the "how did you hear about us" question is removed. Country is now the full alphabetical list (`src/content/countries.ts`), shared with the entry dialog. Availability wording changed to "available to eligible investors worldwide, subject to local rules".
- **Public-page hygiene:** no bracketed placeholders or internal notes on public pages other than the four legal pages and Regional notices; a test enforces this. About shows only the company name until further facts are supplied.

**Design pass 9 Nov (published)**
- Product scenes: the abstract fragments were replaced by designed product scenes (HTML/CSS drawn in Geist, exported to WebP; sources and builders in `design-system/product-scenes/`, `build-scenes-v2.py`). Hero overlays are shown at their real 646px display width, panels full width. On phones they are cropped (not shrunk) so text stays legible. All data is fictional and there are no captions. The footer carries one disclosure sentence that images, deals and examples are for illustration only; Terms clause 8 covers the same.
- Shadows: the "no shadows" brand rule is deliberately relaxed for the product scenes only; the rest of the site stays flat.
- Investor page deal cards look like real listings (fictional names, round sample minimums, status). Check the invented firm names do not match real firms before relying on them.
- Icon set: 24 monoline icons (one teal node) in `src/components/site/icons.tsx` replace the 01/02/03 numerals in process sections. SVG sources in `design-system/icons/`.
- Home headline is now "Private market access, curated." with eyebrow "For investors, sponsors and advisers"; page title and meta updated.
- Mobile QA at 390x844 and 360x640 and desktop overlap checks at 1024, 1280 and 1440 passed; 126 tests pass.

**Still open**
1. Fill the remaining bracketed placeholders: registration number, address, contact emails, jurisdiction, governing law, forum, regulatory status, dates and versions.
2. (Done) Brevo alert emails confirmed working.
3. Photo licence for the two owner-supplied photos (adviser meeting and investor building).
4. Counsel review of the legal text and entry-dialog wording (owner decision on timing).
5. Lovable's built-in visitor analytics left on (owner decision).
6. Old marketplace (project 929dcce9): to be unpublished and its domains removed by the owner.
