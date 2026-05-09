from flask import Blueprint, render_template, request, redirect, session
from models.user import User

auth_bp = Blueprint('auth', __name__)

# LOGIN
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(
            email=email,
            password=password
        ).first()

        if user:
            session['user'] = user.email
            return redirect('/')

        return "Invalid email or password"

    return render_template('login.html')


# LOGOUT
@auth_bp.route('/logout')
def logout():

    session.pop('user', None)

    return redirect('/login')