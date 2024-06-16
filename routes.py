from flask import render_template, url_for, flask, redirect
from flask import RegistrationForm
from models import User, db


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email = form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('Account Created!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form)

