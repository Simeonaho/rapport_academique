from app import app, db
from app.models import Utilisateur

with app.app_context():
    db.create_all()
    print("✅ Base de données créée avec succès.")
