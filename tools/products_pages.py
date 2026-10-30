# Products + interactive demo page (/products/, /zh/products/, /ms/products/).
# Copy per language is written natively (EN written from scratch, not translated).
# Demo data is fictional sample data; it is embedded as JSON and run by /assets/products-demo.js.
import json
import urllib.parse
ADS = {}
ADS["en"] = dict(
 jump="ChatGPT Ads", eyebrow="NEW · CHATGPT ADS",
 h="ChatGPT Ads: be there when your customers ask",
 p=["Many people now ask ChatGPT directly when they want to solve a problem or find a service: <em>how do I…</em>, <em>why does…</em>, <em>what kind of… should I choose?</em> ChatGPT ads appear below the answer, labelled Sponsored, for people on the Free and Go plans, the largest group of ChatGPT users.",
    "Think of it as another place your customers are asking, beyond Google search. It sits alongside the channels you already use."],
 knowh="What to know before you start",
 know=["Self-serve ChatGPT Ads opened in Singapore and Malaysia on 23 September 2026.",
       "The advertising and billing company must be registered in Singapore or Malaysia. New accounts may start limited to their home country.",
       "Targeting is by conversation context. There are no keywords and no audience uploads.",
       "Ads are shown only to Free and Go users, and not on sensitive topics.",
       "We don't promise any budget level, ranking or result. Your ad budget is yours to set."],
 doh="What we do",
 do=["Account setup and verification help",
     "Landing page and tracking setup (OpenAI pixel)",
     "Ad copy and creative",
     "Campaign management",
     "Reporting: where we run paid ads for you, you get a daily ad performance report",
     "Hands-on implementation: Hunter works inside your business with you to get the tools and workflow running"],
 preph="What you need to prepare",
 prep=["A company registered in Singapore or Malaysia",
       "A website or landing page where a tracking tag can be installed",
       "What you sell, your prices, your target customers and areas",
       "A monthly ad budget and a company payment card",
       "Brand images and your logo"],
 intakeh="A few questions to start",
 intake=["Have you run Facebook or Google ads before? (yes or no, roughly how much per month, and results or screenshots if you have them)",
         "Where do your customers come from today?",
         "Do you have a website and a Facebook Page?"],
 cta="Send your answers on WhatsApp", note="Opens WhatsApp with these questions filled in. Nothing is sent until you press send.",
 fine="Scope and fees are agreed in a written quote before we start. Results are never guaranteed: how ads perform depends on your offer, your page and the market. We handle personal data in line with the personal data protection laws of Malaysia and Singapore (PDPA).",
 wamsg="Hi Hunter, I'd like to ask about ChatGPT ads.\n1) Have I run Facebook/Google ads before? (yes/no): __\nRough monthly budget: __\nResults or screenshots: __\n2) Where my customers come from now: __\n3) Website and Facebook Page? __",
)
ADS["zh"] = dict(
 jump="ChatGPT 广告", eyebrow="新服务 · CHATGPT 广告",
 h="ChatGPT 广告：客户提问的时候，你在场",
 p=["现在很多人遇到问题、想找服务，会直接问 ChatGPT：<em>我该怎么…</em>、<em>为什么…</em>、<em>该选哪一种…？</em>ChatGPT 广告出现在回答下方，标注 Sponsored，面向 Free 和 Go 用户，也就是 ChatGPT 最大的用户群。",
    "把它当成 Google 搜索之外，客户提问的另一个地方。它和你现在用的渠道并行，不是取代。"],
 knowh="开始之前先知道",
 know=["ChatGPT 广告自助投放已于 2026 年 9 月 23 日在新加坡和马来西亚开放。",
       "投放和付款的公司必须在新加坡或马来西亚注册。新账号可能一开始只能投放公司所在国。",
       "按对话语境定向，没有关键词，也不能上传受众名单。",
       "广告只显示给 Free 和 Go 用户，敏感话题不显示。",
       "我们不承诺任何预算额度、排名或结果。广告预算由你自己决定。"],
 doh="我们做什么",
 do=["开户与验证协助",
     "落地页与追踪设置（OpenAI pixel）",
     "广告文案与素材",
     "投放管理",
     "报告：若由我们代投广告，每天给你一份广告成效报告",
     "亲手落地：Hunter 和你一起进到你的生意里，把工具和流程跑起来"],
 preph="你需要准备",
 prep=["在新加坡或马来西亚注册的公司",
       "可以安装追踪代码的网站或落地页",
       "你卖什么、价格、目标客户和地区",
       "每月广告预算和公司付款卡",
       "品牌图片和 Logo"],
 intakeh="开始前的几个问题",
 intake=["你以前投过 Facebook 或 Google 广告吗？（有或没有、每月大概多少预算，有成果或截图的话一起发）",
         "你现在的客户从哪里来？",
         "你有网站和 Facebook 专页吗？"],
 cta="用 WhatsApp 发送你的回答", note="会打开 WhatsApp 并填好这些问题。你按发送之前，不会发出任何信息。",
 fine="服务范围和费用在开工前以书面报价确认。不保证任何结果：广告成效取决于你的产品、页面和市场。我们依照马来西亚与新加坡的个人资料保护法（PDPA）处理个人资料。",
 wamsg="你好 Hunter，我想了解 ChatGPT 广告。\n1）以前投过 Facebook/Google 广告吗（有/没有）：＿＿\n每月大概预算：＿＿\n成果或截图：＿＿\n2）现在客户从哪里来：＿＿\n3）有没有网站和 Facebook 专页：＿＿",
)
ADS["ms"] = dict(
 jump="Iklan ChatGPT", eyebrow="BARU · IKLAN CHATGPT",
 h="Iklan ChatGPT: hadir bila pelanggan anda bertanya",
 p=["Ramai orang kini terus bertanya ChatGPT bila nak selesaikan masalah atau cari servis: <em>macam mana nak…</em>, <em>kenapa…</em>, <em>jenis… yang mana patut saya pilih?</em> Iklan ChatGPT muncul di bawah jawapan, berlabel Sponsored, untuk pengguna pelan Free dan Go, kumpulan pengguna ChatGPT yang terbesar.",
    "Anggap ia satu lagi tempat pelanggan anda bertanya, selain carian Google. Ia berjalan bersama saluran yang anda sudah guna."],
 knowh="Perkara perlu tahu sebelum mula",
 know=["Iklan ChatGPT layan diri dibuka di Singapura dan Malaysia pada 23 September 2026.",
       "Syarikat pengiklanan dan pengebilan mesti berdaftar di Singapura atau Malaysia. Akaun baharu mungkin pada mulanya terhad kepada negara asal.",
       "Penyasaran mengikut konteks perbualan. Tiada kata kunci dan tiada muat naik audiens.",
       "Iklan hanya ditunjuk kepada pengguna Free dan Go, dan tidak untuk topik sensitif.",
       "Kami tidak menjanjikan sebarang tahap bajet, kedudukan atau hasil. Bajet iklan anda tentukan sendiri."],
 doh="Apa yang kami buat",
 do=["Bantuan penyediaan akaun dan pengesahan",
     "Persediaan halaman pendaratan dan penjejakan (piksel OpenAI)",
     "Teks iklan dan kreatif",
     "Pengurusan kempen",
     "Laporan: jika kami uruskan iklan berbayar anda, anda terima laporan prestasi iklan setiap hari",
     "Pelaksanaan secara langsung: Hunter bekerja bersama anda dalam perniagaan anda sehingga alat dan aliran kerja berjalan"],
 preph="Apa yang perlu anda sediakan",
 prep=["Syarikat berdaftar di Singapura atau Malaysia",
       "Laman web atau halaman pendaratan yang boleh dipasang kod penjejakan",
       "Apa yang anda jual, harga, pelanggan sasaran dan kawasan",
       "Bajet iklan bulanan dan kad pembayaran syarikat",
       "Imej jenama dan logo anda"],
 intakeh="Beberapa soalan untuk bermula",
 intake=["Pernahkah anda jalankan iklan Facebook atau Google? (ya atau tidak, anggaran bajet sebulan, dan hasil atau tangkapan skrin jika ada)",
         "Dari mana pelanggan anda datang sekarang?",
         "Adakah anda ada laman web dan Halaman Facebook?"],
 cta="Hantar jawapan anda di WhatsApp", note="Membuka WhatsApp dengan soalan ini sudah diisi. Tiada apa dihantar sehingga anda tekan hantar.",
 fine="Skop dan yuran dipersetujui dalam sebut harga bertulis sebelum mula. Hasil tidak dijamin: prestasi iklan bergantung pada tawaran, halaman dan pasaran anda. Kami mengendalikan data peribadi selaras dengan undang-undang perlindungan data peribadi Malaysia dan Singapura (PDPA).",
 wamsg="Hai Hunter, saya nak tanya tentang iklan ChatGPT.\n1) Pernah jalankan iklan Facebook/Google? (ya/tidak): __\nAnggaran bajet sebulan: __\nHasil atau tangkapan skrin: __\n2) Dari mana pelanggan saya datang sekarang: __\n3) Ada laman web dan Halaman Facebook? __",
)

EX = {'en': {'appr': 'You approve every ad before it is submitted.', 'tag': 'Example only', 'h': 'A simple example, step by step', 'intro': 'This is a made-up business, not a real client. It only shows how the pieces fit together. No results or numbers are promised.', 'biz': 'CoolBreeze Aircon (example)', 's1h': '1 · A customer asks ChatGPT', 'q': 'My aircon is leaking water at home. Should I get it serviced or replace it?', 'a': 'ChatGPT gives its usual answer: common causes, what to check, and when servicing is enough. (Shortened sample.)', 's2h': '2 · A Sponsored ad appears under the answer', 'sp': 'Sponsored', 'ah': 'Aircon leaking? Book a check', 'ad': 'Aircon servicing in Singapore. WhatsApp us for a quote.', 'al': 'coolbreeze.example', 's3h': '3 · The customer taps the ad', 's3': 'They land on a short page about aircon servicing, with a WhatsApp button to ask for a quote.', 's4h': '4 · Our services', 's4': ['Helped set up and verify the ad account', 'Set up the landing page and tracking (OpenAI pixel)', 'Wrote the ad copy and chose the image', 'You approved every ad before it was submitted', 'Ran the campaign and sent a daily ad report'], 's5h': '5 · Documents needed', 's5': ['A company registered in Singapore', 'The website, with a tracking tag installed', 'What they sell, prices and areas served', 'A monthly ad budget and a company card', 'Logo and photos']}, 'zh': {'appr': '每一条广告提交之前，都由你批准。', 'tag': '示例', 'h': '一个简单的例子，一步一步看', 'intro': '这是虚构的生意，不是真实客户，只用来说明各个环节怎么配合。不承诺任何结果或数字。', 'biz': 'CoolBreeze 冷气服务（示例）', 's1h': '1 · 客户问 ChatGPT', 'q': '我家冷气漏水，该找人保养还是直接换新的？', 'a': 'ChatGPT 照常给出回答：常见原因、该检查什么、什么时候保养就够了。（简短示意）', 's2h': '2 · 回答下方出现 Sponsored 广告', 'sp': 'Sponsored', 'ah': '冷气漏水？预约检查', 'ad': '新加坡冷气保养服务。WhatsApp 我们问报价。', 'al': 'coolbreeze.example', 's3h': '3 · 客户点进广告', 's3': '来到一个简短的冷气保养页面，页面上有 WhatsApp 按钮，可以直接问报价。', 's4h': '4 · 服务内容', 's4': ['协助开通并验证广告账号', '设置落地页和追踪（OpenAI pixel）', '写广告文案、选图片', '每一条广告提交前都由你批准', '管理投放，每天发一份广告报告'], 's5h': '5 · 所需文件', 's5': ['在新加坡注册的公司', '装好追踪代码的网站', '卖什么、价格和服务地区', '每月广告预算和公司付款卡', 'Logo 和照片']}, 'ms': {'appr': 'Anda luluskan setiap iklan sebelum ia dihantar.', 'tag': 'Contoh sahaja', 'h': 'Satu contoh mudah, langkah demi langkah', 'intro': 'Ini perniagaan rekaan, bukan pelanggan sebenar. Ia hanya menunjukkan bagaimana setiap bahagian bersambung. Tiada hasil atau angka dijanjikan.', 'biz': 'CoolBreeze Aircon (contoh)', 's1h': '1 · Pelanggan bertanya ChatGPT', 'q': 'Aircond rumah saya bocor air. Patut servis atau tukar baharu?', 'a': 'ChatGPT beri jawapan seperti biasa: punca biasa, apa perlu disemak, dan bila servis sudah cukup. (Contoh dipendekkan.)', 's2h': '2 · Iklan Sponsored muncul di bawah jawapan', 'sp': 'Sponsored', 'ah': 'Aircond bocor? Tempah semakan', 'ad': 'Servis aircond di Singapura. WhatsApp kami untuk sebut harga.', 'al': 'coolbreeze.example', 's3h': '3 · Pelanggan tekan iklan', 's3': 'Mereka sampai ke halaman ringkas tentang servis aircond, dengan butang WhatsApp untuk minta sebut harga.', 's4h': '4 · Perkhidmatan kami', 's4': ['Bantu sediakan dan sahkan akaun iklan', 'Sediakan halaman pendaratan dan penjejakan (piksel OpenAI)', 'Tulis teks iklan dan pilih imej', 'Anda luluskan setiap iklan sebelum ia dihantar', 'Uruskan kempen dan hantar laporan iklan harian'], 's5h': '5 · Dokumen diperlukan', 's5': ['Syarikat berdaftar di Singapura', 'Laman web dengan kod penjejakan dipasang', 'Apa dijual, harga dan kawasan perkhidmatan', 'Bajet iklan bulanan dan kad syarikat', 'Logo dan gambar']}}
for _k in ADS:
    ADS[_k]["ex"] = EX[_k]
    ADS[_k]["do"] = ADS[_k]["do"][:3] + [EX[_k]["appr"]] + ADS[_k]["do"][3:]
    ADS[_k]["fine"] = EX[_k]["appr"] + " " + ADS[_k]["fine"]

