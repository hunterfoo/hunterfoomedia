# Homepage (EN / ZH / MS). Copy written natively per language.
# Rules: no timelines, no ranking or AI-recommendation promises, no invented clients/testimonials/portfolio,
# fees by written quote except the website prices (taken from products_pages.WB).
from products_pages import WB, CHECK, PRODUCTS, fee_btn, founding_note
from articles_pages import ARTICLES, DATE_FMT

WA = "https://wa.me/60196273143"
D = "https://www.hunterfoomedia.com"

H = {}
H["en"] = dict(
 title="AI agency in Malaysia & Singapore | Websites AI can read, lead automation | Hunter Foo Media",
 desc="Hunter Foo Media (HF Media Solution) is an AI agency in Kuala Lumpur for businesses in Malaysia and Singapore. Start with a website Google and AI assistants can read (Basic RM399), then automate how you find, follow up and close leads, and your back-office work. WhatsApp +60196273143.",
 eyebrow="AI FOR BUSINESSES · MALAYSIA &amp; SINGAPORE",
 h1='AI that helps you <span class="orange">serve customers</span> — and helps your team with daily work.',
 fde="We learn how your business actually works, then plug AI into the real workflow.",
 img_alt="3D company cutaway: HFM AI linking outward Website, Marketing, Customer Service and inward Manager, Clerk, PA",
 cta1="See website packages", cta_wa="Talk about what you want to automate", cta2="WhatsApp +60 19-627 3143",
 s1e="STEP 1 · WEBSITE", s1h="Start with a website that Google and AI can read.",
 s1p=["For most companies, the most basic step into AI is a website that search engines and AI assistants like ChatGPT and Perplexity can read clearly. That's where we start.",
      "Basic gets you a clean company website. The SEO + AEO/GEO add-on adds what search engines and AI tools read: structured data (schema), Q&amp;A and FAQ content, a sitemap and submission to Google and Bing. Each includes one language and your domain for the first year: English, <span lang='zh-Hans'>中文</span> or BM, plus an llms.txt summary for AI tools. SEO + AEO/GEO is a one-time setup. Optional maintenance: RM199/month."],
 more="Website design details →",
 exh="This site is our first example", exsub="Everything below is live on hunterfoomedia.com today. Check it yourself:",
 ex=[('<a href="/llms.txt">llms.txt</a>', "a plain-text summary of who we are and what we offer, written for AI tools"),
     ('<a href="__EN__">English</a>, <a href="__ZH__" lang="zh-Hans">中文</a> and <a href="__MS__">BM</a>', "three language versions, linked to each other with hreflang tags"),
     ("Structured data", "schema.org markup for our company, services, FAQ and notes"),
     ('<a href="/sitemap.xml">sitemap.xml</a>', "every page in all three languages, listed for search engines"),
     ("IndexNow", "a key in place, so we can tell search engines such as Bing when a page changes")],
 s2e="STEP 2 · LEAD AUTOMATION", s2h="Then automate how you find and follow up leads.",
 s2p="We built this in recruitment first, and it runs every day for our client Sky Employment Pte Ltd, a licensed Singapore employment agency. The same steps work for any business that lives on leads.",
 s2=[("Find leads", "Build a list of potential customers who fit what you sell."),
     ("Fill in contact details", "Add missing phone numbers and email addresses to each lead."),
     ("Email follow-up", "Follow-up emails go out from your own account, so no lead is forgotten."),
     ("Filter the funnel", "Sort leads by how ready they are, so your team talks to the right people first.")],
 proofh="In daily use for our client Sky Employment Pte Ltd",
 proof=[("22", "candidates processed end-to-end: registration → resume → job recommendations"), ("49", "candidate-to-job recommendations generated")],
 proofsrc="From internal records, as of 12 October 2026.",
 s2link="Read the case study →", s2fee="Automation fees are agreed in a written quote before we start.",
 s3e="STEP 3 · CLOSE ON WHATSAPP", s3h="Close the conversation on WhatsApp.",
 s3p=["In Malaysia and Singapore, many customers would rather send a WhatsApp than fill in a form. A WhatsApp digital employee answers the common questions the way your best staff would and tags every chat, so your team knows who to follow up.",
      "A person stays in charge of every decision that matters, and you approve every message template before it goes live."],
 s3link="Try the WhatsApp Digital Employee demo →",
 aie="SEE AI AT WORK", aih="New to AI? Try it in your browser.", aip="Three live demos with made-up sample data. Nothing is sent anywhere.", aitry="Try the demo →",
 ne="NOTES", nh="Latest notes", nall="All notes →",
 fe="FOUNDER", fh="Hunter Foo", frole="Founder, Hunter Foo Media",
 fp=["I started as a CNC programmer in Singapore, then spent 18 years in HR, recruitment and sales.",
     "In early 2025 I started running my own company's daily work with AI, and built an internal HR app to track candidates and follow-ups. I only offer clients what I've used myself and seen work."],
 falt="Portrait of Hunter Foo", fmore="More about us →",
 ce="NEXT STEP", ch="Tell us about your business.", cnote="Malaysian number +60196273143. English, <span lang=\"zh-Hans\">中文</span> or BM. Fees by written quote, except the website prices above.",
 wamsg="Hi Hunter, I'd like to ask about a website / AI for my business.\nMy business: __\nWebsite now (link or none): __",
 # Hero jump links + 业务 (Business, external) / 管理 (Management, internal) areas
 stepsnav=[('#business', 'Business'),
     ('#website', '1 · Website'),
     ('#automation', '2 · Lead automation'),
     ('#whatsapp', '3 · Close on WhatsApp'),
     ('#management', 'Management')],
 bge='BUSINESS · EXTERNAL',
 bgh='Business: win customers.',
 bgp='Three steps that face your customers: get found, follow up leads, close the sale.',
 mge='MANAGEMENT · INTERNAL',
 mgh='Management: run the back office.',
 mgp='Behind every sale is internal work: reports, assignments, paperwork, team updates and approvals. AI takes the repetitive part. Your team still signs off on what matters.',
 mg=[('Reports', 'Daily and weekly reports, pulled together from your own sheets and systems.'),
     ('Matching &amp; assignments', 'Send the right job, case or customer to the right person.'),
     ('Document processing', 'Turn incoming files, forms and resumes into clean, consistent documents.'),
     ('Team workflows &amp; daily summaries', "Everyone sees what's done, what's waiting and what's next."),
     ('Approval queue', 'Drafts wait in a queue. A person approves them before anything goes out.')],
 mgproofh='In daily use: the recruitment system we run for our client Sky Employment',
 mgproof=["New candidates' resumes are prepared automatically, in one consistent format.",
     'Each candidate is matched against the open job orders.',
     'A daily progress report goes to the team.',
     "Every outbound message waits for a person's approval before it is sent."],
 mgnote='The 22 candidates and 49 matches above came through this system.',
 mglink='See the recruitment matching demo →',
 mgfee='Fees: <b>Written quote</b>, agreed before we start.',
)
H["zh"] = dict(
 title="马来西亚与新加坡的 AI Agency｜AI 读得懂的网站与获客自动化｜Hunter Foo Media",
 desc="Hunter Foo Media（HF Media Solution）是吉隆坡的 AI agency，服务马来西亚和新加坡企业。先做 Google 和 AI 助手都读得懂的网站，基础版 RM399；再把找客户、跟进、成交和后台工作自动化。WhatsApp +60196273143。",
 eyebrow="企业 AI · 马来西亚与新加坡",
 h1='AI 帮你<span class="orange">服务客户</span>，也帮团队处理日常工作。',
 fde="先了解你的业务，再把 AI 接进实际工作。",
 img_alt="公司 3D 剖面图：HFM AI 连接对外 Website、Marketing、Customer Service，以及对内 Manager、Clerk、PA",
 cta1="看网站方案", cta_wa="聊聊你想自动化的工作", cta2="WhatsApp +60 19-627 3143",
 s1e="第一步 · 网站", s1h="先有一个 Google 和 AI 都读得懂的网站。",
 s1p=["公司要接上 AI，最基本的一步，就是有一个搜索引擎和 ChatGPT、Perplexity 这类 AI 助手都能读清楚的网站。我们从这里开始。",
      "基础版给你一个清楚好用的公司网站。「SEO + AEO/GEO」加购项，再补上搜索引擎和 AI 工具会读的内容：结构化数据（schema）、问答与 FAQ 内容、网站地图，并提交 Google 与 Bing 收录。两个方案都含 1 种语言（EN、中文或 BM 任选）和第一年域名，并附 llms.txt 给 AI 工具读。SEO + AEO/GEO 是一次性设置；如需维护：每月 RM199。"],
 more="网站设计详情 →",
 exh="这个网站，就是我们的第一个例子", exsub="下面每一项，现在都在 hunterfoomedia.com 上运行，你可以自己点开看：",
 ex=[('<a href="/llms.txt">llms.txt</a>', "一份写给 AI 工具看的纯文字简介：我们是谁、提供什么"),
     ('<a href="__EN__">English</a>、<a href="__ZH__">中文</a>、<a href="__MS__">BM</a>', "三个语言版本，用 hreflang 标签互相对应"),
     ("结构化数据", "公司、服务、常见问题和笔记，都有 schema.org 标记"),
     ('<a href="/sitemap.xml">sitemap.xml</a>', "三种语言的每一页，都列给搜索引擎"),
     ("IndexNow", "已设好密钥，页面更新时可以通知 Bing 等搜索引擎")],
 s2e="第二步 · 获客自动化", s2h="再把找客户、跟进客户自动化。",
 s2p="这套流程我们先在招聘业务里做出来，现在每天为我们的客户 Sky Employment Pte Ltd（新加坡持牌职业中介）运行。靠线索吃饭的生意，都可以用同样的步骤。",
 s2=[("找线索", "整理出一份符合你目标客户的潜在客户名单。"),
     ("补齐联系资料", "帮每条线索补上缺少的电话和电邮。"),
     ("电邮跟进", "跟进电邮从你自己的账号发出，不会漏掉任何一条线索。"),
     ("筛选漏斗", "按客户的成熟度分类，让团队先跟最有机会的人谈。")],
 proofh="每天在用：我们的客户 Sky Employment Pte Ltd",
 proof=[("22", "位候选人走完整个自动流程：登记 → 履历 → 推荐职位"), ("49", "条候选人与职位的匹配推荐")],
 proofsrc="数据来自内部记录，截至 2026 年 10 月 12 日。",
 s2link="看完整案例 →", s2fee="自动化的费用，开工前以书面报价确认。",
 s3e="第三步 · WhatsApp 成交", s3h="最后，在 WhatsApp 上谈成。",
 s3p=["在马来西亚和新加坡，很多客户宁可发 WhatsApp，也不想填表格。WhatsApp 数字员工会像你最好的同事一样回答常见问题，并给每个对话贴好标签，团队一看就知道该跟进谁。",
      "重要的决定始终由人来做；每一条对外的话术模板，都要你批准后才上线。"],
 s3link="试试 WhatsApp 数字员工演示 →",
 aie="看 AI 怎么干活", aih="还不熟悉 AI？直接在浏览器里试。", aip="三个在线演示，用的全是虚构的示例资料，不会发送任何东西。", aitry="打开演示 →",
 ne="笔记", nh="最新笔记", nall="全部笔记 →",
 fe="创办人", fh="Hunter Foo", frole="Hunter Foo Media 创办人",
 fp=["我在新加坡做过 CNC 编程，后来转做人力资源、招聘和销售，前后 18 年。",
     "2025 年初，我开始用 AI 处理自己公司的日常工作，也做了一个内部 HR 应用来整理候选人和跟进。我只给客户做自己用过、确定有效的东西。"],
 falt="Hunter Foo 肖像", fmore="了解更多 →",
 ce="下一步", ch="跟我们说说你的生意。", cnote="马来西亚号码 +60196273143。中文、英文或马来文都可以。除了上面的网站价格，其他费用以书面报价确认。",
 wamsg="你好 Hunter，我想了解网站 / AI 方案。\n我做的是：＿＿\n现在的网站（链接或没有）：＿＿",
 # Hero jump links + 业务 (Business, external) / 管理 (Management, internal) areas
 stepsnav=[('#business', '业务'),
     ('#website', '1 · 网站'),
     ('#automation', '2 · 获客自动化'),
     ('#whatsapp', '3 · WhatsApp 成交'),
     ('#management', '管理')],
 bge='业务 · 对外',
 bgh='业务：把客户赢进来。',
 bgp='这三步都面向客户：让客户找到你、跟进线索、把单谈成。',
 mge='管理 · 对内',
 mgh='管理：后台的活，交给 AI 分担。',
 mgp='每一单生意背后，都有一堆内部工作：做报表、分派任务、整理文件、更新团队进度、走审批。重复的部分交给 AI，重要的事仍由你的团队签核。',
 mg=[('报表', '从你自己的表格和系统里，整理出每日、每周报表。'),
     ('匹配与分派', '把合适的职位、案件或客户，派给合适的人。'),
     ('文件处理', '把收到的文件、表格和简历，整理成格式统一的文档。'),
     ('团队流程与每日汇总', '每个人都清楚：哪些做完了、哪些在等、下一步做什么。'),
     ('审批队列', '草稿先进队列，经人批准后才发出。')],
 mgproofh='每天在用：为我们的客户 Sky Employment 运行的招聘系统',
 mgproof=['新候选人的简历，自动整理成统一格式。',
     '每位候选人自动对照现有职位单进行匹配。',
     '每天自动发进度报告给团队。',
     '每一条对外发出的信息，都要先经人批准。'],
 mgnote='上面的 22 位候选人、49 条匹配，就是这套系统处理的。',
 mglink='看招聘匹配演示 →',
 mgfee='费用：<b>书面报价</b>，开工前确认。',
)
H["ms"] = dict(
 title="Agensi AI di Malaysia & Singapura | Laman web yang AI boleh baca, automasi prospek | Hunter Foo Media",
 desc="Hunter Foo Media (HF Media Solution) ialah agensi AI di Kuala Lumpur untuk perniagaan di Malaysia dan Singapura. Mula dengan laman web yang boleh dibaca Google dan pembantu AI (Asas RM399), kemudian automasikan cara anda cari, susul dan tutup jualan, serta kerja dalaman anda. WhatsApp +60196273143.",
 eyebrow="AI UNTUK PERNIAGAAN · MALAYSIA &amp; SINGAPURA",
 h1='AI yang bantu anda <span class="orange">layan pelanggan</span> — dan bantu pasukan dengan kerja harian.',
 fde="Kami faham cara bisnes anda benar-benar berjalan, kemudian pasang AI ke aliran kerja sebenar.",
 img_alt="Keratan 3D syarikat: AI HFM menghubungkan Website, Marketing, Customer Service di luar dan Manager, Clerk, PA di dalam",
 cta1="Lihat pakej laman web", cta_wa="Bincang kerja yang mahu diautomatikkan", cta2="WhatsApp +60 19-627 3143",
 s1e="LANGKAH 1 · LAMAN WEB", s1h="Mula dengan laman web yang Google dan AI boleh baca.",
 s1p=["Bagi kebanyakan syarikat, langkah paling asas untuk bersedia dengan AI ialah laman web yang boleh dibaca dengan jelas oleh enjin carian dan pembantu AI seperti ChatGPT dan Perplexity. Di situlah kami bermula.",
      "Pakej Asas memberi anda laman web syarikat yang kemas. Tambahan SEO + AEO/GEO menambah apa yang dibaca oleh enjin carian dan alat AI: data berstruktur (schema), kandungan soal jawab dan FAQ, sitemap serta penghantaran kepada Google dan Bing. Kedua-duanya termasuk satu bahasa dan domain untuk tahun pertama: EN, <span lang='zh-Hans'>中文</span> atau BM, serta ringkasan llms.txt untuk alat AI. SEO + AEO/GEO ialah persediaan sekali sahaja. Penyelenggaraan pilihan: RM199/bulan."],
 more="Butiran buat website →",
 exh="Laman ini contoh pertama kami", exsub="Semua di bawah sudah berjalan di hunterfoomedia.com hari ini. Semak sendiri:",
 ex=[('<a href="/llms.txt">llms.txt</a>', "ringkasan teks biasa tentang siapa kami dan apa yang kami tawarkan, ditulis untuk alat AI"),
     ('<a href="__EN__">English</a>, <a href="__ZH__" lang="zh-Hans">中文</a> dan <a href="__MS__">BM</a>', "tiga versi bahasa, dipautkan antara satu sama lain dengan tag hreflang"),
     ("Data berstruktur", "markup schema.org untuk syarikat, servis, FAQ dan catatan kami"),
     ('<a href="/sitemap.xml">sitemap.xml</a>', "setiap halaman dalam ketiga-tiga bahasa, disenaraikan untuk enjin carian"),
     ("IndexNow", "kunci sudah dipasang, supaya kami boleh maklumkan enjin carian seperti Bing apabila halaman berubah")],
 s2e="LANGKAH 2 · AUTOMASI PROSPEK", s2h="Kemudian, automasikan cara anda cari dan susul prospek.",
 s2p="Kami bina sistem ini dalam bidang rekrutmen dahulu, dan ia berjalan setiap hari untuk pelanggan kami Sky Employment Pte Ltd, agensi pekerjaan berlesen di Singapura. Langkah yang sama sesuai untuk mana-mana perniagaan yang bergantung pada prospek.",
 s2=[("Cari prospek", "Bina senarai bakal pelanggan yang sesuai dengan apa yang anda jual."),
     ("Lengkapkan maklumat hubungan", "Tambah nombor telefon dan e-mel yang tiada untuk setiap prospek."),
     ("Susulan e-mel", "E-mel susulan dihantar dari akaun anda sendiri, jadi tiada prospek yang terlepas."),
     ("Tapis corong jualan", "Susun prospek mengikut tahap kesediaan, supaya pasukan anda bercakap dengan orang yang betul dahulu.")],
 proofh="Digunakan setiap hari untuk pelanggan kami Sky Employment Pte Ltd",
 proof=[("22", "calon diproses sepenuhnya: pendaftaran → resume → cadangan kerja"), ("49", "cadangan padanan calon dengan kerja dijana")],
 proofsrc="Daripada rekod dalaman, setakat 12 Oktober 2026.",
 s2link="Baca kajian kes →", s2fee="Yuran automasi dipersetujui dalam sebut harga bertulis sebelum mula.",
 s3e="LANGKAH 3 · TUTUP JUALAN DI WHATSAPP", s3h="Tutup perbualan di WhatsApp.",
 s3p=["Di Malaysia dan Singapura, ramai pelanggan lebih suka hantar WhatsApp daripada isi borang. Pekerja digital WhatsApp menjawab soalan biasa seperti staf terbaik anda dan melabel setiap perbualan, jadi pasukan anda tahu siapa perlu disusul.",
      "Setiap keputusan penting tetap dibuat oleh manusia, dan anda luluskan setiap templat mesej sebelum ia digunakan."],
 s3link="Cuba demo Pekerja Digital WhatsApp →",
 aie="LIHAT AI BEKERJA", aih="Baru dengan AI? Cuba terus dalam pelayar anda.", aip="Tiga demo langsung dengan data contoh rekaan. Tiada apa-apa yang dihantar ke mana-mana.", aitry="Cuba demo →",
 ne="CATATAN", nh="Catatan terkini", nall="Semua catatan →",
 fe="PENGASAS", fh="Hunter Foo", frole="Pengasas, Hunter Foo Media",
 fp=["Saya bermula sebagai pengaturcara CNC di Singapura, kemudian 18 tahun dalam HR, rekrutmen dan jualan.",
     "Pada awal 2025, saya mula menggunakan AI untuk kerja harian syarikat saya sendiri, dan membina aplikasi HR dalaman untuk menjejak calon dan susulan. Saya hanya menawarkan apa yang telah saya guna sendiri dan terbukti berkesan."],
 falt="Potret Hunter Foo", fmore="Lagi tentang kami →",
 ce="LANGKAH SETERUSNYA", ch="Ceritakan tentang perniagaan anda.", cnote="Nombor Malaysia +60196273143. Bahasa Inggeris, Cina atau BM. Yuran melalui sebut harga bertulis, kecuali harga laman web di atas.",
 wamsg="Hai Hunter, saya nak tanya tentang laman web / AI untuk perniagaan saya.\nBisnes saya: __\nLaman web sekarang (pautan atau tiada): __",
 # Hero jump links + 业务 (Business, external) / 管理 (Management, internal) areas
 stepsnav=[('#business', 'Perniagaan'),
     ('#website', '1 · Laman web'),
     ('#automation', '2 · Automasi prospek'),
     ('#whatsapp', '3 · Tutup jualan di WhatsApp'),
     ('#management', 'Pengurusan')],
 bge='PERNIAGAAN · LUARAN',
 bgh='Perniagaan: dapatkan pelanggan.',
 bgp='Tiga langkah yang berdepan dengan pelanggan: mudah ditemui, susul prospek, tutup jualan.',
 mge='PENGURUSAN · DALAMAN',
 mgh='Pengurusan: lancarkan operasi dalaman.',
 mgp='Di sebalik setiap jualan ada kerja dalaman: laporan, agihan tugas, dokumen, kemas kini pasukan dan kelulusan. AI ambil alih bahagian yang berulang. Perkara penting tetap diluluskan oleh pasukan anda.',
 mg=[('Laporan', 'Laporan harian dan mingguan, disusun daripada sheet dan sistem anda sendiri.'),
     ('Padanan &amp; agihan tugas', 'Hantar kerja, kes atau pelanggan yang betul kepada orang yang betul.'),
     ('Pemprosesan dokumen', 'Fail, borang dan resume yang masuk disusun menjadi dokumen yang kemas dan seragam.'),
     ('Aliran kerja pasukan &amp; ringkasan harian', 'Semua orang tahu apa yang sudah siap, apa yang menunggu dan apa seterusnya.'),
     ('Barisan kelulusan', 'Draf menunggu dalam barisan. Seorang manusia meluluskannya sebelum apa-apa dihantar.')],
 mgproofh='Digunakan setiap hari: sistem rekrutmen yang kami jalankan untuk pelanggan kami Sky Employment',
 mgproof=['Resume calon baharu disediakan secara automatik dalam satu format yang seragam.',
     'Setiap calon dipadankan dengan pesanan kerja yang masih dibuka.',
     'Laporan kemajuan harian dihantar kepada pasukan.',
     'Setiap mesej keluar menunggu kelulusan manusia sebelum dihantar.'],
 mgnote='22 calon dan 49 padanan di atas diproses melalui sistem ini.',
 mglink='Lihat demo padanan rekrutmen →',
 mgfee='Yuran: <b>Sebut harga bertulis</b>, dipersetujui sebelum mula.',
)

