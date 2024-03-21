from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.gig import Gig
from models.agent import Agent
from models.venue import Venue
from models.band import Band
from models.musician import Musician
from models.setlist import Setlist
from models.song import Song


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

    venue = [
        Venue(
            title="VALHALLA RESTAURANT BAR",
            manager="Trevor Odinson",
            address="3834 Nelson Bay Road,Bobs Farm, NSW 2316",
            phone="0454234556"
        ),
        Venue(
            title="Lovedale Wedding Chapel and Reception",
            manager="Cyril Lovedale",
            address="842 Lovedale Road, Allandale, NSW 2320",
            phone="0412457889"
        ),
        Venue(
            title="Fort Scratchley Function Centre",
            manager="Cletus Scratchley",
            address="1/3 Nobbys Road, Newcastle East, NSW 2300",
            phone="0415234556"
        )
    ]

    db.session.add_all(venue)

    agent = [
        Agent(
            title="Miller Gold Talent Agency",
            name="Ari Gold",
            email="ari.gold@mga.com",
            phone="0412345678"
        ),
        Agent(
            title="Michael Chugg Entertainment",
            name="Michael Chugg",
            email="chuggy@mce.com.au",
            phone="0487654321"
        )
    ]

    db.session.add_all(agent)

    musicians = [
        Musician(
            id="1",
            name="Miles Davis",
            email="miles@miles.com",
            phone="0454567889",
            instrument="Trumpet",

        ),
        Musician(
            id="2",
            name="Grant Green",
            email="info@grantgreen.net",
            phone="0455566899",
            instrument="Guitar",
        ),
        Musician(
            id="3",
            name="Jaco Pastorius",
            email="j@jaco.com",
            phone="0444587189",
            instrument="Bass",
        ),
                Musician(
            id="4",
            name="Buddy Rich",
            email="buddy@buddyrich.com",
            phone="0454164869",
            instrument="Drums"
        )
    ]
    db.session.add_all(musicians)

    songs = [
        Song(
            id="1",
            title="Chameleon",
            artist="Herbie Hancock",
            genre="Jazz",
            key="Bb",
            tempo="111",
        ),
        Song(
            id="2",
            title="Tennessee Whisky",
            artist="Chris Stapleton",
            genre="Country",
            key="A",
            tempo="98",
        ),
        Song(
            id="3",
            title="Valarie",
            artist="Mark Ronson",
            genre="Pop",
            key="Eb",
            tempo="106",
        ),
    ]
    db.session.add_all(songs)

    db.session.commit()

    print("Tables Seeded")




    # gigs = [
    #     Gig(
    #         date="01/04/2024",
    #         time="17:00",
    #         invoice="1001",
    #         venue="1",
    #         agent="1",
    #         band="1",
    #         setlist="1",
    #         user=users[0]
    #     ),
    #     Gig(
    #         date="10/05/2024",
    #         time="17:00",
    #         invoice="1002",
    #         venue="2",
    #         agent="1",
    #         band="2",
    #         setlist="2",
    #         user=users[0]
    #     ),
    # ]

    # db.session.add_all(gigs)


    # band = [
    #     Band(
    #         id="1",
    #         musician_id="1"
    #     ),
    #     Band(
    #         id="2",
    #         musician_id="2"
    #     ),
    #     Band(
    #         id="3",
    #         musician_id="3"
    #     )
    # ]
    # db.session.add_all(band)



    # setlists = [
    # Setlist(
    #     song_id="1",
    #     song_name="Chameleon",
    #     song_type="Cocktail Hour",
    #     ),
    # Setlist(    
    #     song_id="2",
    #     song_name="placeholder",
    #     song_type="First Dance",
    #     ),
    # Setlist(    
    #     song_id="3",
    #     song_name="placeholder",
    #     song_type="Party",
    #     ),        
    # ]
    
    # db.session.add_all(setlists)





