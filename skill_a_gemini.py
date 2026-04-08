"""
SKILL A — Gemini 文案引擎 v3
強化 prompt：角色設定更精準、輸出格式更嚴格、文案維度更完整
"""
import json, re, urllib.request

def generate_copies(event: dict, api_key: str) -> dict:

    event_name  = event.get('event_name', '')
    topic       = event.get('topic', '')
    date        = event.get('date', '')
    time_       = event.get('time', '')
    venue       = event.get('venue', '')
    org         = event.get('org', 'beBit TECH')
    description = event.get('description', '')
    audience    = event.get('audience', '行銷主管、電商品牌負責人')

    prompt = f"""你是 {org} 的資深社群行銷顧問，專門為 B2B 科技與顧問公司撰寫 Facebook 廣告文案。你深刻理解台灣企業決策者的痛點、語言習慣與行動動機。

## 活動背景

- 活動名稱：{event_name}
- 核心主題：{topic}
- 主辦單位：{org}
- 時間地點：{date} {time_}，{venue}
- 活動內容：{description}
- 目標受眾：{audience}

## 任務

根據上述活動，生成 15 組高轉換率的 Facebook 廣告文案。

每組文案須包含三個欄位：
- h：圖片主標題，15 字以內，要能單獨吸引目光，不依賴上下文
- s：貼文說明，30 字以內，補充說明主標題，具體描述活動價值或行動誘因
- cta：行動按鈕文字，4–6 字，明確、有力

## 15 組必須涵蓋以下維度（每個維度至少 2 組）：

1. 痛點型：點出目標受眾面對的問題或焦慮
2. 利益型：直接說明參加後能獲得什麼具體收益
3. 好奇型：製造懸念或資訊落差，讓人想點擊了解
4. 緊迫型：強調名額限制、時間壓力或稀缺性
5. 權威信任型：強調講者資歷、主辦單位專業度或已有誰參加

## 文案風格要求

- 語氣專業但不說教，貼近台灣 B2B 行銷人員的說話方式
- 避免空泛、口號式的句子（如「掌握未來趨勢」「引領行業革命」）
- 標題要具體、有畫面感，能讓人立刻理解活動是關於什麼
- 副標題要提供新資訊，不重複標題內容
- 文案必須與活動主題高度相關，不得使用與 {topic} 無關的詞彙

## 輸出格式

只輸出 JSON，不要任何說明、標題或 markdown。格式如下：
{{"A01":{{"h":"","s":"","cta":""}},"A02":{{"h":"","s":"","cta":""}},"A03":{{"h":"","s":"","cta":""}},"A04":{{"h":"","s":"","cta":""}},"A05":{{"h":"","s":"","cta":""}},"A06":{{"h":"","s":"","cta":""}},"A07":{{"h":"","s":"","cta":""}},"A08":{{"h":"","s":"","cta":""}},"A09":{{"h":"","s":"","cta":""}},"A10":{{"h":"","s":"","cta":""}},"A11":{{"h":"","s":"","cta":""}},"A12":{{"h":"","s":"","cta":""}},"A13":{{"h":"","s":"","cta":""}},"A14":{{"h":"","s":"","cta":""}},"A15":{{"h":"","s":"","cta":""}}}}"""

    payload = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.85,
            "maxOutputTokens": 4000,
            "responseMimeType": "application/json",
        }
    }).encode('utf-8')

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    req = urllib.request.Request(
        url, data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(req, timeout=45) as resp:
        result = json.loads(resp.read().decode('utf-8'))

    raw = result['candidates'][0]['content']['parts'][0]['text'].strip()
    raw = re.sub(r'```json\s*|```\s*', '', raw).strip()

    try:
        copies = json.loads(raw)
    except json.JSONDecodeError:
        match = re.search(r'\{[\s\S]*\}', raw)
        copies = json.loads(match.group()) if match else {}

    validated = {}
    for i, (k, v) in enumerate(copies.items(), 1):
        if i > 15:
            break
        validated[f'A{i:02d}'] = {
            'h':   str(v.get('h', '精彩活動即將開始')),
            's':   str(v.get('s', '期待您的參與')),
            'cta': str(v.get('cta', '立即報名')),
        }

    if not validated:
        raise ValueError("Gemini 回傳空文案")

    return validated


def get_copies_fallback() -> dict:
    return {
        'A01': {'h': '把握這次深度交流機會', 's': '與業界菁英面對面，激發全新思維與洞察', 'cta': '立即報名'},
        'A02': {'h': '你最不能錯過的年度盛會', 's': '限額名額開放，頂尖講者帶來第一手實戰', 'cta': '搶先報名'},
        'A03': {'h': '一場改變你思維的座談', 's': '從理論到落地，帶走可執行策略', 'cta': '探索更多'},
        'A04': {'h': '決策者都在關注的關鍵議題', 's': '掌握趨勢先機，與業界最前線人才交流', 'cta': '加入我們'},
        'A05': {'h': '頂尖專家親自分享實戰心法', 's': '不再靠猜，直接學習可複製的成功方法', 'cta': '免費報名'},
        'A06': {'h': '你的競爭對手已經知道這些', 's': '現在加入，掌握領先優勢', 'cta': '了解更多'},
        'A07': {'h': '一個下午讓你重新思考全局', 's': '少走彎路，直接掌握核心應用方法', 'cta': '預約席位'},
        'A08': {'h': '限額座談高品質深度交流', 's': '精選嘉賓，確保每位參與者都有收穫', 'cta': '確認席位'},
        'A09': {'h': '這些問題這次都有答案', 's': '現場 Q&A，專家直接回應你的疑問', 'cta': '我要去'},
        'A10': {'h': '從數據到洞察從策略到執行', 's': '完整解析，帶走可立即落地的方法', 'cta': '立即報名'},
        'A11': {'h': '與最聰明的人在同一個房間', 's': '高質量交流，碰撞意想不到的新視角', 'cta': '報名參加'},
        'A12': {'h': '不懂這個你正在落後', 's': '行業快速演變，現在學是最划算的投資', 'cta': '立即了解'},
        'A13': {'h': '為什麼他們都選擇參加', 's': '口碑最好的學習型活動，現在輪到你了', 'cta': '我要參加'},
        'A14': {'h': '90 分鐘讓你的思維升級', 's': '精華濃縮，沒有廢話，全是你需要的', 'cta': '立刻報名'},
        'A15': {'h': '業界最值得關注的一場交流', 's': '把握難得機會，與最前線的人對話', 'cta': '確認出席'},
    }


if __name__ == '__main__':
    print('✅ Skill A Gemini v3 載入完成')
