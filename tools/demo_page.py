# /demo/ (EN / ZH / MS): click-to-try simulation of the six digital employees.
# Static, client-side only (assets/demo.js): no backend, no API, nothing is sent, published or saved.
# Outcomes only: no tool names, vendors or implementation details. All names and figures are made-up sample data.
import urllib.parse, html, json
from services_page import ICONS, P as SP

WA = "https://wa.me/60196273143"
D = "https://www.hunterfoomedia.com"
PATH = "/demo/"
IDS = ["wb", "mk", "cs", "ck", "mg", "pa"]

P = {}
DATA = {}

# ---------------------------------------------------------------- EN
P["en"] = dict(
 title="Try our AI: Interactive Demo (Sample Data) | Hunter Foo Media",
 desc="Click-to-try demo of six AI digital employees: website, marketing, customer service, clerk, manager and PA. Sample data only. Nothing is sent or published.",
 eyebrow="DEMO · SAMPLE DATA", h1='Try what our <span class="orange">AI can do</span>',
 lede="Click through six sample digital employees. This is a demo with made-up sample data. Nothing is sent, published or saved.",
 out="Outside: serving customers", inn="Inside: helping your team",
 short=["Website AI", "Marketing AI", "Customer Service AI", "Clerk AI", "Manager AI", "PA AI"],
 demo_tag="Demo · sample data", nojs="This demo needs JavaScript. Without it, here is what this digital employee does.",
 see_services="See the five services →",
 ce="NEXT STEP", ch="Want digital employees for your business?",
 wamsg="Hi Hunter, I tried your AI demo. My business: __\nI'd like to talk about: __", cta="WhatsApp +60 19-627 3143",
 cnote="Malaysian number +60196273143. English, <span lang=\"zh-Hans\">中文</span> or BM.",
 crumb="Home", crumbp="AI demo",
)
DATA["en"] = dict(
 ui=dict(note="Demo only. Nothing here is sent, published or saved, and all names and figures are made-up samples.", reset="Start over"),
 wb=dict(toggle="Before or after", before="Before", after="After", page_l="Your page section (sample)", read_l="What Google and AI assistants understand",
  ask_l="Someone asks an AI assistant", clear="Clear", unclear="Not clear",
  bh="Welcome to Sample Aircond Services", bp="We are a leading provider of quality solutions for all your needs. Contact us today for more information.",
  ah="Aircond servicing and repair in Petaling Jaya and Kuala Lumpur",
  ap="Sample Aircond Services cleans, services and repairs home and office aircond units. Open Monday to Saturday, 9am to 6pm. Message us for a quote.",
  aq="Do you service all aircond brands?", aa="Yes. Tell us the brand and we will confirm before we come.",
  q="Who can service my aircond in Petaling Jaya?",
  abefore="I can't tell what this company does or where it works.",
  aafter="Sample Aircond Services cleans, services and repairs home and office aircond in Petaling Jaya and Kuala Lumpur, Monday to Saturday, 9am to 6pm.",
  checks=["What you do", "Where you work", "When you are open", "How to contact you"]),
 mk=dict(topic_l="Pick a topic", kind_l="Post for", social="Social media", gbp="Google Business Profile", draft_l="Sample draft",
  waiting="Draft. Waiting for your approval.", approved="Approved (demo). In real use this is when it would be published. Nothing was published here.",
  approve="Approve", another="Another draft",
  topics=[
   dict(id="promo", n="Promotion",
    social=["Aircond not as cold as it used to be? Book a servicing slot this month and we will sort it out. Message us to book.",
            "Servicing slots are open this month for homes and offices in PJ and KL. Message us to pick a time."],
    gbp=["Aircond servicing slots open this month in Petaling Jaya and Kuala Lumpur. Message us to book.",
         "Book your aircond servicing this month. Home and office units welcome."]),
   dict(id="tip", n="Helpful tip",
    social=["Clean your aircond filters every few weeks. It helps the unit cool better and keeps the air fresher. Need a hand? We can do it for you.",
            "Water dripping from your indoor unit? It is often a blocked drain pipe. Message us a photo and we will tell you what to do next."],
    gbp=["Tip: clean your aircond filters every few weeks for better cooling.",
         "Water dripping from the indoor unit? Send us a photo and we will advise."]),
   dict(id="team", n="Behind the scenes",
    social=["Meet the team: our technicians check every unit before and after servicing, so you know it is working properly.",
            "A day at Sample Aircond Services: from the first call to a cool room."],
    gbp=["Our technicians check every unit before and after servicing.",
         "Meet the team behind your cool room."]),
   dict(id="greet", n="Festive greeting",
    social=["Wishing you a joyful festive season! Our hours may change over the holidays, so message us to plan your servicing early.",
            "Happy holidays from all of us at Sample Aircond Services!"],
    gbp=["Festive greetings from Sample Aircond Services. Holiday hours may change; message us to plan ahead.",
         "Happy holidays! Book your servicing early."])]),
 cs=dict(hi="Hi! I am the assistant for Sample Aircond Services. Ask me something, or tap a question below.",
  tryq="Try asking:", ph="Type a question…", send="Send", you="You", bot="AI", handed="Passed to a person",
  chips=["How much is servicing?", "What are your opening hours?", "What services do you offer?", "Do you cover Petaling Jaya?", "I want a refund for a past job"],
  complex=["refund", "complain", "angry", "damage", "compensat", "lawyer", "discount", "customi"],
  qa=[dict(k=["price", "cost", "how much", "charge", "fee"], a="Servicing starts from RM100 per unit (a sample price for this demo). The final quote depends on the unit type and condition."),
      dict(k=["hour", "open", "close", "when", "time"], a="We are open Monday to Saturday, 9am to 6pm, and closed on Sundays and public holidays (sample hours)."),
      dict(k=["book", "appointment", "slot", "schedule"], a="Sure. Tell me your preferred day and I will note it down. A person will confirm the exact time."),
      dict(k=["petaling", "pj", "kuala lumpur", "kl", "area", "cover", "location", "where"], a="Yes, we cover Petaling Jaya and Kuala Lumpur."),
      dict(k=["service", "offer", "repair", "install", "clean"], a="We clean, service and repair aircond units for homes and offices. Want me to help you book a slot?")],
  handoff="This is best handled by a person. I have passed your message to our team, and they will reply to you personally.",
  follow="Customer went quiet? Skip ahead one day", later="One day later. The customer has not replied.",
  fmsg="Hi again! Just checking if you still need your aircond serviced. I can book a slot for you whenever you are ready."),
 ck=dict(pile_l="Messy files (sample)", sort="Sort my files", done="{n} files sorted into {m} folders.",
  folders=[dict(id="invoices", n="Invoices and receipts"), dict(id="resumes", n="Resumes"), dict(id="quotes", n="Quotes"),
           dict(id="contracts", n="Contracts"), dict(id="notes", n="Meeting notes"), dict(id="photos", n="Photos")],
  files=[["IMG_2041.jpg", "photos"], ["invoice_march.pdf", "invoices"], ["resume_Aisha.docx", "resumes"], ["meeting notes final v3.docx", "notes"],
         ["receipt_0412.pdf", "invoices"], ["quote_ClientA.xlsx", "quotes"], ["contract_signed.pdf", "contracts"], ["resume_Daniel.pdf", "resumes"],
         ["IMG_2058.jpg", "photos"], ["quote_ClientB.xlsx", "quotes"]]),
 mg=dict(gen="Show today's report", prep="Preparing the report…", title="Daily progress report (sample team)", sum="{d} done · {t} on track · {s} stuck",
  cols=["Who", "Task", "Status", "Note"], st=dict(done="Done", track="On track", stuck="Stuck"),
  rows=[["Amy", "Update the quote for Client A", "done", "Sent to the client this morning."],
        ["Ben", "Prepare the training materials", "track", "Draft is half done. On track for tomorrow."],
        ["Chloe", "Get the logo from the client", "stuck", "Asked twice. No reply yet."],
        ["Amy", "Book the venue", "track", "Waiting for the venue to confirm."],
        ["Ben", "Invoice for last month", "done", "Issued and filed."]],
  stuck_l="Where things are stuck", stuck="Chloe is waiting for the client's logo. The client has not replied to two messages.",
  today_l="Who should do what today",
  today=["Chloe: call the client about the logo.", "Ben: finish the training materials.", "Amy: confirm the venue by 3pm."]),
 pa=dict(sched_l="Today's schedule", rem_l="Follow-up reminders", draft_l="Draft reply", in_l="Message received", from_="Client A (sample)",
  inmsg="Can we move Thursday's meeting to Friday at 3pm?",
  sched=[["9:30 am", "Call with supplier"], ["11:00 am", "Site visit, Subang"], ["2:00 pm", "Review quotes"], ["4:30 pm", "Team check-in"]],
  moved=["Fri 3:00 pm", "Client A meeting (moved from Thursday)"],
  rem=["Follow up Client A about the quote", "Ask Chloe for the logo", "Send the payment reminder"],
  draft="Hi, Friday at 3pm works for me. I will send an updated invite shortly. Thanks!",
  waiting="Draft. Waiting for your confirmation.", confirm="Confirm and send", sent="Confirmed (demo). In real use it is sent only now. Nothing was sent here."),
)

