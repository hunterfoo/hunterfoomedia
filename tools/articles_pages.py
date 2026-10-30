# Articles section: index + article pages (EN / ZH / MS), built by build_i18n.py.
# Write each language natively. No ranking promises, no timelines, no invented numbers, no client names.
WA = "https://wa.me/60196273143"

INDEX = {
 "en": {"title": "Articles | Hunter Foo Media",
        "desc": "Practical notes for small businesses in Malaysia and Singapore on ads, hiring, content and AI automation. Written from real work, no hype.",
        "eyebrow": "ARTICLES", "h1": "Articles.", "lede": "Practical notes on ads, hiring, content and automation for small businesses in Malaysia and Singapore. Written from what we actually do.",
        "read": "Read the article", "crumb": "Home", "next": "CONTACT", "cta": "Ask us a question.", "wa": "Hi Hunter, I read your articles and have a question:"},
 "zh": {"title": "文章｜Hunter Foo Media",
        "desc": "写给马来西亚与新加坡中小企业的实用笔记：广告、招聘、内容与 AI 自动化。从实际工作出发，不吹牛。",
        "eyebrow": "文章", "h1": "文章。", "lede": "写给马来西亚和新加坡中小企业的实用笔记：广告、招聘、内容和自动化。都是我们实际在做的事。",
        "read": "阅读全文", "crumb": "首页", "next": "联系", "cta": "有问题直接问。", "wa": "你好 Hunter，我看了你的文章，想问："},
 "ms": {"title": "Artikel | Hunter Foo Media",
        "desc": "Nota praktikal untuk perniagaan kecil di Malaysia dan Singapura tentang iklan, pengambilan pekerja, kandungan dan automasi AI. Ditulis daripada kerja sebenar.",
        "eyebrow": "ARTIKEL", "h1": "Artikel.", "lede": "Nota praktikal tentang iklan, pengambilan pekerja, kandungan dan automasi untuk perniagaan kecil di Malaysia dan Singapura. Berdasarkan kerja yang kami buat sendiri.",
        "read": "Baca artikel", "crumb": "Utama", "next": "HUBUNGI", "cta": "Tanya kami.", "wa": "Hai Hunter, saya baca artikel anda dan ada soalan:"},
}

META_HELP = "https://www.facebook.com/business/help/1537759006681893"
TAFEP = "https://www.tal.sg/tafep/employment-practices/recruitment/writing-job-advertisements"
PDPC = "https://www.pdpc.gov.sg/organisations/regulations-decisions/regulatory-guidance/advisory-guidelines-on-the-personal-data-protection-act-for-nric-and-other-national-identification-numbers"

def ext(url, text):
    return '<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>' % (url, text)

