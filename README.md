# beBit TECH · Ad Studio

> Facebook 廣告 HTML 批量生成工具  
> Skills A(Gemini) × B × C × D + Plugin 架構

## 快速開始

```bash
pip3 install flask flask-cors
python3 app.py
# 打開 http://localhost:5000
```

## 使用流程

1. 貼入 Gemini API Key（免費）
2. 填入活動資訊與活動描述
3. 選擇講者（1–4 位）
4. 設定生成數量
5. 按 Generate Ads
6. 下載 ZIP → 加入圖片 → Puppeteer 轉 JPG

## 取得免費 Gemini Key

[aistudio.google.com](https://aistudio.google.com) → Get API Key → Create API Key

## HTML → JPG

```bash
cd 解壓縮資料夾
# 放入 logo.png / darklogo.png / speaker1~4.jpg
npm install puppeteer
node convert.mjs
```

## 檔案結構

```
├── app.py              Flask 後端
├── skill_a_gemini.py   Gemini 文案引擎
├── skill_b_layout.py   版型引擎（Solo 8 種 / Multi 3 種）
├── skill_c_color.py    色彩引擎（淺色 8 / 深色 4）
├── skill_d_deco.py     SVG 裝飾層（5 種）
├── speakers.py         4 位講者資料
├── templates/index.html 前端 UI
├── static/img/         Logo 和講者照片
└── convert.mjs         HTML → JPG 轉換腳本
```
