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
 desc="Hunter Foo Media helps businesses in Malaysia and Singapore stay in sync with AI — serving customers outside and supporting the team inside. WhatsApp +60196273143.",
 eyebrow="AI FOR BUSINESSES · MALAYSIA &amp; SINGAPORE",
 h1='AI that helps you <span class="orange">serve customers</span> — and helps your team with daily work.',
 fde="We help businesses stay in sync with AI, joining the outside and inside pieces so you keep pace with the market and technology.",
 img_alt="3D company cutaway: HFM AI linking outward Website, Marketing, Customer Service and inward Manager, Clerk, PA",
 cta1="See how we help the team", cta_wa="Talk about what you want to automate", cta2="WhatsApp +60 19-627 3143",
 s1e="STEP 1 · WEBSITE", s1h="Start with a website that Google and AI can read.",
 s1p=["A readable website is often the first step into AI. Details confirmed in writing."],
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


 # v8 dual sides + slim flow + bottom links
 out_tag="OUTWARD", out_h="Serve customers",
 out=[("Website", "Update pages so Google and AI assistants can understand them"),
      ("Marketing", "Prepare social posts — published only after you approve"),
      ("Customer Service", "Answer common questions first; complex ones go to a person")],
 in_tag="INWARD", in_h="Help the team",
 in_=[("Clerk", "Organise and archive files"),
      ("Manager", "Follow up staff tasks and reminders"),
      ("PA", "Sort email and draft replies for you to confirm")],
 web_early="Need a company website? See packages ↓",
 flow_e="HOW IT LANDS", flow_h="Lead flow and closing can use AI too",
 flow_p="Finding leads, follow-ups, WhatsApp replies — AI takes the repetitive part; a person still approves before anything goes out. Fees by written quote.",
 flow_chips=["Find leads & fill contacts", "Email follow-up", "WhatsApp answers common Qs", "Human approval before send"],
 founder_link="Meet Hunter →", notes_link="Latest notes →",
 pkg_kicker="SUPPORTING · WEBSITE", pkg_h="Need a clear company website first?",
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
 desc="Hunter Foo Media 帮企业和 AI 同步：对外服务客户，对内帮团队做事，让公司跟上市场和科技的变化。WhatsApp +60196273143。",
 eyebrow="企业 AI · 马来西亚与新加坡",
 h1='AI 帮你<span class="orange">服务客户</span>，也帮团队处理日常工作。',
 fde="帮企业和 AI 同步：拼好对外和对内两块拼图，跟上市场和科技的变化。",
 img_alt="公司 3D 剖面图：HFM AI 连接对外 Website、Marketing、Customer Service，以及对内 Manager、Clerk、PA",
 cta1="看看怎么帮团队", cta_wa="聊聊你想自动化的工作", cta2="WhatsApp +60 19-627 3143",
 s1e="第一步 · 网站", s1h="先有一个 Google 和 AI 都读得懂的网站。",
 s1p=["可读的网站常常是接上 AI 的第一步。详情与报价以书面为准。"],
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


 # v8 dual sides + slim flow + bottom links
 out_tag="对外", out_h="服务客户",
 out=[("Website", "更新网页，让 Google 和 AI 助手读得懂"),
      ("Marketing", "准备社交媒体内容，你批准后才发布"),
      ("Customer Service", "先回常见询问，复杂的转真人")],
 in_tag="对内", in_h="帮团队做事",
 in_=[("Clerk", "整理和归档文件"),
      ("Manager", "跟进员工任务和提醒"),
      ("PA", "分类电邮、拟好回复给你确认")],
 web_early="需要公司网站？看套餐 ↓",
 flow_e="怎么落地", flow_h="获客与成交，也可以接上 AI",
 flow_p="找线索、跟进、WhatsApp 回复——重复的部分交给 AI，发出前仍由人批准。费用书面报价。",
 flow_chips=["找线索 & 补联系方式", "电邮跟进", "WhatsApp 先答常见问题", "人审批后再发出"],
 founder_link="认识 Hunter →", notes_link="最新笔记 →",
 pkg_kicker="支撑服务 · 网站", pkg_h="需要先有一个清楚的公司网站？",
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
 desc="Hunter Foo Media membantu perniagaan di Malaysia dan Singapura seiring dengan AI — melayan pelanggan di luar dan bantu pasukan di dalam. WhatsApp +60196273143.",
 eyebrow="AI UNTUK PERNIAGAAN · MALAYSIA &amp; SINGAPURA",
 h1='AI yang bantu anda <span class="orange">layan pelanggan</span> — dan bantu pasukan dengan kerja harian.',
 fde="Kami bantu perniagaan seiring dengan AI, menyatukan kepingan luar dan dalam supaya anda mengikuti perubahan pasaran dan teknologi.",
 img_alt="Keratan 3D syarikat: AI HFM menghubungkan Website, Marketing, Customer Service di luar dan Manager, Clerk, PA di dalam",
 cta1="Lihat cara bantu pasukan", cta_wa="Bincang kerja yang mahu diautomatikkan", cta2="WhatsApp +60 19-627 3143",
 s1e="LANGKAH 1 · LAMAN WEB", s1h="Mula dengan laman web yang Google dan AI boleh baca.",
 s1p=["Laman yang mudah dibaca sering langkah pertama ke AI. Butiran disahkan secara bertulis."],
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


 # v8 dual sides + slim flow + bottom links
 out_tag="LUARAN", out_h="Layan pelanggan",
 out=[("Website", "Kemas kini laman supaya Google dan pembantu AI faham"),
      ("Marketing", "Sedia kandungan sosial — diterbit selepas anda luluskan"),
      ("Customer Service", "Jawab soalan biasa dahulu; yang kompleks kepada orang")],
 in_tag="DALAMAN", in_h="Bantu pasukan",
 in_=[("Clerk", "Susun dan arkib fail"),
      ("Manager", "Susuli tugas dan peringatan kakitangan"),
      ("PA", "Isih e-mel dan draf balasan untuk anda sahkan")],
 web_early="Perlukan laman syarikat? Lihat pakej ↓",
 flow_e="CARA DILAKSANAKAN", flow_h="Aliran prospek dan tutup jualan juga boleh guna AI",
 flow_p="Cari prospek, susulan, balasan WhatsApp — AI ambil yang berulang; manusia masih luluskan sebelum apa-apa keluar. Yuran melalui sebut harga bertulis.",
 flow_chips=["Cari prospek & lengkapkan kontak", "Susulan e-mel", "WhatsApp jawab soalan biasa", "Kelulusan manusia sebelum hantar"],
 founder_link="Kenali Hunter →", notes_link="Catatan terkini →",
 pkg_kicker="SOKONGAN · LAMAN WEB", pkg_h="Perlukan laman syarikat yang jelas dahulu?",
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