ART_EN = """
<p>Facebook and Instagram are where a lot of people scroll after work, on the MRT, or during lunch. A hiring ad there can reach people who are not checking job portals that week. It can also burn money fast if you set it up like a product ad. Here is what we tell Singapore SMEs before they spend on Meta hiring ads.</p>

<h2>1. Meta treats job ads as their own category</h2>
<p>Meta counts an ad as an employment ad when it promotes or links to a job opportunity: full-time or part-time roles, internships, job fairs, or company perks shown alongside openings. General career advice does not count.</p>
<p>For employment ads Meta has a Special Ad Category called <strong>Employment</strong>. You must choose it if you are an advertiser based in the US, or if your ads reach people in the US, Canada or a list of European countries. When it applies, targeting is limited:</p>
<ul>
<li>Age is fixed at 18 to 65+, and you cannot pick a gender.</li>
<li>No postcode targeting and no location exclusions. Targeting a city, address or pin widens to a minimum radius (25 km in the US and Canada, 15 km in Europe).</li>
<li>No demographic or behaviour targeting, only a limited set of approved interests, and no lookalike audiences.</li>
</ul>
<p>If you are a Singapore business and your ads only reach Singapore or Malaysia, Meta does not currently force these restrictions on you, but Ads Manager may still ask whether your campaign is an employment ad. Meta changes these rules from time to time, so check its help page, %s, on the day you set up the campaign.</p>

<h2>2. Do not use targeting to filter people out</h2>
<p>Even where the Employment category is not mandatory, avoid narrowing your audience by age or gender to screen candidates. Meta's advertising policies do not allow discriminatory ads, and in Singapore the Tripartite Guidelines on Fair Employment Practices ask employers to select on skills, experience and qualifications.</p>
<p>The same applies to your wording. TAFEP's %s lists phrases to avoid: age ranges such as "below 30 only", "preferably female", race or religion preferences, and nationality preferences, including lines like "Malaysians welcome". Language requirements need a job-related reason.</p>
<p>What works better is a reasonable location (where people can realistically commute from) and an ad that does the filtering for you by being specific about the job.</p>

<h2>3. Write the ad like a job, not a slogan</h2>
<ul>
<li><strong>First line:</strong> job title and area. "Warehouse assistant, Tuas" beats "Join our growing family!"</li>
<li><strong>The facts people decide on:</strong> pay range if you can share it, working days and shift hours, and three or four real requirements.</li>
<li><strong>What happens next:</strong> "Message us on WhatsApp, we reply within the day" tells people exactly what to do.</li>
<li><strong>A real picture:</strong> the actual workplace, the team at work, or a clean text card with the job title. Stock photos of a smiling office team for a warehouse role attract the wrong people.</li>
<li><strong>No overpromising:</strong> "easy money" or "high pay, no experience" invites rejection and people who drop out at the interview stage.</li>
</ul>
<p>Keep the caption short and easy to scan. If many of your applicants read Chinese or Malay, a separate ad in that language usually reads better than one long mixed caption.</p>

<h2>4. Let applicants reach you on WhatsApp</h2>
<p>Most job seekers here would rather send a WhatsApp message than fill in a long form. Meta lets you run ads that open a WhatsApp chat in one tap. Before the ad goes live, prepare:</p>
<ul>
<li>A greeting that asks three or four simple questions: which job, which area they live in, when they can start, and their relevant experience.</li>
<li>Quick replies for the questions you get every day: pay, hours, location, transport.</li>
<li>Labels in WhatsApp Business (new, screened, interview booked, hired, not suitable) so nobody falls through the cracks.</li>
</ul>
<p>Do not ask for full NRIC numbers over chat. Singapore's PDPC has %s that limit when organisations may collect them.</p>

<h2>5. Speed of reply matters more than the ad</h2>
<p>People who reply to a hiring ad on social media are often messaging several employers at the same time. The ad gets you the conversation; your reply decides whether they show up.</p>
<ul>
<li>Name one person who owns the inbox while the ad is running, and give them fixed times in the day to clear it.</li>
<li>Offer two or three interview slots instead of asking "when are you free?"</li>
<li>Send a reminder the day before and on the morning of the interview.</li>
<li>When the role is filled, tell the people still waiting. It keeps your page's name clean for the next round.</li>
</ul>

<h2>6. Measure conversations and interviews, not likes</h2>
<p>A hiring ad with many likes and few messages has not done its job. Track how many people messaged, how many passed your basic questions, how many attended an interview, and how many started work. Start with a modest budget, change one thing at a time (the image, the first line, the location), and only spend more once people are actually turning up.</p>

<h2>Where we can help</h2>
<p>Hunter Foo Media plans and runs Meta ads for small businesses in Singapore and Malaysia, including hiring ads: campaign setup, caption and image, the WhatsApp reply flow, and a simple report on what is happening. You approve every ad before it runs. We cannot promise a number of applicants or hires, and we are not a recruitment agency, so the hiring decisions stay with you. Fees are by written quote.</p>
""" % (ext(META_HELP, "About ads for employment"), ext(TAFEP, "guide to writing fair job advertisements"), ext(PDPC, "advisory guidelines on NRIC numbers"))