_I = lambda p: '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">%s</svg>' % p
ICON = {
 "cal": _I('<rect x="3.5" y="5" width="17" height="15" rx="2"/><path d="M8 3v4M16 3v4M3.5 10h17"/>'),
 "bld": _I('<path d="M4 21V6l8-3 8 3v15"/><path d="M9 21v-5h6v5M8.5 9.5h.01M12 9.5h.01M15.5 9.5h.01M8.5 13h.01M12 13h.01M15.5 13h.01"/>'),
 "tgt": _I('<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r=".8"/>'),
 "usr": _I('<circle cx="9" cy="8.5" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 5.5a3.2 3.2 0 0 1 0 6M18.5 14.2A6.5 6.5 0 0 1 21.5 20"/>'),
 "shd": _I('<path d="M12 3l8 3v6c0 4.5-3.3 8-8 9-4.7-1-8-4.5-8-9V6z"/><path d="M9 12l2.2 2.2L15.5 10"/>'),
}
ICON["glb"] = _I('<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.4 2.6 3.6 5.4 3.6 8.5s-1.2 5.9-3.6 8.5c-2.4-2.6-3.6-5.4-3.6-8.5s1.2-5.9 3.6-8.5z"/>')
ICON["srv"] = _I('<rect x="4" y="4.5" width="16" height="6" rx="1.5"/><rect x="4" y="13.5" width="16" height="6" rx="1.5"/><path d="M7.5 7.5h.01M7.5 16.5h.01"/><path d="M3 21L21 3"/>')
ICON["key"] = _I('<circle cx="8" cy="15" r="4"/><path d="M11 12l8.5-8.5M16 7l2.5 2.5M14 9l2 2"/>')
CHECK = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
KNOW_ICONS = ["cal", "bld", "tgt", "usr", "shd"]

# ---- ChatGPT Ads interactive widget (fictional sample data) ----
def _T(name, biz, url, items):
    return {"name": name, "biz": biz, "url": url, "qs": [{"q": q, "h": h, "d": d} for q, h, d in items]}
ADSW = {}
ADSW["en"] = dict(
 pick="Choose a business type", qh="A customer asks ChatGPT", ph="Sponsored ad draft", sp="Sponsored",
 ans="ChatGPT answers the question as usual. The ad appears below the answer. (Sample)",
 nexth="After the tap", nextt="The customer taps the ad and lands on your page or WhatsApp. We set up the page and tracking (OpenAI pixel), and you get a daily ad report where we run the ads for you.",
 step="Human approval", pending="Waiting for your approval. No ad is submitted until you approve.", approve="Approve & submit", change="Request changes",
 approved="Approved. (Demo only: no ad is actually submitted.)", changed="Sent back to the copywriter with your notes. A new draft will appear for approval.",
 types=[_T("Aircon servicing", "CoolBreeze Aircon (example)", "coolbreeze.example", [
   ("My aircon is leaking water at home. Should I get it serviced or replace it?", "Aircon leaking? Book a check", "Aircon servicing in Singapore. WhatsApp us for a quote."),
   ("How often should I service my aircon at home?", "Regular aircon servicing", "Book a servicing slot in Singapore. WhatsApp to ask."),
   ("Why is my aircon not cold anymore?", "Aircon not cold? Get it checked", "We check and service aircons in Singapore. Ask for a quote on WhatsApp.")]),
  _T("Beauty salon", "Glow Studio (example)", "glowstudio.example", [
   ("What facial is good for dry, tight skin?", "Hydrating facial, 60 minutes", "Book a slot at our Puchong studio. WhatsApp to ask."),
   ("How do I choose a salon for my first facial?", "First facial? Ask us first", "Tell us your skin concern on WhatsApp and we'll suggest a treatment."),
   ("How early should I do a facial before a wedding?", "Pre-wedding skin care", "Plan your treatments with us. WhatsApp for available slots.")]),
  _T("Tuition centre", "BrightPath Tuition (example)", "brightpath.example", [
   ("How do I help my child improve in Maths for PSLE?", "PSLE Maths small-group classes", "Small classes in Singapore. Book a trial lesson on WhatsApp."),
   ("What should I look for when choosing a tuition centre?", "Choosing a tuition centre?", "Try a trial lesson and see the class first. WhatsApp to book."),
   ("My child doesn't want to do homework. What can I do?", "Homework help for primary students", "Talk to our teachers on WhatsApp about what your child needs.")])])
ADSW["zh"] = dict(
 pick="选择生意类型", qh="客户问 ChatGPT", ph="Sponsored 广告草稿", sp="Sponsored",
 ans="ChatGPT 照常回答问题，广告出现在回答下方。（示意）",
 nexth="点击之后", nextt="客户点进广告，来到你的页面或 WhatsApp。我们设置页面和追踪（OpenAI pixel）；若由我们代投广告，每天给你一份广告报告。",
 step="人工批准", pending="等待你批准。批准前不会提交任何广告。", approve="批准并提交", change="要求修改",
 approved="已批准。（仅为演示，不会真的提交广告。）", changed="已连同你的意见退回给文案，新草稿会再送来给你批准。",
 types=[_T("冷气保养", "CoolBreeze 冷气服务（示例）", "coolbreeze.example", [
   ("我家冷气漏水，该找人保养还是直接换新的？", "冷气漏水？预约检查", "新加坡冷气保养服务。WhatsApp 我们问报价。"),
   ("家里的冷气多久该保养一次？", "定期冷气保养", "在新加坡预约保养时段。WhatsApp 询问。"),
   ("为什么我的冷气不冷了？", "冷气不冷？先检查", "新加坡冷气检查与保养。WhatsApp 问报价。")]),
  _T("美容院", "Glow Studio（示例）", "glowstudio.example", [
   ("皮肤干又紧绷，做哪种护理比较好？", "补水护理 60 分钟", "蒲种分店预约时段。WhatsApp 询问。"),
   ("第一次做脸，怎么挑美容院？", "第一次做脸？先问我们", "WhatsApp 告诉我们你的皮肤困扰，我们建议适合的护理。"),
   ("婚礼前多早开始做脸比较好？", "婚前肌肤护理", "和我们一起规划护理。WhatsApp 查询空档。")]),
  _T("补习中心", "BrightPath Tuition（示例）", "brightpath.example", [
   ("怎么帮孩子提升 PSLE 数学？", "PSLE 数学小班", "新加坡小班教学。WhatsApp 预约试听。"),
   ("挑补习中心要看什么？", "在挑补习中心？", "先试听，亲眼看看班级。WhatsApp 预约。"),
   ("孩子不想做功课，怎么办？", "小学生功课辅导", "WhatsApp 和老师聊聊孩子需要什么。")])])
ADSW["ms"] = dict(
 pick="Pilih jenis perniagaan", qh="Pelanggan bertanya ChatGPT", ph="Draf iklan Sponsored", sp="Sponsored",
 ans="ChatGPT menjawab soalan seperti biasa. Iklan muncul di bawah jawapan. (Contoh)",
 nexth="Selepas ditekan", nextt="Pelanggan tekan iklan dan sampai ke halaman atau WhatsApp anda. Kami sediakan halaman dan penjejakan (piksel OpenAI), dan jika kami uruskan iklan, anda terima laporan iklan harian.",
 step="Kelulusan manusia", pending="Menunggu kelulusan anda. Tiada iklan dihantar sehingga anda luluskan.", approve="Lulus & hantar", change="Minta pindaan",
 approved="Diluluskan. (Demo sahaja: tiada iklan benar-benar dihantar.)", changed="Dihantar semula kepada penulis bersama nota anda. Draf baharu akan muncul untuk kelulusan.",
 types=[_T("Servis aircond", "CoolBreeze Aircon (contoh)", "coolbreeze.example", [
   ("Aircond rumah saya bocor air. Patut servis atau tukar baharu?", "Aircond bocor? Tempah semakan", "Servis aircond di Singapura. WhatsApp kami untuk sebut harga."),
   ("Berapa kerap patut servis aircond di rumah?", "Servis aircond berkala", "Tempah slot servis di Singapura. WhatsApp untuk bertanya."),
   ("Kenapa aircond saya tak sejuk lagi?", "Aircond tak sejuk? Semak dahulu", "Semakan dan servis aircond di Singapura. WhatsApp untuk sebut harga.")]),
  _T("Salun kecantikan", "Glow Studio (contoh)", "glowstudio.example", [
   ("Rawatan muka apa yang sesuai untuk kulit kering dan tegang?", "Rawatan muka hidrasi 60 minit", "Slot di cawangan Puchong. WhatsApp untuk bertanya."),
   ("Macam mana nak pilih salun untuk rawatan muka pertama?", "Rawatan muka pertama? Tanya kami dahulu", "Beritahu masalah kulit anda di WhatsApp, kami cadangkan rawatan yang sesuai."),
   ("Berapa awal patut buat rawatan muka sebelum majlis kahwin?", "Penjagaan kulit pra-perkahwinan", "Rancang rawatan bersama kami. WhatsApp untuk slot kosong.")]),
  _T("Pusat tuisyen", "BrightPath Tuition (contoh)", "brightpath.example", [
   ("Macam mana nak bantu anak saya baiki Matematik PSLE?", "Kelas kecil Matematik PSLE", "Kelas kecil di Singapura. Tempah kelas percubaan di WhatsApp."),
   ("Apa yang perlu dilihat bila pilih pusat tuisyen?", "Sedang pilih pusat tuisyen?", "Cuba kelas percubaan dan lihat kelasnya dahulu. WhatsApp untuk tempah."),
   ("Anak saya tak mahu buat kerja rumah. Apa patut saya buat?", "Bantuan kerja rumah untuk murid sekolah rendah", "Bualkan dengan guru kami di WhatsApp tentang keperluan anak anda.")])])

