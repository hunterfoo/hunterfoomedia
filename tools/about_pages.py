def _main(h):
    rows = "".join("<tr><th scope=\"row\">%s</th><td>%s</td></tr>" % r for r in h["rows"])
    return ('\n<section class="wrap page-intro">\n<p class="eyebrow"><i></i>%s</p>\n<h1>%s</h1>\n<p class="lede">%s</p>\n</section>\n'
            '<section class="paper"><div class="wrap section prose">\n<h2>%s</h2>\n<table class="biz-id">%s</table>\n'
            '<h2>%s</h2>\n<p>%s</p>\n<p class="agency-note">%s</p>\n</div></section>\n'
            '<section class="wrap section contact" id="contact"><p class="eyebrow"><i></i>%s</p><div class="contact-row"><h2>%s</h2><div class="contact-actions">'
            '<a class="button whatsapp" href="https://wa.me/60196273143" target="_blank" rel="noopener noreferrer">WhatsApp +60196273143 <span aria-hidden="true">↗</span></a>'
            '<a class="email-link" href="mailto:hello@hunterfoomedia.com">hello@hunterfoomedia.com <span aria-hidden="true">↗</span></a></div></div></section>\n'
            ) % (h["eyebrow"], h["h1"], h["lede"], h["idh"], rows, h["founderh"], h["founder"], h["note"], h["next"], h["cta"])

def _rows(l):
    return [(l[0], "HF Media Solution"), (l[1], "Hunter Foo Media"), (l[2], "IP0633909-U"), (l[3], l[4]),
            (l[5], "Hunter Foo"), (l[6], '<a href="https://wa.me/60196273143">+60 19-627 3143</a>'),
            (l[7], '<a href="mailto:hello@hunterfoomedia.com">hello@hunterfoomedia.com</a>'),
            (l[8], '<a href="https://www.hunterfoomedia.com/">www.hunterfoomedia.com</a>'), (l[9], l[10])]

ABOUT = {
 "en": {"title": "About HF Media Solution (IP0633909-U) | Hunter Foo Media",
        "desc": "Hunter Foo Media is the brand of HF Media Solution, a Malaysian registered business (IP0633909-U). AI automation, personal branding and social media for service businesses. WhatsApp +60196273143.",
        "main": None, "d": dict(eyebrow="ABOUT", h1="Who we are.", lede="Hunter Foo Media is the trading brand of HF Media Solution, a business registered in Malaysia. We help service businesses in Malaysia and Singapore get more clients with less busywork.",
        idh="Business details", rows=_rows(["Registered name", "Brand", "Business registration no. (Malaysia)", "Country of registration", "Malaysia", "Founder", "WhatsApp", "Email", "Website", "Service area", "Malaysia and Singapore (remote)"]),
        founderh="Founder", founder="Hunter Foo has 18 years in HR, recruitment and sales, starting as a CNC programmer in Singapore. Since 2025 he has used AI in his own company's daily work and built an internal HR app. He only offers what he has used himself and knows works.",
        note="<strong>Not a recruitment agency.</strong> This business does not post jobs or charge job seekers. We work remotely and have no walk-in office.", next="CONTACT", cta="Talk to us.")},
 "zh": {"title": "关于我们｜HF Media Solution (IP0633909-U)｜Hunter Foo Media",
        "desc": "Hunter Foo Media 是 HF Media Solution 的品牌，马来西亚注册商业（IP0633909-U）。为服务型生意做 AI 自动化、个人品牌与社媒。WhatsApp +60196273143。",
        "main": None, "d": dict(eyebrow="关于我们", h1="我们是谁。", lede="Hunter Foo Media 是 HF Media Solution 的经营品牌，在马来西亚注册。我们帮马来西亚与新加坡的服务型生意多接客户，少做杂事。",
        idh="商业资料", rows=_rows(["注册名称", "品牌", "马来西亚商业注册号", "注册国家", "马来西亚", "创办人", "WhatsApp", "电邮", "网站", "服务地区", "马来西亚与新加坡（远程）"]),
        founderh="创办人", founder="Hunter Foo 在人力资源、招聘和销售做了 18 年，最早在新加坡做 CNC 编程。2025 年开始把 AI 用进自己公司的日常工作，并做了内部 HR 应用。只做自己用过、有效的东西。",
        note="<strong>不是职业中介。</strong>本商业不发职位、不向求职者收费。全部远程服务，没有门店。", next="联系", cta="和我们聊聊。")},
 "ms": {"title": "Tentang HF Media Solution (IP0633909-U) | Hunter Foo Media",
        "desc": "Hunter Foo Media ialah jenama HF Media Solution, perniagaan berdaftar di Malaysia (IP0633909-U). Automasi AI, jenama peribadi dan media sosial untuk perniagaan servis. WhatsApp +60196273143.",
        "main": None, "d": dict(eyebrow="TENTANG KAMI", h1="Siapa kami.", lede="Hunter Foo Media ialah jenama dagangan HF Media Solution, perniagaan berdaftar di Malaysia. Kami bantu perniagaan servis di Malaysia dan Singapura dapat lebih ramai pelanggan dengan kurang kerja remeh.",
        idh="Maklumat perniagaan", rows=_rows(["Nama berdaftar", "Jenama", "No. pendaftaran perniagaan (Malaysia)", "Negara pendaftaran", "Malaysia", "Pengasas", "WhatsApp", "E-mel", "Laman web", "Kawasan servis", "Malaysia dan Singapura (jarak jauh)"]),
        founderh="Pengasas", founder="Hunter Foo mempunyai 18 tahun pengalaman dalam HR, rekrutmen dan jualan, bermula sebagai pengaturcara CNC di Singapura. Sejak 2025 beliau menggunakan AI dalam kerja harian syarikatnya sendiri dan membina aplikasi HR dalaman. Beliau hanya menawarkan apa yang telah digunakan sendiri dan terbukti berkesan.",
        note="<strong>Bukan agensi pekerjaan.</strong> Perniagaan ini tidak mengiklankan jawatan atau mengenakan caj kepada pencari kerja. Kami bekerja secara jarak jauh tanpa pejabat fizikal.", next="HUBUNGI", cta="Bercakap dengan kami.")},
}
for v in ABOUT.values():
    v["main"] = _main(v["d"])
