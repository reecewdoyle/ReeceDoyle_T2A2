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
            name="Miles Davis",
            email="miles@miles.com",
            phone="0454567889",
            instrument="Trumpet"
        ),
        Musician(
            name="Grant Green",
            email="info@grantgreen.net",
            phone="0455566899",
            instrument="Guitar"
        ),
        Musician(
            name="Jaco Pastorius",
            email="j@jaco.com",
            phone="0444587189",
            instrument="Bass"
        ),
        Musician(
            name="Buddy Rich",
            email="buddy@buddyrich.com",
            phone="0454164869",
            instrument="Drums"
        ),
        Musician(
            name="Kenny G",
            email="kennyg@sax.com",
            phone="0422333444",
            instrument="Saxophone"
        ),
        Musician(
            name="Victor Wooten",
            email="victor@wooten.com",
            phone="0454567890",
            instrument="Bass"
        ),
        Musician(
            name="Flea",
            email="flea@redhotchilipeppers.com",
            phone="0433221100",
            instrument="Bass"
        ),
        Musician(
            name="John Mayer",
            email="john@mayer.com",
            phone="0412123456",
            instrument="Guitar"
        ),
        Musician(
            name="Eric Clapton",
            email="eric@clapton.com",
            phone="0478654321",
            instrument="Guitar"
        ),
        Musician(
            name="Stevie Wonder",
            email="stevie@wonder.com",
            phone="0400111000",
            instrument="Keyboard"
        ),
        Musician(
            name="Herbie Hancock",
            email="herbie@hancock.com",
            phone="0488777666",
            instrument="Keyboard"
        ),
        Musician(
            name="Dave Grohl",
            email="dave@grohl.com",
            phone="0433123456",
            instrument="Drums"
        ),
        Musician(
            name="Travis Barker",
            email="travis@barker.com",
            phone="0499888777",
            instrument="Drums"
        ),
           Musician(
        name="Frank Sinatra",
        email="frank@sinatra.com",
        phone="0454123456",
        instrument="Vocals"
        ),
        Musician(
            name="Elvis Presley",
            email="elvis@presley.com",
            phone="0412789456",
            instrument="Vocals"
        ),
        Musician(
            name="Michael Jackson",
            email="michael@jackson.com",
            phone="0432456789",
            instrument="Vocals"
        ),
        Musician(
            name="Freddie Mercury",
            email="freddie@mercury.com",
            phone="0478563412",
            instrument="Vocals"
        ),
        Musician(
            name="John Legend",
            email="john@legend.com",
            phone="0400111222",
            instrument="Vocals"
        ),
        Musician(
            name="Adele",
            email="adele@adele.com",
            phone="0456000000",
            instrument="Vocals"
        ),
        Musician(
            name="Beyoncé",
            email="beyonce@beyonce.com",
            phone="0411333777",
            instrument="Vocals"
        ),
        Musician(
            name="Ariana Grande",
            email="ariana@grande.com",
            phone="0488889999",
            instrument="Vocals"
        ),
        Musician(
            name="Taylor Swift",
            email="taylor@swift.com",
            phone="0466667777",
            instrument="Vocals"
        ),
        Musician(
            name="Whitney Houston",
            email="whitney@houston.com",
            phone="0412345678",
            instrument="Vocals"
        )
    ]

    db.session.add_all(musicians)

    songs = [
 Song(
        title="Chameleon",
        artist="Herbie Hancock",
        genre="Jazz",
        key="Bb",
        tempo="111"
    ),
    Song(
        title="Tennessee Whisky",
        artist="Chris Stapleton",
        genre="Country",
        key="A",
        tempo="98"
    ),
    Song(
        title="Valarie",
        artist="Mark Ronson ft. Amy Winehouse",
        genre="Pop",
        key="Eb",
        tempo="106"
    ),
    Song(
        title="Take Five",
        artist="Dave Brubeck",
        genre="Jazz",
        key="C",
        tempo="174"
    ),
    Song(
        title="Jolene",
        artist="Dolly Parton",
        genre="Country",
        key="G",
        tempo="108"
    ),
    Song(
        title="Uptown Funk",
        artist="Mark Ronson ft. Bruno Mars",
        genre="Pop",
        key="Dm",
        tempo="115"
    ),
    Song(
        title="Summertime",
        artist="Ella Fitzgerald",
        genre="Jazz",
        key="Am",
        tempo="83"
    ),
    Song(
        title="Wagon Wheel",
        artist="Old Crow Medicine Show",
        genre="Country",
        key="A",
        tempo="140"
    ),
    Song(
        title="Shallow",
        artist="Lady Gaga, Bradley Cooper",
        genre="Pop",
        key="G",
        tempo="96"
    ),
    Song(
        title="Feeling Good",
        artist="Nina Simone",
        genre="Jazz",
        key="Cm",
        tempo="128"
    ),
    Song(
        title="Friends in Low Places",
        artist="Garth Brooks",
        genre="Country",
        key="A",
        tempo="132"
    ),
    Song(
        title="Shape of My Heart",
        artist="Sting",
        genre="Pop",
        key="F#m",
        tempo="96"
    ),
    Song(
        title="Fly Me to the Moon",
        artist="Frank Sinatra",
        genre="Jazz",
        key="C",
        tempo="126"
    ),
    Song(
        title="Ring of Fire",
        artist="Johnny Cash",
        genre="Country",
        key="G",
        tempo="106"
    ),
    Song(
        title="Someone Like You",
        artist="Adele",
        genre="Pop",
        key="A",
        tempo="67"
    ),
    Song(
        title="So What",
        artist="Miles Davis",
        genre="Jazz",
        key="D",
        tempo="104"
    ),
    Song(
        title="The Gambler",
        artist="Kenny Rogers",
        genre="Country",
        key="G",
        tempo="118"
    ),
    Song(
        title="Don't Stop Believin'",
        artist="Journey",
        genre="Pop",
        key="E",
        tempo="118"
    ),
    Song(
        title="Autumn Leaves",
        artist="Nat King Cole",
        genre="Jazz",
        key="Gm",
        tempo="88"
    ),
    Song(
        title="Wanted Dead or Alive",
        artist="Bon Jovi",
        genre="Country",
        key="D",
        tempo="125"
    ),
    Song(
        title="Billie Jean",
        artist="Michael Jackson",
        genre="Pop",
        key="F#m",
        tempo="117"
    ),
    Song(
        title="My Favorite Things",
        artist="John Coltrane",
        genre="Jazz",
        key="Em",
        tempo="100"
    ),
    Song(
        title="I Walk the Line",
        artist="Johnny Cash",
        genre="Country",
        key="G",
        tempo="105"
    ),
    Song(
        title="Smooth Operator",
        artist="Sade",
        genre="Pop",
        key="Dm",
        tempo="89"
    ),
    Song(
        title="Take the 'A' Train",
        artist="Duke Ellington",
        genre="Jazz",
        key="C",
        tempo="190"
    ),
    Song(
        title="Cruise",
        artist="Florida Georgia Line",
        genre="Country",
        key="G",
        tempo="68"
    ),
    Song(
        title="Can't Help Falling in Love",
        artist="Elvis Presley",
        genre="Pop",
        key="C",
        tempo="108"
    ),
    Song(
        title="All Blues",
        artist="Miles Davis",
        genre="Jazz",
        key="G",
        tempo="75"
    )
    ]
    db.session.add_all(songs)

    setlists = [
    Setlist(
        song_id="1",
        song_type="Cocktail Hour",
        ),
    Setlist(    
        song_id="2",
        song_type="First Dance",
        ),
    Setlist(    
        song_id="3",
        song_type="Party",
        ),        
    ]
    
    db.session.add_all(setlists)


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











