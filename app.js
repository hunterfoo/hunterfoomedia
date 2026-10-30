(() => {
// Language is fixed per URL (/, /zh/, /ms/). Do not change <html lang> here.
const lang=(document.documentElement.lang||'en').toLowerCase();
const msgs={
 'en':"Hi Hunter, I'd like a free 20-min diagnosis. My business: ____. Where I'm stuck: ____",
 'zh-hans':'你好 Hunter，我想预约 20 分钟免费诊断。我做的是：＿＿，最卡的是：＿＿',
 'ms':'Hai Hunter, saya nak tempah diagnosis percuma 20 minit. Bisnes saya: ____. Masalah utama: ____'
};
const message=msgs[lang]||msgs.en;
document.querySelectorAll('a.whatsapp').forEach(a=>{
 const text=a.dataset.wa||message;
 a.href='https://wa.me/601133154541?text='+encodeURIComponent(text);
});
const year=document.getElementById('year');
if(year) year.textContent=String(new Date().getFullYear());
})();