ART_ZH = """
<p>很多人下班、搭 MRT、午休的时候都在刷 Facebook 和 Instagram。招聘广告投在这里，能碰到那些这个星期根本没打开求职网站的人。但如果当成卖产品的广告来投，钱也花得很快。下面是我们和新加坡中小企业老板投 Meta 招聘广告前，一定会先讲清楚的几件事。</p>

<h2>1. 在 Meta 眼里，招聘广告是单独一类</h2>
<p>只要广告在推广或链接到工作机会，例如全职、兼职、实习、招聘会，或者在招人的同时介绍公司福利，Meta 就当它是就业类广告。单纯分享职场建议不算。</p>
<p>就业类广告在 Meta 有一个特殊广告类别，叫 <strong>Employment（就业）</strong>。如果你是美国的广告主，或者广告会投到美国、加拿大和部分欧洲国家，就必须选这个类别。一旦适用，定位会被限制：</p>
<ul>
<li>年龄固定 18 到 65 岁以上，不能选性别。</li>
<li>不能按邮区定位，也不能排除地区。选城市、地址或定位点时，范围会被扩大到最小半径（美国和加拿大 25 公里，欧洲 15 公里）。</li>
<li>不能用人口统计和行为定位，兴趣只能从有限的核准名单里选，也不能用类似受众（Lookalike）。</li>
</ul>
<p>如果你是新加坡公司，广告只投新加坡或马来西亚，Meta 目前没有强制这些限制，但广告管理工具仍可能问你这是不是就业类广告。Meta 会不时调整规则，开广告当天请以官方说明 %s 为准。</p>

<h2>2. 别用定位来“筛人”</h2>
<p>就算 Employment 类别不是强制的，也不要靠年龄、性别把受众收窄来挑人。Meta 的广告政策不允许歧视性广告；新加坡的《公平雇佣实践三方指导原则》也要求雇主按技能、经验和资历来选人。</p>
<p>文案也一样。TAFEP 的 %s 列出了要避免的写法：“30 岁以下”这类年龄限制、“女性优先”、种族或宗教偏好，以及国籍偏好，连“欢迎马来西亚人”这种句子也在里面。语言要求则要有和工作相关的理由。</p>
<p>更有效的做法是：地区设在应征者真的通勤得到的范围，然后把工作写清楚，让广告自己帮你过滤。</p>

<h2>3. 广告要写得像一份工作，不像口号</h2>
<ul>
<li><strong>第一行：</strong>职位加地区。“Tuas 仓库助理”比“加入我们大家庭！”有用得多。</li>
<li><strong>别人做决定要看的资料：</strong>能公开就写薪资范围、上班日和班次时间，再加三四个真实要求。</li>
<li><strong>下一步怎么做：</strong>“WhatsApp 我们，当天回复”，一句话讲清楚。</li>
<li><strong>用真实的图：</strong>真实工作环境、团队在做事的样子，或者一张写着职位的简洁文字图。仓库职位配一张办公室笑脸图库照，只会招来不对的人。</li>
<li><strong>不要夸大：</strong>“轻松赚钱”“高薪免经验”这种字眼容易被拒登，也会招来到面试就消失的人。</li>
</ul>
<p>文案短一点，一眼看得完。如果很多应征者看中文或马来文，另开一条该语言的广告，通常比一大段中英混写好读。</p>

<h2>4. 让应征者直接 WhatsApp 你</h2>
<p>这里大部分求职者宁愿发 WhatsApp，也不想填一张长表格。Meta 可以投一点就打开 WhatsApp 对话的广告。上线前先准备好：</p>
<ul>
<li>一段欢迎语，问三四个简单问题：应征哪个职位、住哪一区、什么时候能开工、有没有相关经验。</li>
<li>每天都会被问的快捷回复：薪水、工时、地点、交通。</li>
<li>WhatsApp Business 标签（新询问、已初筛、已约面试、已录用、不合适），谁都不会漏掉。</li>
</ul>
<p>不要在聊天里要对方的完整 NRIC 号码。新加坡 PDPC 有 %s，限制机构什么时候可以收集。</p>

<h2>5. 回复速度比广告本身更重要</h2>
<p>在社媒上回应招聘广告的人，往往同时在问好几家。广告帮你拿到对话，你的回复决定对方会不会出现。</p>
<ul>
<li>广告在跑的期间，指定一个人负责回复，每天固定几个时间清消息。</li>
<li>直接给两三个面试时段，不要问“你什么时候有空？”</li>
<li>面试前一天和当天早上各提醒一次。</li>
<li>职位招满了，跟还在等的人说一声。下一轮招人时，专页的名声还是干净的。</li>
</ul>

<h2>6. 看对话和面试，不看点赞</h2>
<p>一条招聘广告点赞很多、私讯很少，就是没做到它该做的事。要记的是：多少人发了消息、多少人通过基本问题、多少人来面试、多少人真的上班。预算先从小开始，一次只改一样（图片、第一行、地区），等真的有人来面试了再加钱。</p>

<h2>我们能帮什么</h2>
<p>Hunter Foo Media 帮新加坡和马来西亚的中小企业规划和投放 Meta 广告，包括招聘广告：开设广告活动、写文案做图、设好 WhatsApp 回复流程，再给你一份看得懂的简单报告。每条广告上线前都由你确认。我们不能保证有多少人应征或录用；我们也不是职业中介，录不录用由你决定。费用以书面报价为准。</p>
""" % (ext(META_HELP, "About ads for employment"), ext(TAFEP, "公平招聘广告写作指南"), ext(PDPC, "关于 NRIC 号码的咨询指南"))

