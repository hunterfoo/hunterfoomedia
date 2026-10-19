#!/usr/bin/env python3
"""Generate EN (/), ZH (/zh/), MS (/ms/) pages from the Chinese source in tools/src_zh/.
Run from repo root: python3 tools/build_i18n.py"""
import re, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from i18n_strings import T
from about_pages import ABOUT
from products_pages import PRODUCTS
D = "https://www.hunterfoomedia.com"
SRC = "tools/src_zh"
PAGES = ["/", "/services/", "/services/ai-automation/", "/services/personal-brand/", "/services/social-reels/"]
ALL = PAGES + ["/products/", "/about/"]
LANGS = {"en": ("", "en", "en_MY", "EN"), "zh": ("/zh", "zh-Hans", "zh_MY", "中文"), "ms": ("/ms", "ms", "ms_MY", "BM")}
IDX = {"en": 0, "ms": 1}
C = r'[\u3000-\u9fff\uff00-\uffef]'
LEGAL = {"en": "About", "zh": "关于我们", "ms": "Tentang Kami"}
MENU = {"en": ("Menu", "Close"), "zh": ("菜单", "关闭"), "ms": ("Menu", "Tutup")}
SUF = {"en": " a year", "ms": " setahun"}

ORG = {"@type": "Organization", "@id": D + "/#organization", "name": "Hunter Foo Media",
       "legalName": "HF Media Solution", "alternateName": "Hunter Foo Media",
       "identifier": {"@type": "PropertyValue", "propertyID": "Malaysia business registration (SSM)", "value": "IP0633909-U"},
       "url": D + "/", "logo": D + "/assets/hfm-logo.png", "email": "hello@hunterfoomedia.com", "telephone": "+60196273143",
       "areaServed": [{"@type": "Country", "name": "Malaysia"}, {"@type": "Country", "name": "Singapore"}],
       "sameAs": ["https://web.facebook.com/hunterfooai/", "https://www.linkedin.com/in/hunterfoo3143/"],
       "founder": {"@id": D + "/#founder"},
       "contactPoint": [{"@type": "ContactPoint", "telephone": "+60196273143", "email": "hello@hunterfoomedia.com",
                         "contactType": "customer service", "url": "https://wa.me/60196273143",
                         "availableLanguage": ["en", "zh-Hans"], "areaServed": ["MY", "SG"]}]}

def tr(s, lang):
    if lang == "zh": return s
    i = IDX[lang]
    def sub_text(m):
        raw = m.group(1); core = raw.strip()
        if core in T:
            lead = raw[:len(raw) - len(raw.lstrip())]; trail = raw[len(raw.rstrip()):]
            return ">" + lead + T[core][i] + trail + "<"
        return m.group(0)
    def sub_q(m):
        core = m.group(1)
        return '"' + T[core][i].replace('"', '&quot;' if m.group(0) else '"') + '"' if core in T else m.group(0)
    s = re.sub(r'>([^<>]*' + C + r'[^<>]*)<', sub_text, s)
    s = re.sub(r'"([^"<>]*' + C + r'[^"<>]*)"', lambda m: '"' + T[m.group(1)][i].replace('"', '\u201d') + '"' if m.group(1) in T else m.group(0), s)
    return s

def L(p, path):  # localized absolute path
    return p + path

def rewrite_urls(s, p):
    if not p: return s
    s = re.sub(r'href="/(?!/|assets/|zh/|ms/|[^"]*\.(?:css|js|png|jpg|webp|svg|ico|xml|txt|pdf)")([^"]*)"', lambda m: 'href="%s/%s"' % (p, m.group(1)), s)
    s = re.sub(re.escape(D) + r'/(?!assets/|#organization|#founder|#website|zh/|ms/)([^"\s?]*)', lambda m: "%s%s/%s" % (D, p, m.group(1)), s)
    return s

def alternates(path):
    out = ['<link rel="alternate" hreflang="%s" href="%s%s%s">' % (LANGS[k][1], D, LANGS[k][0], path) for k in LANGS]
    out.append('<link rel="alternate" hreflang="x-default" href="%s%s">' % (D, path))
    return "\n".join(out)

def switcher(path, lang):
    a = []
    for k, (p, hl, _, label) in LANGS.items():
        cur = ' aria-current="true"' if k == lang else ''
        a.append('<a href="%s%s" hreflang="%s" lang="%s"%s>%s</a>' % (p, path, hl, hl, cur, label))
    return '<div class="lang-switch" role="navigation" aria-label="Language">' + ' <span aria-hidden="true">|</span> '.join(a) + '</div>'

def legal(lang, p):
    return ('<p class="legal">© <span id="year">2026</span> HF Media Solution (IP0633909-U) · Hunter Foo Media · '
            'WhatsApp <a href="https://wa.me/60196273143">+60 19-627 3143</a> · <a href="mailto:hello@hunterfoomedia.com">hello@hunterfoomedia.com</a> · '
            '<a href="%s/about/">%s</a></p>' % (p, LEGAL[lang]))

