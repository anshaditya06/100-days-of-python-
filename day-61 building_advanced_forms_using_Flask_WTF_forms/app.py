import os
from flask import Flask, render_template, redirect, url_for, flash, request
from werkzeug.utils import secure_filename
from forms import RegistrationForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():   # True only on valid POST
        username = form.username.data
        email    = form.email.data
        role     = form.role.data

        # Handle file upload
        avatar_filename = None
        if form.avatar.data:
            file = form.avatar.data
            avatar_filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], avatar_filename)
            file.save(save_path)

        # TODO: Save to database here
        flash(f'Account created for {username}! 🎉', 'success')
        return redirect(url_for('register'))

    return render_template('register.html', form=form)

if __name__ == '__main__':
    os.makedirs('static/uploads', exist_ok=True)
    app.run(debug=True)