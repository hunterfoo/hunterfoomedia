(() => {
let language='zh';
const toggle=document.getElementById('language');
function setLanguage(next){
 language=next;document.documentElement.lang=next==='zh'?'zh-Hans':'en';
 document.querySelectorAll('[data-zh][data-en]').forEach(el=>{el.textContent=el.dataset[next].replace(/\\n/g,'\n');});
 document.querySelectorAll('[data-zh-alt][data-en-alt]').forEach(el=>{el.alt=el.getAttribute(`data-${next}-alt`);});
 toggle.textContent=next==='zh'?'EN':'中文';toggle.setAttribute('aria-label',next==='zh'?'Switch to English':'切换为中文');
 document.querySelector('nav').setAttribute('aria-label',next==='zh'?'主导航':'Main navigation');
 document.querySelector('.brand').setAttribute('aria-label',next==='zh'?'Hunter Foo Media 首页':'Hunter Foo Media home');
 const message=next==='zh'?'Hi Hunter，我从 Hunter Foo Media 官网过来，想聊聊我的项目。':'Hi Hunter, I found Hunter Foo Media and would love to discuss a project.';
 document.querySelectorAll('.whatsapp').forEach(a=>{a.href='https://wa.me/60196273143?text='+encodeURIComponent(message);});
}
toggle.addEventListener('click',()=>setLanguage(language==='zh'?'en':'zh'));
document.getElementById('year').textContent=String(new Date().getFullYear());
setLanguage('zh');
})();