# ---------------------------------------------------------------- ZH
P["zh"] = dict(
 title="试用我们的 AI：互动演示（示例数据）｜Hunter Foo Media",
 desc="点一点就能试：六位 AI 数字员工的互动演示，包括网站、营销、客服、文员、经理和个人助理。全部是示例数据，不会发送或发布任何内容。",
 eyebrow="演示 · 示例数据", h1='试试我们的 <span class="orange">AI 能做什么</span>',
 lede="点开六位示例数字员工，亲手试一试。这是用虚构示例数据做的演示，不会发送、发布或保存任何内容。",
 out="对外：服务客户", inn="对内：帮团队",
 short=["网站 AI", "营销 AI", "客服 AI", "文员 AI", "经理 AI", "助理 AI"],
 demo_tag="演示 · 示例数据", nojs="这个演示需要 JavaScript。没有的话，下面是这位数字员工做的事。",
 see_services="看五项服务 →",
 ce="下一步", ch="想为你的公司设立数字员工？",
 wamsg="你好 Hunter，我试了你们的 AI 演示。我做的是：＿＿\n我想了解：＿＿", cta="WhatsApp +60 19-627 3143",
 cnote="马来西亚号码 +60196273143。中文、英文或马来文都可以。",
 crumb="首页", crumbp="AI 演示",
)
DATA["zh"] = dict(
 ui=dict(note="仅为演示。这里不会发送、发布或保存任何内容，所有名字和数字都是虚构的示例。", reset="重新开始"),
 wb=dict(toggle="改前或改后", before="改前", after="改后", page_l="你的网页内容（示例）", read_l="Google 和 AI 助手读到的是",
  ask_l="有人问 AI 助手", clear="清楚", unclear="不清楚",
  bh="欢迎来到示例冷气公司", bp="我们是领先的优质方案提供者，满足您的各种需求。欢迎随时联系我们了解更多。",
  ah="八打灵再也和吉隆坡的冷气保养与维修",
  ap="示例冷气公司为住家和办公室的冷气机提供清洗、保养和维修。周一至周六，上午 9 点到下午 6 点营业。留言即可报价。",
  aq="所有品牌的冷气都能保养吗？", aa="可以。告诉我们品牌，上门前我们会先确认。",
  q="八打灵再也哪里可以保养冷气？",
  abefore="看不出这家公司做什么，也看不出在哪里服务。",
  aafter="示例冷气公司在八打灵再也和吉隆坡为住家和办公室冷气提供清洗、保养和维修，周一至周六，上午 9 点到下午 6 点。",
  checks=["你做什么", "在哪里服务", "几点营业", "怎么联系你"]),
 mk=dict(topic_l="选一个主题", kind_l="发布到", social="社交媒体", gbp="Google Business Profile", draft_l="示例草稿",
  waiting="草稿。等你批准。", approved="已批准（演示）。真实使用时，这一步之后才会发布。这里没有发布任何内容。",
  approve="批准", another="换一篇草稿",
  topics=[
   dict(id="promo", n="优惠活动",
    social=["冷气没有以前凉了？这个月预约保养，我们帮你处理好。留言即可预约。",
            "这个月八打灵再也和吉隆坡的住家与办公室保养名额开放中。留言选个时间吧。"],
    gbp=["八打灵再也和吉隆坡冷气保养名额本月开放。留言预约。",
         "本月预约冷气保养，住家和办公室都欢迎。"]),
   dict(id="tip", n="实用小贴士",
    social=["每隔几周清洗一次冷气滤网，冷气更凉，空气也更清新。需要帮忙？我们可以代劳。",
            "室内机在滴水？常见原因是排水管堵塞。留言发张照片给我们，我们告诉你下一步怎么做。"],
    gbp=["小贴士：每隔几周清洗冷气滤网，制冷更好。",
         "室内机滴水？发张照片给我们，我们给你建议。"]),
   dict(id="team", n="幕后花絮",
    social=["认识我们的团队：技术员在保养前后都会检查每一台冷气，让你确定它运作正常。",
            "示例冷气公司的一天：从接到电话，到房间变凉。"],
    gbp=["我们的技术员在保养前后都会检查每一台冷气。",
         "认识让你房间变凉的团队。"]),
   dict(id="greet", n="节日祝福",
    social=["祝你节日快乐！假期期间我们的营业时间可能调整，欢迎留言提早安排保养。",
            "示例冷气公司全体祝你假期愉快！"],
    gbp=["示例冷气公司祝你节日快乐。假期营业时间可能调整，欢迎留言提早安排。",
         "假期愉快！欢迎提早预约保养。"])]),
 cs=dict(hi="你好！我是示例冷气公司的助手。可以直接问我，或点下面的问题。",
  tryq="试试问：", ph="输入问题…", send="发送", you="你", bot="AI", handed="已转给真人",
  chips=["保养多少钱？", "几点营业？", "你们做哪些服务？", "有到八打灵再也吗？", "我想为之前的工作退款"],
  complex=["退款", "投诉", "赔", "生气", "损坏", "律师", "折扣", "定制"],
  qa=[dict(k=["多少钱", "价格", "费用", "收费", "报价"], a="保养每台起价 RM100（这个演示的示例价格）。最终报价视冷气类型和状况而定。"),
      dict(k=["营业", "几点", "时间", "开门", "关门"], a="我们周一至周六上午 9 点到下午 6 点营业，周日和公共假期休息（示例营业时间）。"),
      dict(k=["预约", "订", "安排"], a="好的。告诉我你方便的日子，我先记下来，由真人确认确切时间。"),
      dict(k=["八打灵", "吉隆坡", "范围", "地区", "哪里", "有到"], a="有，我们服务八打灵再也和吉隆坡。"),
      dict(k=["服务", "做什么", "维修", "安装", "清洗", "保养"], a="我们为住家和办公室的冷气机提供清洗、保养和维修。要我帮你预约吗？")],
  handoff="这件事最好由真人处理。我已把你的留言转给团队，他们会亲自回复你。",
  follow="客户没回复？快进一天", later="一天后。客户还没有回复。",
  fmsg="你好！想确认一下你的冷气是否还需要保养。你准备好的时候，我随时帮你预约。"),
 ck=dict(pile_l="杂乱的文件（示例）", sort="帮我整理文件", done="{n} 个文件已整理进 {m} 个文件夹。",
  folders=[dict(id="invoices", n="发票和收据"), dict(id="resumes", n="简历"), dict(id="quotes", n="报价单"),
           dict(id="contracts", n="合同"), dict(id="notes", n="会议记录"), dict(id="photos", n="照片")],
  files=DATA["en"]["ck"]["files"]),
 mg=dict(gen="显示今天的报告", prep="正在准备报告…", title="每日进度报告（示例团队）", sum="{d} 项完成 · {t} 项进行中 · {s} 项卡住",
  cols=["谁", "任务", "状态", "备注"], st=dict(done="完成", track="进行中", stuck="卡住"),
  rows=[["Amy", "更新客户 A 的报价单", "done", "今早已发给客户。"],
        ["Ben", "准备培训资料", "track", "草稿完成一半，明天可完成。"],
        ["Chloe", "向客户拿标志文件", "stuck", "已问两次，客户还没回复。"],
        ["Amy", "预订场地", "track", "等场地方确认。"],
        ["Ben", "上个月的发票", "done", "已开出并归档。"]],
  stuck_l="哪里卡住了", stuck="Chloe 在等客户的标志文件。客户没有回复两次留言。",
  today_l="今天谁该做什么",
  today=["Chloe：打电话向客户跟进标志文件。", "Ben：完成培训资料。", "Amy：下午 3 点前确认场地。"]),
 pa=dict(sched_l="今天的日程", rem_l="跟进提醒", draft_l="回复草稿", in_l="收到的留言", from_="客户 A（示例）",
  inmsg="我们可以把星期四的会议改到星期五下午 3 点吗？",
  sched=[["上午 9:30", "和供应商通话"], ["上午 11:00", "实地考察，梳邦"], ["下午 2:00", "审阅报价"], ["下午 4:30", "团队例会"]],
  moved=["周五 下午 3:00", "客户 A 会议（从星期四改期）"],
  rem=["向客户 A 跟进报价", "向 Chloe 要标志文件", "发付款提醒"],
  draft="你好，星期五下午 3 点可以。我稍后发更新后的邀请给你。谢谢！",
  waiting="草稿。等你确认。", confirm="确认并发送", sent="已确认（演示）。真实使用时，这一步之后才会发送。这里没有发送任何内容。"),
)

