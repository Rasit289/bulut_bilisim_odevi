from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'gizli_anahtar'

# Kullanıcı veritabanınızı temsil etmek için basit bir sözlük
user_database = {
    'kullanici1': 'sifre123',
    'kullanici2': 'parola456',
}

class LoginForm(FlaskForm):
    username = StringField('Kullanıcı Adı', [validators.DataRequired()])
    password = PasswordField('Parola', [validators.DataRequired()])
    submit = SubmitField('Giriş Yap')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if username in user_database and user_database[username] == password:
            return f"Merhaba, {username}! Başarıyla giriş yaptınız."
        else:
            return "Hatalı kullanıcı adı veya parola. Tekrar deneyin."

    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run()
