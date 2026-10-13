"""template/引継ぎシート_原版.xlsx を index.html に埋め込み直すスクリプト。
原版を修正したら  python tools/embed_template.py  を実行してください。"""
import base64, re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
html = root / 'index.html'
b64 = base64.b64encode((root / 'template' / '引継ぎシート_原版.xlsx').read_bytes()).decode()
s = html.read_text(encoding='utf-8')
new = f'<script type="text/plain" id="tplXlsx">{b64}</script>'
if 'id="tplXlsx"' in s:
    s = re.sub(r'<script type="text/plain" id="tplXlsx">.*?</script>', lambda m: new, s, flags=re.S)
else:
    s = s.replace('</body>', new + '\n</body>', 1)
html.write_text(s, encoding='utf-8')
print('embedded', len(b64), 'chars')
