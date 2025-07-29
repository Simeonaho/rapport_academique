# 🏫 Plateforme de Gestion des Notes — FAST UNSTIM

Projet de développement d'une plateforme web de gestion des étudiants et de leurs résultats académiques à la Faculté des Sciences et Techniques (FAST - UNSTIM).

---

## 👥 Membres de l'équipe

| Nom                       | Rôle                        |
|--------------------------|-----------------------------|
| AHOSSA Mahouna Siméon    | Développeur Backend (Flask) |
| HOUNVO Sègbédé Modeste   | Développeur Frontend (HTML/CSS/JS) |

---

## 📌 Objectifs du projet

- Concevoir une **plateforme web** de gestion des notes.
- Permettre aux **administrateurs** de gérer les étudiants, leurs résultats et communiquer avec eux.
- Offrir aux **étudiants** la possibilité de consulter leurs résultats et de s’inscrire eux-mêmes.
- **Exporter** les résultats sous forme de **PDF** et **CSV/ZIP**.
- Sécuriser la plateforme de manière progressive.

---

## ⚙️ Technologies utilisées

- **Backend** : Python + Flask
- **Frontend** : HTML, CSS (custom), Jinja2
- **Base de données** : SQLite
- **Authentification** : Flask-Login
- **Formulaires sécurisés** : Flask-WTF (CSRF inclus)
- **Exportation PDF** : `reportlab`
- **Exportation CSV/ZIP** : `zipfile`, `csv`, `io`
- **Envoi d’email** : Flask-Mail

---

## ✅ Fonctionnalités déjà implémentées

### 🔐 Authentification
- Inscription des étudiants **à partir de leur matricule** (préalablement ajouté par l’administrateur).
- Connexion/déconnexion sécurisée (email + mot de passe).
- Rôle `admin` / `etudiant` bien différencié.
- Redirection dynamique en fonction du rôle après connexion.

### 🧑‍🎓 Gestion des étudiants (admin)
- Ajout d’un étudiant via une page dédiée (`/admin/ajouter_etudiant_page`).
- Suppression d’un étudiant (et de ses notes).
- Affichage de la liste des étudiants filtrés par filière/année.
- Attribution d’un **mot de passe temporaire** à l’étudiant.

### 📝 Gestion des notes (admin)
- Ajout de notes (UE/EQ, note, crédit) par matricule.
- Modification des notes avec formulaire dynamique.
- Suppression d’une note individuelle.
- Calcul automatique de la **moyenne** et des **crédits validés**.

### 🧾 Génération de résultats
- Téléchargement des résultats **au format PDF** pour l’étudiant connecté ou par admin.
- Exportation des résultats **en fichiers CSV zippés**, triés par niveau (MI1, MI2, MI3).

### 💬 Communication admin ↔ étudiant
- Formulaire de contact sur le site public.
- Visualisation des messages côté admin.
- Réponse par email depuis l’interface admin.
- Suppression d’un message.

### 🎨 Interface & UX
- Design responsive et clair.
- Boutons d’action avec icônes.
- Amélioration du style des pages ajoutées.

---

## 🛠️ À faire (fonctionnalités restantes)

| Tâche                                            | État       |
|--------------------------------------------------|------------|
| 🔐 Sécurisation finale (réactivation CSRF, CSP)  | 🟡 En cours |
| 📱 Adapter la plateforme en **application mobile** (Android) | 🚫 (optionnel) |
| 📋 Finalisation du design des autres pages       | 🔜 À peaufiner |
| 📦 Déploiement sur un serveur distant (prod)     | 🟠 À planifier |
| 🧪 Tests finaux (UX, sécurité, bugs)             | 🔄 En cours |

---

## 🧪 Procédure d’utilisation en local

```bash
# 1. Cloner le dépôt
git clone https://github.com/Simeonaho/rapport_academique.git
cd rapport_academique

# 2. Créer et activer un environnement virtuel
python -m venv venv
.env\Scriptsctivate    # sous Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer l'application Flask
python run.py

# Mettre à jour le fichier plus tard
pip freeze > requirements.txt

```

---

## 📁 Arborescence du projet (simplifiée)

```
/app
├── static/
├── templates/
│   ├── base.html
│   ├── *.html (vues)
├── models.py
├── forms.py
└── routes.py
run.py
README.md
```

---

## 📝 Notes importantes

- L'interface est conçue pour être **simple, intuitive et responsive**.
- La sécurité est partiellement en place (à renforcer).
- Le code est bien **organisé par rôle et fonction**.

---

## 🏁 Conclusion

Ce projet met en œuvre une **véritable plateforme web fonctionnelle**, avec une **collaboration claire** entre les développeurs backend et frontend. Il constitue une base solide pour une solution complète de gestion académique à la FAST – UNSTIM.
