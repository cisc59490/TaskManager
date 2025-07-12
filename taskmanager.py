# auth.py (New File)
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

users = {
    1: {'id': 1, 'username': 'admin', 'password': generate_password_hash('secret')}
}

# app.py additions
from flask_login import LoginManager, login_user, logout_user, login_required

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        user = next((u for u in users.values() if u['username'] == username), None)
        if user and check_password_hash(user['password'], request.form['password']):
            login_user(User(user['id']))
            return redirect(url_for('home'))
    return render_template('login.html')