ART_MS = """
<p>Ramai orang membuka Facebook dan Instagram selepas kerja, dalam MRT atau masa rehat makan tengah hari. Iklan kerja di situ boleh sampai kepada orang yang minggu itu langsung tidak membuka portal kerja. Tapi kalau disediakan macam iklan produk, bajet boleh habis dengan cepat. Ini perkara yang kami terangkan kepada PKS di Singapura sebelum mereka berbelanja untuk iklan pengambilan pekerja di Meta.</p>

<h2>1. Meta letak iklan kerja dalam kategori tersendiri</h2>
<p>Meta anggap sesuatu iklan itu iklan pekerjaan apabila ia mempromosikan atau memaut kepada peluang kerja: jawatan sepenuh masa atau separuh masa, latihan industri, pameran kerjaya, atau faedah syarikat yang ditunjukkan bersama jawatan kosong. Nasihat kerjaya secara umum tidak termasuk.</p>
<p>Untuk iklan pekerjaan, Meta ada Kategori Iklan Khas bernama <strong>Employment</strong>. Anda wajib memilihnya jika anda pengiklan yang berpangkalan di Amerika Syarikat, atau iklan anda sampai kepada orang di AS, Kanada atau beberapa negara Eropah. Apabila ia terpakai, sasaran dihadkan:</p>
<ul>
<li>Umur ditetapkan 18 hingga 65+, dan jantina tidak boleh dipilih.</li>
<li>Tiada sasaran poskod dan tiada pengecualian lokasi. Sasaran bandar, alamat atau pin akan diluaskan kepada radius minimum (25 km di AS dan Kanada, 15 km di Eropah).</li>
<li>Tiada sasaran demografi atau tingkah laku, minat terhad kepada senarai yang diluluskan, dan tiada lookalike audience.</li>
</ul>
<p>Jika anda perniagaan Singapura dan iklan hanya sampai ke Singapura atau Malaysia, buat masa ini Meta tidak mewajibkan sekatan tersebut, tetapi Ads Manager mungkin masih bertanya sama ada kempen anda iklan pekerjaan. Peraturan Meta berubah dari semasa ke semasa, jadi semak halaman bantuannya, %s, pada hari anda menyediakan kempen.</p>

<h2>2. Jangan guna sasaran untuk menapis orang</h2>
<p>Walaupun kategori Employment tidak wajib, elakkan menyempitkan khalayak mengikut umur atau jantina untuk memilih calon. Polisi pengiklanan Meta tidak membenarkan iklan yang mendiskriminasi, dan di Singapura, Tripartite Guidelines on Fair Employment Practices meminta majikan memilih berdasarkan kemahiran, pengalaman dan kelayakan.</p>
<p>Begitu juga dengan ayat iklan. %s daripada TAFEP menyenaraikan frasa yang perlu dielakkan: had umur seperti "bawah 30 sahaja", "perempuan diutamakan", keutamaan kaum atau agama, dan keutamaan kewarganegaraan, termasuk ayat seperti "Malaysians welcome". Syarat bahasa pula perlu ada sebab yang berkaitan dengan kerja.</p>
<p>Cara yang lebih berkesan: tetapkan lokasi yang munasabah (kawasan yang calon betul-betul boleh berulang-alik), dan biar iklan itu sendiri yang menapis dengan menerangkan kerja secara jelas.</p>

<h2>3. Tulis iklan macam tawaran kerja, bukan slogan</h2>
<ul>
<li><strong>Baris pertama:</strong> jawatan dan kawasan. "Pembantu gudang, Tuas" lebih berkesan daripada "Sertai keluarga kami!"</li>
<li><strong>Fakta yang orang guna untuk buat keputusan:</strong> julat gaji jika boleh dikongsi, hari bekerja dan waktu syif, serta tiga atau empat syarat sebenar.</li>
<li><strong>Langkah seterusnya:</strong> "WhatsApp kami, kami balas pada hari yang sama" terus beritahu orang apa perlu dibuat.</li>
<li><strong>Gambar sebenar:</strong> tempat kerja sebenar, pasukan yang sedang bekerja, atau kad teks ringkas dengan nama jawatan. Gambar stok pejabat yang tersenyum untuk kerja gudang akan menarik orang yang salah.</li>
<li><strong>Jangan berlebih-lebihan:</strong> "duit mudah" atau "gaji tinggi tanpa pengalaman" mudah ditolak dan menarik orang yang hilang pada peringkat temu duga.</li>
</ul>
<p>Pastikan kapsyen pendek dan mudah dibaca sekali imbas. Jika ramai pemohon membaca bahasa Melayu atau Cina, iklan berasingan dalam bahasa itu biasanya lebih mudah difahami daripada satu kapsyen panjang yang bercampur.</p>

<h2>4. Biar pemohon hubungi anda di WhatsApp</h2>
<p>Kebanyakan pencari kerja di sini lebih suka hantar mesej WhatsApp daripada mengisi borang panjang. Meta membolehkan iklan yang membuka chat WhatsApp dengan satu ketikan. Sebelum iklan disiarkan, sediakan:</p>
<ul>
<li>Mesej sambutan yang bertanya tiga atau empat soalan mudah: jawatan mana, tinggal di kawasan mana, bila boleh mula, dan pengalaman berkaitan.</li>
<li>Quick replies untuk soalan yang ditanya setiap hari: gaji, waktu kerja, lokasi, pengangkutan.</li>
<li>Label dalam WhatsApp Business (baharu, sudah disaring, temu duga ditetapkan, diambil bekerja, tidak sesuai) supaya tiada siapa tercicir.</li>
</ul>
<p>Jangan minta nombor NRIC penuh melalui chat. PDPC Singapura ada %s yang mengehadkan bila organisasi boleh mengumpulnya.</p>

<h2>5. Kelajuan membalas lebih penting daripada iklan</h2>
<p>Orang yang membalas iklan kerja di media sosial selalunya sedang menghubungi beberapa majikan serentak. Iklan memberi anda perbualan; balasan anda yang menentukan sama ada mereka datang.</p>
<ul>
<li>Tetapkan seorang yang bertanggungjawab atas inbox sepanjang iklan berjalan, dengan waktu tetap setiap hari untuk membalas.</li>
<li>Tawarkan dua atau tiga slot temu duga, jangan tanya "bila anda free?"</li>
<li>Hantar peringatan sehari sebelum dan pada pagi temu duga.</li>
<li>Apabila jawatan sudah diisi, beritahu mereka yang masih menunggu. Nama page anda kekal baik untuk pusingan seterusnya.</li>
</ul>

<h2>6. Ukur perbualan dan temu duga, bukan like</h2>
<p>Iklan kerja yang banyak like tetapi sedikit mesej belum buat kerjanya. Jejak berapa orang menghantar mesej, berapa lulus soalan asas, berapa hadir temu duga, dan berapa benar-benar mula bekerja. Mulakan dengan bajet sederhana, ubah satu perkara pada satu masa (gambar, baris pertama, lokasi), dan tambah bajet hanya selepas orang betul-betul datang.</p>

<h2>Di mana kami boleh bantu</h2>
<p>Hunter Foo Media merancang dan menjalankan iklan Meta untuk perniagaan kecil di Singapura dan Malaysia, termasuk iklan pengambilan pekerja: persediaan kempen, kapsyen dan gambar, aliran balasan WhatsApp, dan laporan ringkas tentang apa yang berlaku. Anda luluskan setiap iklan sebelum ia disiarkan. Kami tidak boleh menjanjikan bilangan pemohon atau pekerja, dan kami bukan agensi pekerjaan, jadi keputusan pengambilan kekal di tangan anda. Yuran melalui sebut harga bertulis.</p>
""" % (ext(META_HELP, "About ads for employment"), ext(TAFEP, "Panduan menulis iklan kerja yang adil"), ext(PDPC, "garis panduan nasihat tentang nombor NRIC"))

