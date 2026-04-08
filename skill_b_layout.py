"""
SKILL B — 排版引擎 v3
規格：1080×1080px 固定，全 px，無動態單位
Logo：height 130px (≥1/8 畫面) — 強制執行
講者圓形：200px (≥1/5 畫面寬) — 強制執行
講者直式：width 260px, height 320px
深色比例 ≤ 30%，淺色版型優先
講者邏輯：版型依選擇人數對應，不混用
"""

from skill_c_color import get_colors, get_logo
from skill_d_deco import get_decoration

BASE = """
*{margin:0;padding:0;box-sizing:border-box;}
html{display:block;width:1080px;height:1080px;overflow:hidden;}
body{margin:0;padding:0;width:1080px;height:1080px;overflow:hidden;position:relative;display:block;}
"""
LOGO_H = 130   # ≥ 1/8 of 1080
SPK_C  = 200   # circle diameter ≥ 1/5
SPK_W  = 260   # portrait width
SPK_H  = 320   # portrait height

GF = {
    's': 'https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Noto+Sans+TC:wght@400;700&display=swap',
    'p': 'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Noto+Sans+TC:wght@400;700&family=Raleway:wght@300;400;600;700&display=swap',
    'o': 'https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&family=Noto+Sans+TC:wght@400;700&display=swap',
    'b': 'https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@400;600;700;800&family=Noto+Sans+TC:wght@400;700&display=swap',
    'd': 'https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Outfit:wght@400;600;700&family=Noto+Sans+TC:wght@400;700&display=swap',
}
ft = lambda k: f'<link href="{GF[k]}" rel="stylesheet">'

EVENT = {'date':'2025.04.20（四）','time':'14:00–15:20','venue':'台北 W 飯店 皇家宴會廳','topic':'AI × CDP × 電商','org':'beBit TECH'}
ev = lambda k: EVENT[k]

# ═══════════════════════════════════════
# SINGLE-SPEAKER LAYOUTS (6 light + 2 dark = 8 total)
# ═══════════════════════════════════════

def S_L1(cp, co, S, L, d):
    """[淺] Apple 風：極簡白底，大標居中，講者直式右側"""
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">{ft('p')}
<style>{BASE}
body{{background:{co['bg']};font-family:'Noto Sans TC',sans-serif;}}
.rule{{position:absolute;top:0;left:0;width:1080px;height:4px;background:linear-gradient(90deg,{co['primary']},{co['accent']});}}
.wrap{{position:absolute;top:4px;left:0;width:1080px;height:1076px;padding:48px 72px 52px;display:flex;flex-direction:column;}}
.hdr{{display:flex;justify-content:space-between;align-items:center;flex-shrink:0;height:{LOGO_H}px;margin-bottom:36px;}}
.logo img{{height:{LOGO_H}px;width:auto;object-fit:contain;max-width:300px;}}
.yr{{color:{co['sub']};font-family:'Raleway',sans-serif;font-size:22px;font-weight:400;letter-spacing:.12em;}}
.center{{display:flex;gap:52px;flex:1;overflow:hidden;}}
.txt{{flex:1;display:flex;flex-direction:column;justify-content:center;overflow:hidden;}}
.cat{{color:{co['accent']};font-family:'Raleway',sans-serif;font-size:18px;font-weight:700;letter-spacing:.24em;text-transform:uppercase;margin-bottom:16px;}}
.hl{{font-family:'Playfair Display',serif;color:{co['text']};font-size:76px;font-weight:900;line-height:1.07;letter-spacing:-.02em;margin-bottom:22px;}}
.rule2{{width:72px;height:4px;background:{co['accent']};margin-bottom:22px;}}
.sub{{color:{co['sub']};font-family:'Raleway',sans-serif;font-size:36px;font-weight:300;line-height:1.6;}}
.meta{{display:flex;flex-direction:column;gap:10px;margin-top:24px;}}
.ml{{color:{co['sub']};font-family:'Raleway',sans-serif;font-size:26px;}}.em{{color:{co['text']};font-weight:600;}}
.pc{{width:{SPK_W}px;flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:14px;justify-content:center;}}
.spp{{width:{SPK_W}px;height:{SPK_H}px;border-radius:12px;overflow:hidden;border:1px solid {co['border']};}}
.spp img{{width:{SPK_W}px;height:{SPK_H}px;object-fit:cover;object-position:top center;}}
.spkn{{color:{co['text']};font-family:'Raleway',sans-serif;font-size:26px;font-weight:700;text-align:center;}}
.spkr{{color:{co['sub']};font-family:'Raleway',sans-serif;font-size:20px;font-weight:300;text-align:center;line-height:1.4;}}
.foot{{flex-shrink:0;display:flex;justify-content:space-between;align-items:center;margin-top:28px;height:52px;border-top:1px solid {co['border']};padding-top:20px;}}
.org{{color:{co['sub']};font-family:'Raleway',sans-serif;font-size:20px;letter-spacing:.08em;}}
.cta{{display:flex;align-items:center;gap:14px;}}
.ctal{{color:{co['text']};font-family:'Raleway',sans-serif;font-size:26px;font-weight:700;}}
.ctac{{width:48px;height:48px;border-radius:50%;border:2px solid {co['text']};display:flex;align-items:center;justify-content:center;color:{co['text']};font-size:20px;}}
</style></head><body>
{d}<div class="rule"></div>
<div class="wrap">
  <div class="hdr"><div class="logo"><img src="{L}"></div><div class="yr">2025 Seminar</div></div>
  <div class="center">
    <div class="txt">
      <div class="cat">{ev('topic')}</div>
      <div class="hl">{cp['h']}</div>
      <div class="rule2"></div>
      <div class="sub">{cp['s']}</div>
      <div class="meta"><div class="ml"><span class="em">{ev('date')} {ev('time')}</span></div><div class="ml">{ev('venue')}</div></div>
    </div>
    <div class="pc"><div class="spp"><img src="{S[0]['file']}"></div><div class="spkn">{S[0]['name']}</div><div class="spkr">{S[0]['title']}</div></div>
  </div>
  <div class="foot"><div class="org">{ev('org')}</div><div class="cta"><div class="ctal">{cp['cta']}</div><div class="ctac">→</div></div></div>
