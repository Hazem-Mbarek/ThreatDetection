from flask import render_template, redirect, url_for, flash
from .forms import RegistrationForm
from . import app

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Handle successful form submission (e.g., save user to the database)
        username = form.username.data
        email = form.email.data
        password = form.password.data
        
        flash(f'Account created for {username}!', 'success')
        return redirect(url_for('home'))  # Redirect to the home page after registration
    return render_template('register.html', form=form)