def fix_jsonld(s, lang, path):
    p, hl = LANGS[lang][0], LANGS[lang][1]
    def fix(m):
        data = json.loads(m.group(1))
        g = data.get("@graph", [data])
        g = [n for n in g if n.get("@type") != "Organization"]
        for n in g:
            if "inLanguage" in n: n["inLanguage"] = hl
            if n.get("@type") in ("WebPage", "FAQPage", "AboutPage"): n["inLanguage"] = hl
            if n.get("@type") == "WebSite": n["url"] = D + "/"; n["inLanguage"] = ["en", "zh-Hans", "ms"]
            if n.get("@type") == "Person": n["url"] = D + p + "/about/"
        g.insert(0, ORG)
        return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, separators=(",", ":")) + '</script>'
    return re.sub(r'<script type="application/ld\+json">(.*?)</script>', fix, s, flags=re.S)

def build(src, path, lang):
    p, hl, loc, _ = LANGS[lang]
    s = src
    if lang != "zh":
        s = s.replace('"一年 "+f(one*12)', 'f(one*12)+"%s"' % SUF[lang]).replace('"一年 "+f(one)', 'f(one)+"%s"' % SUF[lang])
        s = s.replace('(i==="y1"||i==="y12"?"一年 ":"")+"RM ____"', '"RM ____"+(i==="y1"||i==="y12"?"%s":"")' % SUF[lang])
    s = tr(s, lang)
    s = s.replace('href="/#about"', 'href="/about/"')
    s = rewrite_urls(s, p)
    s = re.sub(r'<html lang="[^"]*">', '<html lang="%s">' % hl, s, 1)
    s = s.replace('content="zh_MY"', 'content="%s"' % loc)
    s = re.sub(r'(<link rel="canonical" href="[^"]*">)', lambda m: m.group(1) + "\n" + alternates(path), s, 1)
    s = fix_jsonld(s, lang, path)
    sw = switcher(path, lang)
    if '<a class="btn sm wa"' in s:
        s = s.replace('<a class="btn sm wa"', sw + '\n    <a class="btn sm wa"', 1)
    else:
        s = s.replace('<div class="header-actions">', '<div class="header-actions">' + sw, 1)
    # mobile hamburger menu
    ml = MENU[lang]
    btn = ('<button type="button" class="menu-toggle" aria-expanded="false" aria-controls="site-menu" data-open="%s" data-close="%s">'
           '<span class="bars" aria-hidden="true"></span><span class="lbl">%s</span></button>\n') % (ml[0], ml[1], ml[0])
    s = re.sub(r'<nav( class="compact")? aria-label="([^"]*)">', lambda m: btn + '<nav id="site-menu"%s aria-label="%s">' % (m.group(1) or '', m.group(2)), s, 1)
    hn = re.search(r'<nav id="site-menu".*?</nav>', s, re.S)
    if hn and ('href="%s/about/"' % p) not in hn.group(0):
        s = s[:hn.end() - 6] + '<a class="m-only" href="%s/about/">%s</a>' % (p, LEGAL[lang]) + s[hn.end() - 6:]
    s = s.replace('</head>', '<link rel="stylesheet" href="/assets/mobile-nav.css">\n</head>', 1)
    s = s.replace('</body>', '<script src="/assets/mobile-nav.js" defer></script>\n</body>', 1)
    s = re.sub(r'<p style="margin-top:10px;font-size:12.5px">© <span id="year">2026</span> Hunter Foo Media</p>', '', s)
    s = s.replace('<span>© <span id="year">2026</span> Hunter Foo Media</span>', '<span>Hunter Foo Media</span>')
    s = s.replace('</footer>', legal(lang, p) + '\n</footer>', 1)
    if lang == "en": s = re.sub(r'\s*<p class="en">.*?</p>', '', s)
    if lang != "zh":
        left = sorted(set(re.findall(r'[^<>"]*' + C + r'[^<>"]*', re.sub(r'<script.*?</script>|lang="zh-Hans"[^>]*>[^<]*', '', s, flags=re.S))))
        left = [x for x in left if x.strip() not in ("中文",)]
        if left: print("UNTRANSLATED", lang, path, left)
    return s

import hashlib
def _v(m):
    fp = m.group(2).lstrip("/")
    if not os.path.isfile(fp): return m.group(0)
    return '%s%s?v=%s"' % (m.group(1), m.group(2), hashlib.md5(open(fp, "rb").read()).hexdigest()[:8])

def bust(html):
    # cache-busting: version every local css/js reference by content hash
    return re.sub(r'((?:href|src)=")(/(?:assets/)?[A-Za-z0-9._-]+\.(?:css|js))"', _v, html)

def write(lang, path, html):
    html = bust(html)
    out = (LANGS[lang][0].lstrip("/") + path).lstrip("/")
    os.makedirs(out or ".", exist_ok=True) if out else None
    with open(os.path.join(out, "index.html"), "w") as f: f.write(html)