def _ads(k, s):
    a = ADS[k]; e = a["ex"]
    link = "https://wa.me/60196273143?text=" + urllib.parse.quote(a["wamsg"], safe="")
    know = "".join('<li class="ad-know"><span class="ad-ico">%s</span><p>%s</p></li>' % (ICON[KNOW_ICONS[i]], x) for i, x in enumerate(a["know"]))
    chk = lambda xs: '<ul class="ad-checks">' + "".join("<li>%s<span>%s</span></li>" % (CHECK, x) for x in xs) + "</ul>"
    W = ADSW[k]; t0 = W["types"][0]
    fb = ('<div class="pd-ads-static"><div class="pd-grid"><div><h4>%s</h4><ol class="pd-cal pd-qs">%s</ol></div><div><h4>%s</h4>'
          '<div class="pd-adcard"><span class="pd-adsp">%s</span><span class="pd-adbiz">%s</span><strong>%s</strong><span>%s</span><span class="pd-adurl">%s</span></div>'
          '<div class="pd-card pd-approve"><h5>\U0001F464 %s</h5><p class="pd-approval">%s</p></div></div></div></div>') % (
        W["qh"], "".join('<li%s><span class="pd-q">%s</span></li>' % (' class="on"' if i == 0 else "", x["q"]) for i, x in enumerate(t0["qs"])),
        W["ph"], W["sp"], t0["biz"], t0["qs"][0]["h"], t0["qs"][0]["d"], t0["url"], W["step"], W["pending"])
    demo = _demo_shell(4, e["h"], e["intro"], s["badge"], '<div class="pd-ads" data-demo="ads">%s</div>' % fb)
    return ('<section class="wrap section pd-products pd-ads-sec" id="chatgpt-ads"><p class="eyebrow"><i></i>%s</p><h2>%s</h2><div class="pd-ads-lede">%s'
            '<p><a class="button whatsapp" href="%s" target="_blank" rel="noopener noreferrer">%s <span aria-hidden="true">↗</span></a></p></div>%s</section>\n'
            '<section class="paper ad-section"><div class="wrap section">'
            '<h3 class="ad-h3">%s</h3><ul class="ad-knows">%s</ul>'
            '<div class="ad-two"><div class="ad-panel"><h3>%s</h3>%s</div><div class="ad-panel"><h3>%s</h3>%s</div></div>'
            '<div class="ad-intake"><div><h3>%s</h3><ol>%s</ol></div><div class="ad-intake-cta"><a class="button whatsapp" href="%s" target="_blank" rel="noopener noreferrer">%s <span aria-hidden="true">↗</span></a><p>%s</p></div></div>'
            '<p class="ad-fine">%s</p></div></section>\n') % (
        a["eyebrow"], a["h"], "".join("<p>%s</p>" % x for x in a["p"]), link, a["cta"], demo,
        a["knowh"], know, a["doh"], chk(a["do"]), a["preph"], chk(a["prep"]),
        a["intakeh"], "".join("<li>%s</li>" % x for x in a["intake"]), link, a["cta"], a["note"], a["fine"])

# ---- Website building (two tiers). Copy written natively per language. Prices shown (Basic RM399 nett; SEO + AEO/GEO +RM994 nett one-time add-on, RM1,393 nett total); custom scope by written quote; no rankings promised. ----
WB = {}
WB["en"] = dict(
 geth="What you get",
 gets=["Hosted on Cloudflare's global network, so your site loads fast, with the HTTPS security padlock included.",
       "No server to rent. Each year, the main cost is just your domain fee.",
       "Your domain and website are in your name, so you're never locked in."],
 scope="Online shop payments, member logins, or a dashboard for editing your own content are quoted separately.",
 jump="Website building", eyebrow="NEW · WEBSITE BUILDING",
 h="Website building: easy for customers to find, clear for AI search to read",
 p=["When people hear about you, most of them look you up online first. We build a clean company website that works well on a phone and makes it easy to message you on WhatsApp.",
    "More people now also ask AI search tools like ChatGPT and Perplexity for advice and recommendations. Think of it as another place customers ask, beyond Google. Our SEO + AEO/GEO package sets your site up so Google and AI search can both read it clearly.",
    "hunterfoomedia.com, the site you're on now, is one we built ourselves."],
 t1tag="Package 1", t1h="Basic", t1sub="A company website that's ready to use",
 t1=["A company website with Home, About, Services and Contact pages",
     "A WhatsApp button on every page",
     "Mobile-friendly design",
     'One language included: English, <span lang="zh-Hans">中文</span> or BM',
     "Domain included, with HTTPS setup",
     "llms.txt: a plain-text summary of your business that AI tools can read"],
 t2tag="Package 2", t2h="SEO + AEO/GEO", t2sub="Everything in Basic, plus:",
 t2=["<b>SEO:</b> page titles and meta descriptions, a sitemap, submission to Google and Bing for indexing, and page speed work",
     "<b>AEO</b> (answer engine optimisation): clear Q&amp;A and FAQ content, so search engines can quote your answers directly",
     "<b>GEO</b> (generative engine optimisation): structured data (schema), an FAQ page and consistent company details, so AI search like ChatGPT and Perplexity can understand and cite your site",
     "An indexing check report",
     "llms.txt, written so AI tools can read your services and FAQ",
     "A one-time setup. Ongoing SEO maintenance is quoted separately if you need it."],
 feel="Fee: ", fee1="RM399 nett", fee2="+RM994 nett add-on (RM1,393 nett total)",
 cta="Ask about a website on WhatsApp",
 fine="Prices above cover the packages as listed. More languages, extra pages or other custom scope are confirmed by written quote. We don't promise rankings, or that Google or any AI tool will show or recommend your site. We tell you exactly what we build and set up; how search engines and AI tools rank and cite sites is up to them.",
 wamsg="Hi Hunter, I'd like to ask about a company website.\nMy business: __\nDo I have a website now? (yes/no, link): __\nBasic or SEO + AEO/GEO: __\nLanguages needed (EN / 中文 / BM): __",
 ld=("Website building", "Company websites for service businesses in Malaysia and Singapore. Basic: Home, About, Services and Contact pages, a WhatsApp button, mobile-friendly design, one language included (English, Chinese or Malay), domain included with HTTPS setup, and an llms.txt AI-readable summary. SEO + AEO/GEO (one-time setup): everything in Basic plus page titles and meta descriptions, a sitemap, submission to Google and Bing for indexing, page speed work, clear Q&A/FAQ content, structured data (schema), an FAQ page, consistent company details, an llms.txt file and an indexing check report. Prices: Basic RM399 nett; SEO + AEO/GEO is a +RM994 nett add-on (RM1,393 nett total). Ongoing maintenance and custom scope (more languages, extra pages) are confirmed by written quote. No rankings are promised."),
)
WB["zh"] = dict(
 geth="你得到什么",
 gets=["放在 Cloudflare 全球服务器，速度快，自带 HTTPS 安全锁。",
       "不用租服务器，每年主要只付域名费。",
       "域名和网站都在你名下，不会被绑住。"],
 scope="网店付款、会员登录、自己改内容的后台，另外报价。",
 jump="网站建设", eyebrow="新服务 · 网站建设",
 h="网站建设：客户找得到，AI 搜索也读得懂",
 p=["客户听说你之后，多数会先上网查一查。我们帮你做一个清楚的公司网站，手机上好看好用，一按就能 WhatsApp 你。",
    "现在也有越来越多人会问 ChatGPT、Perplexity 这类 AI 搜索，请它们给建议、推荐。把它当成 Google 之外，客户提问的另一个地方。「SEO + AEO/GEO」方案会把网站整理好，让 Google 和 AI 搜索都能清楚读懂。",
    "你现在看的 hunterfoomedia.com，就是我们自己做的。"],
 t1tag="方案一", t1h="基础版", t1sub="一个马上能用的公司网站",
 t1=["公司网站：首页、关于我们、服务、联系我们",
     "每一页都有 WhatsApp 按钮",
     "手机友好的设计",
     "含 1 种语言：EN、中文或 BM 任选",
     "含域名，并设置好 HTTPS",
     "llms.txt：一份 AI 工具读得懂的网站简介"],
 t2tag="方案二", t2h="SEO + AEO/GEO", t2sub="包含基础版全部内容，另加：",
 t2=["<b>SEO：</b>每页标题与 meta 描述、网站地图（sitemap）、提交 Google 与 Bing 收录、网页速度优化",
     "<b>AEO</b>（答案引擎优化）：写清楚的问答 / FAQ 内容，方便搜索引擎直接引用你的答案",
     "<b>GEO</b>（生成式引擎优化）：结构化数据（schema）、FAQ 页面、全站一致的公司资料，让 ChatGPT、Perplexity 等 AI 搜索更容易读懂并引用你的网站",
     "收录检查报告",
     "llms.txt：把你的服务和 FAQ 写成 AI 工具读得懂的格式",
     "一次性设置；之后如需维护，另外报价"],
 feel="费用：", fee1="RM399（净价）", fee2="基础版另加 RM994（净价），合共 RM1,393（净价）",
 cta="用 WhatsApp 问网站建设",
 fine="以上价格按所列内容计算。加语言、加页面或其他特别需求，以书面报价确认。我们不承诺排名，也不承诺 Google 或任何 AI 工具会显示或推荐你的网站。我们只把做什么、设置什么写清楚；搜索引擎和 AI 工具怎么排序、引用，由它们决定。",
 wamsg="你好 Hunter，我想了解公司网站。\n我做的是：＿＿\n现在有没有网站（有/没有，链接）：＿＿\n基础版还是 SEO + AEO/GEO：＿＿\n需要哪些语言（EN / 中文 / BM）：＿＿",
 ld=("网站建设", "为马来西亚与新加坡的服务型生意建公司网站。基础版：首页、关于我们、服务、联系我们，WhatsApp 按钮，手机友好设计，含 1 种语言（EN、中文或 BM），含域名并设置 HTTPS，另附 llms.txt AI 可读网站简介。SEO + AEO/GEO（一次性设置）：包含基础版全部内容，另加每页标题与 meta 描述、网站地图、提交 Google 与 Bing 收录、网页速度优化、清楚的问答 / FAQ 内容、结构化数据（schema）、FAQ 页面、全站一致的公司资料、llms.txt，以及收录检查报告。价格：基础版 RM399（净价）；SEO + AEO/GEO 在基础版上另加 RM994（净价），合共 RM1,393（净价）。之后的维护及特别需求（加语言、加页面）以书面报价确认。不承诺排名。"),
)
WB["ms"] = dict(
 geth="Apa yang anda dapat",
 gets=["Dihoskan di rangkaian global Cloudflare, jadi laman anda dibuka dengan pantas, siap dengan ikon mangga keselamatan HTTPS.",
       "Tak perlu sewa server. Setiap tahun, kos utama hanyalah yuran domain.",
       "Domain dan laman web didaftarkan atas nama anda, jadi anda tidak terikat."],
 scope="Pembayaran kedai dalam talian, log masuk ahli, atau papan pemuka untuk anda ubah kandungan sendiri disebut harga secara berasingan.",
 jump="Pembinaan laman web", eyebrow="BARU · PEMBINAAN LAMAN WEB",
 h="Pembinaan laman web: mudah dicari pelanggan, jelas dibaca carian AI",
 p=["Bila orang dengar tentang anda, kebanyakannya akan semak dalam talian dahulu. Kami bina laman web syarikat yang kemas, selesa dibuka di telefon dan memudahkan pelanggan WhatsApp anda.",
    "Semakin ramai juga bertanya kepada carian AI seperti ChatGPT dan Perplexity untuk nasihat dan cadangan. Anggap ia satu lagi tempat pelanggan bertanya, selain Google. Pakej SEO + AEO/GEO kami menyusun laman anda supaya Google dan carian AI sama-sama boleh membacanya dengan jelas.",
    "hunterfoomedia.com, laman yang anda sedang lihat ini, kami bina sendiri."],
 t1tag="Pakej 1", t1h="Asas", t1sub="Laman web syarikat yang sedia digunakan",
 t1=["Laman web syarikat dengan halaman Utama, Tentang Kami, Perkhidmatan dan Hubungi",
     "Butang WhatsApp di setiap halaman",
     "Reka bentuk mesra telefon",
     'Satu bahasa termasuk: EN, <span lang="zh-Hans">中文</span> atau BM',
     "Domain termasuk, dengan persediaan HTTPS",
     "llms.txt: ringkasan perniagaan anda dalam teks biasa yang boleh dibaca alat AI"],
 t2tag="Pakej 2", t2h="SEO + AEO/GEO", t2sub="Semua dalam pakej Asas, serta:",
 t2=["<b>SEO:</b> tajuk halaman dan meta description, sitemap, penghantaran kepada Google dan Bing untuk pengindeksan, dan penambahbaikan kelajuan halaman",
     "<b>AEO</b> (pengoptimuman enjin jawapan): kandungan soal jawab dan FAQ yang jelas, supaya enjin carian boleh memetik jawapan anda secara terus",
     "<b>GEO</b> (pengoptimuman enjin generatif): data berstruktur (schema), halaman FAQ dan maklumat syarikat yang konsisten, supaya carian AI seperti ChatGPT dan Perplexity mudah memahami dan memetik laman anda",
     "Laporan semakan pengindeksan",
     "llms.txt, ditulis supaya alat AI boleh membaca servis dan FAQ anda",
     "Persediaan sekali sahaja. Penyelenggaraan SEO berterusan disebut harga secara berasingan jika diperlukan."],
 feel="Yuran: ", fee1="RM399 nett", fee2="Tambahan RM994 nett (jumlah RM1,393 nett)",
 cta="Tanya tentang laman web di WhatsApp",
 fine="Harga di atas meliputi pakej seperti yang disenaraikan. Bahasa tambahan, halaman tambahan atau skop khas lain disahkan melalui sebut harga bertulis. Kami tidak menjanjikan kedudukan carian, atau bahawa Google atau mana-mana alat AI akan memaparkan atau mengesyorkan laman anda. Kami nyatakan dengan jelas apa yang kami bina dan sediakan; cara enjin carian dan alat AI menyusun dan memetik laman ditentukan oleh mereka.",
 wamsg="Hai Hunter, saya nak tanya tentang laman web syarikat.\nBisnes saya: __\nAda laman web sekarang? (ya/tidak, pautan): __\nAsas atau SEO + AEO/GEO: __\nBahasa diperlukan (EN / 中文 / BM): __",
 ld=("Pembinaan laman web", "Laman web syarikat untuk perniagaan perkhidmatan di Malaysia dan Singapura. Asas: halaman Utama, Tentang Kami, Perkhidmatan dan Hubungi, butang WhatsApp, reka bentuk mesra telefon, satu bahasa termasuk (EN, Cina atau BM), domain termasuk dengan persediaan HTTPS, serta ringkasan llms.txt yang boleh dibaca AI. SEO + AEO/GEO (persediaan sekali sahaja): semua dalam pakej Asas serta tajuk halaman dan meta description, sitemap, penghantaran kepada Google dan Bing untuk pengindeksan, kelajuan halaman, kandungan soal jawab / FAQ yang jelas, data berstruktur (schema), halaman FAQ, maklumat syarikat yang konsisten, fail llms.txt dan laporan semakan pengindeksan. Harga: Asas RM399 nett; SEO + AEO/GEO ialah tambahan RM994 nett (jumlah RM1,393 nett). Penyelenggaraan berterusan dan skop khas (bahasa atau halaman tambahan) disahkan melalui sebut harga bertulis. Kedudukan carian tidak dijanjikan."),
)

