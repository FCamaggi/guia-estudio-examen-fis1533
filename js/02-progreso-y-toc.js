(function () {
  "use strict";
  var KEY = "fis1533-i2-dominados";
  var store = {
    get: function () { try { return JSON.parse(localStorage.getItem(KEY) || "{}"); } catch (e) { return {}; } },
    set: function (v) { try { localStorage.setItem(KEY, JSON.stringify(v)); } catch (e) {} }
  };

  /* ---------- Progreso ---------- */
  var done = store.get();
  var masters = document.querySelectorAll(".master");
  function paintProgress() {
    var n = 0, na = 0, tot = 0, tota = 0;
    masters.forEach(function (b) {
      var id = b.getAttribute("data-sec");
      var on = !!done[id];
      var isAy = id.indexOf("ay") === 0;
      if (isAy) { tota++; if (on) na++; } else { tot++; if (on) n++; }
      b.setAttribute("aria-pressed", on ? "true" : "false");
      var link = document.querySelector('.toc a[data-sec="' + id + '"]');
      if (link) link.classList.toggle("done", on);
    });
    document.getElementById("prog-count").textContent = n;
    document.getElementById("prog-bar").style.width = (100 * n / Math.max(tot, 1)) + "%";
    document.getElementById("prog-count-ay").textContent = na;
    document.getElementById("prog-bar-ay").style.width = (100 * na / Math.max(tota, 1)) + "%";
  }
  masters.forEach(function (b) {
    b.addEventListener("click", function () {
      var id = b.getAttribute("data-sec");
      done[id] = !done[id];
      store.set(done);
      paintProgress();
    });
  });
  paintProgress();

  /* ---------- Sección activa en el índice ---------- */
  var links = {};
  document.querySelectorAll(".toc a").forEach(function (a) { links[a.getAttribute("href").slice(1)] = a; });
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting && links[e.target.id]) {
          Object.keys(links).forEach(function (k) { links[k].classList.remove("active"); });
          links[e.target.id].classList.add("active");
          var l = links[e.target.id];
          if (window.innerWidth <= 900 && l.scrollIntoView) {
            var nav = l.parentElement;
            nav.scrollTo({ left: l.offsetLeft - 12, behavior: "smooth" });
          }
        }
      });
    }, { rootMargin: "-20% 0px -70% 0px" });
    document.querySelectorAll("section.sec").forEach(function (s) { io.observe(s); });
  }
})();
