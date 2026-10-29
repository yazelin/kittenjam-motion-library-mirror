---
name: motion-library
description: 網頁動態效果庫，327 種效果，分成文字、按鈕、表單、卡片、媒體、圖形、背景、版面、游標，每種都有可直接交給 AI 的繁中提示詞和可運作的 CSS/GSAP/Canvas 原始碼。做網頁要加動畫、進場或轉場、hover 效果、捲動效果，或使用者說「加個動態」「動起來」「有沒有酷一點的效果」「motion library」時使用。
---

# 動態效果庫

資料來自 [Motion Library 動態收藏](https://kittenjam-motion-library.vercel.app/)，這裡用的是每日快取站。

## 怎麼找

```bash
python3 motion.py search 關鍵字 [關鍵字...]
```

多個關鍵字要全部符合。比對範圍包含中英文名稱、說明、標籤、風格、技術、元件、時機、情境與提示詞。每行輸出：`id  名稱（英文名）  元件/時機/技術  說明`。

可以用來篩選的代碼：

- 元件：`text` 文字、`button` 按鈕、`control` 表單與控制項、`card` 卡片與群組、`media` 圖片與媒體、`shape` 圖形與 SVG、`bg` 背景與氛圍、`layout` 版面與頁面、`cursor` 游標
- 時機：`enter` 進場、`exit` 退場、`switch` 切換、`loop` 循環待機、`hover` 懸停與點擊、`scroll` 捲動觸發、`drag` 拖曳手勢
- 技術：`CSS`、`GSAP`、`Canvas`
- 情境：`hero`、`emph`、`data`、`bg`、`trans`、`logo`、`ui`、`scroll`、`app`

例如 `search button hover`、`search text enter GSAP`、`search 數字`。

不想跑腳本，也可以直接讀 <https://yazelin.github.io/kittenjam-motion-library-mirror/effects.json>。每筆有 `id`、`zh`、`en`、`desc`、`comp`、`when`、`tech`、`uses`、`tag`、`style`、`prompt`、`copy_prompt`。

## 怎麼用

```bash
python3 motion.py show <id>
```

會印出三段：

1. **提示詞**：和原站「複製提示詞」按鈕的內容相同，只描述動作、節奏與構圖，不指定顏色。要請 AI 實作時，貼進需求即可。
2. **JS 實作**：原站預覽用的程式。`s` 是預覽容器，`x` 是預覽文字。`T()`、`split()`、`el()`、`mqRow()` 等共用函式寫在 [fx.js](https://yazelin.github.io/kittenjam-motion-library-mirror/fx.js) 開頭，搬到專案時要一起帶走，或改寫成專案自己的寫法。
3. **CSS**：這個效果的規則與用到的 `@keyframes`。預覽用 `cqw` 單位與 `--a`（主色）變數，搬過去時換成專案的尺寸與主題色。

實作時：

- 先用提示詞理解效果，再參考原始碼的時間軸與緩動數值，不要整段照抄預覽用的外框。
- 顏色跟著網站既有的主題色走。
- `GSAP` 效果需要載入 GSAP 3.13 和對應的外掛（SplitText、ScrollTrigger、MorphSVG 等，3.13 起都免費），版本照 [index.html](https://yazelin.github.io/kittenjam-motion-library-mirror/) 裡的 script 標籤。
- 加上 `@media (prefers-reduced-motion: reduce)` 關掉或減弱動畫。

要給使用者看效果長什麼樣子，請對方開 <https://yazelin.github.io/kittenjam-motion-library-mirror/> 用名稱搜尋。