def _wb(k):
    w = WB[k]
    link = "https://wa.me/60196273143?text=" + urllib.parse.quote(w["wamsg"], safe="")
    chk = lambda xs: '<ul class="ad-checks">' + "".join("<li>%s<span>%s</span></li>" % (CHECK, x) for x in xs) + "</ul>"
    panel = lambda tag, h, sub, xs, cls, fee: ('<div class="ad-panel wb-tier%s"><p class="wb-tag">%s</p><h3>%s</h3><p class="wb-sub">%s</p>%s'
                                               '<p class="wb-fee">%s<b>%s</b></p></div>') % (cls, tag, h, sub, chk(xs), w["feel"], fee)
    return ('<section class="wrap section pd-products pd-ads-sec wb-sec" id="website-building"><p class="eyebrow"><i></i>%s</p><h2>%s</h2><div class="pd-ads-lede">%s'
            '<p><a class="button whatsapp" href="%s" target="_blank" rel="noopener noreferrer">%s <span aria-hidden="true">↗</span></a></p></div></section>\n'
            '<section class="paper ad-section wb-section"><div class="wrap section">'
            '<h3 class="ad-h3">%s</h3><ul class="wb-gets">%s</ul>'
            '<div class="ad-two wb-two">%s%s</div>'
            '<p class="wb-scope">%s</p>'
            '<p class="ad-fine">%s</p></div></section>\n') % (
        w["eyebrow"], w["h"], "".join("<p>%s</p>" % x for x in w["p"]), link, w["cta"],
        w["geth"], "".join('<li class="ad-know"><span class="ad-ico">%s</span><p>%s</p></li>' % (ICON[i], x) for i, x in zip(["glb", "srv", "key"], w["gets"])),
        panel(w["t1tag"], w["t1h"], w["t1sub"], w["t1"], "", w["fee1"]), panel(w["t2tag"], w["t2h"], w["t2sub"], w["t2"], " wb-plus", w["fee2"]),
        w["scope"], w["fine"])

# ---- FAQ (visible <details> list + FAQPage JSON-LD). Answers only restate what this page already says. ----
FAQ = {}
FAQ["en"] = dict(jump="FAQ", kicker="FAQ", h="Common questions", qa=[
 ("What is a ChatGPT ad, and who sees it?",
  "When someone asks ChatGPT a question, a short ad can appear below the answer, labelled Sponsored. It's matched to what the conversation is about, not to keywords. Ads are shown to people on the Free and Go plans, the largest group of ChatGPT users, so this is where an ad reaches the most people. They don't appear on sensitive topics. The example and demo above show what one can look like."),
 ("How much does it cost?",
  "Scope and fees are agreed in a <b>written quote</b> before we start, for ChatGPT Ads and for the digital employees on this page. Your ad budget is separate: you decide how much to spend, and it's paid with your company card."),
 ("How soon will I see results?",
  "We don't promise a timeline or a result. How ads perform depends on your offer, your page and the market. Where we run the ads for you, you get a daily ad performance report, so you always know how they're doing."),
 ("Do I get to approve the ads?",
  "Yes. We write the ad copy and prepare the creative, but <b>every ad is submitted only after you approve it</b>. If something isn't right, ask for changes and we'll send a new draft for your approval."),
 ("Do I still need Google ads?",
  "ChatGPT ads don't replace Google. Think of ChatGPT as another place your customers ask, beyond Google search. It runs alongside the channels you already use, so if Google ads bring you customers, keep them going."),
 ("How do you handle my data? What about PDPA?",
  "We handle personal data in line with the personal data protection laws of Malaysia and Singapore (PDPA). Your accounts, your data and your customers stay yours: data stays in your own accounts, and we only get the access we need to set up and run the work. The demos on this page use made-up sample data only."),
])
FAQ["zh"] = dict(jump="常见问题", kicker="常见问题", h="你可能想问的", qa=[
 ("什么是 ChatGPT 广告？谁会看到？",
  "有人在 ChatGPT 提问时，回答下方可能出现一则简短的广告，标注 Sponsored。广告按对话内容配对，不是按关键词。广告面向 Free 和 Go 用户，也就是 ChatGPT 最大的用户群，能接触到最多的人。敏感话题不会显示广告。上面的例子和演示，就是广告大概的样子。"),
 ("要多少钱？",
  "服务范围和费用，在开工前以<b>书面报价</b>确认，ChatGPT 广告和本页的数字员工都一样。广告预算另外算：投多少由你自己决定，用你的公司付款卡支付。"),
 ("多久看得到效果？",
  "我们不承诺时间，也不承诺结果。广告成效取决于你的产品、页面和市场。若由我们代投广告，每天给你一份广告成效报告，你随时知道广告跑得怎样。"),
 ("广告要经过我批准吗？",
  "要。广告文案和素材由我们准备，但<b>每一条广告都要你批准之后才提交</b>。哪里不满意就提出修改，我们改好新草稿再给你批准。"),
 ("还需要做 Google 广告吗？",
  "ChatGPT 广告不是取代 Google。把它当成 Google 搜索之外，客户提问的另一个地方。它和你现在用的渠道并行；Google 广告有带来客户，就继续做。"),
 ("你们怎么处理我的资料？有遵守 PDPA 吗？",
  "我们依照马来西亚与新加坡的个人资料保护法（PDPA）处理个人资料。账号、数据、客户都是你的：数据保存在你自己的账号里，我们只取得开设和运行所需的权限。本页演示只使用虚构的示例数据。"),
])
FAQ["ms"] = dict(jump="Soalan lazim", kicker="Soalan lazim", h="Soalan yang mungkin anda ada", qa=[
 ("Apa itu iklan ChatGPT, dan siapa yang nampak?",
  "Bila seseorang bertanya kepada ChatGPT, iklan ringkas boleh muncul di bawah jawapan, berlabel Sponsored. Iklan dipadankan dengan topik perbualan, bukan kata kunci. Iklan ditunjuk kepada pengguna pelan Free dan Go, kumpulan pengguna ChatGPT yang terbesar, jadi di sinilah iklan anda sampai kepada paling ramai orang. Iklan tidak muncul untuk topik sensitif. Contoh dan demo di atas menunjukkan rupa iklan tersebut."),
 ("Berapa kosnya?",
  "Skop dan yuran dipersetujui dalam <b>sebut harga bertulis</b> sebelum kami mula, sama ada untuk Iklan ChatGPT atau pekerja digital di halaman ini. Bajet iklan adalah berasingan: anda sendiri tentukan berapa nak belanja, dan ia dibayar dengan kad syarikat anda."),
 ("Bila saya boleh nampak hasil?",
  "Kami tidak menjanjikan tempoh atau hasil. Prestasi iklan bergantung pada tawaran, halaman dan pasaran anda. Jika kami uruskan iklan anda, anda terima laporan prestasi iklan setiap hari, jadi anda sentiasa tahu perkembangannya."),
 ("Adakah saya perlu luluskan iklan?",
  "Ya. Kami tulis teks iklan dan sediakan kreatif, tetapi <b>setiap iklan hanya dihantar selepas anda meluluskannya</b>. Kalau ada yang tak kena, minta pindaan dan kami hantar draf baharu untuk kelulusan anda."),
 ("Perlukah saya teruskan iklan Google?",
  "Iklan ChatGPT bukan pengganti Google. Anggap ChatGPT satu lagi tempat pelanggan anda bertanya, selain carian Google. Ia berjalan bersama saluran yang anda sudah guna, jadi jika iklan Google membawa pelanggan, teruskan."),
 ("Bagaimana data saya dikendalikan? Bagaimana dengan PDPA?",
  "Kami mengendalikan data peribadi selaras dengan undang-undang perlindungan data peribadi Malaysia dan Singapura (PDPA). Akaun, data dan pelanggan kekal milik anda: data disimpan dalam akaun anda sendiri, dan kami hanya diberi akses yang perlu untuk menyediakan dan menjalankan kerja. Demo di halaman ini hanya guna data contoh rekaan."),
])

import re as _re
def _plain(h):
    return _re.sub(r"<[^>]+>", "", h)

def _faq(k):
    f = FAQ[k]
    items = "".join('<details%s><summary>%s</summary><p>%s</p></details>' % (' open' if i == 0 else '', q, a) for i, (q, a) in enumerate(f["qa"]))
    return ('<section class="paper pd-faq-wrap" id="faq" aria-labelledby="pd-faq-h"><div class="wrap section"><div class="pd-faq">'
            '<p class="pd-kicker">%s</p><h2 id="pd-faq-h">%s</h2>%s</div></div></section>\n') % (f["kicker"], f["h"], items)