# ---- Homepage FAQ (v8: 3–4 short Qs, no prices). Answers match FAQPage JSON-LD. ----
ZH_ = '<span lang="zh-Hans">中文</span>'
HFAQ = {}
HFAQ["en"] = dict(kicker="FAQ", h="Common questions", qa=[
 ("What does Hunter Foo Media do?",
  "An AI agency in Kuala Lumpur for businesses in Malaysia and Singapore: we learn how you work, then plug AI into lead flow, customer service and back-office work."),
 ("Will AI send messages to my customers without my approval?",
  "No. Outbound message templates need your approval first. Drafts wait in a queue until a person approves them."),
 ("Do you guarantee Google rankings or AI recommendations?",
  "No. We tell you exactly what we build and set up; ranking and citation are up to search engines and AI tools."),
 ("Where are you based, and how do I contact you?",
  "Kuala Lumpur, working remotely across Malaysia and Singapore. WhatsApp +60 19-627 3143 or email <!--email_off-->hello@hunterfoomedia.com<!--/email_off-->."),
])
HFAQ["zh"] = dict(kicker="常见问题", h="你可能想问的", qa=[
 ("Hunter Foo Media 是做什么的？",
  "吉隆坡的 AI agency，服务马来西亚与新加坡企业：先弄清楚你怎么做事，再把 AI 接进获客、客服和后台工作。"),
 ("AI 会不经我同意就发信息给客户吗？",
  "不会。对外话术要你批准后才上线；草稿先进审批队列，经人批准后才发出。"),
 ("保证 Google 排名或 AI 推荐吗？",
  "不保证。我们只把做什么、设置什么写清楚；怎么排序、引用由搜索引擎和 AI 工具决定。"),
 ("你们在哪里？怎么联系？",
  "立足吉隆坡，远程服务马来西亚与新加坡。WhatsApp +60 19-627 3143，或电邮 <!--email_off-->hello@hunterfoomedia.com<!--/email_off-->。"),
])
HFAQ["ms"] = dict(kicker="Soalan lazim", h="Soalan yang mungkin anda ada", qa=[
 ("Apa yang Hunter Foo Media buat?",
  "Agensi AI di Kuala Lumpur untuk perniagaan di Malaysia dan Singapura: kami faham cara anda bekerja, kemudian pasang AI ke aliran prospek, khidmat pelanggan dan kerja dalaman."),
 ("Adakah AI akan hantar mesej kepada pelanggan tanpa kelulusan saya?",
  "Tidak. Templat mesej keluar perlu anda luluskan dahulu. Draf menunggu dalam barisan sehingga seorang manusia meluluskannya."),
 ("Adakah anda jamin kedudukan Google atau cadangan AI?",
  "Tidak. Kami beritahu dengan jelas apa yang kami bina dan sediakan; kedudukan dan petikan terserah kepada enjin carian dan alat AI."),
 ("Di mana anda berada, dan bagaimana nak hubungi?",
  "Kuala Lumpur, berkhidmat jarak jauh di Malaysia dan Singapura. WhatsApp +60 19-627 3143 atau e-mel <!--email_off-->hello@hunterfoomedia.com<!--/email_off-->."),
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
    # Hero (v8: no pill row; secondary CTA → #internal)
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
        '<a class="button ghost" href="#internal">%s <span aria-hidden="true">→</span></a>'
        '</div>'
        '</section>\n' % (
            h["eyebrow"], h["h1"], h["fde"], html.escape(h["img_alt"], quote=True),
            wa, h["cta_wa"], h["cta1"],
        )
    )
    # Dual sides matching 3D desks
    def side_items(pairs):
        return "".join('<li><span class="hm-side-ico" aria-hidden="true">%s</span><div><strong>%s</strong><span>%s</span></div></li>' % (a[:2], a, b) for a, b in pairs)
    out.append(
        '<section class="wrap hm-sides" id="sides">'
        '<div class="hm-sides-grid">'
        '<article class="hm-side" id="external"><h2><span class="hm-side-tag">%s</span> %s</h2><ul class="hm-side-list">%s</ul></article>'
        '<article class="hm-side" id="internal"><h2><span class="hm-side-tag">%s</span> %s</h2><ul class="hm-side-list">%s</ul></article>'
        '</div>'
        '<p class="hm-more"><a href="#website">%s</a></p>'
        '</section>\n' % (
            h["out_tag"], h["out_h"], side_items(h["out"]),
            h["in_tag"], h["in_h"], side_items(h["in_"]),
            h["web_early"],
        )
    )
    # Slim lead-flow
    out.append(
        '<section class="wrap section hm-sec hm-dark hm-flow" id="automation">'
        '<p class="eyebrow"><i></i>%s</p><h2 class="hm-h2">%s</h2><p class="hm-lede-d">%s</p>'
        '<div class="hm-chips">%s</div>'
        '</section>\n' % (
            h["flow_e"], h["flow_h"], h["flow_p"],
            "".join('<span class="hm-chip">%s</span>' % c for c in h["flow_chips"]),
        )
    )
    # Demos (before packages)
    out.append('<section class="wrap section hm-sec hm-dark" id="demos"><p class="eyebrow"><i></i>%s</p><h2 class="hm-h2">%s</h2><p class="hm-lede-d">%s</p>'
               '<ul class="hm-demos">%s</ul></section>\n' % (
               h["aie"], h["aih"], h["aip"],
               "".join('<li><a href="/products/#demo-%d"><span class="hm-n">0%d</span><h3>%s</h3><p>%s</p><span class="hm-go">%s</span></a></li>' % (i + 1, i + 1, n, d, h["aitry"]) for i, (n, d) in enumerate(demos))))
    # Website packages (moved down)
    out.append('<section class="paper ad-section hm-sec" id="website"><div class="wrap section">'
               '<p class="pd-kicker">%s</p><h2 class="hm-h2">%s</h2><div class="hm-lede">%s</div>'
               '<div class="ad-two wb-two">%s%s</div>%s<p class="hm-more"><a href="/website-design/">%s</a></p>'
               '<p class="ad-fine">%s</p>'
               '</div></section>\n' % (
               h["pkg_kicker"], h["pkg_h"], "".join("<p>%s</p>" % x for x in h["s1p"]),
               tier(w["t1tag"], w["t1h"], w["t1sub"], w["t1"], "", fee_btn(w, 1)), tier(w["t2tag"], w["t2h"], w["t2sub"], w["t2"], " wb-plus", fee_btn(w, 2)), founding_note(w),
               h["more"], w["fine"]))
    # Founder + notes one-liners
    out.append(
        '<section class="wrap hm-more-links" id="more">'
        '<a class="hm-link" href="/about/">%s</a>'
        '<a class="hm-link" href="/notes/">%s</a>'
        '</section>\n' % (h["founder_link"], h["notes_link"])
    )
    # FAQ then contact
    out.append(_home_faq(k))
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
        {"@type": "Service", "@id": u + "#management", "name": h["in_h"], "description": h["flow_p"], "serviceType": "Back-office AI automation", "provider": {"@id": D + "/#organization"},
         "areaServed": [{"@type": "Country", "name": "Malaysia"}, {"@type": "Country", "name": "Singapore"}], "url": u + "#internal"},
        {"@type": "Person", "@id": D + "/#founder", "name": "Hunter Foo", "jobTitle": "Founder", "image": D + "/assets/hunter-foo-portrait.jpeg",
         "sameAs": ["https://www.linkedin.com/in/hunterfoo3143/"], "worksFor": {"@id": D + "/#organization"}},
        {"@type": "FAQPage", "@id": u + "#faq", "url": u + "#faq", "isPartOf": {"@id": u + "#webpage"},
         "mainEntity": [{"@type": "Question", "name": _faq_plain(q), "acceptedAnswer": {"@type": "Answer", "text": _faq_plain(a)}} for q, a in HFAQ[k]["qa"]]}]}

HOME = {k: {"title": H[k]["title"], "desc": H[k]["desc"], "main": _main(k), "ld": _ld(k)} for k in H}
