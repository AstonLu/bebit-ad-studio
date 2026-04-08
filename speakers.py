"""
speakers.py — 講者資料模組
"""

_SPEAKERS = {
    'S1': {'name': 'Mars Chen',    'title': '業務總監',     'co': 'beBit TECH', 'file': 'speaker1.jpg'},
    'S2': {'name': 'Miya Hsieh',   'title': '銷售總監',     'co': 'beBit TECH', 'file': 'speaker2.jpg'},
    'S3': {'name': 'Ryan Lai',     'title': '資深業務總監', 'co': 'beBit TECH', 'file': 'speaker3.jpg'},
    'S4': {'name': 'Olivia Hsiang','title': '業務副總監',   'co': 'beBit TECH', 'file': 'speaker4.jpg'},
}

def get_speakers() -> dict:
    return _SPEAKERS

def add_speaker(key: str, name: str, title: str, company: str, file: str):
    _SPEAKERS[key] = {'name': name, 'title': title, 'co': company, 'file': file}
    print(f'✅ 新增講者 {key}: {name} / {title}')

if __name__ == '__main__':
    print('✅ 講者清單：')
    for k, v in get_speakers().items():
        print(f'  {k}: {v["name"]} — {v["title"]} @ {v["co"]}  (圖片: {v["file"]})')