# ---------- shared demo structure (language-neutral) ----------
POSITIONS = ["warehouse", "operator", "cs", "tech"]
TAGS = ["exp2", "shift", "forklift", "english", "mandarin", "immediate", "passport", "transport"]
JOBS = [
    {"code": "YU-01", "pos": "warehouse", "area": "woodlands", "pay": "S$2,300–2,600", "hard": ["passport"], "cond": ["exp2", "shift", "forklift", "immediate"]},
    {"code": "YU-02", "pos": "warehouse", "area": "jurong", "pay": "S$2,200–2,500", "hard": ["passport", "forklift"], "cond": ["exp2", "english", "immediate"]},
    {"code": "YU-03", "pos": "operator", "area": "woodlands", "pay": "S$2,000–2,400", "hard": ["passport", "shift"], "cond": ["exp2", "immediate", "transport"]},
    {"code": "YU-04", "pos": "operator", "area": "tuas", "pay": "S$2,100–2,500", "hard": ["passport"], "cond": ["shift", "english", "transport", "exp2"]},
    {"code": "YU-05", "pos": "cs", "area": "changi", "pay": "S$2,500–2,900", "hard": ["passport", "english"], "cond": ["mandarin", "exp2", "shift"]},
    {"code": "YU-06", "pos": "tech", "area": "jurong", "pay": "S$2,800–3,400", "hard": ["passport", "exp2"], "cond": ["english", "shift", "transport"]},
]
PRESETS = [
    {"name": "Aiman (sample)", "pos": "warehouse", "area": "woodlands", "years": 3, "tags": ["shift", "forklift", "passport", "immediate"]},
    {"name": "Mei Ling (sample)", "pos": "cs", "area": "changi", "years": 1, "tags": ["english", "mandarin", "passport", "immediate"]},
    {"name": "Ravi (sample)", "pos": "operator", "area": "tuas", "years": 4, "tags": ["english", "transport"]},
]
AREAS = ["woodlands", "jurong", "tuas", "changi"]

# ---------- per-language strings ----------
S = {}
S["en"] = dict(
 title="Products & live demos | HF Media Solution (IP0633909-U)",
 desc="See what HF Media Solution builds: AI digital employees for recruitment, WhatsApp and content, ChatGPT Ads setup, and company websites with SEO and AEO/GEO. Try the demos with sample data.",
 eyebrow="PRODUCTS", h1="Digital employees you can actually see.",
 lede="HF Media Solution builds and runs AI “digital employees” for service businesses in Malaysia and Singapore. They're automation systems that do the repetitive work: sorting candidates, answering WhatsApp enquiries, preparing social posts. A person stays in charge of every decision that matters.",
 introh="What we do, in plain terms",
 intro=["We work with small service businesses: recruitment agencies, clinics and beauty salons, property agents, tuition centres, and other owner-run teams that live on WhatsApp and Facebook.",
        "Everything is delivered online. We map how you work over video call and WhatsApp, cut the steps that don't need to exist, then build the system on tools you already use, like WhatsApp, Google Sheets and Facebook. We're based in Kuala Lumpur and work mostly online, with nothing to install on site.",
        "<strong>In daily use:</strong> these systems run every day for our client Sky Employment Pte Ltd, a licensed Singapore employment agency. See the case study below."],
 engh="How an engagement works",
 eng=[("1 · Setup", "A one-off project. We map your process, build the system, test it with you and train your team. Scope and fees are agreed in a written quote before we start."),
      ("2 · Monthly operation", "An optional monthly fee. We keep the system running, adjust rules and message templates, and fix anything that breaks. Where we run paid ads for you, you get a daily ad performance report."),
      ("3 · You stay in control", "Your accounts, your data, your customers. You approve every outbound message template and every post before it goes live.")],
 prodh="Three products. Try each one.",
 prodsub="Every demo below runs entirely in your browser with made-up sample data. Nothing is sent anywhere.",
 badge="Demo with sample data",
 p1h="AI Recruitment Matching System",
 p1d="A candidate fills in a short form. The system turns it into a clean, structured profile and checks it against open job orders using clear rules: the desired position must match, every hard requirement must be met, and at least half of the other conditions. Recruiters get a ranked shortlist with the reasons spelled out.",
 p2h="WhatsApp Digital Employee",
 p2d="Answers job seekers on WhatsApp the way your best coordinator would: job details for the area they asked about only, one link per message, an invitation to the application form, and a polite close. Every chat is tagged automatically so your team knows who to follow up.",
 p3h="Content Automation",
 p3d="Plans a week of posts for your business and drafts versions for each of your Facebook pages. Nothing is published until a human on your team approves it.",
 rec=dict(form="Candidate form", preset="Load a sample candidate", name="Name", pos="Desired position", area="Preferred area", years="Years of relevant experience", tagsl="Tick what applies", run="Generate profile & match", summary="Structured profile", shortlist="Shortlist", none="No job order passed all three rules. The system would save this profile and alert the candidate when a matching job opens.",
          rules="Rules: position must match · all hard requirements · at least 50% of conditions", reasons="Why", notmatched="Not shortlisted", hardmiss="Missing hard requirement", posmiss="Different position", condlow="Conditions met", jobs="Sample job orders", yrs="{n} yrs experience", areapref="Prefers {a}", ok="Shortlisted", namedef="Sample candidate", hard="Hard", cond="Conditions",
          pos_labels={"warehouse": "Warehouse assistant", "operator": "Production operator", "cs": "Customer service officer", "tech": "Maintenance technician"},
          tag_labels={"exp2": "2+ years' experience", "shift": "OK with rotating shifts", "forklift": "Forklift licence", "english": "Conversational English", "mandarin": "Conversational Mandarin", "immediate": "Can start within 2 weeks", "passport": "Valid passport", "transport": "Own transport"},
          area_labels={"woodlands": "Woodlands", "jurong": "Jurong", "tuas": "Tuas", "changi": "Changi"}),
 wa=dict(slabel="sample link", pick="Pick an inbound message", reset="Reset chat", contact="Sample contact", panel="Auto-applied", tagsl="Tags", statusl="Follow-up status", rulesl="Rules applied", online="online · demo", start="Choose a message on the left to see how the digital employee replies.", form="https://forms.example.com/apply-sample", sl="SL",
         msgs=[
          dict(label="“I want to apply for the YU-01 job”", user="Hi, I want to apply for the YU-01 job", bot=["Hi! Thanks for your interest 😊 YU-01 is a warehouse assistant role in <b>Woodlands</b>. Pay S$2,300–2,600, rotating shifts, transport from the Causeway provided.", "To apply, please fill in this short form (2 minutes): https://forms.example.com/apply-sample"], tags=["Applicant", "YU-01", "Woodlands"], status="Form sent · reminder in 24h if not completed", rules=["Job details for the area asked only", "One link per message", "Form invitation"]),
          dict(label="“Any jobs in Jurong?”", user="Any jobs in Jurong?", bot=["Yes, two openings in <b>Jurong</b> right now:\n• YU-02 Warehouse assistant (forklift licence needed)\n• YU-06 Maintenance technician", "Tell me which one interests you and I'll send the details. Or fill in the form and we'll match you: https://forms.example.com/apply-sample"], tags=["Enquiry", "Jurong"], status="Awaiting reply · follow up tomorrow 10am", rules=["Only Jurong jobs shown", "One link per message"]),
          dict(label="📄 Sends a resume", user="📄 Resume_sample.pdf", bot=["Got your resume, thank you! A recruiter will review it within 1 working day.", "To make sure we match you correctly, please also complete this form: https://forms.example.com/apply-sample"], tags=["Resume received"], status="Recruiter review · due in 1 working day", rules=["Acknowledge attachment", "One link per message", "Form invitation"]),
          dict(label="“I already found a job”", user="Thanks, but I already found a job", bot=["Congratulations, that's great news! 🎉 I'll stop sending you job updates. If you ever want to look again, just message us here. All the best!"], tags=["Found job", "Do not follow up"], status="Closed · no further messages", rules=["Polite close", "Tag and stop follow-up"])]),
 ct=dict(pick="Choose a business type", cal="This week's plan", post="Draft post, adapted per Facebook page", approve="Approve & schedule", change="Request changes", pending="Waiting for your approval. Nothing is posted until you approve.", approved="Approved. Scheduled for {t}. (Demo only: nothing is actually posted.)", changed="Sent back to the writer with your notes. A new draft will appear for approval.", step="Human approval",
         types=[
          dict(name="Beauty salon", when="Tue 8:00 PM", week=[["Mon", "Before & after: hydrating facial"], ["Tue", "Tip: 3 things to avoid after a peel"], ["Wed", "Meet the team: senior therapist"], ["Thu", "Client question answered"], ["Fri", "Weekend slots now open"], ["Sat", "Short video: treatment room tour"], ["Sun", "Rest day: no post"]],
               pages=[["Main page", "Dry, tight skin after a long day in air-con? 🌿 Our hydrating facial takes 60 minutes and you'll feel the difference the same evening. Weekday slots are open. WhatsApp us to book."], ["Branch page (sample: Puchong)", "Puchong friends 👋 Hydrating facial slots are open at our Puchong branch this week. Free parking downstairs. Message us to grab a time."], ["Founder page", "One thing I tell every client: air-con dries your skin faster than the sun. That's why the hydrating facial is our most-booked treatment this month."]]),
          dict(name="Property agent", when="Wed 9:00 PM", week=[["Mon", "New listing: 3-bed condo (sample)"], ["Tue", "Explainer: stamp duty in 60 seconds"], ["Wed", "Area guide: what's near the MRT"], ["Thu", "Buyer FAQ: loan pre-approval"], ["Fri", "Weekend viewing slots"], ["Sat", "Short video: unit walkthrough"], ["Sun", "Rest day: no post"]],
               pages=[["Agent page", "First home? Get your loan pre-approved before you start viewing. You'll know your real budget and sellers take you seriously. Questions? WhatsApp me."], ["Listings page", "Sample listing: 3-bed condo, 5 minutes' walk to the MRT. Viewing slots this weekend. Message for details."], ["Team page", "This week the team answered the most common buyer question: how long does loan approval take? Short answer: usually 1–2 weeks with complete documents."]]),
          dict(name="Tuition centre", when="Thu 7:30 PM", week=[["Mon", "Exam tip: managing time in Paper 2"], ["Tue", "Student win (anonymised)"], ["Wed", "Parent FAQ: class sizes"], ["Thu", "Trial class invitation"], ["Fri", "Weekend revision timetable"], ["Sat", "Short video: how a lesson runs"], ["Sun", "Rest day: no post"]],
               pages=[["Centre page", "Running out of time in Paper 2? Try this: spend the first 5 minutes reading every question and marking the ones you'll do first. Our tutors drill this every week."], ["Parents page", "Parents often ask how big our classes are. The answer is at most 8 students, so every child gets checked work every lesson. Trial classes are open this month."], ["Tutor page", "A small habit that changes results: finish homework the same day as class. Memory is freshest then. I remind my students every week."]])]),
 howh="How we work",
 how=[("Map", "A video call to see how you work today and where the hours go."), ("Cut, then simplify", "We remove steps that shouldn't exist before automating anything."), ("Build & test", "We build on your existing tools and test with real scenarios, with you watching."), ("Run & improve", "Monthly operation: we monitor, adjust rules and report back.")],
 privh="Data & privacy",
 priv=["The demos on this page use made-up sample data only. No real candidate or customer data is shown or collected.",
       "In client systems, data stays in the client's own accounts (for example their Google Sheets and WhatsApp Business). We only get the access needed to build and maintain the system.",
       "Clients approve every outbound message template and every social post before it goes live. The system doesn't invent offers or reply outside the rules you set.",
       "We handle personal data in line with Malaysia and Singapore personal data protection laws (PDPA)."],
 ctaey="NEXT STEP", ctah="Want to see it with your own workflow?", wamsg="Hi Hunter, I saw the product demos on your website. I'd like a 20-minute call. My business: ____",
 reg="HF Media Solution · Business registration no. IP0633909-U (Malaysia) · Trading as Hunter Foo Media · Remote service across Malaysia and Singapore",
)