</div></body></html>"""

def S_L2(cp, co, S, L, d):
    """[淺] BCG 風：左側粗邊條 + 三欄底部資訊"""
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">{ft('o')}
<style>{BASE}
body{{background:{co['bg']};font-family:'Noto Sans TC',sans-serif;}}
.stripe{{position:absolute;top:0;left:0;width:10px;height:1080px;background:{co['primary']};}}
.wrap{{position:absolute;top:0;left:10px;width:1070px;height:1080px;padding:52px 68px;display:flex;flex-direction:column;}}
.hdr{{display:flex;justify-content:space-between;align-items:center;flex-shrink:0;height:{LOGO_H}px;margin-bottom:40px;}}
.logo img{{height:{LOGO_H}px;width:auto;object-fit:contain;max-width:300px;}}
.tag{{border:1.5px solid {co['accent']};color:{co['accent']};font-family:'Outfit',sans-serif;font-size:18px;font-weight:700;padding:9px 24px;border-radius:4px;letter-spacing:.1em;text-transform:uppercase;}}
.hero{{flex:1;display:flex;gap:44px;overflow:hidden;}}
.txt{{flex:1;display:flex;flex-direction:column;justify-content:center;overflow:hidden;}}
.cat{{color:{co['accent']};font-family:'Outfit',sans-serif;font-size:18px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;margin-bottom:14px;}}
.hl{{font-family:'Outfit',sans-serif;color:{co['text']};font-size:80px;font-weight:800;line-height:1.07;letter-spacing:-.04em;margin-bottom:18px;}}
.sub{{color:{co['sub']};font-family:'Outfit',sans-serif;font-size:36px;font-weight:400;line-height:1.55;}}
.spk-col{{width:{SPK_W}px;flex-shrink:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;}}
.spp{{width:{SPK_W}px;height:{SPK_H}px;border-radius:8px;overflow:hidden;border:1px solid {co['border']};}}
.spp img{{width:{SPK_W}px;height:{SPK_H}px;object-fit:cover;object-position:top center;}}
.spkn{{color:{co['text']};font-family:'Outfit',sans-serif;font-size:26px;font-weight:700;text-align:center;}}
.spkr{{color:{co['sub']};font-family:'Outfit',sans-serif;font-size:20px;text-align:center;line-height:1.4;}}
.foot{{flex-shrink:0;height:140px;border-top:1px solid {co['border']};display:grid;grid-template-columns:1fr 1fr 1fr;margin-top:24px;}}
.fc{{display:flex;flex-direction:column;justify-content:center;padding:0 0 0 0;}}
.fc:not(:first-child){{border-left:1px solid {co['border']};padding-left:28px;}}
.fl{{color:{co['accent']};font-family:'Outfit',sans-serif;font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;margin-bottom:6px;}}
.fv{{color:{co['text']};font-family:'Outfit',sans-serif;font-size:22px;font-weight:600;line-height:1.35;}}
.cta{{background:{co['primary']};color:#FFFFFF;font-family:'Outfit',sans-serif;font-size:22px;font-weight:700;padding:14px 0;border-radius:6px;text-align:center;}}
</style></head><body>
{d}<div class="stripe"></div>
<div class="wrap">
  <div class="hdr"><div class="logo"><img src="{L}"></div><div class="tag">2025 Seminar</div></div>
  <div class="hero">
    <div class="txt"><div class="cat">{ev('topic')}</div><div class="hl">{cp['h']}</div><div class="sub">{cp['s']}</div></div>
    <div class="spk-col"><div class="spp"><img src="{S[0]['file']}"></div><div class="spkn">{S[0]['name']}</div><div class="spkr">{S[0]['title']}</div></div>
  </div>
  <div class="foot">
    <div class="fc"><div class="fl">日期</div><div class="fv">{ev('date')}</div></div>
    <div class="fc"><div class="fl">時間 & 地點</div><div class="fv">{ev('time')}<br>{ev('venue')}</div></div>
    <div class="fc"><div class="fl">立即行動</div><div class="cta" style="margin-top:8px">{cp['cta']} →</div></div>
  </div>
</div></body></html>"""

