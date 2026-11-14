# /services/ (EN / ZH / MS): the single services page. Five services, then the "what our AI can do" block (six pieces).
# Copy is written AROUND Hunter's six pieces (names and one-line outcomes below, no tool names, no invented figures).
# Prices: nothing numeric here. Website prices live on /website-design/ only; the rest is "by quote".
# The company definition is NOT on this page (About only). FAQ answers stay generic.
import urllib.parse, html, re
from home_pages import HFAQ

WA = "https://wa.me/60196273143"
D = "https://www.hunterfoomedia.com"
PATH = "/services/"

def _svg(inner):
    return ('<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true" focusable="false">%s</svg>' % inner)
ICONS = [
 _svg('<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.4 2.6 3.6 5.4 3.6 8.5s-1.2 5.9-3.6 8.5c-2.4-2.6-3.6-5.4-3.6-8.5s1.2-5.9 3.6-8.5z"/>'),
 _svg('<path d="M4 20l1-4L16.5 4.5a2 2 0 0 1 3 3L8 19z"/><path d="M14.5 6.5l3 3"/>'),
 _svg('<path d="M4 5h16v11H10l-5 4v-4H4z"/><path d="M8 10h8"/>'),
 _svg('<path d="M3 7h6l2 2h10v10H3z"/>'),
 _svg('<path d="M4 20V11M10 20V5M16 20v-6M2.5 20h19"/>'),
 _svg('<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M8 3v4M16 3v4"/>'),
]

