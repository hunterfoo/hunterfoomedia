(() => {
let language='zh';
const toggle=document.getElementById('language');
function setLanguage(next){
 language=next;
 document.documentElement.lang=next==='zh'?'zh-Hans':'en';
 document.querySelectorAll('[data-zh][data-en]').forEach(el=>{
  let value=el.dataset[next].replace(/\\n/g,'\n');
  if(value.includes('&lt;')||value.includes('&gt;')||value.includes('&amp;')){
   value=value.replace(/&amp;/g,'&').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&quot;/g,'"');
  }
  if(value.includes('<')) el.innerHTML=value;
  else el.textContent=value;
 });
 document.querySelectorAll('[data-zh-alt][data-en-alt]').forEach(el=>{el.alt=el.getAttribute(`data-${next}-alt`);});
 if(toggle){
  toggle.textContent=next==='zh'?'EN':'中文';
  toggle.setAttribute('aria-label',next==='zh'?'Switch to English':'切换为中文');
 }
 const nav=document.querySelector('header nav');
 if(nav && !nav.classList.contains('compact')) nav.setAttribute('aria-label',next==='zh'?'主导航':'Main navigation');
 const brand=document.querySelector('.brand');
 if(brand && brand.hasAttribute('data-home-label')) brand.setAttribute('aria-label',next==='zh'?'Hunter Foo Media 首页':'Hunter Foo Media home');
 const message=next==='zh'?'Hi Hunter，我从 Hunter Foo Media 官网过来，想聊聊我的项目。':'Hi Hunter, I found Hunter Foo Media and would love to discuss a project.';
 document.querySelectorAll('a.whatsapp').forEach(a=>{
  const text=a.dataset.wa||message;
  a.href='https://wa.me/60196273143?text='+encodeURIComponent(text);
 });
}
if(toggle) toggle.addEventListener('click',()=>setLanguage(language==='zh'?'en':'zh'));
const year=document.getElementById('year');
if(year) year.textContent=String(new Date().getFullYear());
setLanguage(language);
})();