ART2_EN = """
<p>My view is that over the next two to three years, every company will gradually realise the AI era has arrived. That realisation brings anxiety, and anxious businesses tend to grab at whatever help is on offer. The trouble is that while AI keeps changing, there is no way to know which technology or feature will actually work best for you.</p>

<h2>How fast AI moves</h2>
<p>I started working with AI in early 2025. Since then I have watched one feature after another take off and then fade. Something can be the hottest thing around for six months and then drop away just as quickly. That is how fast AI moves.</p>
<p>As of 30 October 2026, it is still changing, and it will keep changing. So what does a new company need to keep in step with it? A subscription? A course? Something else? Honestly, there is no standard answer.</p>

<h2>What we do at HFM</h2>
<p>HFM is an AI agency, and we work as Forward Deployed Engineers (FDEs). A Forward Deployed Engineer works embedded with the client's team, deploying the technology and adapting it to their real business, rather than just selling them a tool. Our job is to help brands and companies stay on the front line of a technology that never stops moving, and keep up with it continuously.</p>

<h2>Two sides of every business</h2>
<p>At its core, any company comes down to two sides: the work that faces outward and the work that runs inside. Put bluntly, one is sales and the other is management.</p>
<p>Making a sale usually depends on one thing: trust. When people can look you up online and find real information about your company, they trust you more. That is why the most basic thing you need is a website.</p>

<h2>Why the website comes first</h2>
<p>People ask me whether Facebook, Instagram or Xiaohongshu is enough. Social media matters, and it is part of the process I describe below. But compare the two: a customer comes across you on social media, or a customer asks ChatGPT or searches on Google and your company comes up. Which one do you think builds more trust? Being findable in search and in AI answers, with a website of your own behind it, is the foundation everything else is built on.</p>

<h2>Next: from public platforms to your own channel</h2>
<p>Once that first layer is in place, you build the sales funnel. Social media gets people interested, and the deal is done on WhatsApp. This is what we call moving customers from the public domain to the private domain: from open platforms into a direct conversation with you.</p>
<p>That is the basic flow, and it is how your company starts bringing AI into the business, step by step.</p>
<p><strong>Have you started bringing AI into your business?</strong></p>

<h2>Where to start</h2>
<p>If you are not sure what your first step should be, take a look at <a href="/products/#website-building">our website building service</a> and the rest of what we do, or message me on WhatsApp. Hunter Foo Media can build the website, the social media content and the WhatsApp flow with you, and you approve each step. We do not promise search rankings or recommendations from AI tools. Fees are by written quote.</p>
"""

ART2_ZH = """
<p>我的看法是：未来 2 到 3 年，每一间公司都会逐渐意识到 AI 时代已经到来。这会带来焦虑，焦虑之下，很多人就开始盲目地寻求帮助。可是在 AI 技能不停迭代的过程中，你根本无法知道哪一个技术或者功能才是最有效的。</p>

<h2>AI 迭代有多快</h2>
<p>我是在 2025 年初开始接触 AI 的。这段时间里，我看着一个又一个 AI 功能崛起，又看着它们没落。一个功能可以非常火爆 6 个月，然后迅速没落，这就是 AI 迭代的速度！</p>
<p>现在是 2026 年 10 月 30 日，AI 科技还会继续迭代。对于一间新的公司，应该具备什么条件，才可以和 AI 科技同步？是订阅吗？是上课吗？还是什么？其实没有标准答案！</p>

<h2>HFM 在做什么</h2>
<p>在 HFM，我们是一家 AI Agency，做的是前沿部署工程师（FDE，Forward Deployed Engineer）。前沿部署工程师会进到客户的团队里一起工作，把技术部署到你真实的业务里，并按实际情况去调整，而不只是卖一个工具给你。我们要做的，是在不断迭代的 AI 科技领域里，帮品牌和公司站在前线，持续跟上。</p>

<h2>公司的两条主线：主外和主内</h2>
<p>整个公司的核心链接，基本上分为两部分：主外和主内。简单粗暴地说，一个是业绩，一个是管理。</p>
<p>交易或者业绩，往往需要一个东西，叫做信任（Trust）。如果别人可以在网上搜到你的信息，信任度会更高。所以最基础需要的，是网站！</p>

<h2>为什么先做网站</h2>
<p>有人问：Facebook、IG 或者小红书可以吗？社交媒体当然有用，下面讲的流程也少不了它。但如果给你做个对比：客户在社交媒体上刷到你，和客户在 ChatGPT 或 Google 搜寻时就看到你的公司，你觉得哪一个带来的信任度比较高？能在搜索和 AI 回答里被找到，背后再有一个属于你自己的网站，这才是一切的基础。</p>

<h2>接下来：从公域到私域</h2>
<p>有了第一层，接下来就开始做销售漏斗（sales funnel）：在社交媒体上种草，然后到 WhatsApp 做交易。这就是所谓的从公域到私域。</p>
<p>这就是基本流程，让你的公司逐步结合 AI 科技！</p>
<p><strong>你开始结合AI了吗？</strong></p>

<h2>从哪里开始</h2>
<p>如果你还不确定第一步该做什么，可以先看看我们的<a href="/products/#website-building">网站建设服务</a>和其他服务，或者直接 WhatsApp 我。Hunter Foo Media 可以和你一起把网站、社交媒体内容和 WhatsApp 流程做起来，每一步都由你确认。我们不保证搜索排名，也不保证会被 AI 工具推荐。费用以书面报价为准。</p>
"""

