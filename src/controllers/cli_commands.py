from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.gig import Gig
from models.agent import Agent
from models.venue import Venue
from models.musician import Musician
from models.first_dance import FirstDanceSong
from models.aisle import AisleSong

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
            name="Admin",
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
            phone="0454234556",
            user=users[0]
        ),
        Venue(
            title="Lovedale Wedding Chapel and Reception",
            manager="Cyril Lovedale",
            address="842 Lovedale Road, Allandale, NSW 2320",
            phone="0412457889",
            user=users[0]
        ),
        Venue(
            title="Fort Scratchley Function Centre",
            manager="Cletus Scratchley",
            address="1/3 Nobbys Road, Newcastle East, NSW 2300",
            phone="0415234556",
            user=users[0]
        )
    ]

    db.session.add_all(venue)

    agent = [
        Agent(
            title="Miller Gold Talent Agency",
            name="Ari Gold",
            email="ari.gold@mga.com",
            phone="0412345678",
            user=users[0]
        ),
        Agent(
            title="Michael Chugg Entertainment",
            name="Michael Chugg",
            email="chuggy@mce.com.au",
            phone="0487654321",
            user=users[0]
        )
    ]

    db.session.add_all(agent)

    musician = [
        Musician(
            name="Grant Green",
            email="info@grantgreen.net",
            phone="0455566899",
            instrument="Guitar",
            user=users[0]
        ),
        Musician(
            name="Wes Montgomery",
            email="info@wes.net",
            phone="0455566888",
            instrument="Guitar",
            user=users[0]
        ),
        Musician(
            name="Guthrie Goven",
            email="guthrie@guthriegoeven.com",
            phone="0455566887",
            instrument="Guitar",
            user=users[0]
        ),
        Musician(
            name="Jaco Pastorius",
            email="j@jaco.com",
            phone="0444587189",
            instrument="Bass",
            user=users[0]
        ),
        Musician(
            name="Victor Wooten",
            email="victor@wooten.com",
            phone="0454567890",
            instrument="Bass",
            user=users[0]
        ),
        Musician(
            name="Flea",
            email="flea@redhotchilipeppers.com",
            phone="0433221100",
            instrument="Bass",
            user=users[0]
        ),
        Musician(
            name="Buddy Rich",
            email="buddy@buddyrich.com",
            phone="0454164869",
            instrument="Drums",
            user=users[0]
        ),
        Musician(
            name="Dave Grohl",
            email="dave@grohl.com",
            phone="0433123456",
            instrument="Drums",
            user=users[0]
        ),
        Musician(
            name="Travis Barker",
            email="travis@barker.com",
            phone="0499888777",
            instrument="Drums",
            user=users[0]
        ),
        Musician(
            name="Miles Davis",
            email="miles@miles.com",
            phone="0454567889",
            instrument="Trumpet",
            user=users[0]
        ),
        Musician(
            name="Kenny G",
            email="kennyg@sax.com",
            phone="0422333444",
            instrument="Saxophone",
            user=users[0]
        ),
        Musician(
            name="Stevie Wonder",
            email="stevie@wonder.com",
            phone="0400111000",
            instrument="Keyboard",
            user=users[0]
        ),
        Musician(
            name="Herbie Hancock",
            email="herbie@hancock.com",
            phone="0488777666",
            instrument="Keyboard",
            user=users[0]
        ),
        Musician(
            name="Frank Sinatra",
            email="frank@sinatra.com",
            phone="0454123456",
            instrument="Vocals",
            user=users[0]
        ),
        Musician(
            name="John Legend",
            email="john@legend.com",
            phone="0400111222",
            instrument="Vocals",
            user=users[0]
        ),
        Musician(
            name="Adele",
            email="adele@adele.com",
            phone="0456000000",
            instrument="Vocals",
            user=users[0]
        ),
        Musician(
            name="Beyoncé",
            email="beyonce@beyonce.com",
            phone="0411333777",
            instrument="Vocals",
            user=users[0]
        )
    ]

    db.session.add_all(musician)

    first_dance_songs = [
        FirstDanceSong(
            title="At Last", 
            artist="Etta James", 
            genre="Soul", 
            key="F major", 
            tempo=65,
            user=users[0]
        ),
        FirstDanceSong(
            title="Thinking Out Loud", 
            artist="Ed Sheeran", 
            genre="Pop", 
            key="D major", 
            tempo=79,
            user=users[0]
        ),
        FirstDanceSong(
            title="Can't Help Falling in Love", 
            artist="Elvis Presley", 
            genre="Rock", 
            key="C major", 
            tempo=68,
            user=users[0]
        ),
        FirstDanceSong(
            title="Unchained Melody", 
            artist="The Righteous Brothers", 
            genre="Pop", 
            key="E♭ major", 
            tempo=87,
            user=users[0]
        ),
        FirstDanceSong(
            title="All of Me", 
            artist="John Legend", 
            genre="R&B", 
            key="A♭ major", 
            tempo=63,
            user=users[0]
        )
    ]
    
    db.session.add_all(first_dance_songs)

    aisle_songs = [
        AisleSong(
            title="Pachelbel's Canon",
            artist="Johann Pachelbel",
            genre="Classical",
            key="D",
            tempo="62",
            user=users[0]
        ),
        AisleSong(
            title="A Thousand Years",
            artist="Christina Perri",
            genre="Pop",
            key="Bb",
            tempo="95",
            user=users[0]
        ),
        AisleSong(
            title="Marry Me",
            artist="Train",
            genre="Pop",
            key="F",
            tempo="145",
            user=users[0]
        ),
        AisleSong(
            title="Can't Help Falling in Love",
            artist="Elvis Presley",
            genre="Pop",
            key="C",
            tempo="88",
            user=users[0]
        ),
        AisleSong(
            title="All of Me",
            artist="John Legend",
            genre="Pop",
            key="Ab",
            tempo="63",
            user=users[0]
        )
    ]

    db.session.add_all(aisle_songs)

    gigs = [
        Gig(
            date="01/04/2024",
            time="17:00",
            invoice="1001",
            venue_id="1",
            agent_id="1",
            user=users[0],
            musician_id="1",
            first_dance_song_id="1",
            aisle_song_id="1",
        ),
        Gig(
            date="10/10/2024",
            time="17:30",
            invoice="1002",
            venue_id="2",
            agent_id="2",
            user=users[0],
            musician_id="3",
            first_dance_song_id="5",
            aisle_song_id="2",
        ),

    ]


    db.session.add_all(gigs)

    db.session.commit()

    print("Tables Seeded")