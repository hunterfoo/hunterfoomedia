(() => {
"use strict";
const dataEl = document.getElementById("dm-data");
if (!dataEl) return;
const D = JSON.parse(dataEl.textContent);
const root = document.documentElement;
root.classList.add("dm-on");
const reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
const h = (tag, attrs, ...kids) => {
  const n = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) {
    if (k === "class") n.className = v;
    else if (k.startsWith("on")) n.addEventListener(k.slice(2), v);
    else n.setAttribute(k, v);
  }
  for (const c of kids.flat()) if (c != null) n.append(c);
  return n;
};
const wait = (fn, ms) => setTimeout(fn, reduce ? Math.min(ms, 120) : ms);
const resetBtn = (fn) => h("button", { type: "button", class: "dm-btn dm-ghost", onclick: fn }, D.ui.reset);

/* ---------- Website AI: before / after ---------- */
function wb(box) {
  const d = D.wb;
  let after = false;
  const bBefore = h("button", { type: "button", "aria-pressed": "true" }, d.before);
  const bAfter = h("button", { type: "button", "aria-pressed": "false" }, d.after);
  const seg = h("div", { class: "dm-seg", role: "group", "aria-label": d.toggle }, bBefore, bAfter);
  const page = h("div", { class: "dm-page" });
  const read = h("div", { class: "dm-read", "aria-live": "polite" });
  const draw = () => {
    bBefore.setAttribute("aria-pressed", String(!after));
    bAfter.setAttribute("aria-pressed", String(after));
    page.className = "dm-page " + (after ? "is-after" : "is-before");
    page.replaceChildren(
      h("div", { class: "dm-bar" }, h("i"), h("i"), h("i")),
      h("div", { class: "dm-pg" },
        h("h3", {}, after ? d.ah : d.bh),
        h("p", {}, after ? d.ap : d.bp),
        after ? h("div", { class: "dm-faq" }, h("strong", {}, d.aq), h("p", {}, d.aa)) : null));
    read.replaceChildren(
      h("p", { class: "dm-ask" }, h("span", {}, d.ask_l), d.q),
      h("p", { class: "dm-ans " + (after ? "ok" : "bad") }, after ? d.aafter : d.abefore),
      h("ul", { class: "dm-checks" }, d.checks.map(c =>
        h("li", { class: after ? "ok" : "bad" }, h("span", { "aria-hidden": "true" }, after ? "✓" : "✕"), c + ": ", h("b", {}, after ? d.clear : d.unclear)))));
  };
  bBefore.addEventListener("click", () => { after = false; draw(); });
  bAfter.addEventListener("click", () => { after = true; draw(); });
  draw();
  box.append(seg, h("div", { class: "dm-two" },
    h("div", {}, h("p", { class: "dm-lab" }, d.page_l), page),
    h("div", {}, h("p", { class: "dm-lab" }, d.read_l), read)));
}

/* ---------- Marketing AI: topic -> draft -> approve ---------- */
function mk(box) {
  const d = D.mk;
  let topic = 0, kind = "social", idx = 0, approved = false;
  const topicsEl = h("div", { class: "dm-chips", role: "group", "aria-label": d.topic_l });
  const kindsEl = h("div", { class: "dm-seg", role: "group", "aria-label": d.kind_l });
  const ta = h("textarea", { class: "dm-ta", rows: "5", "aria-label": d.draft_l });
  const status = h("p", { class: "dm-status wait", "aria-live": "polite" });
  const okBtn = h("button", { type: "button", class: "dm-btn" }, d.approve);
  const anBtn = h("button", { type: "button", class: "dm-btn dm-ghost" }, d.another);
  const tb = d.topics.map((t, i) => h("button", { type: "button", class: "dm-chip", "aria-pressed": String(i === 0), onclick: () => { topic = i; idx = 0; load(); } }, t.n));
  topicsEl.append(...tb);
  const kb = ["social", "gbp"].map(k => h("button", { type: "button", "aria-pressed": String(k === "social"), onclick: () => { kind = k; idx = 0; load(); } }, d[k]));
  kindsEl.append(...kb);
  function load() {
    approved = false;
    tb.forEach((b, i) => b.setAttribute("aria-pressed", String(i === topic)));
    kb.forEach((b, i) => b.setAttribute("aria-pressed", String(["social", "gbp"][i] === kind)));
    ta.value = d.topics[topic][kind][idx];
    ta.disabled = false; okBtn.disabled = false; anBtn.disabled = false;
    status.className = "dm-status wait"; status.textContent = d.waiting;
  }
  okBtn.addEventListener("click", () => { approved = true; ta.disabled = true; okBtn.disabled = true; anBtn.disabled = true; status.className = "dm-status ok"; status.textContent = d.approved; });
  anBtn.addEventListener("click", () => { const n = d.topics[topic][kind].length; idx = (idx + 1) % n; load(); });
  load();
  box.append(h("p", { class: "dm-lab" }, d.topic_l), topicsEl, h("p", { class: "dm-lab" }, d.kind_l), kindsEl,
    h("p", { class: "dm-lab" }, d.draft_l), ta, status, h("div", { class: "dm-actions" }, okBtn, anBtn));
}

/* ---------- Customer Service AI: scripted chat ---------- */
function cs(box) {
  const d = D.cs;
  const log = h("div", { class: "dm-chat", role: "log", "aria-live": "polite" });
  const input = h("input", { type: "text", class: "dm-input", placeholder: d.ph, "aria-label": d.ph, autocomplete: "off", maxlength: "200" });
  const form = h("form", { class: "dm-form" }, input, h("button", { type: "submit", class: "dm-btn" }, d.send));
  let busy = false, followed = false;
  const msg = (who, text, extra) => {
    const m = h("div", { class: "dm-msg " + who }, h("span", { class: "dm-who" }, who === "me" ? d.you : d.bot), h("p", {}, text));
    if (extra) m.append(extra);
    log.append(m); log.scrollTop = log.scrollHeight; return m;
  };
  const sys = (text, cls) => { log.append(h("p", { class: "dm-sys " + (cls || "") }, text)); log.scrollTop = log.scrollHeight; };
  const norm = s => s.toLowerCase().normalize("NFKC");
  function answer(q) {
    const t = norm(q);
    if (d.complex.some(w => t.includes(w))) return { a: d.handoff, hand: true };
    for (const e of d.qa) if (e.k.some(w => t.includes(w))) return { a: e.a };
    return { a: d.handoff, hand: true };
  }
  function ask(q) {
    q = q.trim(); if (!q || busy) return;
    busy = true; msg("me", q); input.value = "";
    const typing = h("p", { class: "dm-sys" }, "…"); log.append(typing); log.scrollTop = log.scrollHeight;
    wait(() => {
      typing.remove();
      const r = answer(q);
      msg("bot", r.a);
      if (r.hand) sys("↪ " + d.handed, "hand");
      busy = false;
    }, 650);
  }
  form.addEventListener("submit", e => { e.preventDefault(); ask(input.value); });
  const chips = h("div", { class: "dm-chips" }, d.chips.map(c => h("button", { type: "button", class: "dm-chip", onclick: () => ask(c) }, c)));
  const follow = h("button", { type: "button", class: "dm-btn dm-ghost", onclick: () => {
    if (followed || busy) return; followed = true; follow.disabled = true;
    sys(d.later, "later"); wait(() => msg("bot", d.fmsg), 500);
  } }, d.follow);
  const start = () => { log.replaceChildren(); followed = false; follow.disabled = false; busy = false; msg("bot", d.hi); };
  start();
  box.append(log, h("p", { class: "dm-lab" }, d.tryq), chips, form, h("div", { class: "dm-actions" }, follow, resetBtn(start)));
}

/* ---------- Clerk AI: files sorted into folders ---------- */
function ck(box) {
  const d = D.ck;
  const pile = h("ul", { class: "dm-pile", "aria-label": d.pile_l });
  const rots = [-3, 2, -1, 4, -4, 1, 3, -2, 2, -3];
  const chips = d.files.map((f, i) => {
    const li = h("li", { class: "dm-file" }, h("span", { class: "dm-fi", "aria-hidden": "true" }), h("span", {}, f[0]));
    li.dataset.f = f[1]; li.style.setProperty("--r", rots[i % rots.length] + "deg");
    return li;
  });
  const folders = {};
  const fgrid = h("div", { class: "dm-folders" }, d.folders.map(f => {
    const list = h("ul", { class: "dm-flist" }); const cnt = h("b", {}, "0");
    folders[f.id] = { list, cnt };
    return h("div", { class: "dm-folder" }, h("h4", {}, h("span", { class: "dm-ficon", "aria-hidden": "true" }), f.n, " ", cnt), list);
  }));
  const status = h("p", { class: "dm-status", "aria-live": "polite" });
  const sortBtn = h("button", { type: "button", class: "dm-btn" }, d.sort);
  pile.append(...chips);
  const counts = () => { for (const f of d.folders) folders[f.id].cnt.textContent = folders[f.id].list.children.length; };
  function move(toFolders) {
    const first = chips.map(c => c.getBoundingClientRect());
    chips.forEach(c => (toFolders ? folders[c.dataset.f].list : pile).append(c));
    chips.forEach((c, i) => {
      c.classList.toggle("sorted", toFolders);
      if (reduce) return;
      const l = c.getBoundingClientRect();
      const r = getComputedStyle(c).getPropertyValue("--r");
      c.style.transition = "none";
      c.style.transform = "translate(" + (first[i].left - l.left) + "px," + (first[i].top - l.top) + "px) rotate(" + (toFolders ? r : "0deg") + ")";
      requestAnimationFrame(() => requestAnimationFrame(() => {
        c.style.transition = "transform .7s cubic-bezier(.2,.8,.2,1) " + (i * 70) + "ms";
        c.style.transform = "";
      }));
    });
    counts();
  }
  sortBtn.addEventListener("click", () => {
    if (pile.children.length === 0) return;
    move(true); sortBtn.disabled = true;
    status.className = "dm-status ok";
    status.textContent = d.done.replace("{n}", d.files.length).replace("{m}", d.folders.length);
  });
  const back = () => { if (pile.children.length) return; move(false); sortBtn.disabled = false; status.className = "dm-status"; status.textContent = ""; };
  box.append(h("p", { class: "dm-lab" }, d.pile_l), pile, h("div", { class: "dm-actions" }, sortBtn, resetBtn(back)), status, fgrid);
}

/* ---------- Manager AI: daily progress report ---------- */
function mg(box) {
  const d = D.mg;
  const out = h("div", { class: "dm-report", "aria-live": "polite" });
  const gen = h("button", { type: "button", class: "dm-btn" }, d.gen);
  const reset = () => { out.replaceChildren(); gen.disabled = false; };
  function show() {
    const c = { done: 0, track: 0, stuck: 0 }; d.rows.forEach(r => c[r[2]]++);
    out.replaceChildren(h("div", { class: "dm-rep" },
      h("h3", {}, d.title),
      h("p", { class: "dm-sum" }, d.sum.replace("{d}", c.done).replace("{t}", c.track).replace("{s}", c.stuck)),
      h("ul", { class: "dm-rows" }, d.rows.map(r => h("li", { class: "dm-row st-" + r[2] },
        h("b", {}, r[0]), h("span", { class: "dm-task" }, r[1]), h("span", { class: "dm-pill " + r[2] }, d.st[r[2]]), h("em", {}, r[3])))),
      h("div", { class: "dm-two dm-two-s" },
        h("div", { class: "dm-box stuck" }, h("h4", {}, d.stuck_l), h("p", {}, d.stuck)),
        h("div", { class: "dm-box" }, h("h4", {}, d.today_l), h("ul", {}, d.today.map(t => h("li", {}, t)))))));
  }
  gen.addEventListener("click", () => {
    gen.disabled = true; out.replaceChildren(h("p", { class: "dm-sys" }, d.prep)); wait(show, 700);
  });
  box.append(h("div", { class: "dm-actions" }, gen, resetBtn(reset)), out);
}

/* ---------- PA AI: schedule, reminders, draft awaiting confirm ---------- */
function pa(box) {
  const d = D.pa;
  const sched = h("ul", { class: "dm-sched" }, d.sched.map(s => h("li", {}, h("b", {}, s[0]), s[1])));
  const moved = h("li", { class: "dm-moved", hidden: "" }, h("b", {}, d.moved[0]), d.moved[1]);
  sched.append(moved);
  const rem = h("ul", { class: "dm-rem" }, d.rem.map((r, i) => {
    const id = "dm-rem-" + i;
    return h("li", {}, h("input", { type: "checkbox", id }), h("label", { for: id }, r));
  }));
  const ta = h("textarea", { class: "dm-ta", rows: "4", "aria-label": d.draft_l }); ta.value = d.draft;
  const status = h("p", { class: "dm-status wait", "aria-live": "polite" }, d.waiting);
  const ok = h("button", { type: "button", class: "dm-btn" }, d.confirm);
  ok.addEventListener("click", () => { ta.disabled = true; ok.disabled = true; moved.hidden = false; status.className = "dm-status ok"; status.textContent = d.sent; });
  const reset = () => {
    ta.disabled = false; ta.value = d.draft; ok.disabled = false; moved.hidden = true;
    status.className = "dm-status wait"; status.textContent = d.waiting;
    rem.querySelectorAll("input").forEach(i => { i.checked = false; });
  };
  box.append(h("div", { class: "dm-three" },
    h("div", { class: "dm-box" }, h("h4", {}, d.sched_l), sched),
    h("div", { class: "dm-box" }, h("h4", {}, d.rem_l), rem),
    h("div", { class: "dm-box" }, h("h4", {}, d.in_l),
      h("blockquote", { class: "dm-in" }, h("cite", {}, d.from_), d.inmsg),
      h("h4", {}, d.draft_l), ta, status, h("div", { class: "dm-actions" }, ok, resetBtn(reset)))));
}

/* ---------- tabs ---------- */
const builders = { wb, mk, cs, ck, mg, pa };
const tabs = [...document.querySelectorAll(".dm-tab")];
const panels = [...document.querySelectorAll(".dm-panel")];
const built = {};
function activate(i, focus, setHash) {
  tabs.forEach((t, j) => { const on = i === j; t.setAttribute("aria-selected", String(on)); t.tabIndex = on ? 0 : -1; t.classList.toggle("is-active", on); });
  panels.forEach((p, j) => p.classList.toggle("is-active", i === j));
  const id = panels[i].id.replace("dm-p-", "");
  if (!built[id]) { built[id] = true; builders[id](panels[i].querySelector(".dm-mock")); }
  if (focus) tabs[i].focus();
  if (setHash && history.replaceState) history.replaceState(null, "", "#" + id);
}
tabs.forEach((t, i) => {
  t.addEventListener("click", () => activate(i, false, true));
  t.addEventListener("keydown", e => {
    const k = e.key; let n = null;
    if (k === "ArrowRight" || k === "ArrowDown") n = (i + 1) % tabs.length;
    else if (k === "ArrowLeft" || k === "ArrowUp") n = (i + tabs.length - 1) % tabs.length;
    else if (k === "Home") n = 0; else if (k === "End") n = tabs.length - 1;
    if (n != null) { e.preventDefault(); activate(n, true, true); }
  });
});
const ids = panels.map(p => p.id.replace("dm-p-", ""));
const start = ids.indexOf(location.hash.slice(1));
activate(start >= 0 ? start : 0, false, false);
})();