S["zh"] = dict(
 title="产品与在线演示｜HF Media Solution (IP0633909-U)",
 desc="看清楚 HF Media Solution 做什么：招聘匹配、WhatsApp 跟进、内容自动化三款 AI 数字员工，另有 ChatGPT 广告与网站建设（SEO + AEO/GEO），附示例数据在线演示。",
 eyebrow="产品", h1="看得见的数字员工。",
 lede="HF Media Solution 为马来西亚与新加坡的服务型生意，搭建并运营 AI「数字员工」：也就是帮你做重复工作的自动化系统，比如筛选候选人、回复 WhatsApp 询问、准备社媒贴文。重要的决定，始终由人来做。",
 introh="我们具体做什么",
 intro=["我们的客户是小型服务型生意：招聘中介、诊所和美容院、房产经纪、补习中心，以及每天靠 WhatsApp 和 Facebook 接客户的老板型团队。",
        "全部线上交付。我们通过视频会议和 WhatsApp 了解你怎么做事，先删掉不必要的步骤，再用你现有的工具（WhatsApp、Google 表格、Facebook）搭系统。我们位于吉隆坡，大部分工作在线上完成，不需要上门安装。",
        "<strong>每天在用：</strong>这些系统每天都在为我们的客户 Sky Employment Pte Ltd（新加坡持牌职业中介）运行。详见下方案例。"],
 engh="合作怎么进行",
 eng=[("1 · 搭建", "一次性项目。梳理流程、搭系统、和你一起测试、培训团队。服务范围和费用在开工前以书面报价确认。"),
      ("2 · 每月运营", "可选月费。我们维护系统运行、调整规则和话术模板、修复问题。若由我们代投广告，每天给你一份广告成效报告。"),
      ("3 · 主控权在你", "账号、数据、客户都是你的。每一条对外信息模板、每一篇贴文，都要你批准才上线。")],
 prodh="三款产品，每款都能试。",
 prodsub="下面的演示全部在你的浏览器里运行，使用虚构的示例数据，不会发送任何资料。",
 badge="示例数据演示",
 p1h="AI 招聘匹配系统",
 p1d="候选人填一份简短表格，系统整理成结构化简历摘要，再按清楚的规则对照职位单：期望职位必须一致、硬性条件全部符合、其他条件至少符合一半。招聘顾问拿到一份附理由的候选名单。",
 p2h="WhatsApp 数字员工",
 p2d="像你最得力的助理一样回复求职者：只讲对方问的那个地区的职位、每条信息只放一个链接、邀请填写申请表、礼貌收尾。每个对话自动贴标签，团队一眼知道该跟进谁。",
 p3h="内容自动化",
 p3d="为你的生意规划一周贴文，并为每个 Facebook 专页写好不同版本。团队里的人批准之前，什么都不会发出去。",
 rec=dict(form="候选人表格", preset="载入示例候选人", name="姓名", pos="期望职位", area="希望工作地区", years="相关经验年数", tagsl="勾选符合的项目", run="生成摘要并匹配", summary="结构化简历摘要", shortlist="候选名单", none="没有职位单同时通过三条规则。系统会保存这份资料，有合适职位时再通知候选人。",
          rules="规则：职位必须一致 · 硬性条件全部符合 · 其他条件至少 50%", reasons="理由", notmatched="未入选", hardmiss="缺少硬性条件", posmiss="职位不同", condlow="条件符合", jobs="示例职位单", yrs="{n} 年经验", areapref="希望在 {a}", ok="入选", namedef="示例候选人", hard="硬性", cond="条件",
          pos_labels={"warehouse": "仓库助理", "operator": "生产操作员", "cs": "客服专员", "tech": "维修技术员"},
          tag_labels={"exp2": "2 年以上经验", "shift": "可轮班", "forklift": "有叉车执照", "english": "会英语对话", "mandarin": "会华语对话", "immediate": "2 周内可上班", "passport": "护照有效", "transport": "有自己的交通"},
          area_labels={"woodlands": "兀兰", "jurong": "裕廊", "tuas": "大士", "changi": "樟宜"}),
 wa=dict(slabel="示例链接", pick="选一条收到的信息", reset="重置对话", contact="示例联系人", panel="自动贴上", tagsl="标签", statusl="跟进状态", rulesl="执行的规则", online="在线 · 演示", start="在左边选一条信息，看数字员工怎么回复。", form="https://forms.example.com/apply-sample", sl="SL",
         msgs=[
          dict(label="「我想申请 YU-01 这份工」", user="你好，我想申请 YU-01 这份工", bot=["你好！谢谢你的兴趣 😊 YU-01 是<b>兀兰</b>的仓库助理，薪水 S$2,300–2,600，轮班，长堤有交通接送。", "申请请填这份简短表格（约 2 分钟）：https://forms.example.com/apply-sample"], tags=["申请者", "YU-01", "兀兰"], status="已发表格 · 24 小时未填自动提醒", rules=["只讲所问地区的职位", "每条信息一个链接", "邀请填表"]),
          dict(label="「裕廊有工作吗？」", user="裕廊有工作吗？", bot=["有的，<b>裕廊</b>目前有两个空缺：\n• YU-02 仓库助理（需叉车执照）\n• YU-06 维修技术员", "告诉我你想了解哪一个，我发详情给你。或者填表让我们帮你配对：https://forms.example.com/apply-sample"], tags=["询问", "裕廊"], status="等待回复 · 明天 10 点跟进", rules=["只显示裕廊职位", "每条信息一个链接"]),
          dict(label="📄 发来简历", user="📄 简历_示例.pdf", bot=["收到你的简历，谢谢！招聘顾问会在 1 个工作日内查看。", "为了配对更准确，也请填一下这份表格：https://forms.example.com/apply-sample"], tags=["已收简历"], status="顾问审核 · 1 个工作日内", rules=["确认收到附件", "每条信息一个链接", "邀请填表"]),
          dict(label="「我已经找到工作了」", user="谢谢，不过我已经找到工作了", bot=["恭喜你，太好了！🎉 之后不会再发职位信息给你。以后想再找工作，随时在这里留言。祝一切顺利！"], tags=["已找到工作", "停止跟进"], status="已结束 · 不再发信息", rules=["礼貌收尾", "贴标签并停止跟进"])]),
 ct=dict(pick="选择生意类型", cal="本周计划", post="贴文草稿（按 Facebook 专页调整）", approve="批准并排程", change="要求修改", pending="等待你批准。批准前不会发布任何内容。", approved="已批准，排程于 {t}。（仅为演示，不会真的发布。）", changed="已连同你的意见退回修改，新草稿会再送来给你批准。", step="人工批准",
         types=[
          dict(name="美容院", when="周二 晚上 8:00", week=[["周一", "前后对比：补水护理"], ["周二", "小贴士：换肤后 3 件别做的事"], ["周三", "认识团队：资深美容师"], ["周四", "回答客户提问"], ["周五", "周末时段开放预约"], ["周六", "短视频：护理室参观"], ["周日", "休息日，不发"]],
               pages=[["主专页", "整天吹冷气，皮肤又干又紧？🌿 我们的补水护理 60 分钟，当晚就感觉不一样。平日时段还有空位，WhatsApp 我们预约。"], ["分店专页（示例：蒲种）", "蒲种的朋友 👋 本周蒲种分店的补水护理还有时段，楼下有免费停车。留言给我们约时间。"], ["创办人专页", "我常跟客户说：冷气比太阳更快让皮肤变干。所以补水护理是我们这个月最多人预约的项目。"]]),
          dict(name="房产经纪", when="周三 晚上 9:00", week=[["周一", "新盘：三房公寓（示例）"], ["周二", "60 秒看懂印花税"], ["周三", "地区指南：地铁站周边"], ["周四", "买家常见问题：贷款预批"], ["周五", "周末看房时段"], ["周六", "短视频：单位导览"], ["周日", "休息日，不发"]],
               pages=[["经纪专页", "第一次买房？先做贷款预批再去看房。你会知道真实预算，卖家也会更认真对待你。有问题 WhatsApp 我。"], ["房源专页", "示例房源：三房公寓，步行 5 分钟到地铁站。本周末可看房，留言了解详情。"], ["团队专页", "本周团队整理了买家最常问的问题：贷款批准要多久？简单说，资料齐全的话通常 1–2 周。"]]),
          dict(name="补习中心", when="周四 晚上 7:30", week=[["周一", "考试技巧：Paper 2 时间分配"], ["周二", "学生进步分享（匿名）"], ["周三", "家长问答：班级人数"], ["周四", "试听课邀请"], ["周五", "周末复习时间表"], ["周六", "短视频：一堂课怎么上"], ["周日", "休息日，不发"]],
               pages=[["中心专页", "Paper 2 总是写不完？试试这样：前 5 分钟先看完所有题目，标出先做哪几题。我们的老师每周都带学生练。"], ["家长专页", "很多家长问我们一班几个人。答案是最多 8 位，每堂课每个孩子的功课都会被检查。本月开放试听。"], ["老师专页", "一个改变成绩的小习惯：上课当天就完成功课，那时记忆最清楚。我每周都提醒学生。"]])]),
 howh="我们怎么做",
 how=[("梳理", "视频会议看你现在怎么做事、时间花在哪里。"), ("先删，再简化", "自动化之前，先删掉不该存在的步骤。"), ("搭建与测试", "用你现有的工具搭系统，用真实情境测试，你在旁边看。"), ("运营与优化", "每月运营：监察、调整规则、定期汇报。")],
 privh="数据与隐私",
 priv=["本页演示只使用虚构的示例数据，不显示也不收集任何真实候选人或客户资料。",
       "客户的系统里，数据保存在客户自己的账号（例如他们的 Google 表格和 WhatsApp Business）。我们只取得搭建和维护所需的权限。",
       "每一条对外信息模板、每一篇社媒贴文，都由客户批准后才上线。系统不会自己编造优惠，也不会超出你定的规则回复。",
       "我们依照马来西亚与新加坡的个人资料保护法（PDPA）处理个人资料。"],
 ctaey="下一步", ctah="想看看用在你的流程上是什么样？", wamsg="你好 Hunter，我在网站上看了产品演示，想预约 20 分钟通话。我做的是：＿＿",
 reg="HF Media Solution · 马来西亚商业注册号 IP0633909-U · 经营品牌 Hunter Foo Media · 远程服务马来西亚与新加坡",
)

