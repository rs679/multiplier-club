// Renders each 1080 x 1350 section of series-01.html to PNG. Pass the scale as the first argument (2 for posting).
const { chromium } = require("playwright");
const path = require("path");
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 1200, height: 1500 },
    deviceScaleFactor: Number(process.argv[2] || 2),
  });
  await page.goto("file://" + path.resolve(__dirname, "series-01.html"));
  await page.evaluate(() => document.fonts.ready);
  const out = path.resolve(__dirname, "..", "png");
  for (const el of await page.$$("section.s")) {
    const id = await el.getAttribute("id");
    await el.screenshot({ path: path.join(out, `multiplier-linkedin-${id}.png`) });
  }
  await browser.close();
})();
