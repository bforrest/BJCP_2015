const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: false
  });
  const context = await browser.newContext();

  // Open new page
  const page = await context.newPage();

  // Go to https://dev.bjcp.org/style/2015/9/
  await page.goto('https://dev.bjcp.org/style/2015/9/');

  // Click article[id="post-4794"]
  await page.click('article[id="post-4794"]');
  // assert.equal(page.url(), 'https://dev.bjcp.org/style/2015/9/strong-european-beer/');

  // Click article[id="post-4795"]
  await page.click('article[id="post-4795"]');

  // Click text=/.*9A\..*/
  await page.click('text=/.*9A\..*/');

  // Click article[id="post-4805"]
  await page.click('article[id="post-4805"]');

  // Click article[id="post-4807"]
  await page.click('article[id="post-4807"]');

  // Close page
  await page.close();

  // ---------------------
  await context.close();
  await browser.close();
})();