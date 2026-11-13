# Simplified homepage (EN / ZH / MS): core line verbatim (H[k]["pos"] from home_pages), no definition line,
# Hero, the five services, a brief six-piece overview linking to /services/, one CTA.
import urllib.parse, html
from home_pages import H
from services_page import P as SP

WA = "https://wa.me/60196273143"
D = "https://www.hunterfoomedia.com"

META = {
 "en": ("AI Agency in Malaysia | Hunter Foo Media",
        "AI agency in Kuala Lumpur. We ease your company's anxiety about AI and help you keep pace with AI. Serving Malaysia and Singapore. WhatsApp +60196273143."),
 "zh": ("马来西亚 AI Agency｜Hunter Foo Media",
        "吉隆坡的 AI agency。解决企业对 AI 的焦虑，帮你跟上 AI 的脚步。服务马来西亚与新加坡企业。WhatsApp +60196273143。"),
 "ms": ("Agensi AI (AI Agency) di Malaysia | Hunter Foo Media",
        "Agensi AI (AI agency) di Kuala Lumpur. Kami meredakan keresahan syarikat anda terhadap AI, dan membantu anda mengikuti rentak AI. Untuk perniagaan di Malaysia dan Singapura."),
}
for _k, (_t, _d) in META.items():
    assert H[_k]["pos"] in _d  # core line verbatim
    H[_k]["title"], H[_k]["desc"] = _t, _d

X = {}
X["en"] = dict(
 see="See our services", sve="WHAT WE DO", svh="Five services",
 lines=["A monthly meeting, and your first main digital employee set up for free.",
        "A company website that Google and AI assistants can read and find.",
        "Your web pages and Google Business Profile, kept up to date.",
        "8 posts and 2 AI reels a month. You approve before anything is published.",
        "Built around your company: an AI that answers from your documents, workflows, calendar and more."],
 tags=["By quote", "RM399 · founding price", "RM499/month · founding price", "By quote", "By quote"],
 aie="SIX DIGITAL EMPLOYEES", aih="Three serve your customers. Three help your team.", out="Outside", inn="Inside", aigo="See what each one does →",
 cnote="Malaysian number +60196273143. English, <span lang=\"zh-Hans\">中文</span> or BM.")
X["zh"] = dict(
 see="看我们的服务", sve="我们做什么", svh="五项服务",
 lines=["每月开会一次，并免费设立你的第一位主要数字员工。",
        "Google 和 AI 助手读得懂、找得到的公司网站。",
        "网页和 Google Business Profile，持续更新。",
        "每月 8 篇帖子加 2 条 AI 短视频，你批准后才发布。",
        "按你的公司量身做：用公司资料回答问题的 AI、自动流程、日历等。"],
 tags=["按报价", "RM399 · 创始价", "每月 RM499 · 创始价", "按报价", "按报价"],
 aie="六位数字员工", aih="三位服务客户，三位帮团队。", out="对外", inn="对内", aigo="看每一位做什么 →",
 cnote="马来西亚号码 +60196273143。中文、英文或马来文都可以。")
X["ms"] = dict(
 see="Lihat perkhidmatan kami", sve="APA KAMI BUAT", svh="Lima perkhidmatan",
 lines=["Mesyuarat sebulan sekali, dan pekerja digital utama pertama anda disediakan percuma.",
        "Laman web syarikat yang boleh dibaca dan ditemui oleh Google dan pembantu AI.",
        "Halaman web dan Google Business Profile anda, sentiasa dikemas kini.",
        "8 hantaran dan 2 reel AI sebulan. Anda luluskan sebelum diterbitkan.",
        "Dibina khas untuk syarikat anda: AI yang menjawab daripada dokumen anda, aliran kerja, kalendar dan lagi."],
 tags=["Ikut sebut harga", "RM399 · harga pelanggan awal", "RM499/bulan · harga pelanggan awal", "Ikut sebut harga", "Ikut sebut harga"],
 aie="ENAM PEKERJA DIGITAL", aih="Tiga melayan pelanggan anda. Tiga membantu pasukan anda.", out="Di luar", inn="Di dalam", aigo="Lihat apa setiap satu buat →",
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
    cards = "".join('<li><a href="/services/#%s"><span class="hm-n">%d</span><h3>%s</h3><p>%s</p><p class="hm-price">%s</p></a></li>' % (sid, i + 1, name, x["lines"][i], x["tags"][i])
                    for i, (sid, name, d_, p_, l_) in enumerate(s["services"]))
    o.append('<section class="paper hm-sec" id="services"><div class="wrap section"><p class="pd-kicker">%s</p><h2 class="hm-h2">%s</h2>'
             '<ol class="hm-cards hm-cards-light hm-cards-5 hm-svc">%s</ol></div></section>\n' % (x["sve"], x["svh"], cards))
    chips = lambda a, b: "".join('<span class="hm-chip">%s</span>' % s["six"][i][0] for i in range(a, b))
    o.append('<section class="wrap section hm-sec hm-dark" id="six"><p class="eyebrow"><i></i>%s</p><h2 class="hm-h2">%s</h2>'
             '<p class="hm-six-l">%s</p><div class="hm-chips">%s</div><p class="hm-six-l">%s</p><div class="hm-chips">%s</div>'
             '<p class="hm-links"><a class="hm-link" href="/services/#ai-can-do">%s</a></p></section>\n'
             % (x["aie"], x["aih"], x["out"], chips(0, 3), x["inn"], chips(3, 6), x["aigo"]))
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
         "sameAs": ["https://www.linkedin.com/in/hunterfoo3143/"], "worksFor": {"@id": D + "/#organization"}}]}

HOME2 = {k: {"title": H[k]["title"], "desc": H[k]["desc"], "main": _main(k), "ld": _ld(k)} for k in H}