# ---------------------------------------------------------------- MS
P["ms"] = dict(
 title="Cuba AI Kami: Demo Interaktif (Data Contoh) | Hunter Foo Media",
 desc="Demo klik-dan-cuba enam pekerja digital AI: laman web, pemasaran, khidmat pelanggan, kerani, pengurus dan PA. Data contoh sahaja. Tiada apa dihantar atau diterbitkan.",
 eyebrow="DEMO · DATA CONTOH", h1='Cuba apa yang <span class="orange">AI kami boleh buat</span>',
 lede="Klik enam pekerja digital contoh. Ini demo dengan data contoh rekaan. Tiada apa dihantar, diterbitkan atau disimpan.",
 out="Di luar: melayan pelanggan", inn="Di dalam: membantu pasukan",
 short=["AI Laman Web", "AI Pemasaran", "AI Khidmat Pelanggan", "AI Kerani", "AI Pengurus", "AI PA"],
 demo_tag="Demo · data contoh", nojs="Demo ini memerlukan JavaScript. Tanpanya, inilah yang dibuat oleh pekerja digital ini.",
 see_services="Lihat lima perkhidmatan →",
 ce="LANGKAH SETERUSNYA", ch="Mahu pekerja digital untuk perniagaan anda?",
 wamsg="Hai Hunter, saya cuba demo AI anda. Bisnes saya: __\nSaya nak bincang tentang: __", cta="WhatsApp +60 19-627 3143",
 cnote="Nombor Malaysia +60196273143. Bahasa Inggeris, Cina atau BM.",
 crumb="Utama", crumbp="Demo AI",
)
DATA["ms"] = dict(
 ui=dict(note="Demo sahaja. Tiada apa di sini dihantar, diterbitkan atau disimpan, dan semua nama serta angka ialah contoh rekaan.", reset="Mula semula"),
 wb=dict(toggle="Sebelum atau selepas", before="Sebelum", after="Selepas", page_l="Bahagian halaman anda (contoh)", read_l="Apa yang Google dan pembantu AI faham",
  ask_l="Seseorang bertanya pembantu AI", clear="Jelas", unclear="Tidak jelas",
  bh="Selamat datang ke Servis Aircond Contoh", bp="Kami penyedia penyelesaian berkualiti terkemuka untuk semua keperluan anda. Hubungi kami hari ini untuk maklumat lanjut.",
  ah="Servis dan baiki aircond di Petaling Jaya dan Kuala Lumpur",
  ap="Servis Aircond Contoh membersih, servis dan membaiki aircond rumah dan pejabat. Buka Isnin hingga Sabtu, 9 pagi hingga 6 petang. Mesej kami untuk sebut harga.",
  aq="Adakah anda servis semua jenama aircond?", aa="Ya. Beritahu kami jenamanya dan kami akan sahkan sebelum datang.",
  q="Siapa boleh servis aircond saya di Petaling Jaya?",
  abefore="Saya tidak dapat tahu apa syarikat ini buat atau di mana ia beroperasi.",
  aafter="Servis Aircond Contoh membersih, servis dan membaiki aircond rumah dan pejabat di Petaling Jaya dan Kuala Lumpur, Isnin hingga Sabtu, 9 pagi hingga 6 petang.",
  checks=["Apa yang anda buat", "Di mana anda beroperasi", "Bila anda buka", "Cara hubungi anda"]),
 mk=dict(topic_l="Pilih topik", kind_l="Hantaran untuk", social="Media sosial", gbp="Google Business Profile", draft_l="Draf contoh",
  waiting="Draf. Menunggu kelulusan anda.", approved="Diluluskan (demo). Dalam penggunaan sebenar, inilah masanya ia diterbitkan. Tiada apa diterbitkan di sini.",
  approve="Luluskan", another="Draf lain",
  topics=[
   dict(id="promo", n="Promosi",
    social=["Aircond tak sejuk macam dulu? Tempah slot servis bulan ini dan kami uruskan. Mesej kami untuk tempah.",
            "Slot servis dibuka bulan ini untuk rumah dan pejabat di PJ dan KL. Mesej kami untuk pilih masa."],
    gbp=["Slot servis aircond dibuka bulan ini di Petaling Jaya dan Kuala Lumpur. Mesej kami untuk tempah.",
         "Tempah servis aircond anda bulan ini. Unit rumah dan pejabat dialu-alukan."]),
   dict(id="tip", n="Petua berguna",
    social=["Bersihkan penapis aircond setiap beberapa minggu. Ia membantu aircond lebih sejuk dan udara lebih segar. Perlukan bantuan? Kami boleh buatkan.",
            "Air menitis dari unit dalam? Selalunya paip saliran tersumbat. Mesej gambar kepada kami dan kami beritahu langkah seterusnya."],
    gbp=["Petua: bersihkan penapis aircond setiap beberapa minggu untuk penyejukan lebih baik.",
         "Air menitis dari unit dalam? Hantar gambar dan kami beri nasihat."]),
   dict(id="team", n="Di sebalik tabir",
    social=["Kenali pasukan kami: juruteknik memeriksa setiap unit sebelum dan selepas servis, supaya anda pasti ia berfungsi dengan baik.",
            "Sehari di Servis Aircond Contoh: dari panggilan pertama hingga bilik sejuk."],
    gbp=["Juruteknik kami memeriksa setiap unit sebelum dan selepas servis.",
         "Kenali pasukan di sebalik bilik sejuk anda."]),
   dict(id="greet", n="Ucapan perayaan",
    social=["Selamat menyambut musim perayaan! Waktu operasi kami mungkin berubah semasa cuti, jadi mesej kami untuk merancang servis lebih awal.",
            "Selamat bercuti daripada kami semua di Servis Aircond Contoh!"],
    gbp=["Ucapan perayaan daripada Servis Aircond Contoh. Waktu cuti mungkin berubah; mesej kami untuk merancang awal.",
         "Selamat bercuti! Tempah servis lebih awal."])]),
 cs=dict(hi="Hai! Saya pembantu Servis Aircond Contoh. Tanya saya sesuatu, atau tekan soalan di bawah.",
  tryq="Cuba tanya:", ph="Taip soalan…", send="Hantar", you="Anda", bot="AI", handed="Diserahkan kepada orang",
  chips=["Berapa harga servis?", "Bila waktu operasi?", "Apa perkhidmatan anda?", "Adakah anda cover Petaling Jaya?", "Saya nak bayaran balik untuk kerja lepas"],
  complex=["bayaran balik", "refund", "komplen", "marah", "rosak", "peguam", "diskaun", "khas"],
  qa=[dict(k=["harga", "berapa", "kos", "caj", "bayaran", "price"], a="Servis bermula dari RM100 seunit (harga contoh untuk demo ini). Sebut harga akhir bergantung pada jenis dan keadaan unit."),
      dict(k=["waktu", "buka", "tutup", "bila", "jam"], a="Kami buka Isnin hingga Sabtu, 9 pagi hingga 6 petang, dan tutup pada hari Ahad dan cuti umum (waktu contoh)."),
      dict(k=["tempah", "temujanji", "slot", "jadual"], a="Baik. Beritahu hari pilihan anda dan saya catatkan. Seorang akan sahkan masa tepat."),
      dict(k=["petaling", "pj", "kuala lumpur", "kl", "kawasan", "cover", "lokasi", "mana"], a="Ya, kami cover Petaling Jaya dan Kuala Lumpur."),
      dict(k=["servis", "perkhidmatan", "baiki", "pasang", "bersih"], a="Kami membersih, servis dan membaiki aircond rumah dan pejabat. Mahu saya bantu tempah slot?")],
  handoff="Perkara ini lebih baik dikendalikan oleh orang. Saya telah serahkan mesej anda kepada pasukan kami, dan mereka akan membalas sendiri.",
  follow="Pelanggan senyap? Pergi ke sehari kemudian", later="Sehari kemudian. Pelanggan belum membalas.",
  fmsg="Hai lagi! Sekadar menyemak sama ada anda masih perlukan servis aircond. Saya boleh tempah slot bila-bila anda sedia."),
 ck=dict(pile_l="Fail bersepah (contoh)", sort="Susun fail saya", done="{n} fail disusun ke dalam {m} folder.",
  folders=[dict(id="invoices", n="Invois dan resit"), dict(id="resumes", n="Resume"), dict(id="quotes", n="Sebut harga"),
           dict(id="contracts", n="Kontrak"), dict(id="notes", n="Minit mesyuarat"), dict(id="photos", n="Gambar")],
  files=DATA["en"]["ck"]["files"]),
 mg=dict(gen="Tunjuk laporan hari ini", prep="Menyediakan laporan…", title="Laporan kemajuan harian (pasukan contoh)", sum="{d} siap · {t} sedang berjalan · {s} tersekat",
  cols=["Siapa", "Tugas", "Status", "Nota"], st=dict(done="Siap", track="Sedang berjalan", stuck="Tersekat"),
  rows=[["Amy", "Kemas kini sebut harga Pelanggan A", "done", "Dihantar kepada pelanggan pagi tadi."],
        ["Ben", "Sediakan bahan latihan", "track", "Draf separuh siap. Sempat siap esok."],
        ["Chloe", "Dapatkan logo daripada pelanggan", "stuck", "Sudah tanya dua kali. Belum ada balasan."],
        ["Amy", "Tempah tempat", "track", "Menunggu pengesahan tempat."],
        ["Ben", "Invois bulan lepas", "done", "Sudah dikeluarkan dan difailkan."]],
  stuck_l="Di mana ia tersekat", stuck="Chloe menunggu logo pelanggan. Pelanggan belum membalas dua mesej.",
  today_l="Siapa patut buat apa hari ini",
  today=["Chloe: telefon pelanggan tentang logo.", "Ben: siapkan bahan latihan.", "Amy: sahkan tempat sebelum 3 petang."]),
 pa=dict(sched_l="Jadual hari ini", rem_l="Peringatan susulan", draft_l="Draf balasan", in_l="Mesej diterima", from_="Pelanggan A (contoh)",
  inmsg="Boleh kita alihkan mesyuarat Khamis ke Jumaat pukul 3 petang?",
  sched=[["9:30 pagi", "Panggilan dengan pembekal"], ["11:00 pagi", "Lawatan tapak, Subang"], ["2:00 petang", "Semak sebut harga"], ["4:30 petang", "Semakan pasukan"]],
  moved=["Jum 3:00 petang", "Mesyuarat Pelanggan A (dialihkan dari Khamis)"],
  rem=["Susuli Pelanggan A tentang sebut harga", "Minta logo daripada Chloe", "Hantar peringatan bayaran"],
  draft="Hai, Jumaat pukul 3 petang boleh. Saya akan hantar jemputan terkini sebentar lagi. Terima kasih!",
  waiting="Draf. Menunggu pengesahan anda.", confirm="Sahkan dan hantar", sent="Disahkan (demo). Dalam penggunaan sebenar, ia dihantar hanya sekarang. Tiada apa dihantar di sini."),
)

