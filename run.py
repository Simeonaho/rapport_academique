from app import create_app
from flask_talisman import Talisman

app = create_app()

# ✅ Définition d'une CSP compatible avec Bootstrap et jQuery (modifiable au besoin)
csp = {
    'default-src': ["'self'"],
    'style-src': ["'self'", "'unsafe-inline'", 'https://cdn.jsdelivr.net', 'https://fonts.googleapis.com'],
    'script-src': ["'self'", "'unsafe-inline'", "'unsafe-eval'", 'https://cdn.jsdelivr.net', 'https://code.jquery.com'],
    'font-src': ["'self'", 'https://fonts.gstatic.com'],
    'img-src': ["'self'", 'data:'],
    'connect-src': ["'self'"],
    'form-action': ["'self'"],
    'frame-ancestors': ["'none'"]
}

# ➕ Application de Talisman avec cette politique CSP
Talisman(app, content_security_policy=csp)

if __name__ == '__main__':
    app.run(debug=True)
