const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
  const browser = await puppeteer.launch({ 
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.goto('https://doe.sp.gov.br/sumario?journalName=Munic%C3%ADpios&rootSectionName=Atos+Municipais', { waitUntil: 'networkidle2' });
  await page.screenshot({ path: 'screenshot.png' });
  const html = await page.content();
  fs.writeFileSync('output.json', JSON.stringify({ html }));
  await browser.close();
  console.log("Scraping finished successfully!");
})();