/**
 * convert.mjs — HTML → JPG 批量轉換
 *
 * 使用方式（在 output/ 資料夾內）：
 *   node ../convert.mjs
 *
 * 或指定目錄：
 *   node convert.mjs --dir ./output
 *
 * 需要：npm install puppeteer
 *
 * 白邊修正：
 *   - page.setViewport 強制 1080×1080
 *   - screenshot clip 硬切 1080×1080
 *   - fullPage: false
 */

import puppeteer from 'puppeteer';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// ── 參數解析 ──
const args = process.argv.slice(2);
const dirIdx = args.indexOf('--dir');
const targetDir = dirIdx !== -1 ? args[dirIdx + 1] : './output';
const absDir = path.resolve(__dirname, targetDir);

const files = fs.readdirSync(absDir).filter(f => f.endsWith('.html'));
if (files.length === 0) {
  console.error(`❌ 找不到 HTML 檔案：${absDir}`);
  process.exit(1);
}

console.log(`\n🚀 HTML → JPG 轉換`);
console.log(`   來源：${absDir}`);
console.log(`   共 ${files.length} 個檔案\n`);

const browser = await puppeteer.launch({
  headless: 'new',
  args: ['--no-sandbox', '--disable-setuid-sandbox'],
});

let done = 0;
for (const file of files) {
  const page = await browser.newPage();

  // ★ 白邊修正關鍵：強制 viewport = 1080×1080，不讓瀏覽器自行縮放
  await page.setViewport({ width: 1080, height: 1080, deviceScaleFactor: 1 });

  const fileUrl = `file://${path.join(absDir, file)}`;
  await page.goto(fileUrl, { waitUntil: 'networkidle0', timeout: 15000 });

  // 等字體載入
  await page.waitForTimeout(400).catch(() => {});

  const outPath = path.join(absDir, file.replace('.html', '.jpg'));
  await page.screenshot({
    path: outPath,
    type: 'jpeg',
    quality: 95,
    // ★ 強制截取精確 1080×1080，不會有多餘邊距
    clip: { x: 0, y: 0, width: 1080, height: 1080 },
    fullPage: false,
  });

  await page.close();
  done++;
  console.log(`  ✅ ${done}/${files.length}  ${file.replace('.html', '.jpg')}`);
}

await browser.close();
console.log(`\n🎉 完成！${done} 個 JPG 已存至 ${absDir}/`);
