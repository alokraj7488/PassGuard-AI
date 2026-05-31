# 🔐 PassGuard AI

<div align="center">

### AI-Powered Password Security Analyzer with Breach Detection

Analyze password strength using **Google Gemini 2.5 Flash**, detect compromised credentials through **Have I Been Pwned (HIBP)**, and receive intelligent, personalized security recommendations in real time.

<br>

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge\&logo=flask)
![Gemini](https://img.shields.io/badge/Google-Gemini%202.5%20Flash-4285F4?style=for-the-badge\&logo=google)
![Security](https://img.shields.io/badge/Security-HIBP-2E8B57?style=for-the-badge)

</div>

---

## 🚀 Overview

Traditional password checkers rely on predefined rules and generic scoring mechanisms. PassGuard AI enhances password security analysis by combining AI-powered evaluation with real-world breach intelligence.

The application leverages **Google Gemini 2.5 Flash** to provide contextual strength assessments and personalized recommendations while integrating the **Have I Been Pwned Passwords API** to identify passwords exposed in known data breaches.

---

## ✨ Features

### 🤖 AI-Powered Password Analysis

* Evaluates password strength using Google Gemini 2.5 Flash.
* Provides contextual and human-readable security feedback.
* Generates actionable recommendations to improve password security.

### 🔍 Real-Time Breach Detection

* Checks passwords against the Have I Been Pwned database.
* Identifies compromised passwords exposed in known breaches.
* Uses privacy-preserving verification techniques.

### 💡 Personalized Security Recommendations

* Suggests improvements tailored to the analyzed password.
* Recommends stronger password alternatives when required.

### 🛡️ Privacy-First Security

* Implements SHA-1 hashing and the k-anonymity model.
* Ensures passwords are never transmitted in plain text.
* Performs secure breach verification without exposing user credentials.

### ⚡ Responsive User Experience

* Instant password evaluation through asynchronous requests.
* Clean and responsive interface built with Flask and JavaScript.

---

## 🏗️ System Workflow

```text
User Password
      │
      ▼
SHA-1 Hashing
      │
      ▼
HIBP Breach Check
      │
      ▼
Gemini 2.5 Flash Analysis
      │
      ▼
Password Strength Rating
      │
      ▼
Security Recommendations
      │
      ▼
Improved Password Suggestion
```

---

## 🛠️ Tech Stack

| Category      | Technologies                                      |
| ------------- | ------------------------------------------------- |
| **Backend**   | Python, Flask                                     |
| **AI**        | Google Gemini 2.5 Flash, Google GenAI SDK         |
| **Security**  | Have I Been Pwned API, SHA-1 Hashing, k-Anonymity |
| **Frontend**  | HTML5, CSS3, JavaScript                           |
| **Libraries** | Requests, Python Dotenv                           |

---

## 📂 Project Structure

```text
PassGuard-AI
│
├── static
│   ├── style.css
│   └── script.js
│
├── templates
│   └── index.html
│
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/alokraj7488/PassGuard-AI.git
cd PassGuard-AI
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=your_google_ai_studio_api_key
```

### 5️⃣ Run the Application

```bash
python app.py
```

### 6️⃣ Open in Browser

```text
http://127.0.0.1:5000
```

---

## 🔒 Security & Privacy

PassGuard AI follows the same privacy-preserving mechanism used by the Have I Been Pwned Passwords API.

### How It Works

* Passwords are hashed locally using SHA-1.
* Only the first 5 characters of the hash are sent to HIBP.
* Remaining hash comparison occurs locally.
* Plain-text passwords are never transmitted.
* User credentials remain private throughout the process.

---

## 🎯 Future Enhancements

* Password history tracking
* Advanced password generation
* Dark/Light theme support
* Multi-language support
* User authentication and dashboard
* Password manager integration

---

## 👨‍💻 Author

**Alok Raj**

🔗 GitHub: https://github.com/alokraj7488

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

</div>
