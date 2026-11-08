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

1. **Counsel sign-off.** The footer disclosure, the draft Terms, Privacy, Risk warning and Cookies pages, and the regional notices for the UAE, Malaysia and Mexico must be reviewed. Replace the "to be confirmed by counsel" wording once approved.
2. **Claims switch.** `src/config.ts` has `CLAIMS_APPROVED = false`. With false, the site shows launch-safe wording and hides the "AI-powered due diligence" and "vetted deals" sections. After counsel approves the exact wording, change it to `true` and republish. Do not flip it earlier.
3. **Log in link.** `LOGIN_URL` in `src/config.ts` is empty, so no Log in button is shown. Set it to the platform URL when you have it (must start with https).
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

The new site client-side redirects these old paths to the same path on https://ma.multiplier.club/uae: /browse, /valuation, /how-it-works, /list-your-business, /resources, /listing, /listings, /insights, /sign-in, /auth, /dashboard, /admin. These are not permanent (301) server redirects. If search ranking of old pages matters, set real 301 redirects at your DNS or CDN layer later.

## What I could not do

- Publish anything, change DNS or connect domains (these are yours to approve).
- Provide the platform Log in URL, the sending domain for email alerts, or counsel-approved wording.
- Visually check the finished Lovable build: Lovable's preview could not be opened from my environment. Please review the previews yourself in step 1.

## Build status (checked 2026-11-08 06:36 UTC)

**New site (project 73e4f557). Built, tested by Lovable, not published.**
- Nine pages: Home, For investors, For sponsors, For advisers, Request access, Terms, Privacy, Risk warning, Cookies, plus the legacy-redirect catch-all.
- Checked by Lovable at 1440, 390 and 360 px with no horizontal scroll; 21 automated tests passed (marketplace redirects, type pre-selection, form errors, launch rules). A real request was submitted and the test row deleted. Request storage and access rules are unchanged.
- `src/config.ts` verified: `CLAIMS_APPROVED = false`, `LOGIN_URL = "#"` (Log in hidden), legacy prefixes set.
- Lovable supplied short headings and FAQ answers where exact copy was not given. Read them before publishing.
- Photographs are served through the project's own image service, not hotlinked.
- Open: final legal text and regional notices (counsel); email alerts; platform Log in URL.

**Legacy marketplace (project 929dcce9). Prepared, tested by Lovable, not published.**
- Router base path `/uae` applies only on hosts starting with `ma.`; on every other host the app behaves as before. A notice bar appears only on the `ma.` host. Canonical URLs, sitemap, robots and llms files use the new address.
- Nine address tests passed; phone layout and error checks passed.
- Known exceptions to handle at switch time:
  1. **Auth redirects.** In the legacy project's Cloud authentication settings, add `https://ma.multiplier.club/uae` (and its sign-in and sign-up paths) to the allowed redirect URLs before users try to sign in on the new host. Sign-in on the new host is unverified until you do this.
  2. **Notification emails.** Emails sent by the backend still link to multiplier.club paths. They will land on the new site, which redirects them to the marketplace, so links keep working. Update the email templates later.
  3. **Static head metadata** keeps the current-host fallback until the app runs; search engines read the updated URLs from the app and from the sitemap.
  4. `ma.multiplier.club` must serve `robots.txt` at the host root (it will, once the domain is attached).

Add to the go-live sequence, between steps 3 and 4: add the auth redirect URLs for the new host (item 1 above).
