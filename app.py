"""
app.py — beBit TECH Ad Studio v5
整合 Gemini 即時文案生成
"""
import os, io, zipfile, json
from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index(): return render_template('index.html')

@app.route('/api/speakers')
def api_speakers():
    from speakers import get_speakers
    return jsonify(get_speakers())

@app.route('/api/generate_copy', methods=['POST'])
def api_generate_copy():
    """先呼叫 Gemini 生成文案，讓前端可以顯示進度"""
    try:
        data = request.get_json()
        api_key = data.get('gemini_api_key', '').strip()
        event = {k: data.get(k, d) for k, d in {
            'event_name':'','date':'','time':'','venue':'',
            'topic':'','org':'beBit TECH',
            'description':'','audience':'企業主管、行銷總監',
        }.items()}

        if api_key:
            from skill_a_gemini import generate_copies, get_copies_fallback
            try:
                copies = generate_copies(event, api_key)
                return jsonify({'success': True, 'copies': copies, 'source': 'gemini'})
            except Exception as e:
                # Gemini 失敗，用備用
                copies = get_copies_fallback()
                return jsonify({'success': True, 'copies': copies, 'source': 'fallback', 'warning': str(e)})
        else:
            from skill_a_gemini import get_copies_fallback
            copies = get_copies_fallback()
            return jsonify({'success': True, 'copies': copies, 'source': 'fallback'})

    except Exception as e:
        import traceback
        return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 500


@app.route('/api/generate', methods=['POST'])
def api_generate():
    try:
        data = request.get_json()

        event = {k: data.get(k, d) for k, d in {
            'date':'2025.04.20（四）','time':'14:00–15:20',
            'venue':'台北 W 飯店 皇家宴會廳','topic':'AI × CDP × 電商',
            'org':'beBit TECH',
        }.items()}

        chosen   = [k for k in data.get('speakers', ['S1']) if k]
        n_total  = max(1, min(int(data.get('n_total', 10)), 50))
        is_multi = len(chosen) > 1

        # 使用前端傳來的文案（已由 Gemini 生成）
        copies_data = data.get('copies', None)

        from skill_b_layout import render_single, render_multi, SOLO_LAYOUTS, MULTI_LAYOUTS, SOLO_SEQ, MULTI_SEQ
        from skill_c_color  import get_colors, get_sequence
        from speakers       import get_speakers
        import skill_b_layout as sb
        sb.EVENT = event

        # 建立 copies dict
        if copies_data:
            copies = copies_data
        else:
            from skill_a_gemini import get_copies_fallback
            copies = get_copies_fallback()

        colors   = get_colors()
        color_seq = get_sequence()
        spk_list = get_speakers()
        valid    = [k for k in chosen if k in spk_list]
        if not valid:
            return jsonify({'error': '請至少選擇一位講者'}), 400

        copy_keys = list(copies.keys())
        plan = []

        if is_multi:
            for i in range(n_total):
                plan.append({
                    'mode':       'multi',
                    'copy_key':   copy_keys[i % len(copy_keys)],
                    'layout_key': MULTI_SEQ[i % len(MULTI_SEQ)],
                    'color_key':  color_seq[i % len(color_seq)],
                    'speakers':   valid,
                    'deco':       i % 5,
                })
        else:
            sp = valid[0]
            for i in range(n_total):
                plan.append({
                    'mode':       'solo',
                    'copy_key':   copy_keys[i % len(copy_keys)],
                    'layout_key': SOLO_SEQ[i % len(SOLO_SEQ)],
                    'color_key':  color_seq[i % len(color_seq)],
                    'speaker':    sp,
                    'deco':       i % 5,
                })

        zip_buf = io.BytesIO()
        with zipfile.ZipFile(zip_buf, 'w', zipfile.ZIP_DEFLATED) as zf:
            for i, p in enumerate(plan, 1):
                cp = copies[p['copy_key']]
                co = colors[p['color_key']]
                if p['mode'] == 'multi':
                    html  = render_multi(p['layout_key'], cp, p['color_key'], p['speakers'], p['deco'])
                    label = '+'.join(p['speakers'])
                else:
                    html  = render_single(p['layout_key'], cp, p['color_key'], p['speaker'], p['deco'])
                    label = p['speaker']
                fname = f"{i:02d}_{label}_{p['copy_key']}_{p['layout_key']}_{p['color_key']}_{co['name']}.html"
                zf.writestr(fname, html)

            zf.writestr('README.txt', f"""beBit TECH Ad Studio 生成結果
活動：{data.get('event_name','')}
日期：{event['date']} {event['time']}  地點：{event['venue']}
講者：{', '.join(spk_list[k]['name'] for k in valid)}
共計：{len(plan)} 個廣告

使用：把 logo.png / darklogo.png / speaker*.jpg 放入同一資料夾
轉 JPG：npm install puppeteer && node convert.mjs""")

        zip_buf.seek(0)
        slug = data.get('event_name','ads').replace(' ','_')[:14]
        return send_file(zip_buf, mimetype='application/zip',
                         as_attachment=True,
                         download_name=f'bebit_ads_{slug}.zip')

    except Exception as e:
        import traceback
        return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 500


if __name__ == '__main__':
    print('\n🚀 beBit TECH Ad Studio v5\n   http://localhost:5000\n')
    app.run(host="0.0.0.0", port=5000, debug=False)