import urllib.parse, html

# ---- Homepage FAQ (visible <details> list + matching FAQPage JSON-LD). Answers only restate what the site already says. ----
ZH_ = '<span lang="zh-Hans">中文</span>'
HFAQ = {}
HFAQ["en"] = dict(kicker="FAQ", h="Common questions", qa=[
 ("What does Hunter Foo Media do?",
  "Hunter Foo Media (HF Media Solution) is an AI agency in Kuala Lumpur for businesses in Malaysia and Singapore. We work as forward deployed engineers: we learn how your team actually works, then build what fits. We start with a website that Google and AI assistants can read, then automate how you find, follow up and close leads, and your back-office work."),
 ("How much does a website cost?",
  "Basic is RM399. SEO + AEO/GEO is RM1,393 in total (Basic RM399 + RM994), a one-time setup. Both include one language and your domain for the first year. Optional maintenance: RM199/month. More languages, extra pages or other custom scope are confirmed by <b>written quote</b>. These prices (including RM199/month maintenance) are founding-client prices for our first 20 clients, in exchange for an honest testimonial. Prices will go up after 20 clients."),
 ("How much does AI automation cost?",
  "Lead automation, the WhatsApp digital employee and back-office (Management) work are priced by <b>written quote</b>, agreed before we start. Only the website packages have fixed prices."),
 ("Will AI send messages to my customers without my approval?",
  "No. A person stays in charge of every decision that matters, and you approve every message template before it goes live. Drafts wait in an approval queue, and a person approves them before anything goes out."),
 ("Do you guarantee Google rankings or AI recommendations?",
  "No. We don't promise rankings, or that Google or any AI tool will show or recommend your site. We tell you exactly what we build and set up."),
 ("Where are you based, and how do I contact you?",
  "We're based in Kuala Lumpur and work remotely across Malaysia and Singapore. WhatsApp +60 19-627 3143 or email <!--email_off-->hello@hunterfoomedia.com<!--/email_off-->, in English, " + ZH_ + " or BM."),
])
HFAQ["zh"] = dict(kicker="常见问题", h="你可能想问的", qa=[
 ("Hunter Foo Media 是做什么的？",
  "Hunter Foo Media（HF Media Solution）是吉隆坡的 AI agency，服务马来西亚和新加坡企业。我们以前沿部署工程师的方式工作：先弄清楚你的团队实际怎么做事，再动手搭建合用的系统。第一步做一个 Google 和 AI 助手都读得懂的网站，接着把找客户、跟进、成交和后台工作自动化。"),
 ("做网站要多少钱？",
  "基础版 RM399；含 SEO + AEO/GEO 合共 RM1,393（基础版 RM399 + RM994），是一次性设置。两个方案都含 1 种语言和第一年域名。如需维护：每月 RM199。加语言、加页面或其他特别需求，以<b>书面报价</b>确认。以上价格（含 RM199/月维护费）为前 20 位客户优惠价，条件是为我们写一则真实评价。满 20 位后将调价。"),
 ("AI 自动化怎么收费？",
  "获客自动化、WhatsApp 数字员工和后台（管理）工作，费用都以<b>书面报价</b>确认，开工前谈好。只有网站方案是固定价格。"),
 ("AI 会不经我同意就发信息给客户吗？",
  "不会。重要的决定始终由人来做；每一条对外的话术模板，都要你批准后才上线。草稿先进审批队列，经人批准后才发出。"),
 ("保证 Google 排名或 AI 推荐吗？",
  "不保证。我们不承诺排名，也不承诺 Google 或任何 AI 工具会显示或推荐你的网站。我们会清楚告诉你做了什么、设置了什么。"),
 ("你们在哪里？怎么联系？",
  "我们立足吉隆坡，远程服务马来西亚与新加坡。WhatsApp +60 19-627 3143，或电邮 <!--email_off-->hello@hunterfoomedia.com<!--/email_off-->；中文、英文或马来文都可以。"),
])
HFAQ["ms"] = dict(kicker="Soalan lazim", h="Soalan yang mungkin anda ada", qa=[
 ("Apa yang Hunter Foo Media buat?",
  "Hunter Foo Media (HF Media Solution) ialah agensi AI di Kuala Lumpur untuk perniagaan di Malaysia dan Singapura. Kami bekerja sebagai forward deployed engineer: kami faham cara pasukan anda sebenarnya bekerja, kemudian bina sistem yang sesuai. Kami mula dengan laman web yang boleh dibaca oleh Google dan pembantu AI, kemudian automasikan cara anda cari, susul dan tutup jualan, serta kerja dalaman anda."),
 ("Berapa harga laman web?",
  "Pakej Asas RM399. SEO + AEO/GEO berjumlah RM1,393 (Asas RM399 + RM994), persediaan sekali sahaja. Kedua-duanya termasuk satu bahasa dan domain untuk tahun pertama. Penyelenggaraan pilihan: RM199/bulan. Bahasa tambahan, halaman tambahan atau skop khas lain disahkan melalui <b>sebut harga bertulis</b>. Harga ini (termasuk penyelenggaraan RM199/bulan) ialah harga pelanggan awal untuk 20 pelanggan pertama, sebagai balasan satu testimoni yang jujur. Harga akan naik selepas 20 pelanggan."),
 ("Berapa kos automasi AI?",
  "Automasi prospek, Pekerja Digital WhatsApp dan kerja dalaman (Pengurusan) dikenakan yuran melalui <b>sebut harga bertulis</b>, dipersetujui sebelum mula. Hanya pakej laman web yang ada harga tetap."),
 ("Adakah AI akan hantar mesej kepada pelanggan saya tanpa kelulusan saya?",
  "Tidak. Setiap keputusan penting tetap dibuat oleh manusia, dan anda luluskan setiap templat mesej sebelum ia digunakan. Draf menunggu dalam barisan kelulusan, dan seorang manusia meluluskannya sebelum apa-apa dihantar."),
 ("Adakah anda jamin kedudukan Google atau cadangan AI?",
  "Tidak. Kami tidak menjanjikan kedudukan, atau bahawa Google atau mana-mana alat AI akan memaparkan atau mengesyorkan laman anda. Kami beritahu dengan jelas apa yang kami bina dan sediakan."),
 ("Di mana anda berada, dan bagaimana nak hubungi?",
  "Kami berpangkalan di Kuala Lumpur dan berkhidmat untuk Malaysia dan Singapura secara jarak jauh. WhatsApp +60 19-627 3143 atau e-mel <!--email_off-->hello@hunterfoomedia.com<!--/email_off-->, dalam bahasa Inggeris, Cina atau BM."),
])

