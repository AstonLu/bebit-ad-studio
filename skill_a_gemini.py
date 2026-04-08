"""
SKILL A — Gemini 文案引擎
根據活動資訊即時生成 15 組多樣化文案
"""
import json, re

def generate_copies(event: dict, api_key: str) -> dict:
    """
    呼叫 Gemini 根據活動資訊生成文案
    回傳格式與 skill_a_copy.get_copies() 相同
    """
    import urllib.request

    prompt = f"""你是一位專業的 B2B 行銷文案專家，擅長為企業活動、論壇、座談會撰寫高轉換率廣告文案。

請根據以下活動資訊，生成 15 組 Facebook 廣告文案。

活動資訊：
- 活動名稱：{event.get('event_name', '')}
- 主題：{event.get('topic', '')}
- 日期：{event.get('date', '')} {event.get('time', '')}
- 地點：{event.get('venue', '')}
- 主辦：{event.get('org', '')}
- 活動描述：{event.get('description', '')}
- 目標受眾：{event.get('audience', '企業主管、行銷總監、業務負責人')}

要求：
1. 每組包含：標題（h，15字以內）、副標（s，30字以內）、CTA文字（cta，4-6字）
2. 15組需涵蓋不同訴求角度：痛點型、利益型、好奇型、緊迫型、權威型、數據型
3. 語調多樣：有理性分析、有情感共鳴、有輕鬆對話
4. 全部繁體中文
5. 不要提及與活動不符的內容

請嚴格以 JSON 格式回覆，不要有任何其他文字：
{{
  "A01": {{"h": "標題", "s": "副標", "cta": "CTA"}},
  "A02": {{"h": "標題", "s": "副標", "cta": "CTA"}},
  ...
  "A15": {{"h": "標題", "s": "副標", "cta": "CTA"}}
}}"""

    payload = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.8,
            "maxOutputTokens": 3000,
        }
    }).encode('utf-8')

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"}, method="POST")

    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode('utf-8'))

    raw = result['candidates'][0]['content']['parts'][0]['text']

    # 清理 markdown 格式
    raw = re.sub(r'```json\s*', '', raw)
    raw = re.sub(r'```\s*', '', raw)
    raw = raw.strip()

    copies = json.loads(raw)

    # 確保格式正確，補足到 15 組
    validated = {}
    for i, (k, v) in enumerate(copies.items(), 1):
        key = f'A{i:02d}'
        validated[key] = {
            'h':   str(v.get('h', v.get('headline', '活動即將開始'))),
            's':   str(v.get('s', v.get('subheadline', '精彩內容等你來'))),
            'cta': str(v.get('cta', '立即報名')),
        }
        if i >= 15:
            break

    return validated


def get_copies_fallback() -> dict:
    """API 失敗時的備用文案（通用版，不涉及特定主題）"""
    return {
        'A01': {'h': '把握這次深度交流機會', 's': '與業界菁英面對面，激發全新思維與洞察', 'cta': '立即報名'},
        'A02': {'h': '你最不能錯過的年度盛會', 's': '限額名額開放，頂尖講者帶來第一手實戰經驗', 'cta': '搶先報名'},
        'A03': {'h': '一場改變你思維的座談', 's': '從理論到落地，完整框架帶走可執行策略', 'cta': '探索更多'},
        'A04': {'h': '決策者都在關注的關鍵議題', 's': '掌握趨勢先機，與業界最前線人才共同交流', 'cta': '加入我們'},
        'A05': {'h': '業界頂尖專家，親自分享實戰心法', 's': '不再靠猜，直接學習可複製的成功方法論', 'cta': '免費報名'},
        'A06': {'h': '你的競爭對手已經知道這些了', 's': '還在等待？現在加入，掌握領先優勢', 'cta': '了解更多'},
        'A07': {'h': '一個下午，值得你重新思考全局', 's': '少走彎路，直接掌握核心應用方法', 'cta': '預約席位'},
        'A08': {'h': '限額座談，高品質深度交流', 's': '精選嘉賓，確保每位參與者都能有所收穫', 'cta': '確認席位'},
        'A09': {'h': '這些問題，這次都有答案', 's': '現場 Q&A，專家直接回應你最想知道的', 'cta': '我要去'},
        'A10': {'h': '從數據到洞察，從策略到執行', 's': '完整解析，讓你帶走可立即落地的方法', 'cta': '立即報名'},
        'A11': {'h': '與最聰明的人在同一個房間', 's': '高質量交流，碰撞出意想不到的新視角', 'cta': '報名參加'},
        'A12': {'h': '不懂這個，你正在落後', 's': '行業正在快速演變，現在學是最划算的投資', 'cta': '立即了解'},
        'A13': {'h': '為什麼他們都選擇參加這場活動', 's': '口碑最好的學習型活動，現在輪到你了', 'cta': '我要參加'},
        'A14': {'h': '90 分鐘，讓你的思維升級', 's': '精華濃縮，沒有廢話，全是你需要的', 'cta': '立刻報名'},
        'A15': {'h': '業界最值得關注的一場交流', 's': '把握難得機會，與最前線的人對話', 'cta': '確認出席'},
    }


if __name__ == '__main__':
    print('✅ Skill A Gemini 文案引擎載入完成')
    print('   使用方式：generate_copies(event, api_key)')
    print('   備用文案：get_copies_fallback()')