P = {}
P["en"] = dict(
 title="AI Agency in Malaysia | Our 5 Services | Hunter Foo Media",
 desc="AI agency in Malaysia: AI consulting (Forward Deployed Engineer style), website building, website and Google Business Profile management, social media management and customized AI systems. Hunter Foo Media, Kuala Lumpur. WhatsApp +60196273143.",
 eyebrow="SERVICES · KUALA LUMPUR", h1='AI Agency in <span class="orange">Malaysia</span>',
 lede="Five services, from AI consulting to building a system made for your company.",
 cta="WhatsApp +60 19-627 3143", wamsg="Hi Hunter, I read your services page. My business: __\nI'd like to talk about service no.: __",
 sve="OUR SERVICES", svh="Five services",
 price_l="Price", quote="By quote", see_web="See the website design page", more_web="Website design page →",
 services=[
  ("ai-consultant", "AI Consulting | Forward Deployed Engineer style", "<p>We work like a Forward Deployed Engineer embedded in your company. We learn how your business and team work, then advise where AI fits, what to do first and how to do it, so you keep up with AI without chasing every new tool.</p><ul class=\"sv-points\"><li>One consulting meeting a month</li><li>Review which tasks can be handed to AI</li><li>A clear plan with priorities</li><li>Hands-on implementation when you need it (optional)</li></ul>", "By quote", None),
  ("website-building", "Website building", "We build a company website that Google and AI assistants can read and find. It is the base Website AI keeps up to date.", "RM399 (Basic), a founding price for the first 5 clients. The package with SEO + AEO/GEO is on the website design page", "/website-design/"),
  ("manage", "Website maintenance + Google Business Profile management", "Website AI keeps your web pages up to date, and we look after your Google Business Profile, so Google and AI assistants keep reading and finding you.", "RM499/month, a founding price for the first 5 clients", "/website-design/"),
  ("social-media", "Social media management", "Marketing AI drafts 2 posts a week for you (caption and image), 8 posts a month, plus 2 AI reels (15 seconds each) a month. Nothing is published until you approve it.", "By quote", None),
  ("custom-ai", "Customized AI system", "If the six digital employees aren't enough, we build something made for your company. For example: an AI knowledge base that answers questions from your own company documents; workflows that link your repeated steps together automatically; a call system where AI assists during phone calls; a calendar system that books and schedules for you. And more, depending on what you need.", "By quote", None)],
 aie="WHAT OUR AI CAN DO", aih="What our AI can do", demo_l="Try the interactive demo",
 aisub="Six digital employees: three serve your customers, three help your team.",
 outh="Outside: serving customers", inh="Inside: helping your team",
 six=[("Website AI", "Updates your web page content, so Google and AI assistants can read and find you."),
      ("Marketing AI", "Drafts your social media and Google Business Profile posts every week, and publishes only after you approve."),
      ("Customer Service AI", "Answers common questions instantly, follows up customers who haven't replied, and hands complex cases to a person."),
      ("Clerk AI", "Organizes your files, makes resumes and documents, and archives your data."),
      ("Manager AI", "Follows up progress, and reports every day who should do what and where things are stuck."),
      ("PA AI", "Manages the boss's schedule, reminds you to follow up, and drafts replies that are sent only after you confirm.")],
 fqe="FAQ", fqh="Common questions",
 faq=[("What is an AI agency?", "An AI agency is a company that helps businesses put AI to work in their daily operations: setting it up, connecting it to how the business already runs, and keeping it working. It is different from only selling a software subscription."),
      ("How much does an AI agency cost in Malaysia?", "It depends on the scope, so there is no single price. At Hunter Foo Media, website building is RM399 (Basic) and website maintenance + Google Business Profile management is RM499/month. These two prices are founding-client prices for the first 5 clients, in exchange for an honest testimonial, and will go up after 5 clients. Social media management, customized AI systems and the maintenance of your digital employees are quoted after we understand how your business works."),
      ("Will the AI send things to my customers without my approval?", "No. Marketing AI publishes only after you approve, Customer Service AI hands complex cases to a person, and PA AI's drafted replies are sent only after you confirm."),
      HFAQ["en"]["qa"][2],
      ("Where are you, and do you serve Singapore?", "We are based in Kuala Lumpur and serve businesses in Malaysia and Singapore, mostly online."),
      ("Is Hunter Foo Media a recruitment agency?", "No. We don't charge job seekers or place candidates ourselves. See the About page for details.")],
 ce="NEXT STEP", ch="Tell us about your business", cnote="Malaysian number +60196273143. English, <span lang=\"zh-Hans\">中文</span> or BM.",
 crumb="Home", crumbp="Services", svcname="AI agency services for businesses in Malaysia and Singapore",
)
P["zh"] = dict(
 title="马来西亚 AI Agency｜我们的五项服务｜Hunter Foo Media",
 desc="马来西亚 AI Agency：AI 顾问（FDE 驻场式陪跑）、制作网站、管理网站和 Google Business Profile、社交媒体管理、定制 AI 系统。Hunter Foo Media，吉隆坡。WhatsApp +60196273143。",
 eyebrow="服务 · 吉隆坡", h1='马来西亚 <span class="orange">AI Agency</span>',
 lede="五项服务：从 AI 顾问陪跑，到做一个为你公司量身定做的系统。",
 cta="WhatsApp +60 19-627 3143", wamsg="你好 Hunter，我看了你们的服务页。我做的是：＿＿\n想聊的服务编号：＿＿",
 sve="我们的服务", svh="五项服务",
 price_l="价格", quote="按报价", see_web="看制作网站页", more_web="制作网站页 →",
 services=[
  ("ai-consultant", "AI 顾问｜FDE 驻场式陪跑", "<p>我们像你公司里的 Forward Deployed Engineer：先了解你的业务和团队，再告诉你哪里适合用 AI、先做什么、怎么做。你不用自己追新工具，有我们帮你判断。</p><ul class=\"sv-points\"><li>每月一次顾问会议</li><li>盘点公司里哪些工作可以交给 AI</li><li>给你一份清楚的建议和优先顺序</li><li>需要落地时，我们可以帮你执行（可选）</li></ul>", "按报价", None),
  ("website-building", "制作网站", "做一个 Google 和 AI 助手读得懂、找得到的公司网站，也是网站 AI 持续更新的基础。", "RM399（基础版），前 5 位客户的创始价。含 SEO + AEO/GEO 的方案见制作网站页", "/website-design/"),
  ("manage", "网站维护 + Google Business Profile 管理", "网站 AI 帮你持续更新网页内容，我们也帮你管理 Google Business Profile，让 Google 和 AI 助手一直读得懂、找得到你。", "每月 RM499，前 5 位客户的创始价", "/website-design/"),
  ("social-media", "Social media management（社交媒体管理）", "营销 AI 每周帮你起草 2 篇帖子（文案加图片），一个月 8 篇，另外每月做 2 条 15 秒的 AI 短视频（reel）。你批准后才发布。", "按报价", None),
  ("custom-ai", "定制 AI 系统", "如果六位数字员工还不够，我们按你公司的需要量身做。例如：用公司资料回答问题的 AI 知识库；把重复的步骤自动串起来的流程；电话通话中由 AI 协助的通话系统；自动排日程、约时间的日历系统。还有别的，看你需要什么。", "按报价", None)],
 aie="我们的 AI 能做什么", aih="我们的 AI 能做什么", demo_l="试用互动演示",
 aisub="六位数字员工：三位服务客户，三位帮团队。",
 outh="对外：服务客户", inh="对内：帮团队做事",
 six=[("网站 AI", "更新网页内容，让 Google 和 AI 助手读得懂、找得到你。"),
      ("营销 AI", "每周起草社交媒体和 Google 商家资料的帖子，你批准后才发布。"),
      ("客服 AI", "即时回答常见问题，跟进没回复的客户，复杂的转给真人。"),
      ("文员 AI", "整理文件，做简历和文档，归档资料。"),
      ("经理 AI", "跟进进度，每天汇报谁该做什么、哪里卡住了。"),
      ("PA AI", "管理老板的日程，提醒跟进，起草回复，你确认后才发出。")],
 fqe="常见问题", fqh="常见问题",
 faq=[("什么是 AI agency？", "AI agency 是帮企业把 AI 用进日常运作的公司：把 AI 设置好，接上企业原本的做事方式，并让它持续运作。和只卖软件订阅不一样。"),
      ("马来西亚的 AI agency 要多少钱？", "要看范围，没有单一价格。在 Hunter Foo Media，制作网站是 RM399（基础版），网站维护 + Google Business Profile 管理是每月 RM499。这两个价格是前 5 位客户的创始价，条件是为我们写一则真实评价，满 5 位后将调价。社交媒体管理、定制 AI 系统，以及数字员工的维护，等我们弄清楚你的生意怎么运作之后，以书面报价确认。"),
      ("AI 会不经我批准就发东西给客户吗？", "不会。营销 AI 要你批准后才发布；客服 AI 遇到复杂情况会交给真人；PA AI 起草的回复，你确认后才发出。"),
      HFAQ["zh"]["qa"][2],
      ("你们在哪里？也服务新加坡吗？", "我们位于吉隆坡，服务马来西亚和新加坡的企业，大部分在线上完成。"),
      ("Hunter Foo Media 是职业中介吗？", "不是。我们不向求职者收费，也不自行安排工作。详情见关于页。")],
 ce="下一步", ch="跟我们说说你的生意", cnote="马来西亚号码 +60196273143。中文、英文或马来文都可以。",
 crumb="首页", crumbp="服务", svcname="面向马来西亚与新加坡企业的 AI agency 服务",
)
P["ms"] = dict(
 title="Agensi AI di Malaysia (AI Agency) | 5 Perkhidmatan Kami | Hunter Foo Media",
 desc="Agensi AI (AI agency) di Malaysia: perundingan AI (gaya Forward Deployed Engineer), pembinaan laman web, pengurusan laman web dan Google Business Profile, pengurusan media sosial dan sistem AI tersuai. Hunter Foo Media, Kuala Lumpur. WhatsApp +60196273143.",
 eyebrow="PERKHIDMATAN · KUALA LUMPUR", h1='Agensi AI <span class="orange">(AI Agency)</span> di Malaysia',
 lede="Lima perkhidmatan, daripada perundingan AI hingga membina sistem yang dibuat khas untuk syarikat anda.",
 cta="WhatsApp +60 19-627 3143", wamsg="Hai Hunter, saya baca halaman perkhidmatan anda. Perniagaan saya: __\nNombor perkhidmatan yang saya nak bincang: __",
 sve="PERKHIDMATAN KAMI", svh="Lima perkhidmatan",
 price_l="Harga", quote="Ikut sebut harga", see_web="Lihat halaman reka bentuk laman web", more_web="Halaman laman web →",
 services=[
  ("ai-consultant", "Perundingan AI | Gaya Forward Deployed Engineer", "<p>Kami bekerja seperti Forward Deployed Engineer yang ditempatkan di syarikat anda. Kami mempelajari bagaimana perniagaan dan pasukan anda berfungsi, kemudian menasihati di mana AI sesuai, apa yang perlu dibuat dahulu dan bagaimana membuatnya, supaya anda dapat mengikuti rentak AI tanpa mengejar setiap alat baharu.</p><ul class=\"sv-points\"><li>Mesyuarat perunding sebulan sekali</li><li>Tinjau tugas mana dalam syarikat yang boleh diserahkan kepada AI</li><li>Satu rancangan yang jelas beserta keutamaan</li><li>Pelaksanaan secara langsung apabila anda memerlukannya (pilihan)</li></ul>", "Ikut sebut harga", None),
  ("website-building", "Pembinaan laman web", "Kami bina laman web syarikat yang boleh dibaca dan ditemui oleh Google dan pembantu AI. Ia asas yang AI Laman Web kemas kini.", "RM399 (Asas), harga pelanggan awal untuk 5 pelanggan pertama. Pakej dengan SEO + AEO/GEO ada di halaman reka bentuk laman web", "/website-design/"),
  ("manage", "Penyelenggaraan laman web + pengurusan Google Business Profile", "AI Laman Web memastikan halaman web anda dikemas kini, dan kami menjaga Google Business Profile anda, supaya Google dan pembantu AI terus membaca dan menemui anda.", "RM499/bulan, harga pelanggan awal untuk 5 pelanggan pertama", "/website-design/"),
  ("social-media", "Pengurusan media sosial", "AI Pemasaran merangka 2 hantaran seminggu untuk anda (kapsyen dan imej), 8 hantaran sebulan, serta 2 reel AI (15 saat setiap satu) sebulan. Tiada apa diterbitkan sehingga anda luluskan.", "Ikut sebut harga", None),
  ("custom-ai", "Sistem AI tersuai", "Jika enam pekerja digital belum cukup, kami bina sesuatu yang dibuat khas untuk syarikat anda. Contohnya: pangkalan pengetahuan AI yang menjawab soalan berdasarkan dokumen syarikat anda sendiri; aliran kerja yang menyambungkan langkah berulang anda secara automatik; sistem panggilan di mana AI membantu semasa panggilan telefon; sistem kalendar yang menetapkan jadual dan temu janji untuk anda. Dan lagi, bergantung pada keperluan anda.", "Ikut sebut harga", None)],
 aie="APA AI KAMI BOLEH BUAT", aih="Apa AI kami boleh buat", demo_l="Cuba demo interaktif",
 aisub="Enam pekerja digital: tiga melayan pelanggan, tiga membantu pasukan.",
 outh="Di luar: melayan pelanggan", inh="Di dalam: membantu pasukan",
 six=[("AI Laman Web", "Mengemas kini kandungan halaman web anda, supaya Google dan pembantu AI boleh membaca dan menemui anda."),
      ("AI Pemasaran", "Merangka hantaran media sosial dan Google Business Profile anda setiap minggu, dan hanya menerbitkan selepas anda luluskan."),
      ("AI Khidmat Pelanggan", "Menjawab soalan lazim serta-merta, menyusuli pelanggan yang belum membalas, dan menyerahkan kes rumit kepada orang."),
      ("AI Kerani", "Menyusun fail anda, menyediakan resume dan dokumen, dan mengarkibkan data."),
      ("AI Pengurus", "Menyusuli kemajuan, dan melaporkan setiap hari siapa patut buat apa dan di mana ia tersekat."),
      ("AI PA", "Mengurus jadual bos, mengingatkan tindakan susulan, dan merangka balasan yang dihantar hanya selepas anda sahkan.")],
 fqe="SOALAN LAZIM", fqh="Soalan lazim",
 faq=[("Apa itu agensi AI (AI agency)?", "Agensi AI ialah syarikat yang membantu perniagaan menggunakan AI dalam operasi harian: menyediakannya, menyambungkannya dengan cara perniagaan sedia berjalan, dan memastikan ia terus berfungsi. Ia berbeza daripada sekadar menjual langganan perisian."),
      ("Berapa kos agensi AI di Malaysia?", "Bergantung kepada skop, jadi tiada satu harga. Di Hunter Foo Media, pembinaan laman web ialah RM399 (Asas) dan penyelenggaraan laman web + pengurusan Google Business Profile ialah RM499/bulan. Dua harga ini ialah harga pelanggan awal untuk 5 pelanggan pertama, sebagai balasan satu testimoni yang jujur, dan akan naik selepas 5 pelanggan. Pengurusan media sosial, sistem AI tersuai dan penyelenggaraan pekerja digital anda disebut harga selepas kami faham cara perniagaan anda berjalan."),
      ("Adakah AI hantar sesuatu kepada pelanggan tanpa kelulusan saya?", "Tidak. AI Pemasaran hanya menerbitkan selepas anda luluskan, AI Khidmat Pelanggan menyerahkan kes rumit kepada orang, dan balasan yang dirangka AI PA dihantar hanya selepas anda sahkan."),
      HFAQ["ms"]["qa"][2],
      ("Di mana anda, dan adakah anda berkhidmat di Singapura?", "Kami berpangkalan di Kuala Lumpur dan berkhidmat untuk perniagaan di Malaysia dan Singapura, kebanyakannya secara dalam talian."),
      ("Adakah Hunter Foo Media agensi pekerjaan?", "Bukan. Kami tidak mengenakan caj kepada pencari kerja dan tidak menempatkan calon sendiri. Lihat halaman Tentang Kami untuk butiran.")],
 ce="LANGKAH SETERUSNYA", ch="Ceritakan tentang perniagaan anda", cnote="Nombor Malaysia +60196273143. Bahasa Inggeris, Cina atau BM.",
 crumb="Utama", crumbp="Perkhidmatan", svcname="Perkhidmatan agensi AI untuk perniagaan di Malaysia dan Singapura",
)