import re as _re
def _faq_plain(s):
    # strips tags and the <!--email_off--> markers (they stop Cloudflare Email Obfuscation rewriting the address in the visible answer)
    return html.unescape(_re.sub(r"<!--.*?-->|<[^>]+>", "", s))

def _home_faq(k):
    f = HFAQ[k]
    items = "".join('<details%s><summary>%s</summary><p>%s</p></details>' % (' open' if i == 0 else '', q, a) for i, (q, a) in enumerate(f["qa"]))
    return ('<section class="paper pd-faq-wrap" id="faq" aria-labelledby="hm-faq-h"><div class="wrap section"><div class="pd-faq">'
            '<p class="pd-kicker">%s</p><h2 id="hm-faq-h">%s</h2>%s</div></div></section>\n') % (f["kicker"], f["h"], items)
def _main(k):
    h = H[k]; w = WB[k]
    wa = WA + "?text=" + urllib.parse.quote(h["wamsg"], safe="")
    chk = lambda xs: '<ul class="ad-checks">' + "".join("<li>%s<span>%s</span></li>" % (CHECK, x) for x in xs) + "</ul>"
    tier = lambda tag, t, sub, xs, cls, fee: ('<div class="ad-panel wb-tier%s"><p class="wb-tag">%s</p><h3>%s</h3><p class="wb-sub">%s</p>%s'
                                              '%s</div>') % (cls, tag, t, sub, chk(xs), fee)
    demos = PRODUCTS[k]["services"]
    out = []
    # Hero (v6 visual: headline + FDE line + 3D company image + WhatsApp CTA)
    out.append(
        '<section class="wrap hm-hero">'
        '<p class="eyebrow"><i></i>%s</p>'
        '<h1>%s</h1>'
        '<p class="hm-fde">%s</p>'
        '<figure class="hm-3d">'
        '<picture>'
        '<source type="image/webp" srcset="/assets/hfm-ai-company-3d.webp">'
        '<img src="/assets/hfm-ai-company-3d.jpg" width="1280" height="720" alt="%s" decoding="async" fetchpriority="high">'
        '</picture>'
        '</figure>'
        '<div class="hm-ctas">'
        '<a class="button" href="%s" target="_blank" rel="noopener noreferrer">%s <span aria-hidden="true">↗</span></a>'
        '<a class="button ghost" href="#website">%s <span aria-hidden="true">→</span></a>'
        '</div>'
        '<nav class="hm-stepsnav" aria-label="%s">%s</nav>'
        '</section>\n' % (
            h["eyebrow"], h["h1"], h["fde"], html.escape(h["img_alt"], quote=True),
            wa, h["cta_wa"], h["cta1"],
            h["s1e"].split("·")[0].strip(),
            "".join('<a href="%s">%s</a>' % x for x in h["stepsnav"]),
        )
    )
    # 业务 (Business, external): group header for steps 1-3
    out.append('<section class="wrap hm-area" id="business"><p class="eyebrow"><i></i>%s</p><h2 class="hm-area-h">%s</h2><p class="hm-lede-d">%s</p></section>\n' % (
               h["bge"], h["bgh"], h["bgp"]))
    # Step 1: website
    out.append('<section class="paper ad-section hm-sec" id="website"><div class="wrap section">'
               '<p class="pd-kicker">%s</p><h2 class="hm-h2">%s</h2><div class="hm-lede">%s</div>'
               '<div class="ad-two wb-two">%s%s</div>%s<p class="hm-more"><a href="/website-design/">%s</a></p>'
               '<p class="ad-fine">%s</p>'
               '<div class="hm-example"><h3>%s</h3><p>%s</p><ul>%s</ul></div>'
               '</div></section>\n' % (
               h["s1e"], h["s1h"], "".join("<p>%s</p>" % x for x in h["s1p"]),
               tier(w["t1tag"], w["t1h"], w["t1sub"], w["t1"], "", fee_btn(w, 1)), tier(w["t2tag"], w["t2h"], w["t2sub"], w["t2"], " wb-plus", fee_btn(w, 2)), founding_note(w),
               h["more"], w["fine"], h["exh"], h["exsub"],
               "".join('<li>%s<b>%s</b><span>%s</span></li>' % (CHECK, a, b) for a, b in h["ex"])))
    # Step 2: lead automation
    out.append('<section class="wrap section hm-sec hm-dark" id="automation"><p class="eyebrow"><i></i>%s</p><h2 class="hm-h2">%s</h2><p class="hm-lede-d">%s</p>'
               '<ol class="hm-cards">%s</ol>'
               '<div class="hm-proof"><h3>%s</h3><ul>%s</ul><p class="hm-src">%s</p><p><a class="hm-link" href="/products/#case-study">%s</a></p></div>'
               '<p class="hm-fine">%s</p></section>\n' % (
               h["s2e"], h["s2h"], h["s2p"],
               "".join('<li><span class="hm-n">%d</span><h3>%s</h3><p>%s</p></li>' % (i + 1, a, b) for i, (a, b) in enumerate(h["s2"])),
               h["proofh"], "".join('<li><b>%s</b><span>%s</span></li>' % x for x in h["proof"]), h["proofsrc"], h["s2link"], h["s2fee"]))
    # Step 3: WhatsApp
    out.append('<section class="paper hm-sec" id="whatsapp"><div class="wrap section hm-split"><div><p class="pd-kicker">%s</p><h2 class="hm-h2">%s</h2></div>'
               '<div>%s<p><a class="button" href="/products/#demo-2">%s</a></p></div></div></section>\n' % (
               h["s3e"], h["s3h"], "".join('<p class="hm-p">%s</p>' % x for x in h["s3p"]), h["s3link"].rstrip(" →") + ' <span aria-hidden="true">→</span>'))
    # 管理 (Management, internal): back-office work, recruitment system as proof; fee by written quote only
    out.append('<section class="wrap hm-area hm-mgmt" id="management"><p class="eyebrow"><i></i>%s</p><h2 class="hm-area-h">%s</h2><p class="hm-lede-d">%s</p>'
               '<ol class="hm-cards hm-cards-5">%s</ol>'
               '<div class="hm-proof hm-mg-proof"><h3>%s</h3><ul>%s</ul><p class="hm-src">%s</p><p><a class="hm-link" href="/products/#demo-1">%s</a></p></div>'
               '<p class="hm-fine hm-mg-fee">%s</p></section>\n' % (
               h["mge"], h["mgh"], h["mgp"],
               "".join('<li><span class="hm-n">%d</span><h3>%s</h3><p>%s</p></li>' % (i + 1, a, b) for i, (a, b) in enumerate(h["mg"])),
               h["mgproofh"], "".join('<li>%s<span>%s</span></li>' % (CHECK, x) for x in h["mgproof"]), h["mgnote"], h["mglink"], h["mgfee"]))
    # See AI at work
    out.append('<section class="wrap section hm-sec hm-dark" id="demos"><p class="eyebrow"><i></i>%s</p><h2 class="hm-h2">%s</h2><p class="hm-lede-d">%s</p>'
               '<ul class="hm-demos">%s</ul></section>\n' % (
               h["aie"], h["aih"], h["aip"],
               "".join('<li><a href="/products/#demo-%d"><span class="hm-n">0%d</span><h3>%s</h3><p>%s</p><span class="hm-go">%s</span></a></li>' % (i + 1, i + 1, n, d, h["aitry"]) for i, (n, d) in enumerate(demos))))
    # Latest notes
    out.append('<section class="paper hm-sec" id="notes"><div class="wrap section"><p class="pd-kicker">%s</p><h2 class="hm-h2">%s</h2><ul class="hm-notes">%s</ul>'
               '<p class="hm-more"><a href="/notes/">%s</a></p></div></section>\n' % (
               h["ne"], h["nh"],
               "".join('<li><a href="/notes/%s/"><time datetime="%s">%s</time><h3>%s</h3><p>%s</p></a></li>' % (a["slug"], a["date"], DATE_FMT[k](a["date"]), a[k]["h1"], a[k]["desc"]) for a in ARTICLES[:2]),
               h["nall"]))
    # Founder
    out.append('<section class="wrap section hm-sec hm-dark hm-founder" id="founder"><img src="/assets/hunter-foo-avatar.jpg" width="160" height="160" alt="%s" loading="lazy" decoding="async">'
               '<div><p class="eyebrow"><i></i>%s</p><h2 class="hm-h2">%s</h2><p class="hm-role">%s</p>%s'
               '<p class="hm-links"><a class="hm-link" href="/about/">%s</a><a class="hm-link" href="https://www.linkedin.com/in/hunterfoo3143/" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></p></div></section>\n' % (
               h["falt"], h["fe"], h["fh"], h["frole"], "".join('<p class="hm-lede-d">%s</p>' % x for x in h["fp"]), h["fmore"]))
    # FAQ (matches the FAQPage JSON-LD in _ld)
    out.append(_home_faq(k))
    # Contact
    out.append('<section class="wrap section contact" id="contact"><p class="eyebrow"><i></i>%s</p><div class="contact-row"><h2>%s</h2><div class="contact-actions">'
               '<a class="button whatsapp" data-wa="%s" href="%s" target="_blank" rel="noopener noreferrer">WhatsApp +60196273143 <span aria-hidden="true">↗</span></a>'
               '<!--email_off--><a class="email-link" href="mailto:hello@hunterfoomedia.com">hello@hunterfoomedia.com <span aria-hidden="true">↗</span></a><!--/email_off--><p>%s</p></div></div></section>\n' % (
               h["ce"], h["ch"], html.escape(h["wamsg"]), wa, h["cnote"]))
    return "\n" + "".join(out)

