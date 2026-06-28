from flask import Flask, render_template, request

app = Flask(__name__)

# Route 1: Show the form (GET request)
@app.route('/')
def show_form():
    return render_template('form.html')

# Route 2: Handle form submission (POST request)
@app.route('/submit', methods=['POST'])
def handle_submit():
    # Read each field by its name="" attribute
    first_name = request.form['first_name']
    last_name  = request.form['last_name']
    email      = request.form['email']
    password   = request.form['password']
    role       = request.form['role']
    gender     = request.form.get('gender', 'Not specified')  # .get() is safe if field is optional
    bio        = request.form.get('bio', '')
    terms      = request.form.get('terms', 'off')  # 'on' if checked, missing if not

    # Package everything into a dict to pass to the template
    user_data = {
        'name'    : f"{first_name} {last_name}",
        'email'   : email,
        'role'    : role,
        'gender'  : gender,
        'bio'     : bio,
        'terms'   : 'Agreed' if terms == 'on' else 'Not agreed'
    }

    return render_template('success.html', user=user_data)

if __name__ == '__main__':
    app.run(debug=True)