ART2_MS = """
<p>Pada pandangan saya, dalam dua hingga tiga tahun akan datang, setiap syarikat akan perlahan-lahan sedar bahawa era AI sudah tiba. Kesedaran itu membawa kebimbangan, dan apabila bimbang, ramai yang terus mencari bantuan tanpa arah. Masalahnya, selagi AI terus berubah, anda tidak dapat tahu teknologi atau fungsi mana yang benar-benar paling berkesan.</p>

<h2>Betapa pantasnya AI berubah</h2>
<p>Saya mula menggunakan AI pada awal 2025. Sejak itu, saya melihat satu demi satu fungsi AI naik, kemudian merosot. Sesuatu fungsi boleh jadi sangat popular selama enam bulan, kemudian cepat dilupakan. Itulah kelajuan AI berubah!</p>
<p>Setakat 30 Oktober 2026, teknologi AI masih terus berubah, dan akan terus berubah. Jadi, apa yang syarikat baharu perlukan untuk kekal seiring dengannya? Langganan? Kursus? Atau sesuatu yang lain? Sebenarnya, tiada jawapan standard!</p>

<h2>Apa yang kami buat di HFM</h2>
<p>HFM ialah sebuah agensi AI, dan kami bekerja sebagai Forward Deployed Engineer (FDE). Forward Deployed Engineer ialah jurutera yang bekerja bersama pasukan pelanggan, memasang dan menyesuaikan teknologi dengan perniagaan sebenar mereka, bukan sekadar menjual alat. Tugas kami ialah membantu jenama dan syarikat kekal di barisan hadapan dalam teknologi AI yang tidak henti berubah, dan terus mengikutinya secara berterusan.</p>

<h2>Dua bahagian dalam setiap perniagaan</h2>
<p>Pada dasarnya, sesebuah syarikat boleh dibahagikan kepada dua: urusan luar dan urusan dalam. Secara mudahnya, satu ialah jualan, satu lagi pengurusan.</p>
<p>Jualan biasanya bergantung pada satu perkara: kepercayaan. Apabila orang boleh mencari maklumat syarikat anda dalam talian, kepercayaan mereka lebih tinggi. Sebab itu, perkara paling asas yang anda perlukan ialah laman web!</p>

<h2>Kenapa laman web dahulu</h2>
<p>Ada yang bertanya, cukupkah Facebook, Instagram atau Xiaohongshu sahaja? Media sosial memang penting, dan ia sebahagian daripada aliran yang saya terangkan di bawah. Tapi cuba bandingkan: pelanggan terjumpa anda di media sosial, atau pelanggan bertanya kepada ChatGPT atau mencari di Google dan syarikat anda muncul. Pada pendapat anda, mana satu yang membina lebih banyak kepercayaan? Boleh ditemui dalam carian dan jawapan AI, dengan laman web milik anda sendiri di belakangnya, itulah asas kepada segala-galanya.</p>

<h2>Seterusnya: dari platform awam ke saluran anda sendiri</h2>
<p>Selepas lapisan pertama siap, barulah bina corong jualan (sales funnel): tarik minat orang di media sosial, kemudian tutup jualan di WhatsApp. Inilah yang dipanggil membawa pelanggan dari ruang awam ke ruang peribadi, iaitu dari platform terbuka kepada perbualan terus dengan anda.</p>
<p>Itulah aliran asasnya, supaya syarikat anda boleh menggabungkan teknologi AI langkah demi langkah.</p>
<p><strong>Sudahkah anda mula membawa AI ke dalam perniagaan anda?</strong></p>

<h2>Di mana hendak bermula</h2>
<p>Jika anda belum pasti apa langkah pertama, lihat <a href="/products/#website-building">servis pembinaan laman web</a> kami dan servis lain, atau WhatsApp saya terus. Hunter Foo Media boleh membina laman web, kandungan media sosial dan aliran WhatsApp bersama anda, dan anda luluskan setiap langkah. Kami tidak menjanjikan kedudukan carian atau cadangan daripada alat AI. Yuran melalui sebut harga bertulis.</p>
"""

