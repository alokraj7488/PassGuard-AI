let timeout;

async function analyzePassword() {
  const password = document.getElementById("password").value;
  const feedbackBox = document.getElementById("feedback");

  if (!password) {
    feedbackBox.textContent = "Start typing to get feedback...";
    return;
  }

  // Debounce to avoid multiple rapid calls
  clearTimeout(timeout);
  timeout = setTimeout(async () => {
    feedbackBox.textContent = "⏳ Analyzing password...";
    
    try {
      const response = await fetch("/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password }),
      });

      const data = await response.json();
      feedbackBox.innerHTML = data.feedback.replace(/\n/g, "<br>");
    } catch (error) {
      feedbackBox.textContent = "❌ Error connecting to server.";
    }
  }, 700);
}
