# Simplified homepage (EN / ZH / MS): core line verbatim (H[k]["pos"] from home_pages), no definition line,
# Hero, the five services, a brief six-piece overview linking to /services/, one CTA.
import urllib.parse, html, re
from home_pages import H, HFAQ, _home_faq, _faq_plain
from services_page import P as SP
from articles_pages import ARTICLES, DATE_FMT

WA = "https://wa.me/60196273143"
D = "https://www.hunterfoomedia.com"

META = {
 "en": ("AI Agency in Malaysia | AI Automation | Hunter Foo Media",
        "AI automation for businesses in Malaysia and Singapore. We ease your company's anxiety about AI and help you keep pace with AI. WhatsApp +60196273143."),
 "zh": ("马来西亚企业 AI 自动化｜AI Agency｜Hunter Foo Media",
        "为马来西亚与新加坡企业提供 AI 自动化。解决企业对 AI 的焦虑，帮你跟上 AI 的脚步。顾问建议，落地可选。欢迎 WhatsApp 询价 +60196273143。"),
 "ms": ("Automasi AI & Agensi AI di Malaysia | Hunter Foo Media",
        "Automasi AI untuk perniagaan di Malaysia dan Singapura. Kami meredakan keresahan syarikat anda terhadap AI, dan membantu anda mengikuti rentak AI."),
}
for _k, (_t, _d) in META.items():
    assert H[_k]["pos"] in _d  # core line verbatim
    H[_k]["title"], H[_k]["desc"] = _t, _d

X = {}
X["en"] = dict(
 see="See our services", demo="Try AI Demo", sve="WHAT WE DO", svh="Five services",
 lines=["A monthly meeting to advise where AI fits, what to do first and how.",
        "A company website that Google and AI assistants can read and find.",
        "Your web pages and Google Business Profile, kept up to date.",
        "8 posts and 2 AI reels a month. You approve before anything is published.",
        "Built around your company: an AI that answers from your documents, workflows, calendar and more."],
 tags=["Contact us on WhatsApp for a quote", "Contact us on WhatsApp for a quote", "Contact us on WhatsApp for a quote", "Contact us on WhatsApp for a quote", "Contact us on WhatsApp for a quote"],
 aie="SIX DIGITAL EMPLOYEES", aih="Three serve your customers. Three help your team.", out="Outside", inn="Inside", aigo="See what each one does →",
 nte="FROM OUR NOTES", nth="Notes for businesses keeping up with AI",
 ntp="Two short notes from real work: how a business can keep pace with AI, and what to get right before running hiring ads.",
 nall="All notes →",
 nblurb={"keeping-your-business-in-step-with-ai": "How a business can keep pace with AI: start with trust and a website, then a funnel from social media to WhatsApp.",
         "meta-hiring-ads-singapore-sme": "What to get right before running Meta hiring ads in Singapore: the rules, fair wording, and WhatsApp follow-up."},
 cnote="Malaysian number +60196273143. English, <span lang=\"zh-Hans\">中文</span> or BM.")
X["zh"] = dict(
 see="看我们的服务", demo="试用 AI 演示", sve="我们做什么", svh="五项服务",
 lines=["每月一次顾问会议，告诉你哪里适合用 AI、先做什么、怎么做。",
        "Google 和 AI 助手读得懂、找得到的公司网站。",
        "网页和 Google Business Profile，持续更新。",
        "每月 8 篇帖子加 2 条 AI 短视频，你批准后才发布。",
        "按你的公司量身做：用公司资料回答问题的 AI、自动流程、日历等。"],
 tags=["欢迎 WhatsApp 咨询报价", "欢迎 WhatsApp 咨询报价", "欢迎 WhatsApp 咨询报价", "欢迎 WhatsApp 咨询报价", "欢迎 WhatsApp 咨询报价"],
 aie="六位数字员工", aih="三位服务客户，三位帮团队。", out="对外", inn="对内", aigo="看每一位做什么 →",
 nte="来自我们的笔记", nth="帮企业跟上 AI 的笔记",
 ntp="两篇从实际工作写出的短文：企业怎样跟上 AI，以及投放招聘广告前要先做对的事。",
 nall="全部笔记 →",
 nblurb={"keeping-your-business-in-step-with-ai": "企业怎样跟上 AI：先建立信任、从网站开始，再做从社交媒体到 WhatsApp 的销售漏斗。",
         "meta-hiring-ads-singapore-sme": "在新加坡投 Meta 招聘广告前要先做对的事：规则、公平的写法，以及用 WhatsApp 跟进。"},
 cnote="马来西亚号码 +60196273143。中文、英文或马来文都可以。")
