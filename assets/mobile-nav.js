(() => {
const btn = document.querySelector(".menu-toggle"); if (!btn) return;
const hdr = btn.closest("header"), mq = matchMedia("(max-width:760px)");
const set = open => { hdr.classList.toggle("menu-open", open); btn.setAttribute("aria-expanded", String(open)); btn.querySelector(".lbl").textContent = open ? btn.dataset.close : btn.dataset.open; };
btn.addEventListener("click", () => set(btn.getAttribute("aria-expanded") !== "true"));
document.addEventListener("keydown", e => { if (e.key === "Escape" && hdr.classList.contains("menu-open")) { set(false); btn.focus(); } });
hdr.addEventListener("click", e => { if (e.target.closest("nav a, .lang-switch a, .btn, .header-contact")) set(false); });
mq.addEventListener("change", e => { if (!e.matches) set(false); });
})();