ART2 = {"slug": "keeping-your-business-in-step-with-ai", "date": "2026-10-30",
  "en": {"title": "Keeping Your Business in Step with AI | Hunter Foo Media",
         "h1": "Keeping your business in step with AI",
         "desc": "AI tools rise and fade fast, and there is no standard way to keep up. Hunter Foo on what a Forward Deployed Engineer does, why trust starts with a website, and the funnel from social media to WhatsApp.",
         "lede": "Sooner or later every company feels the pressure of AI. Here is how I think a business can keep up: build trust first, starting with a website, then a funnel from social media to WhatsApp.",
         "eyebrow": "AI · BUSINESS", "body": ART2_EN, "next": "NEXT STEP", "cta": "Not sure where to start?",
         "wa": "Hi Hunter, I read your article on keeping up with AI. Our business is: ____", "cta_note": "Malaysian number +60196273143. English or Chinese. Fees by written quote."},
  "zh": {"title": "公司怎样和 AI 科技同步？先从信任和网站开始｜Hunter Foo Media",
         "h1": "AI 不停迭代，公司怎样持续跟上？",
         "desc": "AI 功能起落很快，跟上 AI 没有标准答案。Hunter Foo 谈前沿部署工程师（FDE）在做什么、为什么信任从网站开始，以及从社交媒体到 WhatsApp 的销售漏斗。",
         "lede": "每间公司迟早都会感受到 AI 带来的压力。我的看法是：先建立信任，从网站开始，再做从社交媒体到 WhatsApp 的销售漏斗。",
         "eyebrow": "AI · 企业", "body": ART2_ZH, "next": "下一步", "cta": "不知道从哪里开始？",
         "wa": "你好 Hunter，我看了你写的 AI 文章。我们的业务是：＿＿", "cta_note": "马来西亚号码 +60196273143。简体中文或英文都行。费用以书面报价为准。"},
  "ms": {"title": "Kekal Seiring dengan AI: Panduan untuk Perniagaan | Hunter Foo Media",
         "h1": "Bagaimana perniagaan boleh kekal seiring dengan AI",
         "desc": "Alat AI cepat naik dan cepat hilang, dan tiada cara standard untuk kekal seiring. Hunter Foo tentang kerja Forward Deployed Engineer, kenapa kepercayaan bermula dengan laman web, dan corong jualan dari media sosial ke WhatsApp.",
         "lede": "Lambat-laun setiap syarikat akan merasai tekanan AI. Begini saya lihat cara perniagaan boleh kekal seiring: bina kepercayaan dahulu, bermula dengan laman web, kemudian corong jualan dari media sosial ke WhatsApp.",
         "eyebrow": "AI · PERNIAGAAN", "body": ART2_MS, "next": "LANGKAH SETERUSNYA", "cta": "Tidak pasti di mana hendak bermula?",
         "wa": "Hai Hunter, saya baca artikel anda tentang AI. Perniagaan kami: ____", "cta_note": "Nombor Malaysia +60196273143. Bahasa Inggeris atau Cina. Yuran melalui sebut harga bertulis."}}

ARTICLES = [
 ART2,
 {"slug": "meta-hiring-ads-singapore-sme", "date": "2026-10-28",
  "en": {"title": "Before Running Meta Hiring Ads in Singapore: What SMEs Should Know | Hunter Foo Media",
         "h1": "What Singapore SMEs should know before running Meta hiring ads",
         "desc": "Meta's Employment ad category, targeting limits, fair job ad wording, simple caption tips, WhatsApp for applicants and fast follow-up. A practical guide for Singapore SMEs.",
         "lede": "Facebook and Instagram can reach people who are not on job portals. Here is what to get right first: Meta's rules, fair wording, the ad itself, and how you reply.",
         "eyebrow": "META ADS · HIRING", "body": ART_EN, "next": "NEXT STEP", "cta": "Planning a hiring ad?",
         "wa": "Hi Hunter, I read your article on Meta hiring ads. We are hiring for: ____ in ____", "cta_note": "Malaysian number +60196273143. English or Chinese. Fees by written quote."},
  "zh": {"title": "新加坡 SME 投 Meta 招聘广告前要知道的事｜Hunter Foo Media",
         "h1": "新加坡 SME 投 Meta 招聘广告前要知道的事",
         "desc": "Meta 就业类特殊广告限制、定位限制、公平招聘文案、简单的图文技巧、用 WhatsApp 接应征者、快速跟进。写给新加坡中小企业的实用指南。",
         "lede": "Facebook 和 Instagram 能碰到不上求职网站的人。投之前先把几件事做对：Meta 的规则、公平的写法、广告本身，以及你怎么回复。",
         "eyebrow": "META 广告 · 招聘", "body": ART_ZH, "next": "下一步", "cta": "准备投招聘广告？",
         "wa": "你好 Hunter，我看了你写的 Meta 招聘广告文章。我们在招：＿＿，地点：＿＿", "cta_note": "马来西亚号码 +60196273143。简体中文或英文都行。费用以书面报价为准。"},
  "ms": {"title": "Sebelum Iklan Kerja Meta di Singapura: Apa PKS Perlu Tahu | Hunter Foo Media",
         "h1": "Apa yang PKS Singapura perlu tahu sebelum menjalankan iklan kerja di Meta",
         "desc": "Kategori iklan Employment Meta, had sasaran, ayat iklan kerja yang adil, tip kapsyen ringkas, WhatsApp untuk pemohon dan susulan pantas. Panduan praktikal untuk PKS Singapura.",
         "lede": "Facebook dan Instagram boleh sampai kepada orang yang tidak membuka portal kerja. Ini yang perlu dibetulkan dahulu: peraturan Meta, ayat yang adil, iklan itu sendiri, dan cara anda membalas.",
         "eyebrow": "IKLAN META · PENGAMBILAN", "body": ART_MS, "next": "LANGKAH SETERUSNYA", "cta": "Merancang iklan kerja?",
         "wa": "Hai Hunter, saya baca artikel anda tentang iklan kerja Meta. Kami mencari: ____ di ____", "cta_note": "Nombor Malaysia +60196273143. Bahasa Inggeris atau Cina. Yuran melalui sebut harga bertulis."}},
]

