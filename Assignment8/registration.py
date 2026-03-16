# IMPORTING
from flask import Flask, render_template, request

# INTERACTION
web = Flask(__name__)

# MAPPING
@web.route('/')
@web.route('/register')
# INPUT
def home():
    return render_template('register.html')

@web.route("/confirmation", methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        u = request.form.get('name')
        c = request.form.get('city')
        p = request.form.get('phone')
        return render_template('confirm.html', name=u, city=c, phone=p)

# MAIN
if __name__ == '__main__':
    web.run(debug=True)



