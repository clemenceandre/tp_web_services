from flask import Flask, send_from_directory
import os
from models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@localhost:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisez db avec l'application Flask
db.init_app(app)

# Importez vos modèles après avoir initialisé db
from models import owner, application

def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Utilisez un gestionnaire de contexte pour s'assurer que les opérations sont effectuées dans le contexte de l'application Flask
with app.app_context():
    # Ligne de code pour supprimer toutes les tables dans la base de données
    db.drop_all()

    # Ligne de code pour créer les tables dans la base de données
    db.create_all()

# Le reste de votre application Flask...

if __name__ == '__main__':
    app.run()
