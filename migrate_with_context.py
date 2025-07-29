from app import create_app
import os

app = create_app()

with app.app_context():
    os.system('alembic revision --autogenerate -m "Ajout des champs filiere et annee"')