X["ms"] = dict(
 see="Lihat perkhidmatan kami", demo="Cuba Demo AI", sve="APA KAMI BUAT", svh="Lima perkhidmatan",
 lines=["Mesyuarat perunding sebulan sekali: di mana AI sesuai, apa dibuat dahulu dan bagaimana.",
        "Laman web syarikat yang boleh dibaca dan ditemui oleh Google dan pembantu AI.",
        "Halaman web dan Google Business Profile anda, sentiasa dikemas kini.",
        "8 hantaran dan 2 reel AI sebulan. Anda luluskan sebelum diterbitkan.",
        "Dibina khas untuk syarikat anda: AI yang menjawab daripada dokumen anda, aliran kerja, kalendar dan lagi."],
 tags=["Hubungi kami di WhatsApp untuk sebut harga", "Hubungi kami di WhatsApp untuk sebut harga", "Hubungi kami di WhatsApp untuk sebut harga", "Hubungi kami di WhatsApp untuk sebut harga", "Hubungi kami di WhatsApp untuk sebut harga"],
 aie="ENAM PEKERJA DIGITAL", aih="Tiga melayan pelanggan anda. Tiga membantu pasukan anda.", out="Di luar", inn="Di dalam", aigo="Lihat apa setiap satu buat →",
 nte="DARIPADA CATATAN KAMI", nth="Catatan untuk perniagaan yang mahu kekal seiring dengan AI",
 ntp="Dua catatan ringkas daripada kerja sebenar: cara perniagaan kekal seiring dengan AI, dan apa yang perlu dibetulkan sebelum iklan pengambilan pekerja.",
 nall="Semua catatan →",
 nblurb={"keeping-your-business-in-step-with-ai": "Cara perniagaan kekal seiring dengan AI: mula dengan kepercayaan dan laman web, kemudian corong dari media sosial ke WhatsApp.",
         "meta-hiring-ads-singapore-sme": "Apa yang perlu dibetulkan sebelum iklan pengambilan pekerja Meta di Singapura: peraturan, ayat yang adil, dan susulan WhatsApp."},
 cnote="Nombor Malaysia +60196273143. Bahasa Inggeris, Cina atau BM.")

