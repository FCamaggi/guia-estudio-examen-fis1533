(function () {
  "use strict";
  /* ---------- Quiz ---------- */
  var qs = document.querySelectorAll(".q");
  function paintScore() {
    var ok = document.querySelectorAll(".q.correct").length;
    var ans = document.querySelectorAll(".q.answered").length;
    document.getElementById("score").textContent = ok + "/" + qs.length + " correctas" + (ans < qs.length ? " · " + (qs.length - ans) + " sin responder" : "");
  }
  qs.forEach(function (q) {
    var correct = q.getAttribute("data-correct");
    q.querySelectorAll(".opts button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        if (q.classList.contains("answered")) return;
        q.classList.add("answered");
        var pick = btn.getAttribute("data-o");
        q.querySelectorAll(".opts button").forEach(function (b) {
          b.disabled = true;
          if (b.getAttribute("data-o") === correct) b.classList.add("right");
        });
        if (pick === correct) q.classList.add("correct"); else btn.classList.add("wrong");
        paintScore();
      });
    });
  });
  document.getElementById("quiz-reset").addEventListener("click", function () {
    qs.forEach(function (q) {
      q.classList.remove("answered", "correct");
      q.querySelectorAll(".opts button").forEach(function (b) { b.disabled = false; b.classList.remove("right", "wrong"); });
    });
    paintScore();
  });
  paintScore();
})();