S["ms"] = dict(
 title="Produk & demo langsung | HF Media Solution (IP0633909-U)",
 desc="Lihat apa yang HF Media Solution bina: pekerja digital AI untuk rekrutmen, WhatsApp dan kandungan, Iklan ChatGPT, serta pembinaan laman web dengan SEO dan AEO/GEO. Cuba demo dengan data contoh.",
 eyebrow="PRODUK", h1="Pekerja digital yang boleh anda lihat.",
 lede="HF Media Solution membina dan mengendalikan “pekerja digital” AI untuk perniagaan servis di Malaysia dan Singapura. Ia sistem automasi yang buat kerja berulang: menapis calon, menjawab pertanyaan WhatsApp, menyediakan post media sosial. Keputusan penting tetap dibuat oleh manusia.",
 introh="Apa yang kami buat",
 intro=["Pelanggan kami ialah perniagaan servis kecil: agensi rekrutmen, klinik dan salun kecantikan, ejen hartanah, pusat tuisyen dan pasukan kecil yang bergantung pada WhatsApp dan Facebook setiap hari.",
        "Semuanya diserahkan secara dalam talian. Kami fahami cara kerja anda melalui panggilan video dan WhatsApp, buang langkah yang tak perlu, kemudian bina sistem atas alat yang anda sudah guna: WhatsApp, Google Sheets dan Facebook. Kami berpangkalan di Kuala Lumpur dan kebanyakan kerja dibuat dalam talian, tanpa pemasangan di premis.",
        "<strong>Digunakan setiap hari:</strong> sistem ini berjalan setiap hari untuk pelanggan kami Sky Employment Pte Ltd, agensi pekerjaan berlesen di Singapura. Lihat kajian kes di bawah."],
 engh="Cara kerjasama berjalan",
 eng=[("1 · Persediaan", "Projek sekali. Kami petakan proses, bina sistem, uji bersama anda dan latih pasukan anda. Skop dan yuran dipersetujui dalam sebut harga bertulis sebelum mula."),
      ("2 · Operasi bulanan", "Yuran bulanan pilihan. Kami pastikan sistem berjalan, laraskan peraturan dan templat mesej serta baiki sebarang masalah. Jika kami uruskan iklan berbayar anda, anda terima laporan prestasi iklan setiap hari."),
      ("3 · Anda tetap mengawal", "Akaun, data dan pelanggan milik anda. Setiap templat mesej keluar dan setiap post perlu kelulusan anda sebelum disiarkan.")],
 prodh="Tiga produk. Cuba setiap satu.",
 prodsub="Semua demo di bawah berjalan sepenuhnya dalam pelayar anda dengan data contoh rekaan. Tiada apa-apa dihantar.",
 badge="Demo dengan data contoh",
 p1h="Sistem Padanan Rekrutmen AI",
 p1d="Calon isi borang ringkas. Sistem menyusunnya menjadi profil berstruktur dan menyemak dengan pesanan kerja menggunakan peraturan yang jelas: jawatan pilihan mesti sepadan, semua syarat wajib dipenuhi dan sekurang-kurangnya separuh syarat lain. Perekrut terima senarai pendek berserta sebabnya.",
 p2h="Pekerja Digital WhatsApp",
 p2d="Menjawab pencari kerja di WhatsApp seperti koordinator terbaik anda: butiran kerja untuk kawasan yang ditanya sahaja, satu pautan setiap mesej, jemputan isi borang permohonan dan penutup yang sopan. Setiap chat ditag secara automatik supaya pasukan tahu siapa perlu di-follow-up.",
 p3h="Automasi Kandungan",
 p3d="Merancang post seminggu untuk perniagaan anda dan menyediakan versi untuk setiap halaman Facebook anda. Tiada apa disiarkan sehingga seseorang dalam pasukan anda meluluskannya.",
 rec=dict(form="Borang calon", preset="Muat calon contoh", name="Nama", pos="Jawatan pilihan", area="Kawasan pilihan", years="Tahun pengalaman berkaitan", tagsl="Tandakan yang berkenaan", run="Jana profil & padankan", summary="Profil berstruktur", shortlist="Senarai pendek", none="Tiada pesanan kerja yang lulus ketiga-tiga peraturan. Sistem akan simpan profil ini dan maklumkan calon apabila ada kerja yang sesuai.",
          rules="Peraturan: jawatan mesti sepadan · semua syarat wajib · sekurang-kurangnya 50% syarat lain", reasons="Sebab", notmatched="Tidak disenarai pendek", hardmiss="Syarat wajib tidak dipenuhi", posmiss="Jawatan berbeza", condlow="Syarat dipenuhi", jobs="Pesanan kerja contoh", yrs="{n} tahun pengalaman", areapref="Pilih {a}", ok="Disenarai pendek", namedef="Calon contoh", hard="Wajib", cond="Syarat",
          pos_labels={"warehouse": "Pembantu gudang", "operator": "Operator pengeluaran", "cs": "Pegawai khidmat pelanggan", "tech": "Juruteknik penyelenggaraan"},
          tag_labels={"exp2": "Pengalaman 2 tahun ke atas", "shift": "Boleh kerja syif bergilir", "forklift": "Lesen forklift", "english": "Boleh bertutur Bahasa Inggeris", "mandarin": "Boleh bertutur Mandarin", "immediate": "Boleh mula dalam 2 minggu", "passport": "Pasport sah", "transport": "Ada kenderaan sendiri"},
          area_labels={"woodlands": "Woodlands", "jurong": "Jurong", "tuas": "Tuas", "changi": "Changi"}),
 wa=dict(slabel="pautan contoh", pick="Pilih mesej masuk", reset="Set semula chat", contact="Kenalan contoh", panel="Ditetapkan automatik", tagsl="Tag", statusl="Status follow-up", rulesl="Peraturan digunakan", online="dalam talian · demo", start="Pilih mesej di sebelah kiri untuk lihat cara pekerja digital membalas.", form="https://forms.example.com/apply-sample", sl="SL",
         msgs=[
          dict(label="“Saya nak mohon kerja YU-01”", user="Hai, saya nak mohon kerja YU-01", bot=["Hai! Terima kasih atas minat anda 😊 YU-01 ialah jawatan pembantu gudang di <b>Woodlands</b>. Gaji S$2,300–2,600, syif bergilir, pengangkutan dari Tambak disediakan.", "Untuk memohon, sila isi borang ringkas ini (2 minit): https://forms.example.com/apply-sample"], tags=["Pemohon", "YU-01", "Woodlands"], status="Borang dihantar · peringatan dalam 24 jam jika belum diisi", rules=["Butiran kerja kawasan yang ditanya sahaja", "Satu pautan setiap mesej", "Jemputan isi borang"]),
          dict(label="“Ada kerja di Jurong?”", user="Ada kerja di Jurong?", bot=["Ada, dua kekosongan di <b>Jurong</b> sekarang:\n• YU-02 Pembantu gudang (perlu lesen forklift)\n• YU-06 Juruteknik penyelenggaraan", "Beritahu saya yang mana menarik minat anda, saya hantar butirannya. Atau isi borang dan kami padankan: https://forms.example.com/apply-sample"], tags=["Pertanyaan", "Jurong"], status="Menunggu balasan · follow-up esok 10 pagi", rules=["Kerja Jurong sahaja ditunjukkan", "Satu pautan setiap mesej"]),
          dict(label="📄 Hantar resume", user="📄 Resume_contoh.pdf", bot=["Resume anda sudah diterima, terima kasih! Perekrut akan semak dalam 1 hari bekerja.", "Supaya padanan lebih tepat, sila lengkapkan juga borang ini: https://forms.example.com/apply-sample"], tags=["Resume diterima"], status="Semakan perekrut · dalam 1 hari bekerja", rules=["Sahkan lampiran diterima", "Satu pautan setiap mesej", "Jemputan isi borang"]),
          dict(label="“Saya dah dapat kerja”", user="Terima kasih, tapi saya dah dapat kerja", bot=["Tahniah, berita baik! 🎉 Kami tak akan hantar maklumat kerja lagi. Kalau nak cari semula nanti, mesej saja di sini. Semoga berjaya!"], tags=["Dah dapat kerja", "Jangan follow-up"], status="Ditutup · tiada mesej lagi", rules=["Penutup sopan", "Tag dan hentikan follow-up"])]),
 ct=dict(pick="Pilih jenis perniagaan", cal="Pelan minggu ini", post="Draf post, disesuaikan ikut halaman Facebook", approve="Lulus & jadualkan", change="Minta pindaan", pending="Menunggu kelulusan anda. Tiada apa disiarkan sebelum anda luluskan.", approved="Diluluskan. Dijadualkan pada {t}. (Demo sahaja: tiada apa yang benar-benar disiarkan.)", changed="Dihantar semula kepada penulis bersama nota anda. Draf baharu akan muncul untuk kelulusan.", step="Kelulusan manusia",
         types=[
          dict(name="Salun kecantikan", when="Sel 8:00 malam", week=[["Isn", "Sebelum & selepas: rawatan muka hidrasi"], ["Sel", "Tip: 3 perkara dielak selepas peel"], ["Rab", "Kenali pasukan: terapis kanan"], ["Kha", "Jawab soalan pelanggan"], ["Jum", "Slot hujung minggu dibuka"], ["Sab", "Video pendek: lawatan bilik rawatan"], ["Ahd", "Hari rehat: tiada post"]],
               pages=[["Halaman utama", "Kulit kering dan tegang lepas seharian dalam air-cond? 🌿 Rawatan muka hidrasi kami 60 minit dan anda rasa bezanya malam itu juga. Slot hari biasa masih ada. WhatsApp kami untuk tempah."], ["Halaman cawangan (contoh: Puchong)", "Kawan-kawan Puchong 👋 Slot rawatan muka hidrasi di cawangan Puchong masih ada minggu ini. Parkir percuma di bawah. Mesej kami untuk pilih masa."], ["Halaman pengasas", "Satu perkara yang saya selalu pesan: air-cond keringkan kulit lebih cepat daripada matahari. Sebab itu rawatan hidrasi paling banyak ditempah bulan ini."]]),
          dict(name="Ejen hartanah", when="Rab 9:00 malam", week=[["Isn", "Listing baharu: kondo 3 bilik (contoh)"], ["Sel", "Duti setem dalam 60 saat"], ["Rab", "Panduan kawasan: sekitar stesen MRT"], ["Kha", "Soalan pembeli: pra-kelulusan pinjaman"], ["Jum", "Slot tinjauan hujung minggu"], ["Sab", "Video pendek: tinjauan unit"], ["Ahd", "Hari rehat: tiada post"]],
               pages=[["Halaman ejen", "Rumah pertama? Dapatkan pra-kelulusan pinjaman sebelum mula tengok rumah. Anda tahu bajet sebenar dan penjual lebih serius dengan anda. Ada soalan? WhatsApp saya."], ["Halaman listing", "Listing contoh: kondo 3 bilik, 5 minit jalan kaki ke MRT. Slot tinjauan hujung minggu ini. Mesej untuk butiran."], ["Halaman pasukan", "Minggu ini pasukan jawab soalan paling kerap daripada pembeli: berapa lama kelulusan pinjaman? Biasanya 1–2 minggu jika dokumen lengkap."]]),
          dict(name="Pusat tuisyen", when="Kha 7:30 malam", week=[["Isn", "Tip peperiksaan: urus masa Kertas 2"], ["Sel", "Kejayaan pelajar (tanpa nama)"], ["Rab", "Soalan ibu bapa: saiz kelas"], ["Kha", "Jemputan kelas percubaan"], ["Jum", "Jadual ulang kaji hujung minggu"], ["Sab", "Video pendek: cara kelas berjalan"], ["Ahd", "Hari rehat: tiada post"]],
               pages=[["Halaman pusat", "Selalu tak sempat habis Kertas 2? Cuba ini: guna 5 minit pertama baca semua soalan dan tanda yang nak dijawab dulu. Guru kami latih ini setiap minggu."], ["Halaman ibu bapa", "Ramai ibu bapa tanya berapa orang sekelas. Jawapannya paling ramai 8 orang, jadi kerja setiap anak disemak setiap kelas. Kelas percubaan dibuka bulan ini."], ["Halaman guru", "Satu tabiat kecil yang ubah keputusan: siapkan kerja rumah pada hari kelas. Ingatan paling segar ketika itu. Saya ingatkan pelajar setiap minggu."]])]),
 howh="Cara kami bekerja",
 how=[("Petakan", "Panggilan video untuk lihat cara anda bekerja sekarang dan ke mana masa anda pergi."), ("Buang, kemudian ringkaskan", "Kami buang langkah yang tak sepatutnya ada sebelum automasi apa-apa."), ("Bina & uji", "Kami bina atas alat sedia ada dan uji dengan senario sebenar, anda turut melihat."), ("Jalankan & tambah baik", "Operasi bulanan: kami pantau, laraskan peraturan dan laporkan.")],
 privh="Data & privasi",
 priv=["Demo di halaman ini hanya guna data contoh rekaan. Tiada data calon atau pelanggan sebenar ditunjukkan atau dikumpul.",
       "Dalam sistem pelanggan, data kekal dalam akaun pelanggan sendiri (contohnya Google Sheets dan WhatsApp Business mereka). Kami hanya diberi akses yang perlu untuk membina dan menyelenggara sistem.",
       "Pelanggan meluluskan setiap templat mesej keluar dan setiap post media sosial sebelum disiarkan. Sistem tidak mereka tawaran atau membalas di luar peraturan yang anda tetapkan.",
       "Kami mengendalikan data peribadi selaras dengan undang-undang perlindungan data peribadi Malaysia dan Singapura (PDPA)."],
 ctaey="LANGKAH SETERUSNYA", ctah="Nak lihat ia dengan aliran kerja anda?", wamsg="Hai Hunter, saya dah tengok demo produk di laman web anda. Saya nak panggilan 20 minit. Bisnes saya: ____",
 reg="HF Media Solution · No. pendaftaran perniagaan IP0633909-U (Malaysia) · Berdagang sebagai Hunter Foo Media · Servis jarak jauh di Malaysia dan Singapura",
)