def _ld(k):
    h = H[k]; w = WB[k]
    u = D + "/"
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "@id": D + "/#website", "url": u, "name": "Hunter Foo Media", "publisher": {"@id": D + "/#organization"}},
        {"@type": "WebPage", "@id": u + "#webpage", "url": u, "name": h["title"], "description": h["desc"], "about": {"@id": D + "/#organization"}, "isPartOf": {"@id": D + "/#website"}},
        {"@type": "Service", "@id": u + "#website-building", "name": w["ld"][0], "description": w["ld"][1], "serviceType": "Website building", "provider": {"@id": D + "/#organization"},
         "areaServed": [{"@type": "Country", "name": "Malaysia"}, {"@type": "Country", "name": "Singapore"}], "url": D + "/website-design/"},
        {"@type": "Service", "@id": u + "#management", "name": h["mgh"].rstrip(".。"), "description": h["mgp"], "serviceType": "Back-office AI automation", "provider": {"@id": D + "/#organization"},
         "areaServed": [{"@type": "Country", "name": "Malaysia"}, {"@type": "Country", "name": "Singapore"}], "url": u + "#management"},
        {"@type": "Person", "@id": D + "/#founder", "name": "Hunter Foo", "jobTitle": "Founder", "image": D + "/assets/hunter-foo-portrait.jpeg",
         "sameAs": ["https://www.linkedin.com/in/hunterfoo3143/"], "worksFor": {"@id": D + "/#organization"}},
        {"@type": "FAQPage", "@id": u + "#faq", "url": u + "#faq", "isPartOf": {"@id": u + "#webpage"},
         "mainEntity": [{"@type": "Question", "name": _faq_plain(q), "acceptedAnswer": {"@type": "Answer", "text": _faq_plain(a)}} for q, a in HFAQ[k]["qa"]]}]}

HOME = {k: {"title": H[k]["title"], "desc": H[k]["desc"], "main": _main(k), "ld": _ld(k)} for k in H}
