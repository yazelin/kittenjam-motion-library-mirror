# kittenjam-motion-library-mirror

網頁動態效果收藏「Motion Library 動態收藏」的每日快取，附上讓 AI 直接查詢、取用的 skill。

- 原站：<https://kittenjam-motion-library.vercel.app/>
- 原作者作品集：[hannahchao-portfolio.vercel.app](https://hannahchao-portfolio.vercel.app/)（原站頁尾連結）
- 快取版網站：<https://yazelin.github.io/kittenjam-motion-library-mirror/>

## 這個版本多了什麼

原站是給人瀏覽、按按鈕複製提示詞的網頁。這個版本保留同一個網頁，另外提供 AI 能直接使用的入口：

| 入口 | 內容 |
|---|---|
| [`skills/motion-library/`](skills/motion-library/) | AI agent 的 skill。`SKILL.md` 寫明何時使用、怎麼搜尋、怎麼把效果搬進專案；`motion.py` 負責搜尋，並取出單一效果的提示詞、JS 與 CSS，只用 Python 標準函式庫 |
| [`effects.json`](https://yazelin.github.io/kittenjam-motion-library-mirror/effects.json) | 全部 327 種效果的資料：名稱、說明、元件、時機、技術、情境、提示詞，以及原站「複製提示詞」的完整內容 |
| [`llms.txt`](https://yazelin.github.io/kittenjam-motion-library-mirror/llms.txt) | 給 AI 讀的網站簡介，指向上面兩項與原始碼 |

### 給 AI 用

把 skill 裝進 agent 的 skill 目錄（Claude Code 為例）：

```bash
git clone https://github.com/yazelin/kittenjam-motion-library-mirror.git
ln -s "$PWD/kittenjam-motion-library-mirror/skills/motion-library" ~/.claude/skills/motion-library
```

其他 agent 直接讀 `skills/motion-library/SKILL.md` 照著做即可。不想安裝的話，對 AI 說「讀 https://yazelin.github.io/kittenjam-motion-library-mirror/llms.txt，幫我的按鈕挑一個 hover 效果」也可以。

```bash
python3 skills/motion-library/motion.py search button hover
python3 skills/motion-library/motion.py show 1
```

## 和原站相比改了什麼

GitHub Actions 每天台灣時間 03:17 用 `wget -p` 抓一次原站（HTML、JS、CSS、og 圖），部署到 GitHub Pages：

1. 原站的檔案原樣保留，沒有修改。GSAP 與 Google Fonts 照原站從 CDN 載入。原站的 Vercel Web Analytics 在 GitHub Pages 上不會運作。
2. 多產出 `effects.json` 和 `llms.txt`（見上一節）。`effects.json` 是從原站 `data.js` 轉出來的，內容相同，只多一個 `copy_prompt` 欄位。

要手動更新，到 Actions 分頁對 mirror 按 Run workflow。內容版權歸原作者所有。
