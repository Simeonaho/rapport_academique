import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'votre_cle_secrete'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configuration Flask-Mail
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'hounvosegbede@gmail.com'
MAIL_PASSWORD = 'couhrlmeyelovzzb'
MAIL_DEFAULT_SENDER = MAIL_USERNAME
