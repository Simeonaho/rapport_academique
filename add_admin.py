from app import create_app, db
from app.models import Utilisateur

# Créer une application Flask (c'est nécessaire pour utiliser db)
app = create_app()

# Fonction pour ajouter un administrateur
def ajouter_admin():
    with app.app_context():  # Assure-toi que tu travailles dans le bon contexte de l'application
        # Vérifier si l'administrateur existe déjà
        admin = Utilisateur.query.filter_by(email='admin@example.com').first()

        if not admin:
            # Ajouter l'administrateur avec email et mot de passe prédéfinis
            admin = Utilisateur(
                nom='Admin',
                matricule='admin123',
                email='admin@example.com',
                role='admin'
            )
            admin.set_password('adminpassword')  # Remplace par un mot de passe sécurisé
            db.session.add(admin)
            db.session.commit()
            print("Administrateur ajouté.")
        else:
            print("L'administrateur existe déjà.")

# Appeler la fonction pour ajouter l'administrateur
ajouter_admin()