def _main(k):
    h = H[k]; x = X[k]; s = SP[k]
    wa = WA + "?text=" + urllib.parse.quote(h["wamsg"], safe="")
    o = []
    o.append('<section class="wrap hm-hero"><p class="eyebrow"><i></i>%s</p><h1>%s</h1><p class="hm-pos">%s</p>'
             '<figure class="hm-3d"><picture><source type="image/webp" srcset="/assets/hfm-ai-company-3d.webp">'
             '<img src="/assets/hfm-ai-company-3d.jpg" width="1280" height="720" alt="%s" decoding="async" fetchpriority="high"></picture></figure>'
             '<div class="hm-ctas"><a class="button" href="%s" target="_blank" rel="noopener noreferrer">%s <span aria-hidden="true">↗</span></a>'
             '<a class="button ghost" href="/services/">%s <span aria-hidden="true">→</span></a></div></section>\n'
             % (h["eyebrow"], h["h1"], h["pos"], html.escape(h["img_alt"], quote=True), wa, h["cta_wa"], x["see"]))
    short = lambda n: re.split(r"\s*[｜|]\s*", n, maxsplit=1)[0]
    qlink = '<a href="%s" target="_blank" rel="noopener noreferrer">%s <span aria-hidden="true">↗</span></a>' % (wa, x["tags"][0])
    cards = "".join('<li><a href="/services/#%s"><span class="hm-n">%d</span><h3>%s</h3><p>%s</p></a><p class="hm-price">%s</p></li>' % (sid, i + 1, short(name), x["lines"][i], qlink)
                    for i, (sid, name, d_, p_, l_) in enumerate(s["services"]))
    o.append('<section class="paper hm-sec" id="services"><div class="wrap section"><p class="pd-kicker">%s</p><h2 class="hm-h2">%s</h2>'
             '<ol class="hm-cards hm-cards-light hm-cards-5 hm-svc">%s</ol>'
             '<p class="hm-demo"><a class="button" href="/demo/">%s <span aria-hidden="true">→</span></a></p></div></section>\n' % (x["sve"], x["svh"], cards, x["demo"]))
    chips = lambda a, b: "".join('<span class="hm-chip">%s</span>' % s["six"][i][0] for i in range(a, b))
    o.append('<section class="wrap section hm-sec hm-dark" id="six"><p class="eyebrow"><i></i>%s</p><h2 class="hm-h2">%s</h2>'
             '<p class="hm-six-l">%s</p><div class="hm-chips">%s</div><p class="hm-six-l">%s</p><div class="hm-chips">%s</div>'
             '<p class="hm-links"><a class="hm-link" href="/services/#ai-can-do">%s</a></p></section>\n'
             % (x["aie"], x["aih"], x["out"], chips(0, 3), x["inn"], chips(3, 6), x["aigo"]))
    cards = "".join('<li><a href="/notes/%s/"><time datetime="%s">%s</time><h3>%s</h3><p>%s</p></a></li>'
                    % (a["slug"], a["date"], DATE_FMT[k](a["date"]), a[k]["h1"], x["nblurb"][a["slug"]]) for a in ARTICLES)
    o.append('<section class="paper hm-sec" id="notes"><div class="wrap section"><p class="pd-kicker">%s</p><h2 class="hm-h2">%s</h2><p class="hm-lede">%s</p>'
             '<ul class="hm-notes">%s</ul><p class="hm-links"><a class="hm-link" href="/notes/">%s</a></p></div></section>\n'
             % (x["nte"], x["nth"], x["ntp"], cards, x["nall"]))
    o.append(_home_faq(k))
    o.append('<section class="wrap section contact" id="contact"><p class="eyebrow"><i></i>%s</p><div class="contact-row"><h2>%s</h2><div class="contact-actions">'
             '<a class="button whatsapp" data-wa="%s" href="%s" target="_blank" rel="noopener noreferrer">WhatsApp +60196273143 <span aria-hidden="true">↗</span></a>'
             '<!--email_off--><a class="email-link" href="mailto:hello@hunterfoomedia.com">hello@hunterfoomedia.com <span aria-hidden="true">↗</span></a><!--/email_off--><p>%s</p></div></div></section>\n'
             % (h["ce"], h["ch"], html.escape(h["wamsg"]), wa, x["cnote"]))
    return "\n" + "".join(o)

def _ld(k):
    h = H[k]; u = D + "/"
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "@id": D + "/#website", "url": u, "name": "Hunter Foo Media", "publisher": {"@id": D + "/#organization"}},
        {"@type": "WebPage", "@id": u + "#webpage", "url": u, "name": h["title"], "description": h["desc"], "about": {"@id": D + "/#organization"}, "isPartOf": {"@id": D + "/#website"}},
        {"@type": "Person", "@id": D + "/#founder", "name": "Hunter Foo", "jobTitle": "Founder", "image": D + "/assets/hunter-foo-portrait.jpeg",
         "sameAs": ["https://www.linkedin.com/in/hunterfoo3143/"], "worksFor": {"@id": D + "/#organization"}},
        {"@type": "FAQPage", "@id": u + "#faq", "url": u + "#faq", "isPartOf": {"@id": u + "#webpage"},
         "mainEntity": [{"@type": "Question", "name": _faq_plain(q), "acceptedAnswer": {"@type": "Answer", "text": _faq_plain(a)}} for q, a in HFAQ[k]["qa"]]}]}

HOME2 = {k: {"title": H[k]["title"], "desc": H[k]["desc"], "main": _main(k), "ld": _ld(k)} for k in H}
