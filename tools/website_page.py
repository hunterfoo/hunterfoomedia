# Standalone "Website design" page (/website-design/, EN / ZH / MS). Copy written natively per language.
# Rules: fixed package prices only (taken from products_pages.WB), no "from/起/Dari"; no timelines; no ranking or
# AI-recommendation promises; no client website portfolio or testimonials (none exist); custom scope by written quote.
import urllib.parse, html
from products_pages import WB, CHECK, ICON, fee_btn

WA = "https://wa.me/60196273143"
D = "https://www.hunterfoomedia.com"
ZH = '<span lang="zh-Hans">中文</span>'

P = {}
P["en"] = dict(
 title="Website Design Malaysia – RM399 | SEO + AEO/GEO | Hunter Foo Media",
 desc="Website design in Malaysia for SMEs: a company website for RM399, or RM1,393 with SEO + AEO/GEO so Google and AI assistants can read it. Domain for the first year included. Kuala Lumpur team. WhatsApp +60196273143.",
 eyebrow="WEBSITE DESIGN · MALAYSIA",
 h1='Website design in Malaysia: <span class="orange">a company website customers and AI can find.</span>',
 lede=["We're a Kuala Lumpur team building company websites for SMEs in Malaysia and Singapore. Two packages, fixed prices: Basic RM399, or RM1,393 with SEO + AEO/GEO.",
       "Ask on WhatsApp and you'll get a straight answer."],
 cta1="See packages &amp; prices", cta2="WhatsApp +60 19-627 3143",
 whye="WHY A WEBSITE", whyh="Why SME owners build a website",
 why=[("Customers check you first", "Before they call, customers, banks and suppliers search your company name. A proper website shows you're a real, established business."),
      ("Be found on Google and AI assistants", "People search on Google and ask AI assistants like ChatGPT. A clear website gives both something reliable to read about you."),
      ("Enquiries straight to WhatsApp", "Every page has a WhatsApp button, so a visitor becomes a conversation in one tap."),
      ("Not only Facebook", "A Facebook Page can be restricted, and ads can get more expensive. Your website and domain stay yours, whatever happens on social media."),
      ("A professional image", "A clean site on your own domain makes your brand look as serious as your work.")],
 aie="YOUR FIRST STEP INTO AI", aih="A website AI can read is your first step into AI.",
 aip=["Before any chatbot or automation, AI tools need clear facts about your business. We write your site so they can read it:"],
 ai=["<b>llms.txt</b>: a plain-text summary of your business, written for AI tools",
     "<b>Structured data</b> (schema): your company details in a format machines understand",
     "<b>Clear Q&amp;A content</b>: the questions customers ask, answered in your words"],
 aiex='This site is an example. See our <a class="hm-link" href="/llms.txt">llms.txt</a>.',
 aifine="We don't promise rankings, or that any AI tool will recommend your business. We make your site clear and easy to read.",
 pke="PACKAGES &amp; PRICES", pkh="Two website packages, fixed prices",
 pre="HOW IT WORKS", prh="How we build your website",
 pr=[("WhatsApp us", "Tell us about your business and pick Basic or SEO + AEO/GEO."),
     ("Share your materials", "Send your logo, photos and company details. We arrange them into clear pages."),
     ("Review and approve", "We build the site and you review it. Nothing goes live until you approve."),
     ("Go live", "We connect your domain with HTTPS. With SEO + AEO/GEO, we also submit your site to Google and Bing for indexing."),
     ("After launch", "Need a change? WhatsApp us. If you update often, choose maintenance at RM199/month.")],
 fqe="FAQ", fqh="Website questions",
 faq=[("How much does a website cost in Malaysia?",
       "With us, Basic is RM399 and SEO + AEO/GEO is RM1,393 in total (Basic RM399 + RM994). Both include one language and your domain for the first year. More languages, extra pages or other custom work are confirmed by <b>written quote</b>. Prices in the market vary a lot with scope, so compare what each quote includes."),
      ("Does the website come with an admin login, so I can edit it myself?",
       "Websites on the Basic and SEO + AEO/GEO packages don't come with an admin panel. That keeps the site faster and more secure, and easier for AI tools to read. To change something, just WhatsApp us. If you update often, you can choose maintenance at RM199/month. If you'd still rather log in and edit the text and images yourself, we can add an admin panel separately, by <b>written quote</b>."),
      ("What happens with the domain after the first year?",
       "The first year of your domain is included. From the second year, domain renewal is billed separately. Your domain and website are registered in your name."),
      ("Can I add more languages?",
       "Each package includes one language: English, " + ZH + " or BM. More languages can be added, by <b>written quote</b>."),
      ("Do you guarantee the first page of Google?",
       "No. Nobody controls how Google or AI tools rank websites. We build and set up exactly what's listed; ranking also depends on things like other sites linking to you, your Google Business Profile and customer reviews."),
      ("What's the difference between Basic and SEO + AEO/GEO?",
       "Basic gives you a clean company website. SEO + AEO/GEO adds what search engines and AI tools read: page titles and descriptions, a sitemap, submission to Google and Bing, FAQ content, structured data and an indexing check report. It's a one-time setup. Optional maintenance: RM199/month.")],
 pfe="PROOF YOU CAN CHECK", pfh="Our own work, in the open",
 pf=["We don't show a client website portfolio yet. What you can check is hunterfoomedia.com itself: built by us in English, " + ZH + " and BM, with llms.txt, structured data and a sitemap.",
     "We also build and run AI automation every day for our client Sky Employment Pte Ltd, a licensed Singapore employment agency."],
 pfl=[("/", "This website →"), ("/llms.txt", "Our llms.txt →"), ("/products/#case-study", "Case study →")],
 ce="NEXT STEP", ch="Ready to build your website?", cnote="Malaysian number +60196273143. English, " + ZH + " or BM. Package prices as above; anything beyond the packages by written quote.",
 crumb="Home",
)
P["zh"] = dict(
 title="马来西亚网站设计｜做网站 RM399，含 SEO 方案｜Hunter Foo Media",
 desc="马来西亚中小企业网站设计：公司网站 RM399；加 SEO + AEO/GEO 合共 RM1,393，让 Google 和 AI 助手都读得懂。含第一年域名，吉隆坡团队。想做网站、架设网站，直接 WhatsApp +60196273143。",
 eyebrow="网站设计 · 马来西亚",
 h1='马来西亚网站设计：<span class="orange">做一个客户和 AI 都找得到的公司网站。</span>',
 lede=["我们是吉隆坡的团队，为马来西亚和新加坡的中小企业做网站。两个网站制作方案，价格固定：基础版 RM399；含 SEO + AEO/GEO 合共 RM1,393。",
       "想架设网站，WhatsApp 问一句，我们直接回答。"],
 cta1="看方案与价格", cta2="WhatsApp +60 19-627 3143",
 whye="为什么要做网站", whyh="老板为什么要做网站？",
 why=[("客户会先查你", "客户、银行、供应商在联系你之前，多半会先搜你的公司名字。有一个像样的公司网站，证明你是真实、正规的生意。"),
      ("Google 和 AI 助手找得到你", "现在的人会在 Google 搜，也会问 ChatGPT 这类 AI 助手。清楚的网站，让两边都有可靠的资料读到你。"),
      ("询问直接进 WhatsApp", "每一页都有 WhatsApp 按钮，访客一按就变成对话。"),
      ("不只靠 Facebook", "Facebook 专页可能被限制，广告也可能越来越贵。网站和域名是你自己的，不受社媒变化影响。"),
      ("专业形象", "干净的网站加上自己的域名，让品牌看起来和你的工作一样专业。")],
 aie="接上 AI 的第一步", aih="AI 读得懂的网站，是公司接上 AI 的第一步。",
 aip=["在用聊天机器人或自动化之前，AI 工具先要读到你公司清楚的资料。我们把网站写成 AI 读得懂的样子："],
 ai=["<b>llms.txt</b>：一份写给 AI 工具看的公司简介",
     "<b>结构化数据</b>（schema）：用机器看得懂的格式标好公司资料",
     "<b>清楚的问答内容</b>：客户常问的问题，用你的话回答"],
 aiex='这个网站就是例子，可以看看我们的 <a class="hm-link" href="/llms.txt">llms.txt</a>。',
 aifine="我们不承诺排名，也不承诺任何 AI 工具会推荐你；我们做的是让网站清楚、好读。",
 pke="方案与价格", pkh="两个网站制作方案，价格固定",
 pre="流程", prh="做网站的流程",
 pr=[("WhatsApp 我们", "说说你的生意，选基础版或 SEO + AEO/GEO。"),
     ("提供资料", "发来公司 logo、照片和公司资料，我们整理成清楚的页面。"),
     ("你审核、批准", "网站做好先给你看，你批准了才上线。"),
     ("上线", "接好域名和 HTTPS。选了 SEO + AEO/GEO 的，我们也提交 Google 与 Bing 收录。"),
     ("上线之后", "要改内容，WhatsApp 我们；需要经常更新的，可以选每月 RM199 的维护。")],
 fqe="常见问题", fqh="做网站常见问题",
 faq=[("做网站要多少钱？",
       "在我们这里，基础版 RM399；含 SEO + AEO/GEO 合共 RM1,393（基础版 RM399 + RM994）。两个方案都含 1 种语言和第一年域名。加语言、加页面或其他特别需求，以<b>书面报价</b>确认。市面上做网站的价格差别很大，主要看范围，比较时看清楚每份报价包含什么。"),
      ("网站有后台，可以自己登入修改吗？",
       "基础版和 SEO + AEO/GEO 方案的网站不带后台，这样网站更快、更安全，AI 也更容易读懂。要改内容，直接 WhatsApp 我们；需要经常更新的，可以选每月 RM199 的维护。如果你一定要自己登入修改文字和图片，我们可以另外加后台，费用以<b>书面报价</b>确认。"),
      ("第一年之后，域名怎么算？",
       "方案含第一年域名。第二年起只需续域名费（另计）。域名和网站都在你名下。"),
      ("可以加语言吗？",
       "每个方案含 1 种语言（EN、中文或 BM 任选）。要加语言可以，费用以<b>书面报价</b>确认。"),
      ("保证排在 Google 第一页吗？",
       "不保证。没有人能控制 Google 或 AI 工具怎么排序。我们把列出的内容做好、设置好；排名还跟其他网站链接到你、Google 商家资料、客户评价等因素有关。"),
      ("基础版和 SEO + AEO/GEO 有什么不同？",
       "基础版给你一个清楚好用的公司网站。SEO + AEO/GEO 再补上搜索引擎和 AI 工具会读的内容：每页标题与描述、网站地图、提交 Google 与 Bing 收录、FAQ 内容、结构化数据和收录检查报告。这是一次性设置；如需维护：每月 RM199。")],
 pfe="可以查证的例子", pfh="我们自己的作品，公开可查",
 pf=["我们目前没有公开的客户网站作品集。你可以直接查看 hunterfoomedia.com：这是我们自己做的网站，有 EN / 中文 / BM 三语、llms.txt、结构化数据和网站地图。",
     "我们也每天为我们的客户 Sky Employment Pte Ltd（新加坡持牌职业中介）搭建并运行 AI 自动化系统。"],
 pfl=[("/", "看这个网站 →"), ("/llms.txt", "我们的 llms.txt →"), ("/products/#case-study", "看客户案例 →")],
 ce="下一步", ch="准备好做网站了吗？", cnote="马来西亚号码 +60196273143。中文、英文或马来文都可以。方案价格如上；方案以外的需求以书面报价确认。",
 crumb="首页",
)
P["ms"] = dict(
 title="Buat Website Malaysia RM399 | Pakej & Harga | Hunter Foo Media",
 desc="Buat website syarikat di Malaysia: pakej Asas RM399, atau RM1,393 dengan SEO + AEO/GEO supaya Google dan pembantu AI boleh membacanya. Domain tahun pertama termasuk. Pasukan di Kuala Lumpur. WhatsApp +60196273143.",
 eyebrow="BUAT WEBSITE · MALAYSIA",
 h1='Buat website syarikat di Malaysia: <span class="orange">mudah dicari pelanggan dan AI.</span>',
 lede=["Kami pasukan di Kuala Lumpur yang membina laman web syarikat untuk PKS di Malaysia dan Singapura. Dua pakej website, harga tetap: Asas RM399, atau RM1,393 dengan SEO + AEO/GEO.",
       "Tanya di WhatsApp, kami jawab dengan jelas."],
 cta1="Lihat pakej &amp; harga", cta2="WhatsApp +60 19-627 3143",
 whye="KENAPA PERLU WEBSITE", whyh="Kenapa pemilik PKS buat website?",
 why=[("Pelanggan semak anda dahulu", "Sebelum menghubungi anda, pelanggan, bank dan pembekal biasanya mencari nama syarikat anda. Laman web syarikat yang kemas menunjukkan perniagaan anda sah dan serius."),
      ("Ditemui di Google dan pembantu AI", "Orang mencari di Google dan bertanya kepada pembantu AI seperti ChatGPT. Laman web yang jelas memberi kedua-duanya maklumat yang boleh dipercayai tentang anda."),
      ("Pertanyaan terus ke WhatsApp", "Setiap halaman ada butang WhatsApp, jadi pelawat boleh terus berbual dengan anda."),
      ("Bukan bergantung pada Facebook sahaja", "Facebook Page boleh disekat, dan kos iklan boleh meningkat. Laman web dan domain anda kekal milik anda, apa pun yang berlaku di media sosial."),
      ("Imej profesional", "Laman web yang kemas dengan domain sendiri menjadikan jenama anda nampak seserius kerja anda.")],
 aie="LANGKAH PERTAMA KE AI", aih="Laman web yang AI boleh baca ialah langkah pertama syarikat ke arah AI.",
 aip=["Sebelum chatbot atau automasi, alat AI perlu membaca maklumat yang jelas tentang perniagaan anda. Kami susun laman anda supaya mudah dibaca:"],
 ai=["<b>llms.txt</b>: ringkasan perniagaan anda dalam teks biasa, ditulis untuk alat AI",
     "<b>Data berstruktur</b> (schema): maklumat syarikat dalam format yang difahami mesin",
     "<b>Kandungan soal jawab yang jelas</b>: soalan yang pelanggan tanya, dijawab dengan kata-kata anda"],
 aiex='Laman ini sendiri contohnya. Lihat <a class="hm-link" href="/llms.txt">llms.txt</a> kami.',
 aifine="Kami tidak menjanjikan kedudukan carian, atau bahawa mana-mana alat AI akan mengesyorkan perniagaan anda. Kami jadikan laman anda jelas dan mudah dibaca.",
 pke="PAKEJ &amp; HARGA", pkh="Dua pakej website, harga tetap",
 pre="CARA KERJA", prh="Cara kami buat website anda",
 pr=[("WhatsApp kami", "Ceritakan tentang perniagaan anda dan pilih Asas atau SEO + AEO/GEO."),
     ("Hantar bahan", "Hantar logo, gambar dan maklumat syarikat. Kami susun menjadi halaman yang jelas."),
     ("Semak dan luluskan", "Kami bina laman web dan anda semak dahulu. Laman hanya dilancarkan selepas anda luluskan."),
     ("Dilancarkan", "Kami sambungkan domain dengan HTTPS. Dengan SEO + AEO/GEO, kami juga hantar laman anda kepada Google dan Bing untuk pengindeksan."),
     ("Selepas dilancarkan", "Nak ubah sesuatu? WhatsApp kami. Jika kerap kemas kini, pilih penyelenggaraan RM199/bulan.")],
 fqe="SOALAN LAZIM", fqh="Soalan tentang buat website",
 faq=[("Harga buat website di Malaysia?",
       "Dengan kami, pakej Asas RM399 dan SEO + AEO/GEO RM1,393 semuanya (Asas RM399 + RM994). Kedua-dua pakej termasuk satu bahasa dan domain untuk tahun pertama. Bahasa tambahan, halaman tambahan atau skop khas disahkan melalui <b>sebut harga bertulis</b>. Upah buat website di pasaran berbeza-beza mengikut skop, jadi bandingkan apa yang termasuk dalam setiap sebut harga."),
      ("Adakah laman web ada panel admin, supaya saya boleh log masuk dan ubah sendiri?",
       "Laman web pakej Asas dan SEO + AEO/GEO tidak disertakan panel admin. Ini menjadikan laman lebih pantas, lebih selamat dan lebih mudah dibaca oleh AI. Nak ubah kandungan, WhatsApp saja kami. Jika anda kerap mengemas kini, boleh pilih penyelenggaraan RM199/bulan. Jika anda tetap mahu log masuk dan ubah teks serta gambar sendiri, kami boleh tambah panel admin secara berasingan, dengan <b>sebut harga bertulis</b>."),
      ("Bagaimana dengan domain selepas tahun pertama?",
       "Domain untuk tahun pertama termasuk. Mulai tahun kedua, pembaharuan domain dikenakan berasingan. Domain dan laman web didaftarkan atas nama anda."),
      ("Boleh tambah bahasa?",
       "Setiap pakej termasuk satu bahasa: EN, " + ZH + " atau BM. Bahasa tambahan boleh ditambah, melalui <b>sebut harga bertulis</b>."),
      ("Adakah anda jamin halaman pertama Google?",
       "Tidak. Tiada siapa boleh mengawal cara Google atau alat AI menyusun laman web. Kami bina dan sediakan apa yang disenaraikan; kedudukan juga bergantung pada perkara seperti laman lain yang memaut kepada anda, Google Business Profile dan ulasan pelanggan."),
      ("Apa beza pakej Asas dan SEO + AEO/GEO?",
       "Pakej Asas memberi anda laman web syarikat yang kemas. SEO + AEO/GEO menambah apa yang dibaca oleh enjin carian dan alat AI: tajuk dan meta description, sitemap, penghantaran kepada Google dan Bing, kandungan FAQ, data berstruktur dan laporan semakan pengindeksan. Ia persediaan sekali sahaja. Penyelenggaraan pilihan: RM199/bulan.")],
 pfe="BUKTI YANG BOLEH DISEMAK", pfh="Kerja kami sendiri, terbuka untuk disemak",
 pf=["Kami belum memaparkan portfolio laman web pelanggan. Yang boleh anda semak ialah hunterfoomedia.com sendiri: kami bina dalam EN, " + ZH + " dan BM, dengan llms.txt, data berstruktur dan sitemap.",
     "Kami juga membina dan menjalankan automasi AI setiap hari untuk pelanggan kami Sky Employment Pte Ltd, agensi pekerjaan berlesen di Singapura."],
 pfl=[("/", "Laman web ini →"), ("/llms.txt", "llms.txt kami →"), ("/products/#case-study", "Kajian kes →")],
 ce="LANGKAH SETERUSNYA", ch="Sedia untuk buat website?", cnote="Nombor Malaysia +60196273143. Bahasa Inggeris, Cina atau BM. Harga pakej seperti di atas; keperluan di luar pakej melalui sebut harga bertulis.",
 crumb="Utama",
)