def six_cards(k):
    h = P[k]
    card = lambda i: ('<li><span class="sv-ico">%s</span><h3>%s</h3><p>%s</p></li>' % (ICONS[i], h["six"][i][0], h["six"][i][1]))
    return ('<p class="hm-lede-d">%s</p><h3 class="ad-h3 sv-h3">%s</h3><ul class="hm-cards hm-cards-light sv-six">%s</ul>'
            '<h3 class="ad-h3 sv-h3">%s</h3><ul class="hm-cards hm-cards-light sv-six">%s</ul>'
            '<p class="sv-demo"><a class="button" href="/demo/">%s <span aria-hidden="true">→</span></a></p>'
            % (h["aisub"], h["outh"], "".join(card(i) for i in range(3)), h["inh"], "".join(card(i) for i in range(3, 6)), h["demo_l"]))

def _main(k):
    h = P[k]
    wa = WA + "?text=" + urllib.parse.quote(h["wamsg"], safe="")
    o = []
    o.append('<section class="wrap hm-hero wd-hero"><p class="eyebrow"><i></i>%s</p><h1>%s</h1><p class="lede">%s</p>'
             '<div class="hm-ctas"><a class="button" href="%s" target="_blank" rel="noopener noreferrer">%s <span aria-hidden="true">↗</span></a></div></section>\n'
             % (h["eyebrow"], h["h1"], h["lede"], wa, h["cta"]))
    blocks = []
    for i, (sid, name, desc, price, link) in enumerate(h["services"]):
        more = '<p class="sv-more"><a class="hm-link" href="%s">%s</a></p>' % (link, h["more_web"]) if link else ""
        copy = desc if desc.lstrip().startswith("<") else "<p>%s</p>" % desc
        blocks.append('<article class="sv-block" id="%s"><span class="hm-n">%d</span><div class="sv-body"><h3>%s</h3>%s<p class="sv-price"><strong>%s</strong> %s</p>%s</div></article>'
                      % (sid, i + 1, name, copy, h["price_l"], price, more))
    o.append('<section class="paper hm-sec sv-sec" id="services"><div class="wrap section"><p class="pd-kicker">%s</p><h2 class="hm-h2">%s</h2>%s</div></section>\n'
             % (h["sve"], h["svh"], "".join(blocks)))
    o.append('<section class="paper pd-faq-wrap" id="faq" aria-labelledby="sv-faq-h"><div class="wrap section"><div class="pd-faq">'
             '<p class="pd-kicker">%s</p><h2 id="sv-faq-h">%s</h2>%s</div></div></section>\n'
             % (h["fqe"], h["fqh"], "".join('<details%s><summary>%s</summary><p>%s</p></details>' % (' open' if j == 0 else '', q, a) for j, (q, a) in enumerate(h["faq"]))))
    o.append('<section class="wrap section hm-sec hm-dark" id="ai-can-do"><p class="eyebrow"><i></i>%s</p><h2 class="hm-h2">%s</h2>%s</section>\n'
             % (h["aie"], h["aih"], six_cards(k)))
    o.append('<section class="wrap section contact" id="contact"><p class="eyebrow"><i></i>%s</p><div class="contact-row"><h2>%s</h2><div class="contact-actions">'
             '<a class="button whatsapp" data-wa="%s" href="%s" target="_blank" rel="noopener noreferrer">WhatsApp +60196273143 <span aria-hidden="true">↗</span></a>'
             '<!--email_off--><a class="email-link" href="mailto:hello@hunterfoomedia.com">hello@hunterfoomedia.com <span aria-hidden="true">↗</span></a><!--/email_off--><p>%s</p></div></div></section>\n'
             % (h["ce"], h["ch"], html.escape(h["wamsg"]), wa, h["cnote"]))
    return "\n" + "".join(o)

