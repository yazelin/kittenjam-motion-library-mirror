"""查 Motion Library 的動態效果：
  python3 motion.py search 關鍵字 [關鍵字...]   列出符合的效果（id、名稱、元件、時機、說明）
  python3 motion.py show <id>                  印出提示詞、JS 實作（fx.js）與 CSS（fx.css）
資料來源是每日快取站，不需要安裝套件。"""
import json, re, sys, urllib.request

BASE = 'https://yazelin.github.io/kittenjam-motion-library-mirror/'
PALETTE = '\n配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。'


def get(name):
    return urllib.request.urlopen(BASE + name, timeout=30).read().decode('utf-8')


def items():
    s = get('data.js')
    i = s.index('const ITEMS=') + len('const ITEMS=')
    return json.loads(s[i:s.index('];', i) + 1])


def search(words):
    for it in items():
        hay = ' '.join([it['zh'], it['en'], it['desc'], it['tag'], it['style'], it['tech'], it['comp'],
                        *it['when'], *it['uses'], it['prompt']]).lower()
        if all(w.lower() in hay for w in words):
            print(f"{it['id']:>4}  {it['zh']}（{it['en']}）  {it['comp']}/{','.join(it['when'])}/{it['tech']}  {it['desc']}")


def show(id_):
    it = next(x for x in items() if x['id'] == id_)
    print(f"# {it['zh']}（{it['en']}）  id={id_}  元件={it['comp']}  時機={','.join(it['when'])}  技術={it['tech']}\n")
    print('## 提示詞（原站「複製提示詞」的內容）\n')
    print(f"「{it['zh']}（{it['en']}）」動態效果：{it['prompt']}{PALETTE}\n")
    js = re.search(rf'^{id_}\(.*?(?=^\d+\(|^\}};)', get('fx.js'), re.M | re.S)
    print('## JS 實作（fx.js 的 FX[id]，s 是預覽容器、x 是預覽文字；T、split、el 等共用函式在 fx.js 開頭）\n')
    print(js[0].rstrip() if js else '（這個效果沒有 JS，只靠 CSS）')
    css = get('fx.css')
    # 前面的效果用 .fx<id> 開頭；後面的效果用 JS 裡自己取的 class（例如 .sv-bdg）。一到兩個字的共用 class 不算
    classes = {c for q in re.findall(r"el\('\w+','([^']+)'|class=\\?\"([^\"\\]+)", js[0] if js else '') for part in q for c in part.split() if len(c) > 2}
    heads = [rf'\.fx{id_}(?![0-9])'] + [rf'\.{re.escape(c)}(?![\w-])' for c in classes]
    rules = re.findall(rf'(?<![\w-])(?:{"|".join(heads)})[^{{}}@]*\{{[^}}]*\}}', css)
    names = {n for r in rules for n in re.findall(r'animation(?:-name)?:\s*([A-Za-z_][\w-]*)', r)}
    frames = [m[0] for n in names for m in re.finditer(rf'@keyframes {re.escape(n)}\{{(?:[^{{}}]*\{{[^}}]*\}})*[^{{}}]*\}}', css)]
    print('\n## CSS（fx.css 裡這個效果的規則與用到的 @keyframes；共用樣式在 fx.css 開頭 shared 區）\n')
    print('\n'.join(rules + frames) or '（沒有專屬 CSS：動畫寫在上面的 JS 裡，或用 fx.css 開頭的共用樣式）')


if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == 'search':
        search(sys.argv[2:])
    elif len(sys.argv) == 3 and sys.argv[1] == 'show':
        show(int(sys.argv[2]))
    else:
        print(__doc__)