def S_L3(cp, co, S, L, d):
    """[淺] Bain 風：報章大標 + 底部全寬橫條"""
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">{ft('p')}
<style>{BASE}
body{{background:{co['bg']};font-family:'Noto Sans TC',sans-serif;}}
.top-bar{{position:absolute;top:0;left:0;width:1080px;height:88px;border-bottom:2px solid {co['text']};display:flex;align-items:center;justify-content:space-between;padding:0 60px;}}
.logo img{{height:{LOGO_H}px;width:auto;object-fit:contain;max-width:300px;}}
.top-r{{display:flex;align-items:center;gap:20px;}}
.top-tag{{color:{co['sub']};font-family:'Raleway',sans-serif;font-size:18px;font-weight:400;letter-spacing:.1em;}}
.cat-bar{{position:absolute;top:88px;left:0;width:1080px;height:52px;background:{co['primary']};display:flex;align-items:center;padding:0 60px;}}
.cat{{color:#FFFFFF;font-family:'Raleway',sans-serif;font-size:16px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;}}
.hero{{position:absolute;top:140px;left:0;width:1080px;height:664px;padding:44px 60px 36px;display:flex;gap:52px;overflow:hidden;}}
.txt{{flex:1;display:flex;flex-direction:column;justify-content:space-between;overflow:hidden;}}
.hl{{font-family:'Playfair Display',serif;color:{co['text']};font-size:82px;font-weight:900;line-height:1.06;letter-spacing:-.02em;}}
.sub{{color:{co['sub']};font-family:'Raleway',sans-serif;font-size:34px;font-weight:300;line-height:1.6;}}
.spk-col{{width:{SPK_W}px;flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:14px;justify-content:center;}}
.spp{{width:{SPK_W}px;height:{SPK_H}px;border-radius:8px;overflow:hidden;border:1px solid {co['border']};}}
.spp img{{width:{SPK_W}px;height:{SPK_H}px;object-fit:cover;object-position:top center;}}
.spkn{{color:{co['text']};font-family:'Raleway',sans-serif;font-size:26px;font-weight:700;text-align:center;}}
.spkr{{color:{co['sub']};font-family:'Raleway',sans-serif;font-size:20px;font-weight:300;text-align:center;line-height:1.4;}}
.bot{{position:absolute;top:804px;left:0;width:1080px;height:276px;border-top:2px solid {co['text']};display:flex;align-items:stretch;padding:0 60px;}}
.bc{{flex:1;display:flex;flex-direction:column;justify-content:center;gap:8px;padding:24px 0;}}
.bc+.bc{{border-left:1px solid {co['border']};padding-left:36px;margin-left:36px;}}
.bl{{color:{co['accent']};font-family:'Raleway',sans-serif;font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;margin-bottom:4px;}}
.bv{{color:{co['text']};font-family:'Raleway',sans-serif;font-size:24px;font-weight:600;line-height:1.35;}}
.cta{{background:{co['primary']};color:#FFFFFF;font-family:'Raleway',sans-serif;font-size:22px;font-weight:700;padding:14px 40px;border-radius:4px;align-self:center;white-space:nowrap;}}
</style></head><body>
{d}
<div class="top-bar"><div class="logo"><img src="{L}"></div><div class="top-r"><div class="top-tag">{ev('org')} · 2025</div></div></div>
<div class="cat-bar"><div class="cat">{ev('topic')} · 專題座談</div></div>
<div class="hero">
  <div class="txt"><div class="hl">{cp['h']}</div><div class="sub">{cp['s']}</div></div>
  <div class="spk-col"><div class="spp"><img src="{S[0]['file']}"></div><div class="spkn">{S[0]['name']}</div><div class="spkr">{S[0]['title']}</div></div>
</div>
<div class="bot">
  <div class="bc"><div class="bl">日期</div><div class="bv">{ev('date')}</div></div>
  <div class="bc"><div class="bl">時間</div><div class="bv">{ev('time')}</div></div>
  <div class="bc"><div class="bl">地點</div><div class="bv">{ev('venue')}</div></div>
  <div class="bc"><div class="cta">{cp['cta']} →</div></div>
</div></body></html>"""

def S_L4(cp, co, S, L, d):
    """[淺] McKinsey 風：框中框，講者右側"""
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">{ft('o')}
<style>{BASE}
body{{background:{co['bg']};font-family:'Noto Sans TC',sans-serif;padding:32px;}}
.frame{{position:absolute;top:32px;left:32px;width:1016px;height:1016px;border:2px solid {co['primary']};border-radius:4px;overflow:hidden;}}
.inner{{position:absolute;top:0;left:0;width:1016px;height:1016px;padding:44px 52px;display:flex;flex-direction:column;}}
.hdr{{display:flex;justify-content:space-between;align-items:center;flex-shrink:0;height:{LOGO_H}px;margin-bottom:32px;}}
.logo img{{height:{LOGO_H}px;width:auto;object-fit:contain;max-width:300px;}}
.tag{{border:1px solid {co['accent']};color:{co['accent']};font-family:'Outfit',sans-serif;font-size:17px;font-weight:700;padding:8px 22px;border-radius:4px;letter-spacing:.1em;text-transform:uppercase;}}
.content{{flex:1;display:flex;gap:44px;overflow:hidden;}}
.txt{{flex:1;display:flex;flex-direction:column;justify-content:space-between;overflow:hidden;}}
.cat{{color:{co['accent']};font-family:'Outfit',sans-serif;font-size:17px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;margin-bottom:14px;}}
.hl{{font-family:'Outfit',sans-serif;color:{co['text']};font-size:74px;font-weight:800;line-height:1.08;letter-spacing:-.04em;margin-bottom:18px;}}
.sub{{color:{co['sub']};font-family:'Outfit',sans-serif;font-size:34px;font-weight:400;line-height:1.55;}}
.meta{{display:flex;flex-direction:column;gap:9px;}}
.ml{{color:{co['sub']};font-size:23px;}}.em{{color:{co['text']};font-weight:600;}}
.spk-panel{{width:240px;flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:14px;justify-content:center;border-left:1px solid {co['border']};padding-left:32px;}}
.sp{{width:180px;height:180px;border-radius:50%;overflow:hidden;border:2px solid {co['border']};}}
.sp img{{width:180px;height:180px;object-fit:cover;object-position:top center;}}
.spkn{{color:{co['text']};font-family:'Outfit',sans-serif;font-size:24px;font-weight:700;text-align:center;}}
.spkr{{color:{co['sub']};font-family:'Outfit',sans-serif;font-size:18px;text-align:center;line-height:1.4;}}
.foot{{flex-shrink:0;display:flex;justify-content:flex-end;margin-top:24px;}}
.cta{{background:{co['primary']};color:#FFFFFF;font-family:'Outfit',sans-serif;font-size:22px;font-weight:700;padding:14px 52px;border-radius:4px;}}
</style></head><body>
{d}
<div class="frame">
  <div class="inner">
    <div class="hdr"><div class="logo"><img src="{L}"></div><div class="tag">{ev('topic')}</div></div>
    <div class="content">
      <div class="txt">
        <div><div class="cat">2025 座談會</div><div class="hl">{cp['h']}</div><div class="sub">{cp['s']}</div></div>
        <div class="meta"><div class="ml"><span class="em">{ev('date')} {ev('time')}</span></div><div class="ml">{ev('venue')}</div></div>
      </div>
      <div class="spk-panel"><div class="sp"><img src="{S[0]['file']}"></div><div class="spkn">{S[0]['name']}</div><div class="spkr">{S[0]['title']}</div></div>
    </div>
    <div class="foot"><div class="cta">{cp['cta']} →</div></div>
  </div>
</div></body></html>"""

def S_L5(cp, co, S, L, d):
    """[淺] 大色塊底部 CTA + 講者右側"""
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">{ft('o')}
<style>{BASE}
body{{background:{co['bg']};font-family:'Noto Sans TC',sans-serif;}}
.wrap{{position:absolute;top:0;left:0;width:1080px;height:1080px;display:flex;flex-direction:column;}}
.upper{{flex:1;padding:52px 68px 32px;display:flex;flex-direction:column;overflow:hidden;}}
.hdr{{display:flex;justify-content:space-between;align-items:center;flex-shrink:0;height:{LOGO_H}px;margin-bottom:36px;}}
.logo img{{height:{LOGO_H}px;width:auto;object-fit:contain;max-width:300px;}}
.tag{{background:{co['tag']};border:1px solid {co['border']};color:{co['accent']};font-family:'Outfit',sans-serif;font-size:18px;font-weight:700;padding:9px 24px;border-radius:20px;}}
.mid{{flex:1;display:flex;gap:44px;align-items:center;overflow:hidden;}}
.txt{{flex:1;overflow:hidden;}}
.cat{{color:{co['accent']};font-family:'Outfit',sans-serif;font-size:18px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;margin-bottom:14px;}}
.hl{{font-family:'Outfit',sans-serif;color:{co['text']};font-size:80px;font-weight:800;line-height:1.07;letter-spacing:-.04em;margin-bottom:18px;}}
.sub{{color:{co['sub']};font-family:'Outfit',sans-serif;font-size:36px;font-weight:400;line-height:1.5;}}
.spk-card{{width:240px;flex-shrink:0;background:{co['card']};border:1px solid {co['border']};border-radius:10px;padding:24px 20px;display:flex;flex-direction:column;align-items:center;gap:12px;}}
.sp{{width:160px;height:160px;border-radius:50%;overflow:hidden;border:2px solid {co['border']};}}
.sp img{{width:160px;height:160px;object-fit:cover;object-position:top center;}}
.spkn{{color:{co['text']};font-family:'Outfit',sans-serif;font-size:24px;font-weight:700;text-align:center;}}
.spkr{{color:{co['sub']};font-family:'Outfit',sans-serif;font-size:18px;text-align:center;line-height:1.4;}}
.lower{{flex-shrink:0;height:190px;background:{co['primary']};display:flex;align-items:center;justify-content:space-between;padding:0 68px;}}
.meta{{display:flex;flex-direction:column;gap:10px;}}
.mr{{color:rgba(255,255,255,0.75);font-size:26px;display:flex;align-items:center;gap:10px;}}.dot{{width:5px;height:5px;border-radius:50%;background:rgba(255,255,255,0.6);}}
.cta{{background:#FFFFFF;color:{co['primary']};font-family:'Outfit',sans-serif;font-size:24px;font-weight:800;padding:16px 52px;border-radius:50px;white-space:nowrap;}}
</style></head><body>
{d}
<div class="wrap">
  <div class="upper">
    <div class="hdr"><div class="logo"><img src="{L}"></div><div class="tag">{ev('topic')}</div></div>
    <div class="mid">
      <div class="txt"><div class="cat">2025 座談會</div><div class="hl">{cp['h']}</div><div class="sub">{cp['s']}</div></div>
      <div class="spk-card"><div class="sp"><img src="{S[0]['file']}"></div><div class="spkn">{S[0]['name']}</div><div class="spkr">{S[0]['title']}</div></div>
    </div>
  </div>
  <div class="lower">
    <div class="meta"><div class="mr"><div class="dot"></div>{ev('date')} {ev('time')}</div><div class="mr"><div class="dot"></div>{ev('venue')}</div></div>
    <div class="cta">{cp['cta']} →</div>
  </div>
</div></body></html>"""

def S_L6(cp, co, S, L, d):
    """[淺] 三欄 editorial，講者中欄"""
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">{ft('o')}
<style>{BASE}
body{{background:{co['bg']};font-family:'Noto Sans TC',sans-serif;}}
.wrap{{position:absolute;top:0;left:0;width:1080px;height:1080px;padding:52px 56px;display:flex;flex-direction:column;}}
.hdr{{display:flex;justify-content:space-between;align-items:center;flex-shrink:0;height:{LOGO_H}px;margin-bottom:32px;}}
.logo img{{height:{LOGO_H}px;width:auto;object-fit:contain;max-width:300px;}}
.badge{{background:{co['tag']};border:1px solid {co['border']};color:{co['accent']};font-family:'Outfit',sans-serif;font-size:18px;font-weight:700;padding:9px 24px;border-radius:20px;}}
.cols{{display:grid;grid-template-columns:1fr 1px 220px 1px 1fr;flex:1;overflow:hidden;}}
.sep{{background:{co['border']};}}
.col{{padding:0 36px;display:flex;flex-direction:column;justify-content:space-between;overflow:hidden;}}
.col:first-child{{padding-left:0;}}
.col:last-child{{padding-right:0;}}
.cl{{color:{co['accent']};font-family:'Outfit',sans-serif;font-size:12px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;margin-bottom:14px;}}
.hl{{font-family:'Outfit',sans-serif;color:{co['text']};font-size:66px;font-weight:800;line-height:1.09;letter-spacing:-.035em;}}
.sub{{color:{co['sub']};font-size:30px;line-height:1.55;margin-top:16px;}}
.mid-col{{padding:0 16px;display:flex;flex-direction:column;align-items:center;gap:16px;}}
.sp{{width:180px;height:180px;border-radius:50%;overflow:hidden;border:2px solid {co['border']};}}
.sp img{{width:180px;height:180px;object-fit:cover;object-position:top center;}}
.spkn{{color:{co['text']};font-family:'Outfit',sans-serif;font-size:24px;font-weight:700;text-align:center;}}
.spkr{{color:{co['sub']};font-size:18px;text-align:center;line-height:1.4;}}
.info-list{{display:flex;flex-direction:column;gap:14px;}}
.ii{{border-left:3px solid {co['accent']};padding-left:14px;}}
.il{{color:{co['accent']};font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;margin-bottom:4px;}}
.iv{{color:{co['text']};font-size:22px;font-weight:600;line-height:1.35;}}
.cta{{background:{co['primary']};color:#FFFFFF;font-family:'Outfit',sans-serif;font-size:22px;font-weight:700;padding:14px 0;border-radius:6px;text-align:center;}}
</style></head><body>
{d}
<div class="wrap">
  <div class="hdr"><div class="logo"><img src="{L}"></div><div class="badge">{ev('topic')}</div></div>
  <div class="cols">
    <div class="col">
      <div><div class="cl">本次主題</div><div class="hl">{cp['h']}</div><div class="sub">{cp['s']}</div></div>
    </div>
    <div class="sep"></div>
    <div class="col">
      <div class="cl" style="text-align:center">主講者</div>
      <div class="mid-col"><div class="sp"><img src="{S[0]['file']}"></div><div class="spkn">{S[0]['name']}</div><div class="spkr">{S[0]['title']}</div></div>
      <div></div>
    </div>
    <div class="sep"></div>
    <div class="col">
      <div>
        <div class="cl">活動資訊</div>
        <div class="info-list">
          <div class="ii"><div class="il">日期</div><div class="iv">{ev('date')}</div></div>
          <div class="ii"><div class="il">時間</div><div class="iv">{ev('time')}</div></div>
          <div class="ii"><div class="il">地點</div><div class="iv">{ev('venue')}</div></div>
        </div>
      </div>
      <div class="cta">{cp['cta']} →</div>
    </div>
  </div>
</div></body></html>"""

def S_D1(cp, co, S, L, d):
    """[深] 科技風：大光暈 + 底部橫條，講者圓形"""
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">{ft('s')}
<style>{BASE}
body{{background:{co['bg']};font-family:'Noto Sans TC',sans-serif;}}
.g1{{position:absolute;width:760px;height:760px;background:radial-gradient(circle,{co['primary']}50,transparent 65%);top:-240px;right:-160px;}}
.g2{{position:absolute;width:440px;height:440px;background:radial-gradient(circle,{co['accent']}14,transparent 65%);bottom:-80px;left:-60px;}}
.wrap{{position:absolute;top:0;left:0;width:1080px;height:1080px;display:flex;flex-direction:column;z-index:5;}}
.top{{display:flex;justify-content:space-between;align-items:center;padding:50px 68px 0;flex-shrink:0;height:{LOGO_H+50}px;}}
.logo img{{height:{LOGO_H}px;width:auto;object-fit:contain;max-width:300px;filter:brightness(0) invert(1);}}
.tag{{background:{co['tag']};border:1px solid {co['border']};color:{co['accent']};font-family:'Syne',sans-serif;font-size:21px;font-weight:700;padding:10px 28px;border-radius:40px;}}
.body{{flex:1;padding:28px 68px 0;display:flex;flex-direction:column;justify-content:center;overflow:hidden;}}
.eye{{color:{co['accent']};font-family:'Syne',sans-serif;font-size:21px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;display:flex;align-items:center;gap:14px;margin-bottom:16px;}}
.eye::before{{content:'';width:44px;height:3px;background:{co['accent']};}}
.hl{{font-family:'Syne',sans-serif;color:{co['text']};font-size:92px;font-weight:800;line-height:1.06;letter-spacing:-.04em;margin-bottom:16px;}}
.sub{{color:{co['sub']};font-size:38px;line-height:1.5;}}
.bar{{flex-shrink:0;height:230px;background:{co['card']};border-top:2px solid {co['accent']}40;padding:0 68px;display:flex;align-items:center;justify-content:space-between;}}
.spk{{display:flex;align-items:center;gap:22px;}}
.sp{{width:{SPK_C}px;height:{SPK_C}px;border-radius:50%;overflow:hidden;border:3px solid {co['accent']}65;flex-shrink:0;}}
.sp img{{width:{SPK_C}px;height:{SPK_C}px;object-fit:cover;object-position:top center;}}
.spkn{{color:{co['text']};font-family:'Syne',sans-serif;font-size:38px;font-weight:700;}}
.spkr{{color:{co['sub']};font-size:28px;margin-top:5px;}}
.rb{{display:flex;flex-direction:column;align-items:flex-end;gap:12px;}}
.mr{{color:{co['sub']};font-size:26px;}}
.cta{{background:{co['primary']};color:#FFFFFF;font-family:'Syne',sans-serif;font-size:26px;font-weight:700;padding:14px 48px;border-radius:50px;border:1px solid {co['accent']}60;}}
</style></head><body>
<div class="g1"></div><div class="g2"></div>{d}
<div class="wrap">
  <div class="top"><div class="logo"><img src="{L}"></div><div class="tag">{ev('topic')}</div></div>
  <div class="body"><div class="eye">2025 座談會</div><div class="hl">{cp['h']}</div><div class="sub">{cp['s']}</div></div>
  <div class="bar">
    <div class="spk"><div class="sp"><img src="{S[0]['file']}"></div><div><div class="spkn">{S[0]['name']}</div><div class="spkr">{S[0]['title']}</div></div></div>
    <div class="rb"><div class="mr">{ev('date')} {ev('time')}</div><div class="mr">{ev('venue')}</div><div class="cta">{cp['cta']} →</div></div>
  </div>
</div></body></html>"""

def S_D2(cp, co, S, L, d):
    """[深] 卡片堆疊，講者圓形右上，info grid"""
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">{ft('b')}
<style>{BASE}
body{{background:{co['bg']};font-family:'Noto Sans TC',sans-serif;}}
.b1{{position:absolute;width:600px;height:600px;background:radial-gradient(circle,{co['primary']}48,transparent 65%);top:-200px;right:-120px;}}
.b2{{position:absolute;width:400px;height:400px;background:radial-gradient(circle,{co['accent']}15,transparent 65%);bottom:-100px;left:-60px;}}
.wrap{{position:absolute;top:0;left:0;width:1080px;height:1080px;padding:44px 56px;display:flex;flex-direction:column;gap:14px;z-index:5;}}
.top{{display:flex;justify-content:space-between;align-items:center;flex-shrink:0;height:{LOGO_H}px;}}
.logo img{{height:{LOGO_H}px;width:auto;object-fit:contain;max-width:300px;filter:brightness(0) invert(1);}}
.badge{{background:{co['accent']};color:{co['bg']};font-family:'Outfit',sans-serif;font-size:20px;font-weight:700;padding:10px 26px;border-radius:22px;}}
.card{{background:{co['card']};border:1px solid {co['border']};border-radius:20px;padding:36px 44px;position:relative;flex:1;overflow:hidden;display:flex;flex-direction:column;justify-content:space-between;}}
.card::before{{content:'';position:absolute;inset:0;border-radius:20px;background:linear-gradient(135deg,{co['accent']}10,transparent 50%);pointer-events:none;}}
.spp{{position:absolute;top:28px;right:36px;width:{SPK_C}px;height:{SPK_C}px;border-radius:50%;overflow:hidden;border:3px solid {co['accent']}65;box-shadow:0 0 44px {co['accent']}28;}}
.spp img{{width:{SPK_C}px;height:{SPK_C}px;object-fit:cover;object-position:top center;}}
.cat{{color:{co['accent']};font-family:'Outfit',sans-serif;font-size:18px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;margin-bottom:12px;}}
.hl{{font-family:'Bebas Neue',sans-serif;color:{co['text']};font-size:88px;line-height:.97;max-width:680px;margin-bottom:14px;}}
.sub{{color:{co['sub']};font-family:'Outfit',sans-serif;font-size:36px;font-weight:400;line-height:1.5;max-width:680px;}}
.chip{{display:inline-flex;align-items:center;gap:12px;border:1px solid {co['border']};border-radius:28px;padding:10px 24px;margin-top:14px;}}
.chipt{{color:{co['sub']};font-family:'Outfit',sans-serif;font-size:22px;}}
.grid{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;flex-shrink:0;height:96px;}}
.gc{{background:{co['card']};border:1px solid {co['border']};border-radius:10px;padding:14px 18px;}}
.gl{{color:{co['accent']};font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;margin-bottom:4px;}}
.gv{{color:{co['text']};font-size:21px;font-weight:600;line-height:1.3;}}
.ctac{{background:{co['primary']};border-radius:12px;height:68px;display:flex;align-items:center;justify-content:center;border:1px solid {co['accent']}50;flex-shrink:0;}}
.ctact{{color:#FFFFFF;font-family:'Outfit',sans-serif;font-size:24px;font-weight:700;}}
</style></head><body>
<div class="b1"></div><div class="b2"></div>{d}
<div class="wrap">
  <div class="top"><div class="logo"><img src="{L}"></div><div class="badge">座談會 2025</div></div>
  <div class="card"><div class="spp"><img src="{S[0]['file']}"></div>
    <div><div class="cat">{ev('topic')}</div><div class="hl">{cp['h']}</div><div class="sub">{cp['s']}</div></div>
    <div class="chip"><span class="chipt">講者｜{S[0]['name']} · {S[0]['title']}</span></div>
  </div>
  <div class="grid">
    <div class="gc"><div class="gl">日期</div><div class="gv">{ev('date')}</div></div>
    <div class="gc"><div class="gl">時間</div><div class="gv">{ev('time')}</div></div>
    <div class="gc"><div class="gl">地點</div><div class="gv">{ev('venue')}</div></div>
  </div>
  <div class="ctac"><div class="ctact">{cp['cta']} →</div></div>
</div></body></html>"""

# ═══════════════════════════════════════
# MULTI-SPEAKER LAYOUTS  (2–4 人通用)
# ═══════════════════════════════════════

def M_L1(cp, co, speakers, L, d):
    """[淺] 多人：講者圓形橫排 + 大標上方"""
    spk_html = ''.join(f'''
      <div class="spk-item">
        <div class="sp"><img src="{s['file']}"></div>
        <div class="spkn">{s['name']}</div>
        <div class="spkr">{s['title']}</div>
      </div>''' for s in speakers)
    n = len(speakers)
    sp_sz = max(140, min(200, 700 // n))
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">{ft('p')}
<style>{BASE}
body{{background:{co['bg']};font-family:'Noto Sans TC',sans-serif;}}
.rule{{position:absolute;top:0;left:0;width:1080px;height:4px;background:linear-gradient(90deg,{co['primary']},{co['accent']});}}
.wrap{{position:absolute;top:4px;left:0;width:1080px;height:1076px;padding:48px 68px 52px;display:flex;flex-direction:column;}}
.hdr{{display:flex;justify-content:space-between;align-items:center;flex-shrink:0;height:{LOGO_H}px;margin-bottom:32px;}}
.logo img{{height:{LOGO_H}px;width:auto;object-fit:contain;max-width:300px;}}
.yr{{color:{co['sub']};font-family:'Raleway',sans-serif;font-size:22px;letter-spacing:.1em;}}
.hero{{flex:1;display:flex;flex-direction:column;justify-content:center;overflow:hidden;}}
.cat{{color:{co['accent']};font-family:'Raleway',sans-serif;font-size:18px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;margin-bottom:14px;}}
.hl{{font-family:'Playfair Display',serif;color:{co['text']};font-size:76px;font-weight:900;line-height:1.07;letter-spacing:-.02em;margin-bottom:16px;}}
.sub{{color:{co['sub']};font-family:'Raleway',sans-serif;font-size:34px;font-weight:300;line-height:1.6;}}
.speakers-row{{flex-shrink:0;display:flex;justify-content:center;gap:36px;padding:28px 0 20px;border-top:1px solid {co['border']};margin-top:20px;}}
.spk-item{{display:flex;flex-direction:column;align-items:center;gap:10px;}}
.sp{{width:{sp_sz}px;height:{sp_sz}px;border-radius:50%;overflow:hidden;border:2px solid {co['border']};}}
.sp img{{width:{sp_sz}px;height:{sp_sz}px;object-fit:cover;object-position:top center;}}
.spkn{{color:{co['text']};font-family:'Raleway',sans-serif;font-size:22px;font-weight:700;text-align:center;}}
.spkr{{color:{co['sub']};font-family:'Raleway',sans-serif;font-size:17px;font-weight:300;text-align:center;line-height:1.4;}}
.foot{{flex-shrink:0;display:flex;justify-content:space-between;align-items:center;padding-top:16px;border-top:1px solid {co['border']};height:64px;}}
.meta{{display:flex;gap:24px;flex-wrap:wrap;}}
.ml{{color:{co['sub']};font-family:'Raleway',sans-serif;font-size:22px;}}
.cta{{background:{co['primary']};color:#FFFFFF;font-family:'Raleway',sans-serif;font-size:22px;font-weight:700;padding:12px 44px;border-radius:4px;white-space:nowrap;}}
</style></head><body>
{d}<div class="rule"></div>
<div class="wrap">
  <div class="hdr"><div class="logo"><img src="{L}"></div><div class="yr">2025 Seminar · {ev('org')}</div></div>
  <div class="hero">
    <div class="cat">{ev('topic')}</div>
    <div class="hl">{cp['h']}</div>
    <div class="sub">{cp['s']}</div>
  </div>
  <div class="speakers-row">{spk_html}</div>
  <div class="foot">
    <div class="meta"><div class="ml">{ev('date')} {ev('time')}</div><div class="ml">{ev('venue')}</div></div>
    <div class="cta">{cp['cta']} →</div>
  </div>
</div></body></html>"""

def M_L2(cp, co, speakers, L, d):
    """[淺] 多人：左側文案 + 右側講者縱列"""
    n = len(speakers)
    sp_sz = max(130, min(180, 720 // n))
    spk_html = ''.join(f'''
      <div class="spk-item">
        <div class="sp"><img src="{s['file']}"></div>
        <div class="spkn">{s['name']}</div>
        <div class="spkr">{s['title']}</div>
      </div>''' for s in speakers)
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">{ft('o')}
<style>{BASE}
body{{background:{co['bg']};font-family:'Noto Sans TC',sans-serif;}}
.stripe{{position:absolute;top:0;left:0;width:8px;height:1080px;background:linear-gradient(180deg,{co['primary']},{co['accent']},{co['primary']}30);}}
.wrap{{position:absolute;top:0;left:8px;width:1072px;height:1080px;padding:52px 64px;display:flex;gap:44px;}}
.left{{flex:1;display:flex;flex-direction:column;justify-content:space-between;overflow:hidden;}}
.logo img{{height:{LOGO_H}px;width:auto;object-fit:contain;max-width:300px;}}
.mid{{flex:1;display:flex;flex-direction:column;justify-content:center;gap:16px;}}
.cat{{color:{co['accent']};font-family:'Outfit',sans-serif;font-size:18px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;}}
.hl{{font-family:'Outfit',sans-serif;color:{co['text']};font-size:76px;font-weight:800;line-height:1.07;letter-spacing:-.04em;}}
.sub{{color:{co['sub']};font-family:'Outfit',sans-serif;font-size:34px;font-weight:400;line-height:1.5;}}
.meta{{display:flex;flex-direction:column;gap:9px;}}
.ml{{color:{co['sub']};font-size:24px;}}.em{{color:{co['text']};font-weight:600;}}
.cta{{background:{co['primary']};color:#FFFFFF;font-family:'Outfit',sans-serif;font-size:24px;font-weight:700;padding:16px 0;border-radius:6px;text-align:center;}}
.right{{width:260px;flex-shrink:0;display:flex;flex-direction:column;justify-content:center;gap:24px;border-left:1px solid {co['border']};padding-left:36px;}}
.spk-item{{display:flex;flex-direction:column;align-items:center;gap:10px;}}
.sp{{width:{sp_sz}px;height:{sp_sz}px;border-radius:50%;overflow:hidden;border:2px solid {co['border']};}}
.sp img{{width:{sp_sz}px;height:{sp_sz}px;object-fit:cover;object-position:top center;}}
.spkn{{color:{co['text']};font-family:'Outfit',sans-serif;font-size:20px;font-weight:700;text-align:center;}}
.spkr{{color:{co['sub']};font-family:'Outfit',sans-serif;font-size:16px;text-align:center;line-height:1.4;}}
</style></head><body>
{d}<div class="stripe"></div>
<div class="wrap">
  <div class="left">
    <div class="logo"><img src="{L}"></div>
    <div class="mid"><div class="cat">{ev('topic')}</div><div class="hl">{cp['h']}</div><div class="sub">{cp['s']}</div></div>
    <div class="meta"><div class="ml"><span class="em">{ev('date')} {ev('time')}</span></div><div class="ml">{ev('venue')}</div></div>
    <div class="cta">{cp['cta']} →</div>
  </div>
  <div class="right">{spk_html}</div>
</div></body></html>"""

def M_D1(cp, co, speakers, L, d):
    """[深] 多人：大光暈 + 底部講者橫排"""
    n = len(speakers)
    sp_sz = max(150, min(200, 820 // n))
    spk_html = ''.join(f'''
      <div class="spk-item">
        <div class="sp"><img src="{s['file']}"></div>
        <div class="spkn">{s['name']}</div>
        <div class="spkr">{s['title']}</div>
      </div>''' for s in speakers)
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">{ft('s')}
<style>{BASE}
body{{background:{co['bg']};font-family:'Noto Sans TC',sans-serif;}}
.g1{{position:absolute;width:760px;height:760px;background:radial-gradient(circle,{co['primary']}48,transparent 65%);top:-220px;right:-150px;}}
.g2{{position:absolute;width:440px;height:440px;background:radial-gradient(circle,{co['accent']}14,transparent 65%);bottom:-80px;left:-60px;}}
.wrap{{position:absolute;top:0;left:0;width:1080px;height:1080px;display:flex;flex-direction:column;z-index:5;}}
.top{{display:flex;justify-content:space-between;align-items:center;padding:50px 68px 0;flex-shrink:0;height:{LOGO_H+50}px;}}
.logo img{{height:{LOGO_H}px;width:auto;object-fit:contain;max-width:300px;filter:brightness(0) invert(1);}}
.tag{{background:{co['tag']};border:1px solid {co['border']};color:{co['accent']};font-family:'Syne',sans-serif;font-size:20px;font-weight:700;padding:10px 26px;border-radius:40px;}}
.body{{flex:1;padding:28px 68px 0;display:flex;flex-direction:column;justify-content:center;overflow:hidden;}}
.eye{{color:{co['accent']};font-family:'Syne',sans-serif;font-size:20px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;display:flex;align-items:center;gap:14px;margin-bottom:14px;}}
.eye::before{{content:'';width:40px;height:3px;background:{co['accent']};}}
.hl{{font-family:'Syne',sans-serif;color:{co['text']};font-size:90px;font-weight:800;line-height:1.06;letter-spacing:-.04em;margin-bottom:14px;}}
.sub{{color:{co['sub']};font-size:36px;line-height:1.5;}}
.bar{{flex-shrink:0;background:{co['card']};border-top:2px solid {co['accent']}40;padding:20px 68px;display:flex;align-items:center;justify-content:space-between;}}
.speakers-row{{display:flex;gap:28px;align-items:center;}}
.spk-item{{display:flex;flex-direction:column;align-items:center;gap:8px;}}
.sp{{width:{sp_sz}px;height:{sp_sz}px;border-radius:50%;overflow:hidden;border:3px solid {co['accent']}65;flex-shrink:0;}}
.sp img{{width:{sp_sz}px;height:{sp_sz}px;object-fit:cover;object-position:top center;}}
.spkn{{color:{co['text']};font-family:'Syne',sans-serif;font-size:22px;font-weight:700;text-align:center;}}
.spkr{{color:{co['sub']};font-size:18px;text-align:center;}}
.rb{{display:flex;flex-direction:column;align-items:flex-end;gap:12px;flex-shrink:0;}}
.mr{{color:{co['sub']};font-size:24px;}}
.cta{{background:{co['primary']};color:#FFFFFF;font-family:'Syne',sans-serif;font-size:24px;font-weight:700;padding:13px 44px;border-radius:50px;border:1px solid {co['accent']}60;}}
</style></head><body>
<div class="g1"></div><div class="g2"></div>{d}
<div class="wrap">
  <div class="top"><div class="logo"><img src="{L}"></div><div class="tag">{ev('topic')}</div></div>
  <div class="body"><div class="eye">2025 座談會</div><div class="hl">{cp['h']}</div><div class="sub">{cp['s']}</div></div>
  <div class="bar">
    <div class="speakers-row">{spk_html}</div>
    <div class="rb"><div class="mr">{ev('date')} {ev('time')}</div><div class="mr">{ev('venue')}</div><div class="cta">{cp['cta']} →</div></div>
  </div>
</div></body></html>"""

# ─────────────────────────────────────────────
# Registry
# ─────────────────────────────────────────────
SOLO_LAYOUTS  = {'S_L1':S_L1,'S_L2':S_L2,'S_L3':S_L3,'S_L4':S_L4,'S_L5':S_L5,'S_L6':S_L6,'S_D1':S_D1,'S_D2':S_D2}
MULTI_LAYOUTS = {'M_L1':M_L1,'M_L2':M_L2,'M_D1':M_D1}

# Weighted sequence: 6 light + 2 dark = 75% light for solo
SOLO_SEQ  = ['S_L1','S_L2','S_L3','S_L4','S_L5','S_L6','S_D1','S_L1','S_L2','S_L3','S_D2','S_L4','S_L5','S_L6']
MULTI_SEQ = ['M_L1','M_L2','M_L1','M_D1','M_L2','M_L1']

def render_single(layout_key, cp, color_key, speaker_key, deco_variant=0):
    from skill_c_color import get_colors, get_logo
    from skill_d_deco  import get_decoration
    from speakers      import get_speakers
    co   = get_colors()[color_key]
    L    = get_logo(color_key)
    spk  = get_speakers()
    S    = [spk[speaker_key]]
    deco = get_decoration(deco_variant, co)
    return SOLO_LAYOUTS[layout_key](cp, co, S, L, deco)

def render_multi(layout_key, cp, color_key, speaker_keys, deco_variant=0):
    from skill_c_color import get_colors, get_logo
    from skill_d_deco  import get_decoration
    from speakers      import get_speakers
    co   = get_colors()[color_key]
    L    = get_logo(color_key)
    spk  = get_speakers()
    S    = [spk[k] for k in speaker_keys if k in spk]
    deco = get_decoration(deco_variant, co)
    return MULTI_LAYOUTS[layout_key](cp, co, S, L, deco)

# backward compat
def render_solo(layout_key, cp, color_key, speaker_key, deco_variant=0):
    return render_single(layout_key, cp, color_key, speaker_key, deco_variant)

if __name__ == '__main__':
    light = sum(1 for k in SOLO_LAYOUTS if '_L' in k)
    dark  = sum(1 for k in SOLO_LAYOUTS if '_D' in k)
    print(f'Solo 版型：淺 {light} / 深 {dark} = 深色 {dark/(light+dark)*100:.0f}%')
    print(f'Multi 版型：{list(MULTI_LAYOUTS.keys())}')
