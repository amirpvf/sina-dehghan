"""Build ../index.html from index.tpl.html: embed the Parastoo fonts and wrap the page.
Usage:  python3 src/build.py   (run from the repository root or from src/)"""
import base64, os
here = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(here, 'index.tpl.html'), encoding='utf-8').read()
f = lambda n: base64.b64encode(open(os.path.join(here, 'fonts', n), 'rb').read()).decode()
t = t.replace('{{FONT_R}}', f('Parastoo-FD.woff2')).replace('{{FONT_B}}', f('Parastoo-Bold-FD.woff2'))
i = t.index('</style>') + len('</style>')
html = ('<!doctype html>\n<html lang="fa" dir="rtl">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '<meta name="description" content="دکتر سینا دهقان، داروساز | رزومه، پروژه‌ها و مدارک">\n'
        + t[:i] + '\n</head>\n<body>\n' + t[i:] + '\n</body>\n</html>\n')
open(os.path.join(here, '..', 'index.html'), 'w', encoding='utf-8').write(html)
print('index.html built')
