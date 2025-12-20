from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
import hashlib
import requests
import re

app = Flask(__name__)

# Gemini configuration
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# --- Function: Check password in HaveIBeenPwned ---
def check_pwned_password(password):
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    try:
        response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}", timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return " Could not connect to HaveIBeenPwned API."

    hashes = (line.split(":") for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return f" This password has appeared in {count} data breaches!"
    return " This password has never been found in known breaches."

# --- Function: AI-based password feedback using Gemini ---
def ai_password_feedback(password):
    breach_result = check_pwned_password(password)

    main_prompt = f"""
    Analyze this password: '{password}'.
    1. Rate its strength from 1–10.
    2. Give 3 specific, non-generic suggestions to improve it.
    3. Mention if it’s predictable or commonly used.
    Breach Info: {breach_result}
    Provide a short, nicely formatted answer with emojis.
    """

    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        response = model.generate_content(main_prompt)
        feedback_text = response.text.strip()

        # --- Extract numeric rating ---
        rating_match = re.search(r'(\d{1,2})/10', feedback_text)
        rating = int(rating_match.group(1)) if rating_match else 0

        # --- Generate a meaningful 10/10 password if not perfect ---
        if rating < 10:
            improve_prompt = f"""
            The user password is: '{password}' (rated {rating}/10).
            Create a STRONG yet MEANINGFUL password that would be rated 10/10.
            Rules:
            - It must be memorable by humans (e.g., a creative passphrase).
            - Combine at least 3 random words (like “OceanTigerDance”) but make it stronger by adding:
              - symbols or numbers in between words
              - capital letters in unpredictable places
            - Avoid using personal data from the given password.
            - Output only the final password, no extra text.
            """

            improve_response = model.generate_content(improve_prompt)
            improved_password = improve_response.text.strip()

            feedback_text += f"\n\n Suggested Password: `{improved_password}`"
        else:
            feedback_text += "\n\n Your password is already 10/10 perfect!"

        return feedback_text

    except Exception as e:
        print(f"Error from Gemini API: {e}")
        return " Error connecting to AI feedback system."

# --- ROUTES ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_password():
    data = request.get_json()
    password = data.get("password", "")

    if not password:
        return jsonify({"feedback": "Please enter a password."})

    feedback = ai_password_feedback(password)
    return jsonify({"feedback": feedback})

if __name__ == "__main__":
    app.run(debug=True)
