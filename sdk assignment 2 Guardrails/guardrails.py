"""
Assignment 2 Math Agent with Guardrails
No API key required. Only answers math questions and blocks politics.
"""

# Simple function to detect politics
def is_political(text):
    political_keywords = ["president", "election", "government"]
    for word in political_keywords:
        if word in text.lower():
            return True
    return False

# Function to calculate basic math
def calculate_math(expr):
    try:
        # Only allow digits and math operators
        allowed_chars = "0123456789+-*/.() "
        if any(c not in allowed_chars for c in expr):
            return "Invalid characters in expression."
        return eval(expr)
    except:
        return "Invalid math expression."

# Main loop
if __name__ == "__main__":
    print("Math agent running (type quit to exit)")
    while True:
        msg = input("You: ")
        if msg.lower() == "quit":
            break

        if is_political(msg):
            print("Bot: Sorry, I cannot answer political questions.")
            continue

        result = calculate_math(msg)
        print("Bot:", result)
