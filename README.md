# Hunter Foo Media

静态站，部署在 Cloudflare Pages。推送 `main` 会自动发布。不要在这个仓库里改 DNS。

线上是 [www.hunterfoomedia.com](https://www.hunterfoomedia.com)。裸域若还要 301 到 www，用 Cloudflare Redirect Rule（见下文），不要改 MX。

## 页面

- https://www.hunterfoomedia.com/
- https://www.hunterfoomedia.com/services/
- https://www.hunterfoomedia.com/services/ai-automation/
- https://www.hunterfoomedia.com/services/personal-brand/
- https://www.hunterfoomedia.com/services/social-reels/
- https://www.hunterfoomedia.com/malaysia/
- https://www.hunterfoomedia.com/singapore/

`sitemap.xml` 只列以上地址。未知路径仍返回 `404.html`，不要加「所有路径都改写成首页」的重定向。

## 这个版本改了什么

- 保留原单页视觉与文案；首屏说明加上「马来西亚 AI 自动化、个人品牌与社媒」
- `robots.txt` 允许抓取；页面 `meta robots` 为 `index,follow`
- canonical、`og:url`、JSON-LD `@id` 全部指向 `https://www.hunterfoomedia.com/`
- `sitemap.xml` 含首页、服务总览、三项服务、马来西亚与新加坡页面
- 增加中文 FAQ + `FAQPage` schema（服务、MY+SG 远程、联系方式、不是招聘中介）
- 自定义 `404.html`
- 头图：原 `hero.png` 约 1.9MB → WebP 约 47KB，PNG 降色后备约 0.7MB
- 机构 schema 不再把 SG Jobs 专页写成同一主体；FAQ 写明那是独立 Facebook 页

## 部署到 Cloudflare Pages

域名已在 Cloudflare 购买。构建不需要：输出就是仓库根目录。

1. 本机登录 GitHub：`gh auth login`（当前环境未登录，所以没有推仓库）。
2. 在账号下建空仓库并推送，例如：
   ```bash
   cd /path/to/hunterfoomedia
   gh repo create hunterfoomedia --private --source=. --remote=origin --push
   ```
   公开或私有都可以，Pages 连私有库没问题。
3. Cloudflare 控制台 → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**。
4. 选这个仓库。
5. 设置：
   - Production branch: `main`
   - Framework preset: **None**
   - Build command: 留空
   - Build output directory: `/`
6. 保存并部署。先打开 `https://<project>.pages.dev` 看首页、语言切换、FAQ、404。
7. **Custom domains** 里添加 `www.hunterfoomedia.com`。
8. 再添加裸域 `hunterfoomedia.com`。Pages 会提示改 DNS；域名已在同一 Cloudflare 账号时，一般是：
   - `www` CNAME 到 `<project>.pages.dev`（代理橙云打开）
   - 裸域用 CNAME flattening（Cloudflare 自动）
9. **先确认预览正常，再改掉现在指向 ChatGPT Sites 的记录。** 切之前看 DNS 里 `www` 现有的 CNAME/A，避免和 Pages 两条同时生效。
10. 上线后检查：
    - `https://www.hunterfoomedia.com/robots.txt` 为 `Allow: /`
    - 首页 canonical 为 `https://www.hunterfoomedia.com/`
    - `https://www.hunterfoomedia.com/sitemap.xml`

## 裸域跳到 www（DNS / 规则，不靠代码单独完成）

`_redirects` 里有一条：

```
https://hunterfoomedia.com/* https://www.hunterfoomedia.com/:splat 301
```

两个主机名都绑在同一个 Pages 项目上时，这条不一定覆盖所有裸域请求。请在 Cloudflare 再加一条 **Redirect Rule**（Rules → Redirect Rules）：

- 条件：Hostname equals `hunterfoomedia.com`
- 动作：Dynamic，`concat("https://www.hunterfoomedia.com", http.request.uri.path)`，状态码 301
- 保留 query string

不要只在 DNS 里把裸域 CNAME 到 www 就以为完成了跳转；CNAME 只解析，不改浏览器地址。跳转用上面的 Redirect Rule。

## 本地预览

```bash
python3 -m http.server 8787
```

打开 `http://127.0.0.1:8787/`。