for lang in LANGS:
    for path in PAGES:
        src = open(os.path.join(SRC, path.lstrip("/"), "index.html")).read()
        write(lang, path, build(src, path, lang))
    # About page: built from the AI automation page shell
    shell = open(os.path.join(SRC, "services/ai-automation/index.html")).read()
    a = ABOUT[lang]
    shell = re.sub(r'<title>.*?</title>', '<title>%s</title>' % a["title"], shell)
    shell = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % a["desc"], shell)
    shell = re.sub(r'<meta (property|name)="(og|twitter):title" content="[^"]*">', lambda m: '<meta %s="%s:title" content="%s">' % (m.group(1), m.group(2), a["title"]), shell)
    shell = re.sub(r'<meta (property|name)="(og|twitter):description" content="[^"]*">', lambda m: '<meta %s="%s:description" content="%s">' % (m.group(1), m.group(2), a["desc"]), shell)
    shell = shell.replace(D + "/services/ai-automation/", D + "/about/").replace(' aria-current="page"', '')
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "AboutPage", "@id": D + "/about/#webpage", "url": D + "/about/", "name": a["title"], "description": a["desc"], "about": {"@id": D + "/#organization"}, "isPartOf": {"@id": D + "/#website"}},
        {"@type": "Person", "@id": D + "/#founder", "name": "Hunter Foo", "jobTitle": "Founder", "image": D + "/assets/hunter-foo-portrait.jpeg", "sameAs": ["https://www.linkedin.com/in/hunterfoo3143/"], "worksFor": {"@id": D + "/#organization"}}]}
    shell = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>', shell, flags=re.S)
    shell = re.sub(r'<main id="main">.*</main>', lambda m: '<main id="main">' + a["main"] + '</main>', shell, flags=re.S)
    write(lang, "/about/", build(shell, "/about/", lang))

    # Products + demo page: same shell pattern as About
    shell = open(os.path.join(SRC, "services/ai-automation/index.html")).read()
    a = PRODUCTS[lang]
    shell = re.sub(r'<title>.*?</title>', '<title>%s</title>' % a["title"], shell)
    shell = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % a["desc"], shell)
    shell = re.sub(r'<meta (property|name)="(og|twitter):title" content="[^"]*">', lambda m: '<meta %s="%s:title" content="%s">' % (m.group(1), m.group(2), a["title"]), shell)
    shell = re.sub(r'<meta (property|name)="(og|twitter):description" content="[^"]*">', lambda m: '<meta %s="%s:description" content="%s">' % (m.group(1), m.group(2), a["desc"]), shell)
    shell = shell.replace(D + "/services/ai-automation/", D + "/products/").replace(' aria-current="page"', '')
    shell = shell.replace('<a href="/products/">', '<a href="/products/" aria-current="page">')
    shell = shell.replace('<link rel="stylesheet" href="/styles.css">', '<link rel="stylesheet" href="/styles.css">\n<link rel="stylesheet" href="/assets/products.css">')
    pu = D + "/products/"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": pu + "#webpage", "url": pu, "name": a["title"], "description": a["desc"], "about": {"@id": D + "/#organization"}, "isPartOf": {"@id": D + "/#website"}}] + [
        {"@type": "Service", "@id": pu + "#product-%d" % (i + 1), "name": n, "description": d, "serviceType": "AI automation", "provider": {"@id": D + "/#organization"},
         "areaServed": [{"@type": "Country", "name": "Malaysia"}, {"@type": "Country", "name": "Singapore"}], "url": pu + "#demo-%d" % (i + 1)} for i, (n, d) in enumerate(a["services"])] + [
        {"@type": "Service", "@id": pu + "#chatgpt-ads", "name": a["ads_service"][0], "description": a["ads_service"][1], "serviceType": "ChatGPT Ads", "provider": {"@id": D + "/#organization"},
         "areaServed": [{"@type": "Country", "name": "Malaysia"}, {"@type": "Country", "name": "Singapore"}], "url": pu + "#chatgpt-ads"}]}
    shell = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>', shell, flags=re.S)
    shell = re.sub(r'<main id="main">.*</main>', lambda m: '<main id="main">' + a["main"] + '</main>', shell, flags=re.S)
    write(lang, "/products/", build(shell, "/products/", lang))

# sitemap
urls = []
for path in ALL:
    for k in LANGS:
        alt = "".join('\n    <xhtml:link rel="alternate" hreflang="%s" href="%s%s%s"/>' % (LANGS[j][1], D, LANGS[j][0], path) for j in LANGS)
        alt += '\n    <xhtml:link rel="alternate" hreflang="x-default" href="%s%s"/>' % (D, path)
        urls.append('  <url>\n    <loc>%s%s%s</loc>%s\n  </url>' % (D, LANGS[k][0], path, alt))
open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")
print("done")
