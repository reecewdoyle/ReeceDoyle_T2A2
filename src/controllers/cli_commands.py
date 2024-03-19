from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.gig import Gig
from models.agent import Agent


db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables Dropped")

@db_commands.cli.command("seed")
def seed_tables():
    users = [
        User(
            email="admin@weddingband.com",
            password=bcrypt.generate_password_hash('123456').decode('utf-8'),
            is_admin=True
        ),
        User(
            name="User 1",
            email="user1@weddingband.com",
            password=bcrypt.generate_password_hash('123456').decode('utf-8')
        )
    ]

    db.session.add_all(users)

    gigs = [
        Gig(
            id="1",
            date="01/04/2024",
            time="17:00",
            invoice="1001",
            venue="1",
            agent="1",
            band="1",
            setlist="1",
            user=users[0]
        ),
        Gig(
            id="2",
            date="10/05/2024",
            time="17:00",
            invoice="1002",
            venue="2",
            agent="1",
            band="2",
            setlist="2",
            user=users[0]
        ),
    ]

    db.session.add_all(gigs)

    agent = [
        Agent(
            id="1",
            title="Miller Gold Talent Agency",
            name="Ari Gold",
            email="ari.gold@mga.com",
            phone="0412345678"
        ),
        Agent(
            id="2",
            title="Michael Chugg Entertainment",
            name="Michael Chugg",
            email="chuggy@mce.com.au",
            phone="0487654321"
        )
    ]

    db.session.add_all(agent)
    
    db.session.commit()

    print("Tables Seeded")