def _main(k):
    h = P[k]; w = WB[k]
    wa = WA + "?text=" + urllib.parse.quote(w["wamsg"], safe="")
    chk = lambda xs: '<ul class="ad-checks">' + "".join("<li>%s<span>%s</span></li>" % (CHECK, x) for x in xs) + "</ul>"
    panel = lambda tag, t, sub, xs, cls, n: ('<div class="ad-panel wb-tier%s"><p class="wb-tag">%s</p><h3>%s</h3><p class="wb-sub">%s</p>%s%s</div>'
                                             % (cls, tag, t, sub, chk(xs), fee_btn(w, n)))
    cards = lambda xs, cls: '<ol class="hm-cards %s">%s</ol>' % (cls, "".join('<li><span class="hm-n">%d</span><h3>%s</h3><p>%s</p></li>' % (i + 1, a, b) for i, (a, b) in enumerate(xs)))
    o = []
    o.append('<section class="wrap hm-hero wd-hero"><p class="eyebrow"><i></i>%s</p><h1>%s</h1>%s'
             '<div class="hm-ctas"><a class="button" href="#packages">%s <span aria-hidden="true">↓</span></a>'
             '<a class="button ghost" href="%s" target="_blank" rel="noopener noreferrer">%s <span aria-hidden="true">↗</span></a></div></section>\n'
             % (h["eyebrow"], h["h1"], "".join('<p class="lede">%s</p>' % x for x in h["lede"]), h["cta1"], wa, h["cta2"]))
    o.append('<section class="paper hm-sec" id="why"><div class="wrap section"><p class="pd-kicker">%s</p><h2 class="hm-h2">%s</h2>%s</div></section>\n'
             % (h["whye"], h["whyh"], cards(h["why"], "hm-cards-light hm-cards-5")))
    o.append('<section class="wrap section hm-sec hm-dark" id="ai-ready"><p class="eyebrow"><i></i>%s</p><h2 class="hm-h2">%s</h2>%s'
             '<div class="hm-proof hm-mg-proof wd-ai"><ul>%s</ul><p class="hm-src">%s</p></div><p class="hm-fine">%s</p></section>\n'
             % (h["aie"], h["aih"], "".join('<p class="hm-lede-d">%s</p>' % x for x in h["aip"]),
                "".join('<li>%s<span>%s</span></li>' % (CHECK, x) for x in h["ai"]), h["aiex"], h["aifine"]))
    o.append('<section class="paper ad-section wb-section hm-sec" id="packages"><div class="wrap section"><p class="pd-kicker">%s</p><h2 class="hm-h2">%s</h2>'
             '<h3 class="ad-h3">%s</h3><ul class="wb-gets">%s</ul>'
             '<div class="ad-two wb-two">%s%s</div><p class="wb-scope">%s</p><p class="ad-fine">%s</p></div></section>\n'
             % (h["pke"], h["pkh"], w["geth"],
                "".join('<li class="ad-know"><span class="ad-ico">%s</span><p>%s</p></li>' % (ICON[i], x) for i, x in zip(["glb", "srv", "key"], w["gets"])),
                panel(w["t1tag"], w["t1h"], w["t1sub"], w["t1"], "", 1), panel(w["t2tag"], w["t2h"], w["t2sub"], w["t2"], " wb-plus", 2),
                w["scope"], w["fine"]))
    o.append('<section class="wrap section hm-sec hm-dark" id="process"><p class="eyebrow"><i></i>%s</p><h2 class="hm-h2">%s</h2>%s</section>\n'
             % (h["pre"], h["prh"], cards(h["pr"], "hm-cards-5")))
    o.append('<section class="paper pd-faq-wrap" id="faq" aria-labelledby="wd-faq-h"><div class="wrap section"><div class="pd-faq">'
             '<p class="pd-kicker">%s</p><h2 id="wd-faq-h">%s</h2>%s</div></div></section>\n'
             % (h["fqe"], h["fqh"], "".join('<details%s><summary>%s</summary><p>%s</p></details>' % (' open' if i == 0 else '', q, a) for i, (q, a) in enumerate(h["faq"]))))
    o.append('<section class="wrap section hm-sec hm-dark" id="proof"><p class="eyebrow"><i></i>%s</p><h2 class="hm-h2">%s</h2>%s<p class="hm-links">%s</p></section>\n'
             % (h["pfe"], h["pfh"], "".join('<p class="hm-lede-d">%s</p>' % x for x in h["pf"]),
                "".join('<a class="hm-link" href="%s">%s</a>' % x for x in h["pfl"])))
    o.append('<section class="wrap section contact" id="contact"><p class="eyebrow"><i></i>%s</p><div class="contact-row"><h2>%s</h2><div class="contact-actions">'
             '<a class="button whatsapp" data-wa="%s" href="%s" target="_blank" rel="noopener noreferrer">WhatsApp +60196273143 <span aria-hidden="true">↗</span></a>'
             '<a class="email-link" href="mailto:hello@hunterfoomedia.com">hello@hunterfoomedia.com <span aria-hidden="true">↗</span></a><p>%s</p></div></div></section>\n'
             % (h["ce"], h["ch"], html.escape(w["wamsg"]), wa, h["cnote"]))
    return "\n" + "".join(o)

