# kittenjam-motion-library-mirror

網頁動態效果收藏「Motion Library 動態收藏」的靜態快取。

- 原站：https://kittenjam-motion-library.vercel.app/
- 原作者作品集：https://hannahchao-portfolio.vercel.app/（原站頁尾連結）
- 快取版：https://yazelin.github.io/kittenjam-motion-library-mirror/

## 我們做了什麼

GitHub Actions 每天台灣時間 03:17 用 `wget -p` 抓一次原站（HTML、JS、CSS、og 圖），原樣部署到 GitHub Pages，檔案內容沒有修改。GSAP 與 Google Fonts 照原站從 CDN 載入。原站的 Vercel Web Analytics 在 GitHub Pages 上不會運作。

要手動更新，到 Actions 分頁對 mirror 按 Run workflow。內容版權歸原作者所有。