def _plain(s):
    import re
    return re.sub(r"<[^>]+>", "", s)

def _main(k):
    h = P[k]; s = SP[k]
    wa = WA + "?text=" + urllib.parse.quote(h["wamsg"], safe="")
    o = []
    o.append('<section class="wrap hm-hero wd-hero dm-hero"><p class="eyebrow"><i></i>%s</p><h1>%s</h1><p class="lede">%s</p></section>\n'
             % (h["eyebrow"], h["h1"], h["lede"]))
    tab = lambda i: ('<button type="button" role="tab" class="dm-tab" id="dm-t-%s" aria-controls="dm-p-%s" aria-selected="false" tabindex="-1">'
                     '<span class="sv-ico">%s</span><span class="dm-tn">%s</span></button>' % (IDS[i], IDS[i], ICONS[i], h["short"][i]))
    tabs = ('<div class="dm-tabwrap"><div class="dm-tabs" role="tablist" aria-label="%s">'
            '<div class="dm-grp" role="presentation"><p class="dm-gl">%s</p><div class="dm-trow" role="presentation">%s</div></div>'
            '<div class="dm-grp" role="presentation"><p class="dm-gl">%s</p><div class="dm-trow" role="presentation">%s</div></div></div></div>'
            % (_plain(h["h1"]), h["out"], "".join(tab(i) for i in range(3)), h["inn"], "".join(tab(i) for i in range(3, 6))))
    panels = "".join(
        '<section class="dm-panel" id="dm-p-%s" role="tabpanel" aria-labelledby="dm-t-%s" tabindex="0">'
        '<div class="dm-head"><span class="sv-ico">%s</span><div><h2>%s</h2><p>%s</p></div><span class="dm-badge">%s</span></div>'
        '<p class="dm-note">%s</p>'
        '<div class="dm-mock" data-mock="%s"><noscript><p class="dm-nojs">%s</p></noscript></div></section>'
        % (IDS[i], IDS[i], ICONS[i], h["short"][i], s["six"][i][1], h["demo_tag"], DATA[k]["ui"]["note"], IDS[i], h["nojs"])
        for i in range(6))
    blob = json.dumps(DATA[k], ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    o.append('<section class="paper dm-sec" id="demo"><div class="wrap dm-wrap">%s%s<p class="dm-more"><a class="hm-link" href="/services/">%s</a></p></div></section>\n'
             % (tabs, panels, h["see_services"]))
    o.append('<script type="application/json" id="dm-data">%s</script>\n' % blob)
    o.append('<section class="wrap section contact" id="contact"><p class="eyebrow"><i></i>%s</p><div class="contact-row"><h2>%s</h2><div class="contact-actions">'
             '<a class="button whatsapp" data-wa="%s" href="%s" target="_blank" rel="noopener noreferrer">%s <span aria-hidden="true">↗</span></a>'
             '<!--email_off--><a class="email-link" href="mailto:hello@hunterfoomedia.com">hello@hunterfoomedia.com <span aria-hidden="true">↗</span></a><!--/email_off--><p>%s</p></div></div></section>\n'
             % (h["ce"], h["ch"], html.escape(h["wamsg"]), wa, h["cta"], h["cnote"]))
    return "\n" + "".join(o)

def _ld(k):
    h = P[k]; u = D + PATH
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": u + "#webpage", "url": u, "name": h["title"], "description": h["desc"],
         "about": {"@id": D + "/#organization"}, "isPartOf": {"@id": D + "/#website"}, "breadcrumb": {"@id": u + "#breadcrumb"}},
        {"@type": "BreadcrumbList", "@id": u + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": h["crumb"], "item": D + "/"},
            {"@type": "ListItem", "position": 2, "name": h["crumbp"], "item": u}]}]}

DM = {k: {"title": P[k]["title"], "desc": P[k]["desc"], "main": _main(k), "ld": _ld(k)} for k in P}
FOOT_DEMO = {"en": "Try the AI demo", "zh": "试用 AI 演示", "ms": "Cuba demo AI"}
