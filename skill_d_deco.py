"""
SKILL D — 裝飾引擎（Decoration Engine）
輸入：variant index (0-4)、color dict
輸出：inline SVG 字串，疊加在畫面上

D0 — 六角網格
D1 — 電路板線條 + 點陣
D2 — 幾何角落色塊
D3 — 流線數據曲線
D4 — 對角線 + 同心圓
"""

def get_decoration(variant: int, co: dict) -> str:
    a = co['accent']
    p = co['primary']
    v = variant % 5
    svgs = [
        # D0: Hex grid
        f'<svg style="position:absolute;inset:0;width:1080px;height:1080px;pointer-events:none;z-index:1" viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="hx" x="0" y="0" width="60" height="52" patternUnits="userSpaceOnUse"><polygon points="30,2 58,17 58,47 30,62 2,47 2,17" fill="none" stroke="{a}" stroke-width="0.7" opacity="0.15"/></pattern></defs><rect width="1080" height="1080" fill="url(#hx)"/><circle cx="1040" cy="40" r="90" fill="none" stroke="{a}" stroke-width="1.2" opacity="0.18"/><circle cx="40" cy="1040" r="70" fill="none" stroke="{a}" stroke-width="1" opacity="0.15"/><line x1="0" y1="180" x2="280" y2="180" stroke="{a}" stroke-width="1.2" opacity="0.22"/><line x1="800" y1="900" x2="1080" y2="900" stroke="{a}" stroke-width="1.2" opacity="0.22"/></svg>',
        # D1: Circuit + dots
        f'<svg style="position:absolute;inset:0;width:1080px;height:1080px;pointer-events:none;z-index:1" viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="dt" x="0" y="0" width="36" height="36" patternUnits="userSpaceOnUse"><circle cx="18" cy="18" r="1.2" fill="{a}" opacity="0.18"/></pattern></defs><rect width="1080" height="1080" fill="url(#dt)"/><path d="M0,90 H180 V270 H380 V180 H560" stroke="{a}" stroke-width="1.4" fill="none" opacity="0.2"/><path d="M1080,810 H900 V630 H700 V720 H500 V920" stroke="{a}" stroke-width="1.4" fill="none" opacity="0.2"/><circle cx="180" cy="90" r="5" fill="{a}" opacity="0.35"/><circle cx="380" cy="270" r="5" fill="{a}" opacity="0.35"/><circle cx="900" cy="810" r="5" fill="{a}" opacity="0.35"/><circle cx="700" cy="630" r="5" fill="{a}" opacity="0.35"/></svg>',
        # D2: Geometric corners
        f'<svg style="position:absolute;inset:0;width:1080px;height:1080px;pointer-events:none;z-index:1" viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg"><polygon points="1080,0 1080,100 980,0" fill="{a}" opacity="0.2"/><polygon points="0,1080 100,1080 0,980" fill="{a}" opacity="0.2"/><polygon points="1080,250 1080,290 1040,290 1040,250" fill="{a}" opacity="0.25"/><polygon points="0,790 40,790 40,830 0,830" fill="{a}" opacity="0.25"/><path d="M860,40 L910,0 L960,40 L910,80 Z" fill="{p}" opacity="0.2"/><path d="M120,1000 L170,960 L220,1000 L170,1040 Z" fill="{p}" opacity="0.18"/><line x1="940" y1="120" x2="1080" y2="120" stroke="{a}" stroke-width="2" opacity="0.25"/><line x1="0" y1="960" x2="140" y2="960" stroke="{a}" stroke-width="2" opacity="0.25"/></svg>',
        # D3: Flow curves
        f'<svg style="position:absolute;inset:0;width:1080px;height:1080px;pointer-events:none;z-index:1" viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg"><path d="M0,820 Q200,740 400,780 T800,720 T1080,760" stroke="{a}" stroke-width="2" fill="none" opacity="0.22"/><path d="M0,860 Q200,780 400,820 T800,760 T1080,800" stroke="{a}" stroke-width="1.2" fill="none" opacity="0.14"/><path d="M0,300 Q250,220 500,270 T900,220 T1080,250" stroke="{a}" stroke-width="1.5" fill="none" opacity="0.18"/><circle cx="200" cy="754" r="5" fill="{a}" opacity="0.55"/><circle cx="540" cy="718" r="5" fill="{a}" opacity="0.55"/><circle cx="880" cy="736" r="5" fill="{a}" opacity="0.55"/><circle cx="300" cy="248" r="4" fill="{a}" opacity="0.45"/><circle cx="750" cy="228" r="4" fill="{a}" opacity="0.45"/></svg>',
        # D4: Diagonals + circles
        f'<svg style="position:absolute;inset:0;width:1080px;height:1080px;pointer-events:none;z-index:1" viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg"><line x1="0" y1="0" x2="1080" y2="1080" stroke="{a}" stroke-width="1" opacity="0.07"/><line x1="180" y1="0" x2="1080" y2="900" stroke="{a}" stroke-width="0.8" opacity="0.05"/><line x1="0" y1="180" x2="900" y2="1080" stroke="{a}" stroke-width="0.8" opacity="0.05"/><circle cx="540" cy="540" r="420" fill="none" stroke="{a}" stroke-width="0.8" opacity="0.08"/><circle cx="540" cy="540" r="280" fill="none" stroke="{a}" stroke-width="0.6" opacity="0.06"/><rect x="18" y="18" width="84" height="84" fill="none" stroke="{a}" stroke-width="2.2" opacity="0.32"/><rect x="978" y="978" width="84" height="84" fill="none" stroke="{a}" stroke-width="2.2" opacity="0.32"/></svg>',
    ]
    return svgs[v]

def list_variants():
    return {0:'六角網格', 1:'電路板線條+點陣', 2:'幾何角落色塊', 3:'流線數據曲線', 4:'對角線+同心圓'}


if __name__ == '__main__':
    print('✅ Skill D — 裝飾款式清單：')
    for k, v in list_variants().items():
        print(f'  D{k}: {v}')
