from faker import Faker
from flask import Flask
from models import db, owner, application

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@localhost:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisez db avec l'application Flask
db.init_app(app)

def populate():
    fake = Faker()
    with app.app_context():  # Créer un contexte d'application Flask
        for _ in range(100):  # Générer 100 enregistrements factices
            # Générer des données factices pour un propriétaire
            firstname = fake.first_name()
            lastname = fake.last_name()
            age = fake.random_int(min=18, max=50)
            email = fake.email()
            job = fake.job()

            # Créer un nouvel objet owner avec les données factices
            new_owner = owner(firstname=firstname, lastname=lastname, age=age, email=email, job=job)

            # Ajouter l'objet à la session SQLAlchemy
            db.session.add(new_owner)

            # Générer des données factices pour une application
            appname = fake.random_element(elements=("Facebook", "Instagram", "Snapchat", "TikTok", "X"))
            username = fake.user_name()
            lastconnection = fake.date_time_this_year()

            # Créer un nouvel objet application avec les données factices
            new_app = application(appname=appname, username=username, lastconnection=lastconnection, owner=new_owner)

            # Ajouter l'objet à la session SQLAlchemy
            db.session.add(new_app)

        # Valider les modifications et enregistrer les données dans la base de données
        db.session.commit()

if __name__ == '__main__':
    populate()
