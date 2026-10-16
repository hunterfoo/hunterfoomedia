(() => {
"use strict";
const el = document.getElementById("pd-data");
if (!el) return;
const D = JSON.parse(el.textContent);
const h = (tag, attrs, ...kids) => {
  const n = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) {
    if (k === "class") n.className = v; else if (k === "html") n.innerHTML = v;
    else if (k.startsWith("on")) n.addEventListener(k.slice(2), v); else n.setAttribute(k, v);
  }
  for (const c of kids.flat()) if (c != null) n.append(c);
  return n;
};
const fmt = (s, o) => s.replace(/\{(\w+)\}/g, (_, k) => o[k]);

/* ---------- 1. Recruitment matching ---------- */
(function rec() {
  const root = document.querySelector('[data-demo="rec"]'); if (!root) return;
  const R = D.rec, uid = "rec";
  const sel = (id, opts, labels) => h("select", { id: uid + id, name: id }, opts.map(o => h("option", { value: o }, labels[o])));
  const name = h("input", { id: uid + "name", name: "name", type: "text", autocomplete: "off", value: "" });
  const pos = sel("pos", D.positions, R.pos_labels), area = sel("area", D.areas, R.area_labels);
  const years = h("input", { id: uid + "years", name: "years", type: "number", min: "0", max: "40", value: "2" });
  const boxes = D.tags.map(t => h("label", { class: "pd-check" }, h("input", { type: "checkbox", value: t }), " " + R.tag_labels[t]));
  const presetBar = h("div", { class: "pd-chips", role: "group", "aria-label": R.preset }, h("span", { class: "pd-mini" }, R.preset + ":"),
    D.presets.map(p => h("button", { type: "button", class: "pd-chip", onclick: () => load(p) }, p.name)));
  const out = h("div", { class: "pd-out", "aria-live": "polite" });
  const form = h("form", { class: "pd-form", novalidate: "" },
    h("h4", {}, R.form), presetBar,
    h("label", { for: uid + "name" }, R.name), name,
    h("div", { class: "pd-two" }, h("div", {}, h("label", { for: uid + "pos" }, R.pos), pos), h("div", {}, h("label", { for: uid + "area" }, R.area), area)),
    h("label", { for: uid + "years" }, R.years), years,
    h("fieldset", {}, h("legend", {}, R.tagsl), h("div", { class: "pd-checks" }, boxes)),
    h("button", { type: "submit", class: "button pd-run" }, R.run, h("span", { "aria-hidden": "true" }, "→")));
  form.addEventListener("submit", e => { e.preventDefault(); run(); });
  const jobsList = h("details", { class: "pd-jobs" }, h("summary", {}, R.jobs + " (" + D.jobs.length + ")"),
    h("ul", {}, D.jobs.map(j => h("li", {}, h("b", {}, j.code + " · " + R.pos_labels[j.pos] + " · " + R.area_labels[j.area]), " " + j.pay,
      h("br"), h("small", {}, R.hard + ": " + j.hard.map(t => R.tag_labels[t]).join(", ") + " | " + R.cond + ": " + j.cond.map(t => R.tag_labels[t]).join(", "))))));
  root.append(h("div", { class: "pd-grid" }, form, h("div", {}, out, jobsList)));
  function load(p) {
    name.value = p.name; pos.value = p.pos; area.value = p.area; years.value = p.years;
    boxes.forEach(b => { const i = b.querySelector("input"); i.checked = p.tags.includes(i.value); });
    run();
  }
  function run() {
    const tags = boxes.map(b => b.querySelector("input")).filter(i => i.checked).map(i => i.value);
    const y = Math.max(0, parseInt(years.value, 10) || 0);
    if (y >= 2 && !tags.includes("exp2")) tags.push("exp2");
    if (y < 2) { const i = tags.indexOf("exp2"); if (i > -1) tags.splice(i, 1); }
    const nm = name.value.trim() || R.namedef;
    const res = D.jobs.map(j => {
      const posOk = j.pos === pos.value;
      const missing = j.hard.filter(t => !tags.includes(t));
      const met = j.cond.filter(t => tags.includes(t));
      const ratio = met.length / j.cond.length;
      return { j, posOk, missing, met, ratio, ok: posOk && !missing.length && ratio >= 0.5, near: j.area === area.value };
    });
    const ok = res.filter(r => r.ok).sort((a, b) => (b.near - a.near) || (b.ratio - a.ratio));
    const bad = res.filter(r => !r.ok);
    out.replaceChildren(
      h("div", { class: "pd-card" }, h("h4", {}, R.summary),
        h("dl", { class: "pd-dl" },
          h("dt", {}, R.name), h("dd", {}, nm),
          h("dt", {}, R.pos), h("dd", {}, R.pos_labels[pos.value]),
          h("dt", {}, R.area), h("dd", {}, R.area_labels[area.value]),
          h("dt", {}, R.years), h("dd", {}, fmt(R.yrs, { n: y })),
          h("dt", {}, R.tagsl), h("dd", {}, tags.length ? tags.map(t => R.tag_labels[t]).join(" · ") : "—"))),
      h("div", { class: "pd-card" }, h("h4", {}, R.shortlist + " (" + ok.length + ")"), h("p", { class: "pd-mini" }, R.rules),
        ok.length ? h("ol", { class: "pd-short" }, ok.map(r => h("li", {},
          h("b", {}, r.j.code + " · " + R.pos_labels[r.j.pos] + " · " + R.area_labels[r.j.area]), h("span", { class: "pd-ok" }, "✓ " + R.ok),
          h("ul", { class: "pd-why", "aria-label": R.reasons },
            h("li", {}, "✓ " + R.pos + ": " + R.pos_labels[r.j.pos]),
            h("li", {}, "✓ " + R.hard + ": " + r.j.hard.map(t => R.tag_labels[t]).join(", ")),
            h("li", {}, "✓ " + R.condlow + ": " + r.met.length + "/" + r.j.cond.length + " (" + r.met.map(t => R.tag_labels[t]).join(", ") + ")"),
            r.near ? h("li", {}, "★ " + fmt(R.areapref, { a: R.area_labels[r.j.area] })) : null)))) : h("p", {}, R.none),
        h("details", {}, h("summary", {}, R.notmatched + " (" + bad.length + ")"),
          h("ul", { class: "pd-why" }, bad.map(r => h("li", {}, r.j.code + ": " +
            (!r.posOk ? R.posmiss : r.missing.length ? R.hardmiss + " (" + r.missing.map(t => R.tag_labels[t]).join(", ") + ")" : R.condlow + " " + r.met.length + "/" + r.j.cond.length)))))));
  }
  load(D.presets[0]);
})();

/* ---------- 2. WhatsApp digital employee ---------- */
(function wa() {
  const root = document.querySelector('[data-demo="wa"]'); if (!root) return;
  const W = D.wa;
  const log = h("div", { class: "pd-chatlog", role: "log", "aria-live": "polite" });
  const tags = h("ul", { class: "pd-tags" }), status = h("p", { class: "pd-status" }, "—"), rules = h("ul", { class: "pd-rules" });
  const linkify = s => s.replace(/(https:\/\/\S+)/g, '<span class="pd-link">$1</span> <span class="pd-slabel">(' + W.slabel + ')</span>').replace(/\n/g, "<br>");
  const bubble = (who, html) => h("div", { class: "pd-msg " + who, html: linkify(html) + '<span class="pd-time">' + new Date().toTimeString().slice(0, 5) + (who === "out" ? " ✓✓" : "") + "</span>" });
  let timer = [];
  const reset = () => { timer.forEach(clearTimeout); timer = []; log.replaceChildren(h("p", { class: "pd-sys" }, W.start)); tags.replaceChildren(); status.textContent = "—"; rules.replaceChildren(); btns.forEach(b => b.disabled = false); };
  const btns = W.msgs.map(m => h("button", { type: "button", class: "pd-chip pd-block", onclick: () => send(m) }, m.label));
  function send(m) {
    btns.forEach(b => b.disabled = true);
    log.querySelector(".pd-sys")?.remove();
    log.append(bubble("in", m.user)); log.scrollTop = log.scrollHeight;
    const typing = h("div", { class: "pd-msg out pd-typing", "aria-label": "typing" }, "• • •");
    m.bot.forEach((b, i) => timer.push(setTimeout(() => {
      typing.remove(); log.append(bubble("out", b));
      if (i < m.bot.length - 1) log.append(typing);
      log.scrollTop = log.scrollHeight;
      if (i === m.bot.length - 1) {
        tags.replaceChildren(...m.tags.map(t => h("li", {}, t)));
        status.textContent = m.status;
        rules.replaceChildren(...m.rules.map(r => h("li", {}, "✓ " + r)));
        btns.forEach(x => x.disabled = false);
      }
    }, 500 + i * 700)));
    log.append(typing);
  }
  root.append(h("div", { class: "pd-grid pd-wagrid" },
    h("div", {}, h("h4", {}, W.pick), h("div", { class: "pd-stack" }, btns), h("button", { type: "button", class: "pd-reset", onclick: reset }, W.reset)),
    h("div", { class: "pd-phone" }, h("div", { class: "pd-phonebar" }, h("span", { class: "pd-avatar", "aria-hidden": "true" }, "HF"), h("div", {}, h("b", {}, "Digital Employee"), h("small", {}, W.online))), log),
    h("aside", { class: "pd-card pd-panel", "aria-label": W.panel }, h("h4", {}, W.panel), h("p", { class: "pd-mini" }, W.contact + ": +60 1X-XXX XXXX"),
      h("h5", {}, W.tagsl), tags, h("h5", {}, W.statusl), status, h("h5", {}, W.rulesl), rules)));
  reset();
})();

/* ---------- 3. Content automation ---------- */
(function ct() {
  const root = document.querySelector('[data-demo="ct"]'); if (!root) return;
  const C = D.ct;
  const tabs = h("div", { class: "pd-chips", role: "tablist", "aria-label": C.pick });
  const body = h("div", { class: "pd-ctbody", role: "tabpanel" });
  const tabBtns = C.types.map((t, i) => h("button", { type: "button", role: "tab", class: "pd-chip", "aria-selected": "false", onclick: () => show(i) }, t.name));
  tabs.append(...tabBtns);
  function show(i) {
    const t = C.types[i];
    tabBtns.forEach((b, j) => b.setAttribute("aria-selected", String(i === j)));
    const st = h("p", { class: "pd-approval", "aria-live": "polite" }, C.pending);
    const ap = h("button", { type: "button", class: "button pd-run" }, C.approve, h("span", { "aria-hidden": "true" }, "✓"));
    const ch = h("button", { type: "button", class: "pd-reset" }, C.change);
    ap.addEventListener("click", () => { st.textContent = fmt(C.approved, { t: t.when }); st.dataset.state = "ok"; ap.disabled = ch.disabled = true; });
    ch.addEventListener("click", () => { st.textContent = C.changed; st.dataset.state = "back"; });
    body.replaceChildren(
      h("div", { class: "pd-grid" },
        h("div", {}, h("h4", {}, C.cal), h("ol", { class: "pd-cal" }, t.week.map(([d, x], k) => h("li", { class: k === 1 ? "on" : "" }, h("b", {}, d), h("span", {}, x))))),
        h("div", {}, h("h4", {}, C.post), h("div", { class: "pd-posts" }, t.pages.map(([pg, tx]) => h("div", { class: "pd-post" }, h("p", { class: "pd-pg" }, h("span", { class: "pd-avatar", "aria-hidden": "true" }, "f"), " " + pg), h("p", {}, tx)))),
          h("div", { class: "pd-card pd-approve" }, h("h5", {}, "👤 " + C.step), st, h("div", { class: "pd-row" }, ap, ch)))));
  }
  root.append(h("h4", {}, C.pick), tabs, body);
  show(0);
})();
/* ---------- 4. ChatGPT Ads draft + approval ---------- */
(function ads() {
  const root = document.querySelector('[data-demo="ads"]'); if (!root || !D.ads) return;
  const C = D.ads;
  const tabs = h("div", { class: "pd-chips", role: "tablist", "aria-label": C.pick });
  const body = h("div", { class: "pd-ctbody", role: "tabpanel" });
  const tabBtns = C.types.map((t, i) => h("button", { type: "button", role: "tab", class: "pd-chip", "aria-selected": "false", onclick: () => show(i, 0) }, t.name));
  tabs.append(...tabBtns);
  function show(i, qi) {
    const t = C.types[i], q = t.qs[qi];
    tabBtns.forEach((b, j) => b.setAttribute("aria-selected", String(i === j)));
    const st = h("p", { class: "pd-approval", "aria-live": "polite" }, C.pending);
    const ap = h("button", { type: "button", class: "button pd-run" }, C.approve, h("span", { "aria-hidden": "true" }, "✓"));
    const ch = h("button", { type: "button", class: "pd-reset" }, C.change);
    ap.addEventListener("click", () => { st.textContent = C.approved; st.dataset.state = "ok"; ap.disabled = ch.disabled = true; });
    ch.addEventListener("click", () => { st.textContent = C.changed; st.dataset.state = "back"; });
    const qs = h("ol", { class: "pd-cal pd-qs" }, t.qs.map((x, k) => h("li", { class: k === qi ? "on" : "" },
      h("button", { type: "button", class: "pd-q", "aria-pressed": String(k === qi), onclick: () => show(i, k) }, x.q))));
    body.replaceChildren(
      h("div", { class: "pd-grid" },
        h("div", {}, h("h4", {}, C.qh), qs),
        h("div", {}, h("h4", {}, C.ph),
          h("div", { class: "pd-post pd-askpost" }, h("p", { class: "pd-pg" }, "💬 " + q.q), h("p", { class: "pd-mini" }, C.ans)),
          h("div", { class: "pd-adcard" }, h("span", { class: "pd-adsp" }, C.sp), h("span", { class: "pd-adbiz" }, t.biz), h("strong", {}, q.h), h("span", {}, q.d), h("span", { class: "pd-adurl" }, t.url)),
          h("p", { class: "pd-mini pd-adnext" }, h("b", {}, C.nexth + ": "), C.nextt),
          h("div", { class: "pd-card pd-approve" }, h("h5", {}, "👤 " + C.step), st, h("div", { class: "pd-row" }, ap, ch)))));
  }
  root.replaceChildren(h("h4", {}, C.pick), tabs, body);
  show(0, 0);
})();
})();