def _plain(s):
    import re
    return re.sub(r"<[^>]+>", "", s)

def _ld(k):
    h = P[k]; w = WB[k]; u = D + "/website-design/"
    area = [{"@type": "Country", "name": "Malaysia"}, {"@type": "Country", "name": "Singapore"}]
    offer = lambda name, price, desc, extra=None: dict({"@type": "Offer", "name": name, "price": price, "priceCurrency": "MYR", "description": desc,
                                                       "url": u + "#packages", "availability": "https://schema.org/InStock", "seller": {"@id": D + "/#organization"}}, **(extra or {}))
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": u + "#webpage", "url": u, "name": h["title"], "description": h["desc"],
         "about": {"@id": u + "#service"}, "isPartOf": {"@id": D + "/#website"}, "breadcrumb": {"@id": u + "#breadcrumb"}},
        {"@type": "Service", "@id": u + "#service", "name": w["ld"][0], "serviceType": "Website design", "description": w["ld"][1],
         "provider": {"@id": D + "/#organization"}, "areaServed": area, "url": u,
         "offers": [offer(w["t1h"], "399", _plain(" · ".join(w["t1"]))),
                    offer(w["t2h"], "1393", _plain(" · ".join(w["t2"]))),
                    offer(w["t2h"] + " maintenance (optional)", "199", "Optional maintenance, per month",
                          {"priceSpecification": {"@type": "UnitPriceSpecification", "price": "199", "priceCurrency": "MYR", "unitCode": "MON", "referenceQuantity": {"@type": "QuantitativeValue", "value": 1, "unitCode": "MON"}}})]},
        {"@type": "FAQPage", "@id": u + "#faq", "url": u + "#faq", "isPartOf": {"@id": u + "#webpage"},
         "mainEntity": [{"@type": "Question", "name": _plain(q), "acceptedAnswer": {"@type": "Answer", "text": _plain(a)}} for q, a in h["faq"]]},
        {"@type": "BreadcrumbList", "@id": u + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": h["crumb"], "item": D + "/"},
            {"@type": "ListItem", "position": 2, "name": _plain(h["h1"]).split("：")[0].split(":")[0], "item": u}]}]}

WD = {k: {"title": P[k]["title"], "desc": P[k]["desc"], "main": _main(k), "ld": _ld(k)} for k in P}
