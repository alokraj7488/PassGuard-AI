/* ============================================================
   PassGuard AI — script.js  v2
   Verify-button triggered · AI-driven strength from backend
   ============================================================ */

let isVisible = false;

// ── Eye toggle ────────────────────────────────────────────────
function toggleVisibility() {
  const input = document.getElementById("password");
  isVisible = !isVisible;
  input.type = isVisible ? "text" : "password";
  document.getElementById("eyeShow").style.display = isVisible ? "none" : "block";
  document.getElementById("eyeHide").style.display = isVisible ? "block" : "none";
}

// ── Live client-side checks (instant, no API) ─────────────────
function onPasswordInput() {
  const pw  = document.getElementById("password").value;
  const btn = document.getElementById("verifyBtn");

  const rules = {
    "chk-length":  pw.length >= 8,
    "chk-upper":   /[A-Z]/.test(pw),
    "chk-number":  /[0-9]/.test(pw),
    "chk-special": /[^A-Za-z0-9]/.test(pw),
  };

  for (const [id, met] of Object.entries(rules)) {
    document.getElementById(id).classList.toggle("met", met);
  }

  // Enable verify only when password is non-empty
  btn.disabled = pw.length === 0;
}

// ── Strength segment bar ──────────────────────────────────────
function setStrength(rating, label) {
  const panel    = document.getElementById("strengthPanel");
  const score    = document.getElementById("strengthScore");
  const badge    = document.getElementById("strengthBadge");
  const segments = document.querySelectorAll(".seg");

  // Determine colour class
  let cls = "weak";
  if (rating >= 9)      cls = "excellent";
  else if (rating >= 7) cls = "strong";
  else if (rating >= 5) cls = "good";
  else if (rating >= 3) cls = "fair";

  // Animate score
  score.textContent = `${rating}/10`;
  score.className   = `strength-score ${cls}`;

  badge.textContent = label;
  badge.className   = `strength-badge ${cls}`;

  // Fill segments with a staggered delay
  segments.forEach((seg, i) => {
    seg.className = "seg"; // reset
    setTimeout(() => {
      if (i < rating) seg.classList.add(cls);
    }, i * 45);
  });

  panel.classList.add("visible");
}

// ── Shimmer skeleton loader ───────────────────────────────────
function showSkeleton(feedbackBox) {
  feedbackBox.innerHTML = `
    <div class="skel" style="width:92%"></div>
    <div class="skel" style="width:78%"></div>
    <div class="skel" style="width:65%"></div>
    <div class="skel" style="width:83%"></div>
    <div class="skel" style="width:50%"></div>
  `;
}

// ── Render markdown-lite feedback ────────────────────────────
function renderFeedback(text) {
  return text
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
    .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\n/g, "<br>");
}

// ── Main verify function (triggered by button only) ───────────
async function analyzePassword() {
  const password    = document.getElementById("password").value.trim();
  const feedbackBox = document.getElementById("feedback");
  const feedbackWrap= document.getElementById("feedbackWrap");
  const verifyBtn   = document.getElementById("verifyBtn");
  const btnIdle     = verifyBtn.querySelector(".btn-idle");
  const btnLoading  = verifyBtn.querySelector(".btn-loading");

  if (!password) return;

  // Button → loading state
  verifyBtn.classList.add("loading");
  verifyBtn.disabled = true;
  btnIdle.style.display   = "none";
  btnLoading.style.display = "flex";

  // Show skeleton in feedback area
  feedbackWrap.classList.add("active");
  showSkeleton(feedbackBox);

  // Reset strength panel while loading
  document.getElementById("strengthPanel").classList.remove("visible");
  document.querySelectorAll(".seg").forEach(s => s.className = "seg");

  try {
    const response = await fetch("/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ password }),
    });

    if (!response.ok) throw new Error(`Server error: ${response.status}`);

    const data = await response.json();

    // Update strength from AI rating
    setStrength(data.rating ?? 0, data.strength ?? "—");

    // Render feedback
    // feedbackBox.innerHTML = renderFeedback(data.feedback || "No feedback received.");
    const feedbackText = data.feedback || "No feedback received.";
    const pwnedText = data.pwned || "";
    feedbackBox.innerHTML = renderFeedback(
      feedbackText + "\n\n---\n\n🔐 **Breach Check**\n" + pwnedText
    );


  } catch (error) {
    feedbackWrap.classList.remove("active");
    feedbackBox.innerHTML = `
      <div style="display:flex;align-items:center;gap:10px;color:var(--weak);font-size:0.85rem;">
        <svg viewBox="0 0 20 20" fill="currentColor" width="18">
          <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/>
        </svg>
        ${error.message || "Could not connect to PassGuard AI. Please try again."}
      </div>`;
  } finally {
    // Restore button
    verifyBtn.classList.remove("loading");
    verifyBtn.disabled = false;
    btnIdle.style.display    = "flex";
    btnLoading.style.display = "none";
  }
}

// ── Allow Enter key to trigger verify ────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("password").addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      const btn = document.getElementById("verifyBtn");
      if (!btn.disabled) analyzePassword();
    }
  });
});
