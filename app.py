from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Password Validation Function
def check_password_strength(password):
    # Dictionary to hold validation results
    feedback = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digit': bool(re.search(r'\d', password)),
        'special_char': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }

    # Password Strength
    if all(feedback.values()):
        strength = 'Strong'
    elif any(feedback.values()):
        strength = 'Medium'
    else:
        strength = 'Weak'
    
    # Return feedback and strength
    return feedback, strength

@app.route('/', methods=['GET', 'POST'])
def index():
    feedback = None
    strength = None
    password = ''
    
    if request.method == 'POST':
        password = request.form['password']
        feedback, strength = check_password_strength(password)
    
    return render_template('index.html', feedback=feedback, strength=strength, password=password)

if __name__ == '__main__':
    app.run(debug=True)
