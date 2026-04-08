"""
SKILL C — 色彩引擎
比例：淺色 8 套 / 深色 4 套 = 深色佔 33%
"""

COLORS = {
    # ── 淺色（8 套）──
    'L1': {'name':'純白海軍','dark':False,'bg':'#FFFFFF','primary':'#003366','accent':'#0055CC','text':'#0A0A0A','sub':'#4A5568','card':'#F7F8FA','border':'#E2E8F0','tag':'#EBF2FF'},
    'L2': {'name':'霧白石墨','dark':False,'bg':'#F9FAFB','primary':'#111827','accent':'#374151','text':'#111827','sub':'#6B7280','card':'#FFFFFF','border':'#E5E7EB','tag':'#F3F4F6'},
    'L3': {'name':'冰藍商務','dark':False,'bg':'#F0F4F8','primary':'#1A365D','accent':'#2B6CB0','text':'#1A202C','sub':'#4A5568','card':'#FFFFFF','border':'#CBD5E0','tag':'#EBF8FF'},
    'L4': {'name':'暖白鉛灰','dark':False,'bg':'#FAFAFA','primary':'#2D3748','accent':'#4A5568','text':'#1A202C','sub':'#718096','card':'#FFFFFF','border':'#E2E8F0','tag':'#EDF2F7'},
    'L5': {'name':'珍珠蔚藍','dark':False,'bg':'#F8FAFF','primary':'#1E40AF','accent':'#3B82F6','text':'#1E293B','sub':'#475569','card':'#FFFFFF','border':'#DBEAFE','tag':'#EFF6FF'},
    'L6': {'name':'米白主管','dark':False,'bg':'#FFFDF7','primary':'#1C1C1E','accent':'#6D5C3A','text':'#1C1C1E','sub':'#5A5248','card':'#FFFFFF','border':'#E8E0D0','tag':'#FBF7EE'},
    'L7': {'name':'冷灰精英','dark':False,'bg':'#F4F6F8','primary':'#0F2D52','accent':'#1D6FA4','text':'#0F172A','sub':'#334155','card':'#FFFFFF','border':'#D1DCE8','tag':'#E8F0F8'},
    'L8': {'name':'白底朱紅','dark':False,'bg':'#FFFFFF','primary':'#991B1B','accent':'#DC2626','text':'#0F172A','sub':'#475569','card':'#FEF2F2','border':'#FCA5A5','tag':'#FEF2F2'},

    # ── 深色（4 套）──
    'D1': {'name':'科技深藍','dark':True, 'bg':'#06111F','primary':'#1D4ED8','accent':'#38BDF8','text':'#FFFFFF','sub':'#93C5FD','card':'#0C1E35','border':'rgba(56,189,248,0.2)','tag':'#0F2744'},
    'D2': {'name':'深夜石墨','dark':True, 'bg':'#0F1117','primary':'#374151','accent':'#9CA3AF','text':'#FFFFFF','sub':'#9CA3AF','card':'#1C1D26','border':'rgba(156,163,175,0.2)','tag':'#1F2130'},
    'D3': {'name':'墨綠科技','dark':True, 'bg':'#071A10','primary':'#065F46','accent':'#34D399','text':'#FFFFFF','sub':'#6EE7B7','card':'#0A2218','border':'rgba(52,211,153,0.2)','tag':'#0D2E1C'},
    'D4': {'name':'深寶藍',  'dark':True, 'bg':'#0A0F1E','primary':'#1E3A5F','accent':'#60A5FA','text':'#FFFFFF','sub':'#93C5FD','card':'#0F1A30','border':'rgba(96,165,250,0.2)','tag':'#132040'},
}

DARK = {'D1','D2','D3','D4'}

# 70% light, 30% dark → weighted rotation
COLOR_SEQUENCE = ['L1','L2','L3','L4','L5','L6','L7','L8','L1','D1','L2','L3','D2','L4','L5','L6','D3','L7','L8','L1','D4','L2','L3','L4','L5']

def get_colors(): return COLORS
def get_logo(k): return 'darklogo.png' if k in DARK else 'logo.png'
def get_sequence(): return COLOR_SEQUENCE

if __name__ == '__main__':
    light = sum(1 for k in COLORS if not COLORS[k]['dark'])
    dark  = sum(1 for k in COLORS if COLORS[k]['dark'])
    print(f'淺色 {light} 套 / 深色 {dark} 套 / 深色佔比 {dark/(light+dark)*100:.0f}%')
    for k,v in COLORS.items():
        print(f'  {k} {v["name"]} ({"深" if v["dark"] else "淺"}色)')
