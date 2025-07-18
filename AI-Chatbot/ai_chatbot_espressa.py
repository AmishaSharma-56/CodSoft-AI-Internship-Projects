import re

def display_welcome():
    print("="*60)
    print("🤖 Welcome, I am Espressa - Your Assistant for La Dolce Vita Restaurant, Chandigarh")
    print("Type your query or ask about our specials, timings, reservations, location, offers, and more!")
    print("Type 'bye' anytime to end the chat.")
    print("="*60)

def get_response(user_input):
    user_input = user_input.lower()

    # Farewell
    if re.search(r'\b(thanks|thank you|bye|goodbye|exit|see you|ok bye|okay bye)\b', user_input):
        return "👋 Thank you for chatting with La Dolce Vita Restaurant. We hope to serve you soon in Chandigarh. For any other queries, call us at ☎️ 1800-274-2213 or email 📧 support@ldvrestaurant.com\n"

    # Greetings
    elif re.search(r'\b(hello|hi|hey|namaste|greetings)\b', user_input):
        return "👋 Hello! Welcome to La Dolce Vita Restaurant. I can help you with specials, reservations, timings, deals, and more. What would you like to know?\n"

    # Opening Hours
    elif re.search(r'(opening|closing|timing|hours|open|close)', user_input):
        return "🕒 We're open every day from 11:00 AM to 11:00 PM. Have questions? Call us at ☎️ 1800-274-2213.\n"

    # Reservation
    elif re.search(r'(book|reservation|reserve|table)', user_input):
        return (
            "📅 To make a reservation at La Dolce Vita, Chandigarh, please give us a call 📞 at 1800-274-2213.\n"
            "Our team will be delighted 😊 to assist you with your booking!\n"
        )
    
    # Special Offers
    elif re.search(r'(offer|deal|discount|specials)', user_input):
        return (
            "🎉 Ongoing Offers:\n"
            "✅ 10% off on dine-in orders above ₹1000 (Mon-Thu)\n"
            "✅ Weekend Family Combo for ₹799\n"
            "🛍️ Online orders get exclusive discounts via our app!\n"
            "📞 For more details, call us at 1800-274-2213\n"
        )

    # Menu / Special Items
    elif re.search(r'(menu|items|dishes|available|serve|special)', user_input):
        return (
            "🍝 Our Italian Specials:\n"
            "🍕 Margherita Pizza - ₹399\n"
            "🍝 Spaghetti Carbonara - ₹429\n"
            "🍤 Seafood Risotto - ₹549\n"
            "🍕 Quattro Formaggi (Four Cheese) Pizza - ₹499\n"
            "🍰 Tiramisu (Classic Italian Dessert) - ₹199\n"
            "☕ Espresso / Cappuccino - ₹149\n\n"
            "📞 For the full authentic Italian menu, please call us at 1800-274-2213 or email 📧 support@ldvrestaurant.com\n"
        )

    # Order
    elif re.search(r'(order|takeaway|delivery|pickup|home delivery)', user_input):
        return (
            "🛵 We offer takeaway and home delivery in Chandigarh.\n"
            "Place your order now:\n"
            "📱 Phone: 1800-274-2213\n"
            "🌐 Or visit our website: www.ldvrestaurant.com\n"
        )

    # Location
    elif re.search(r'(location|address|where|situated|find you)', user_input):
        return (
            "📍 Our Address:\n"
            "La Dolce Vita Restaurant, Sector 26, Madhya Marg, Chandigarh\n"
            "📱 For directions or assistance, call: 1800-274-2213\n"
            "🌐 Find us on Google Maps: https://goo.gl/maps/ldvrestaurant\n"
        )


    # Contact Info
    elif re.search(r'(contact|phone|email|call|number)', user_input):
        return (
            "📞 Contact Details:\n"
            "Phone: 1800-274-2213\n"
            "Email: support@ldvrestaurant.com\n"
            "Website: www.ldvrestaurant.com\n"
        )

    # Feedback
    elif re.search(r'(feedback|complain|suggestion|review)', user_input):
        return (
            "📝 We value your feedback!\n"
            "Please email us at 📧 feedback@ldvrestaurant.com or call ☎️ 1800-274-2213.\n"
            "You can also leave a review on Google/Instagram – we'd love that. ❤️\n"
        )

    # Help / Default
    else:
        return (
            "🤔 I didn't get that. I can help you with:\n"
            "• Special Dishes\n• Reserving a Table\n• Takeaway/Delivery\n"
            "• Operating Hours\n• Location\n• Offers & Contact Info\n\n"
            "Need help right away? ☎️ Call us at 1800-274-2213.\n"
        )

def chatbot():
    display_welcome()
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Espressa: {response}")
        if "bye" in user_input.lower():
            break

if __name__ == '__main__':
    chatbot()
