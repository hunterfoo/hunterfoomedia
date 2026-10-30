ADDRESS = "D-1, 28, Residensi Bandar Razak, Salak Selatan, 57100 Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur, Malaysia"

def _main(h):
    rows = "".join("<tr><th scope=\"row\">%s</th><td>%s</td></tr>" % r for r in h["rows"])
    return ('\n<section class="wrap page-intro">\n<p class="eyebrow"><i></i>%s</p>\n<h1>%s</h1>\n<p class="lede">%s</p>\n</section>\n'
            '<section class="paper"><div class="wrap section prose">\n<h2>%s</h2>\n<table class="biz-id">%s</table>\n'
            '<h2>%s</h2>\n<p>%s</p>\n<p class="agency-note">%s</p>\n</div></section>\n'
            '<section class="wrap section contact" id="contact"><p class="eyebrow"><i></i>%s</p><div class="contact-row"><h2>%s</h2><div class="contact-actions">'
            '<a class="button whatsapp" href="https://wa.me/601133154541" target="_blank" rel="noopener noreferrer">WhatsApp +60 11-3315 4541 <span aria-hidden="true">↗</span></a>'
            '<a class="email-link" href="mailto:hello@hunterfoomedia.com">hello@hunterfoomedia.com <span aria-hidden="true">↗</span></a></div></div></section>\n'
            ) % (h["eyebrow"], h["h1"], h["lede"], h["idh"], rows, h["founderh"], h["founder"], h["note"], h["next"], h["cta"])

def _rows(l):
    return [(l[0], "HF Media Solution"), (l[1], "Hunter Foo Media"), (l[2], "IP0633909-U"), (l[3], l[4]),
            (l[5], "Hunter Foo"), (l[6], '<a href="https://wa.me/601133154541">+60 11-3315 4541</a>'),
            (l[7], '<a href="mailto:hello@hunterfoomedia.com">hello@hunterfoomedia.com</a>'),
            (l[8], '<a href="https://www.hunterfoomedia.com/">www.hunterfoomedia.com</a>'), (l[11], ADDRESS), (l[9], l[10])]

ABOUT = {
 "en": {"title": "About HF Media Solution (IP0633909-U) | Hunter Foo Media",
        "desc": "Hunter Foo Media is a brand of HF Media Solution (IP0633909-U), registered in Malaysia. Business details, founder background and how to reach us.",
        "main": None, "d": dict(eyebrow="ABOUT", h1="Who we are.", lede="Hunter Foo Media is the trading name of HF Media Solution, a business registered in Malaysia. We help service businesses in Malaysia and Singapore win more clients and spend less time on admin.",
        idh="Business details", rows=_rows(["Registered name", "Brand", "Business registration no. (Malaysia)", "Country of registration", "Malaysia", "Founder", "WhatsApp", "Email", "Website", "Service area", "Malaysia and Singapore (remote)", "Address"]),
        founderh="Founder", founder="Hunter Foo started as a CNC programmer in Singapore and has spent 18 years in HR, recruitment and sales. Since 2025 he has run his own company's daily work with AI and built an internal HR app. He only offers clients what he has tested in his own business.",
        note="<strong>Not a recruitment agency.</strong> We don't charge job seekers or place candidates ourselves. The Singapore job posts we manage are published for our client Sky Employment Pte Ltd, a licensed employment agency (MOM EA licence 08C5793). We are based in Kuala Lumpur and serve clients across Malaysia and Singapore, mostly online.", next="CONTACT", cta="Get in touch.")},
 "zh": {"title": "关于我们｜HF Media Solution (IP0633909-U)｜Hunter Foo Media",
        "desc": "Hunter Foo Media 是 HF Media Solution 的品牌，马来西亚注册商业（IP0633909-U）。为服务型生意做 AI 自动化、个人品牌与社媒。WhatsApp +60 11-3315 4541。",
        "main": None, "d": dict(eyebrow="关于我们", h1="我们是谁。", lede="Hunter Foo Media 是 HF Media Solution 的经营品牌，在马来西亚注册。我们帮马来西亚与新加坡的服务型生意多接客户，少做杂事。",
        idh="商业资料", rows=_rows(["注册名称", "品牌", "马来西亚商业注册号", "注册国家", "马来西亚", "创办人", "WhatsApp", "电邮", "网站", "服务地区", "马来西亚与新加坡（远程）", "地址"]),
        founderh="创办人", founder="Hunter Foo 在人力资源、招聘和销售做了 18 年，最早在新加坡做 CNC 编程。2025 年开始把 AI 用进自己公司的日常工作，并做了内部 HR 应用。只做自己用过、有效的东西。",
        note="<strong>不是职业中介。</strong>本商业不向求职者收费，也不自行安排工作。我们管理的新加坡职位贴文，是为客户 Sky Employment Pte Ltd（持牌职业中介，MOM EA 08C5793）发布的。我们位于吉隆坡，服务马来西亚与新加坡的客户，大部分工作在线上完成。", next="联系", cta="和我们聊聊。")},
 "ms": {"title": "Tentang HF Media Solution (IP0633909-U) | Hunter Foo Media",
        "desc": "Hunter Foo Media ialah jenama HF Media Solution, perniagaan berdaftar di Malaysia (IP0633909-U). Automasi AI, jenama peribadi dan media sosial untuk perniagaan servis. WhatsApp +60 11-3315 4541.",
        "main": None, "d": dict(eyebrow="TENTANG KAMI", h1="Siapa kami.", lede="Hunter Foo Media ialah jenama dagangan HF Media Solution, perniagaan berdaftar di Malaysia. Kami bantu perniagaan servis di Malaysia dan Singapura dapat lebih ramai pelanggan dengan kurang kerja remeh.",
        idh="Maklumat perniagaan", rows=_rows(["Nama berdaftar", "Jenama", "No. pendaftaran perniagaan (Malaysia)", "Negara pendaftaran", "Malaysia", "Pengasas", "WhatsApp", "E-mel", "Laman web", "Kawasan servis", "Malaysia dan Singapura (jarak jauh)", "Alamat"]),
        founderh="Pengasas", founder="Hunter Foo mempunyai 18 tahun pengalaman dalam HR, rekrutmen dan jualan, bermula sebagai pengaturcara CNC di Singapura. Sejak 2025 beliau menggunakan AI dalam kerja harian syarikatnya sendiri dan membina aplikasi HR dalaman. Beliau hanya menawarkan apa yang telah digunakan sendiri dan terbukti berkesan.",
        note="<strong>Bukan agensi pekerjaan.</strong> Perniagaan ini tidak mengenakan caj kepada pencari kerja dan tidak menempatkan calon sendiri. Iklan kerja Singapura yang kami urus diterbitkan untuk pelanggan kami Sky Employment Pte Ltd, agensi pekerjaan berlesen (lesen EA MOM 08C5793). Kami berpangkalan di Kuala Lumpur dan berkhidmat untuk pelanggan di seluruh Malaysia dan Singapura, kebanyakannya secara dalam talian.", next="HUBUNGI", cta="Bercakap dengan kami.")},
}
for v in ABOUT.values():
    v["main"] = _main(v["d"])
