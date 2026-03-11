# 🔐 PassGuard AI (AI-Password Strength Analyzer with Breach Detection)

An intelligent password evaluator that combines **Google's Gemini AI** for smart strength analysis and the **Have I Been Pwned (HIBP)** API to check for compromised passwords in real time.

Unlike traditional rule-based tools, this analyzer delivers **personalized, natural-language feedback** powered by AI — making password security intuitive for everyone.

## ✨ Features

- **AI-Driven Strength Scoring**: Uses **Gemini AI** to evaluate passwords contextually and generate human-readable feedback (e.g., “This password is weak because it uses a common phrase”).
- **Real-Time Breach Detection**: Integrates with the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3) using k-anonymity to safely check if a password has appeared in known data breaches.
- **Responsive Web Interface**: Built with **Flask (Python)** on the backend and **HTML/CSS/JavaScript** on the frontend for a smooth, mobile-friendly user experience.
- **Personalized Recommendations**: Offers actionable tips (e.g., “Add symbols and numbers” or “Avoid dictionary words”) based on AI analysis.
- **Instant Feedback**: Analyzes passwords as you type—no page reloads needed.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **AI**: Google Generative AI (Gemini API)
- **Security**: Have I Been Pwned API (v3)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript (or specify if you used a framework)
- **Environment Management**: `.env` for secure API key handling

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- A [Google AI Studio API key](https://aistudio.google.com/app/apikey)
- Internet connection (for HIBP and Gemini API calls)

### Setup

1. **Clone the repository** -
   git clone https://github.com/alokraj7488/AI-Powered_Password_Strength_Analyzer.git
   cd AI-Powered_Password_Strength_Analyzer