CS = {'en': {'csh': 'Case study: Sky Employment Pte Ltd', 'jump': 'Case study', 'cslede': 'Our client Sky Employment Pte Ltd is a Singapore employment agency (MOM EA licence 08C5793). HF Media Solution manages its recruitment marketing and operations, including its jobseeker channel, <strong>SG Jobs For Malaysians</strong>. The demos above are simplified versions of the systems we run for them.', 'scopeh': 'What we manage', 'scope': ['<strong>Facebook / Meta paid ads.</strong> Planning and running campaigns, with a daily ad performance report.', '<strong>Facebook Page content.</strong> Daily job-info posts and hiring posters for the SG Jobs For Malaysians page and the Sky Employment Pte Ltd page.', '<strong>WhatsApp Business.</strong> Replying to jobseekers, sending job details and the application form, following up, and labelling every chat.', '<strong>WhatsApp Channel “SG Jobs For Malaysians”.</strong> Daily job updates for followers.', '<strong>Google Drive &amp; Sheets.</strong> The job order list, candidate registration through a Google Form, resume production and a resume index.', '<strong>AI candidate-to-job matching.</strong> Each registered candidate is checked against open job orders and gets a list of recommended jobs.'], 'numh': 'By the numbers', 'asof': 'From internal records, as of 12 October 2026.', 'nums': [('22', 'candidates processed end-to-end through the automated pipeline: registration → resume → job recommendations'), ('49', 'candidate-to-job recommendations generated')], 'note': 'Sky Employment Pte Ltd is the licensed employment agency. HF Media Solution provides marketing, operations and automation services to it and does not charge job seekers.', 'links': 'Public pages', 'l1': 'SG Jobs For Malaysians on Facebook', 'l2': 'Sky Employment Pte Ltd on Facebook'}, 'zh': {'csh': '案例：Sky Employment Pte Ltd', 'jump': '客户案例', 'cslede': '我们的客户 Sky Employment Pte Ltd 是新加坡职业中介（MOM EA 执照 08C5793）。HF Media Solution 为其管理招聘营销与运营，包括它的求职频道 <strong>SG Jobs For Malaysians</strong>。上面的演示，就是我们为它运行的系统的简化版。', 'scopeh': '我们负责的范围', 'scope': ['<strong>Facebook / Meta 付费广告。</strong>规划和投放广告活动，每天提供广告成效报告。', '<strong>Facebook 专页内容。</strong>为 SG Jobs For Malaysians 专页和 Sky Employment Pte Ltd 专页每天发布职位资讯和招聘海报。', '<strong>WhatsApp Business。</strong>回复求职者、发送职位详情和申请表、跟进，并为每个对话贴标签。', '<strong>WhatsApp 频道「SG Jobs For Malaysians」。</strong>每天发布职位资讯。', '<strong>Google Drive 与表格。</strong>职位单清单、通过 Google 表单登记候选人、制作简历及简历索引。', '<strong>AI 候选人与职位匹配。</strong>每位登记的候选人都会对照现有职位单，得到一份推荐职位清单。'], 'numh': '数据', 'asof': '内部记录，截至 2026 年 10 月 12 日。', 'nums': [('22', '位候选人走完整个自动化流程：登记 → 简历 → 职位推荐'), ('49', '条候选人与职位推荐')], 'note': 'Sky Employment Pte Ltd 是持牌职业中介。HF Media Solution 为其提供营销、运营与自动化服务，不向求职者收费。', 'links': '公开专页', 'l1': 'SG Jobs For Malaysians（Facebook）', 'l2': 'Sky Employment Pte Ltd（Facebook）'}, 'ms': {'csh': 'Kajian kes: Sky Employment Pte Ltd', 'jump': 'Kajian kes', 'cslede': 'Pelanggan kami Sky Employment Pte Ltd ialah agensi pekerjaan di Singapura (lesen EA MOM 08C5793). HF Media Solution mengurus pemasaran dan operasi rekrutmennya, termasuk saluran pencari kerjanya, <strong>SG Jobs For Malaysians</strong>. Demo di atas ialah versi ringkas sistem yang kami jalankan untuknya.', 'scopeh': 'Apa yang kami urus', 'scope': ['<strong>Iklan berbayar Facebook / Meta.</strong> Merancang dan menjalankan kempen, dengan laporan prestasi iklan setiap hari.', '<strong>Kandungan Facebook Page.</strong> Post maklumat kerja dan poster pengambilan setiap hari untuk page SG Jobs For Malaysians dan page Sky Employment Pte Ltd.', '<strong>WhatsApp Business.</strong> Membalas pencari kerja, menghantar butiran kerja dan borang permohonan, follow-up dan melabel setiap chat.', '<strong>WhatsApp Channel “SG Jobs For Malaysians”.</strong> Maklumat kerja setiap hari.', '<strong>Google Drive &amp; Sheets.</strong> Senarai pesanan kerja, pendaftaran calon melalui Google Form, penghasilan resume dan indeks resume.', '<strong>Padanan calon-kerja AI.</strong> Setiap calon berdaftar disemak dengan pesanan kerja terbuka dan menerima senarai kerja yang disyorkan.'], 'numh': 'Dalam angka', 'asof': 'Daripada rekod dalaman, setakat 12 Oktober 2026.', 'nums': [('22', 'calon diproses sepenuhnya melalui aliran automatik: pendaftaran → resume → cadangan kerja'), ('49', 'cadangan calon-kerja dijana')], 'note': 'Sky Employment Pte Ltd ialah agensi pekerjaan berlesen. HF Media Solution menyediakan perkhidmatan pemasaran, operasi dan automasi kepadanya dan tidak mengenakan caj kepada pencari kerja.', 'links': 'Page awam', 'l1': 'SG Jobs For Malaysians di Facebook', 'l2': 'Sky Employment Pte Ltd di Facebook'}}

def _case(c):
    sc = ''.join('<li>%s</li>' % x for x in c['scope'])
    nm = ''.join('<li><b>%s</b><span>%s</span></li>' % x for x in c['nums'])
    return ('<section class="paper" id="case-study"><div class="wrap section prose"><h2>%s</h2><p class="pd-cslede">%s</p><div class="pd-intro"><div><h3>%s</h3><ul class="pd-priv">%s</ul></div>'
            '<div><h3>%s</h3><ul class="pd-nums">%s</ul><p class="pd-mini">%s</p><p class="agency-note">%s</p><h3>%s</h3><ul class="pd-priv"><li><a href="https://www.facebook.com/1162142606978815" target="_blank" rel="noopener noreferrer">%s ↗</a></li><li><a href="https://www.facebook.com/293845950684130" target="_blank" rel="noopener noreferrer">%s ↗</a></li></ul></div></div></div></section>\n') % (c['csh'], c['cslede'], c['scopeh'], sc, c['numh'], nm, c['asof'], c['note'], c['links'], c['l1'], c['l2'])

def _esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")

def _demo_shell(n, h, d, badge, inner):
    return ('<article class="pd-product" id="demo-%s" aria-labelledby="pd-h%s"><div class="pd-head"><p class="pd-num">0%s</p><div><h3 id="pd-h%s">%s</h3><p>%s</p></div></div>'
            '<div class="pd-demo"><p class="pd-badge"><span aria-hidden="true">●</span> %s</p>%s</div></article>') % (n, n, n, n, h, d, badge, inner)

def _main(s):
    intro = "".join("<p>%s</p>" % p for p in s["intro"])
    eng = "".join('<li><h3>%s</h3><p>%s</p></li>' % e for e in s["eng"])
    how = "".join('<li><h3>%s</h3><p>%s</p></li>' % e for e in s["how"])
    priv = "".join("<li>%s</li>" % p for p in s["priv"])
    d1 = '<div class="pd-rec" data-demo="rec"></div>'
    d2 = '<div class="pd-wa" data-demo="wa"></div>'
    d3 = '<div class="pd-ct" data-demo="ct"></div>'
    return ('\n<section class="wrap page-intro"><p class="eyebrow"><i></i>%s</p><h1>%s</h1><p class="lede">%s</p>'
            '<nav class="pd-jump" aria-label="%s"><a href="#demo-1">%s</a><a href="#demo-2">%s</a><a href="#demo-3">%s</a><a href="#chatgpt-ads">%s</a><a href="#website-building">%s</a><a href="#case-study">%s</a><a href="#faq">%s</a></nav></section>\n'
            '<section class="paper"><div class="wrap section prose pd-intro"><div><h2>%s</h2>%s</div><div><h2>%s</h2><ol class="pd-steps">%s</ol></div></div></section>\n'
            '<section class="wrap section pd-products" id="demos"><h2>%s</h2><p class="pd-sub">%s</p>%s%s%s</section>\n'
            '%s%s<section class="paper pd-how-wrap"><div class="wrap section prose pd-intro"><div><h2>%s</h2><ol class="pd-steps pd-how">%s</ol></div><div><h2>%s</h2><ul class="pd-priv">%s</ul></div></div></section>\n'
            '%s<section class="wrap section contact" id="contact"><p class="eyebrow"><i></i>%s</p><div class="contact-row"><h2>%s</h2><div class="contact-actions">'
            '<a class="button whatsapp" data-wa="%s" href="https://wa.me/60196273143" target="_blank" rel="noopener noreferrer">WhatsApp +60196273143 <span aria-hidden="true">↗</span></a>'
            '<a class="email-link" href="mailto:hello@hunterfoomedia.com">hello@hunterfoomedia.com <span aria-hidden="true">↗</span></a></div></div>'
            '<p class="pd-reg">%s</p></section>\n'
            '<script type="application/json" id="pd-data">%s</script>\n<script src="/assets/products-demo.js" defer></script>\n'
            ) % (s["eyebrow"], s["h1"], s["lede"], s["prodh"], s["p1h"], s["p2h"], s["p3h"], ADS[s["k"]]["jump"], WB[s["k"]]["jump"], CS[s["k"]]["jump"], FAQ[s["k"]]["jump"],
                 s["introh"], intro, s["engh"], eng,
                 s["prodh"], s["prodsub"],
                 _demo_shell(1, s["p1h"], s["p1d"], s["badge"], d1), _demo_shell(2, s["p2h"], s["p2d"], s["badge"], d2), _demo_shell(3, s["p3h"], s["p3d"], s["badge"], d3),
                 _ads(s["k"], s) + _wb(s["k"]), _case(CS[s["k"]]), s["howh"], how, s["privh"], priv, _faq(s["k"]),
                 s["ctaey"], s["ctah"], _esc(s["wamsg"]), s["reg"],
                 json.dumps({"rec": s["rec"], "wa": s["wa"], "ct": s["ct"], "ads": ADSW[s["k"]], "jobs": JOBS, "presets": PRESETS, "positions": POSITIONS, "tags": TAGS, "areas": AREAS}, ensure_ascii=False).replace("</", "<\\/"))

ADS_LD = {
    "en": ("ChatGPT Ads", "Help setting up and running ChatGPT Ads for service businesses in Malaysia and Singapore: account setup and verification help, landing page and tracking setup (OpenAI pixel), ad copy and creative, campaign management and reporting. You approve every ad before it is submitted. Scope and fees are agreed in a written quote; results are never guaranteed."),
    "zh": ("ChatGPT 广告", "为马来西亚与新加坡的服务型生意提供 ChatGPT 广告服务：开户与验证协助、落地页与追踪设置（OpenAI pixel）、广告文案与素材、投放管理与报告。每一条广告提交之前，都由你批准。服务范围和费用在开工前以书面报价确认，不保证任何结果。"),
    "ms": ("Iklan ChatGPT", "Servis Iklan ChatGPT untuk perniagaan perkhidmatan di Malaysia dan Singapura: bantuan penyediaan akaun dan pengesahan, persediaan halaman pendaratan dan penjejakan (piksel OpenAI), teks iklan dan kreatif, pengurusan kempen dan laporan. Anda luluskan setiap iklan sebelum ia dihantar. Skop dan yuran dipersetujui dalam sebut harga bertulis; hasil tidak dijamin."),
}
PRODUCTS = {}
for k, s in S.items():
    s["k"] = k
    PRODUCTS[k] = {"title": s["title"], "desc": s["desc"], "main": _main(s),
                   "services": [(s["p1h"], s["p1d"]), (s["p2h"], s["p2d"]), (s["p3h"], s["p3d"])],
                   "ads_service": ADS_LD[k],
                   "web_service": WB[k]["ld"],
                   "faq": [(q, _plain(a)) for q, a in FAQ[k]["qa"]]}