def _plain(s):
    s = re.sub(r"</li>", "; ", s)
    s = re.sub(r"</(p|div|h3)>", " ", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s).strip().rstrip(";").strip()

def _ld(k):
    h = P[k]; u = D + PATH
    area = [{"@type": "Country", "name": "Malaysia"}, {"@type": "Country", "name": "Singapore"}]
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": u + "#webpage", "url": u, "name": h["title"], "description": h["desc"],
         "about": {"@id": D + "/#organization"}, "isPartOf": {"@id": D + "/#website"}, "breadcrumb": {"@id": u + "#breadcrumb"}}] + [
        {"@type": "Service", "@id": u + "#" + sid, "name": _plain(name), "serviceType": "AI agency", "description": _plain(desc),
         "provider": {"@id": D + "/#organization"}, "areaServed": area, "url": u + "#" + sid}
        for sid, name, desc, price, link in h["services"]] + [
        {"@type": "FAQPage", "@id": u + "#faq", "url": u + "#faq", "isPartOf": {"@id": u + "#webpage"},
         "mainEntity": [{"@type": "Question", "name": _plain(q), "acceptedAnswer": {"@type": "Answer", "text": _plain(a)}} for q, a in h["faq"]]},
        {"@type": "BreadcrumbList", "@id": u + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": h["crumb"], "item": D + "/"},
            {"@type": "ListItem", "position": 2, "name": h["crumbp"], "item": u}]}]}

SV = {k: {"title": P[k]["title"], "desc": P[k]["desc"], "main": _main(k), "ld": _ld(k)} for k in P}
