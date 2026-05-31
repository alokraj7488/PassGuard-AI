from flask import Flask, render_template, request, jsonify
from google import genai
import hashlib
import requests
import re

app = Flask(__name__)

# ✅ Gemini configuration (NEW SDK)
client = genai.Client(api_key="AIzaSyAZT_ARBQsqFzNgnEvWMZ0st_r1NHLyZ94")


# --- Function: Check password in HaveIBeenPwned ---
def check_pwned_password(password):
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    try:
        response = requests.get(
            f"https://api.pwnedpasswords.com/range/{prefix}", timeout=5
        )
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return "Could not connect to HaveIBeenPwned API."

    hashes = (line.split(":") for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return f"⚠️ This password has appeared in **{count}** data breaches!"
    return "✅ This password has never been found in known breaches."


# --- Map numeric rating to strength label ---
def rating_to_strength(rating):
    if rating <= 2:
        return "Weak"
    elif rating <= 4:
        return "Fair"
    elif rating <= 6:
        return "Good"
    elif rating <= 8:
        return "Strong"
    else:
        return "Excellent"


# --- Function: AI-based password feedback using Gemini ---
def ai_password_feedback(password):
    breach_result = check_pwned_password(password)

    # ✅ Single optimized prompt
    main_prompt = f"""
    Analyze this password: '{password}'.

    Provide:
    1. Strength rating (format exactly like: X/10)
    2. Strength label (Weak, Fair, Good, Strong, Excellent)
    3. 3 specific suggestions to improve it
    4. ONE improved strong password suggestion

    Breach Info: {breach_result}

    Format your response clearly like this:

    Rating: X/10  
    Strength: <label>  

    Suggestions:
    - ...
    - ...
    - ...

    Suggested Password:
    <password only>

    Keep it short and clean.
    """

    try:
        # ✅ ONLY ONE API CALL
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=main_prompt
        )

        feedback_text = response.text.strip()

        # --- Extract rating ---
        rating_match = re.search(r"(\d{1,2})/10", feedback_text)
        rating = int(rating_match.group(1)) if rating_match else 5

        # --- Extract strength label ---
        strength_match = re.search(
            r"(Weak|Fair|Good|Strong|Excellent)", feedback_text, re.IGNORECASE
        )
        strength_label = (
            strength_match.group(1).capitalize()
            if strength_match else rating_to_strength(rating)
        )

        return {
            "feedback": feedback_text,
            "rating": rating,
            "strength": strength_label,
            "pwned": breach_result
        }

    except Exception as e:
        print("Gemini Error:", e)
        return {
            "feedback": f"❌ Error connecting to AI feedback system: {str(e)}",
            "rating": 0,
            "strength": "Unknown",
        }


# --- ROUTES ---
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze_password():
    data = request.get_json()
    password = data.get("password", "")

    if not password:
        return jsonify({
            "feedback": "Please enter a password.",
            "rating": 0,
            "strength": "—"
        })

    result = ai_password_feedback(password)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)