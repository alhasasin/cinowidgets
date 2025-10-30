from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# -----------------------
# WEBSITE ROUTES
# -----------------------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/chat-widget')
def chat_widget():
    return render_template('widget.html')


# -----------------------
# SMART CHATBOT LOGIC
# -----------------------

@app.route('/get', methods=['POST'])
def chatbot_response():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    # Intent-based keyword detection
    greetings = ["hello", "hi", "hey", "good morning", "good afternoon"]
    breads = ["bread", "loaf", "small bread", "large bread", "medium bread"]
    snacks = ["snack", "meat pie", "egg roll", "doughnut", "puff", "pie"]
    price = ["price", "cost", "how much", "amount"]
    thanks = ["thanks", "thank you", "appreciate"]
    location = ["location", "where", "address", "place", "find you"]
    contact = ["phone", "contact", "call", "number"]
    hours = ["open", "close", "time", "working hours"]

    # Responses for each category
    if any(word in user_message for word in greetings):
        reply = random.choice([
            "Hello there! 👋 Welcome to CINO Bakery & Confectionary!",
            "Hey! Nice to see you 😊 What delicious treat can I get you today?",
            "Welcome to CINO Bakery — where every bite is happiness! 🍞"
        ])

    elif any(word in user_message for word in breads):
        reply = random.choice([
            "We bake fresh loaves every morning — small, medium, and large sizes 🍞.",
            "Our bread is soft and fresh! Available in small (₦300), medium (₦600), large (₦1000) and jumbo (₦1500) sizes.",
            "You’ll love our golden-brown bread — it’s our customer favorite!"
        ])

    elif any(word in user_message for word in snacks):
        reply = random.choice([
            "We have hot snacks like meat pies, doughnuts, and egg rolls 😋.",
            "Craving something crunchy? Try our pastries — baked fresh every few hours.",
            "Snacks available: meat pie, doughnut, puff puff, and sausage rolls!"
        ])

    elif any(word in user_message for word in price):
        reply = random.choice([
            "Our bread prices: Small ₦300, Medium ₦600, Large ₦1000, Jumbo ₦1500.",
            "Snacks like meat pie and doughnut go for ₦400 each.",
            "All our prices are friendly and worth the taste! 😍"
        ])

    elif any(word in user_message for word in location):
        reply = random.choice([
            "📍 We’re located at No. 18 Dogon Bauchi Road, Sabon Gari, Zaria.",
            "You can find us easily in Sabon Gari Market — follow the sweet smell of bread 😉",
            "We’re right at the heart of Zaria — Dogon Bauchi Road, Sabon Gari."
        ])

    elif any(word in user_message for word in contact):
        reply = random.choice([
            "📞 Call or WhatsApp us at 0803 260 0887.",
            "You can reach us anytime at cinofoods@gmail.com or 0803 260 0887.",
            "Need help? Chat with us here or call 08032600887."
        ])

    elif any(word in user_message for word in hours):
        reply = random.choice([
            "We’re open every day from 7:00 AM to 8:00 PM 🕗.",
            "You can visit us between 7 AM and 8 PM daily — fresh bakes all day!",
            "We open bright and early (7 AM) till evening (8 PM)."
        ])

    elif any(word in user_message for word in thanks):
        reply = random.choice([
            "You’re very welcome! 🥰 Enjoy your treats!",
            "Thank you for choosing CINO Bakery ❤️",
            "We appreciate you — come back soon for more fresh bread!"
        ])

    else:
        reply = random.choice([
            "Hmm, I didn’t quite get that — but I can tell you about our bread, snacks, or prices 🍰",
            "Sorry, could you rephrase that? I can help with products, prices, or location.",
            "I might not know that yet, but our bread always knows how to make people smile 😄"
        ])

    return jsonify({"response": reply})


# -----------------------
# AUTO RUN (No if-statement)
# -----------------------
if __name__ == "__main__":
    app.run(debug=True)