DATE_FMT = {"en": lambda d: "%d %s %s" % (int(d[8:]), ["January","February","March","April","May","June","July","August","September","October","November","December"][int(d[5:7])-1], d[:4]),
            "zh": lambda d: "%s 年 %d 月 %d 日" % (d[:4], int(d[5:7]), int(d[8:])),
            "ms": lambda d: "%d %s %s" % (int(d[8:]), ["Januari","Februari","Mac","April","Mei","Jun","Julai","Ogos","September","Oktober","November","Disember"][int(d[5:7])-1], d[:4])}
BY = {"en": "By Hunter Foo", "zh": "作者：Hunter Foo", "ms": "Oleh Hunter Foo"}
ALL_LABEL = {"en": "All articles", "zh": "全部文章", "ms": "Semua artikel"}

def contact(lang, next_, cta, wa, note=""):
    n = '<p>%s</p>' % note if note else ''
    return ('<section class="wrap section contact" id="contact"><p class="eyebrow"><i></i>%s</p><div class="contact-row"><h2>%s</h2><div class="contact-actions">'
            '<a class="button whatsapp" data-wa="%s" href="%s" target="_blank" rel="noopener noreferrer">WhatsApp +60196273143 <span aria-hidden="true">↗</span></a>'
            '<a class="email-link" href="mailto:hello@hunterfoomedia.com">hello@hunterfoomedia.com <span aria-hidden="true">↗</span></a>%s</div></div></section>\n') % (next_, cta, wa, WA, n)

def index_main(lang, p):
    h = INDEX[lang]
    items = "".join('<li><h3><a href="%s/articles/%s/">%s</a></h3><p>%s · %s</p><p>%s</p><p><a href="%s/articles/%s/">%s →</a></p></li>\n' % (
        p, a["slug"], a[lang]["h1"], DATE_FMT[lang](a["date"]), BY[lang], a[lang]["desc"], p, a["slug"], h["read"]) for a in ARTICLES)
    return ('\n<section class="wrap page-intro">\n<p class="crumbs"><a href="/">%s</a> / %s</p>\n<p class="eyebrow"><i></i>%s</p>\n<h1>%s</h1>\n<p class="lede">%s</p>\n</section>\n'
            '<section class="paper"><div class="wrap section prose">\n<ul class="article-list" style="list-style:none;padding-left:0">\n%s</ul>\n</div></section>\n' % (h["crumb"], h["h1"].rstrip(".。"), h["eyebrow"], h["h1"], h["lede"], items)
            + contact(lang, h["next"], h["cta"], h["wa"]))

def article_main(lang, a, p):
    t = a[lang]; h = INDEX[lang]
    return ('\n<article>\n<section class="wrap page-intro">\n<p class="crumbs"><a href="/">%s</a> / <a href="/articles/">%s</a> / %s</p>\n<p class="eyebrow"><i></i>%s</p>\n<h1>%s</h1>\n<p class="lede">%s</p>\n'
            '<p class="crumbs" style="margin-top:18px"><time datetime="%s">%s</time> · %s</p>\n</section>\n'
            '<section class="paper"><div class="wrap section prose">\n%s\n<p class="related"><a href="/articles/">← %s</a><a href="/products/">%s</a></p>\n</div></section>\n</article>\n' % (
            h["crumb"], h["h1"].rstrip(".。"), t["h1"], t["eyebrow"], t["h1"], t["lede"], a["date"], DATE_FMT[lang](a["date"]), BY[lang], t["body"], ALL_LABEL[lang],
            {"en": "Our services and demos", "zh": "看我们的服务与演示", "ms": "Servis dan demo kami"}[lang])
            + contact(lang, t["next"], t["cta"], t["wa"], t["cta_note"]))
