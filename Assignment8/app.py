from flask import Flask, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash

# Import the other py files required
from model import User, db
from forms import LoginForm, UserDetails

# App Creation:
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning

# Bind SQLAlchemy to app
db.init_app(app)

# CSRF Secret Key
app.config['SECRET_KEY'] = 'mysecretkey123'

# Routing for Home or Login page:
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = LoginForm()

    # Check of POST/SUBMIT is done on login Page:
    if form_login.validate_on_submit():
        user = User.query.filter_by(userid=form_login.userid.data).first()
        if not user:
            return "User not found"
        elif user and check_password_hash(user.password, form_login.password.data):
            return redirect(url_for('user_detail', userid = form_login.userid.data))
        else:
            return 'Invalid Userid or Password'

    return render_template('login.html', form=form_login)


# Routing for register page:
@app.route('/register', methods=['GET', 'POST'])
def register():
    form_register = UserDetails()

    # Import data from form and export it to db.
    if form_register.validate_on_submit():
        hashed_password = generate_password_hash(form_register.password.data)  # convert to hash password
        user = User(userid=form_register.userid.data,
        username = form_register.username.data,
        email = form_register.email.data,
        phone = form_register.phone.data,
        city = form_register.city.data,
        password = hashed_password)  # store the hash password
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('success', userid = form_register.userid.data))

    return render_template('register.html', form = form_register)

# Routing for success page:
@app.route('/success')
def success():
    userid = request.args.get('userid') # fetch userid  from URL
    user = User.query.filter_by(userid=userid).first()  # fetch from DB
    return render_template('success.html', user=user)

# Routing for user_detail:
@app.route('/user_detail', methods=['GET', 'POST'])
def user_detail():
    userid = request.args.get('userid') # fetch userid  from URL
    user = User.query.filter_by(userid=userid).first()  # fetch from DB
    return render_template('user_detail.html', user=user)

# Route to delete the user
@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return "User not found"

    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('login'))  # or login page

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)