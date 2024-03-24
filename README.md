# Reece Doyle T2A2 -  Wedding Band API
## R1 - Identification of the problem you are trying to solve by building this particular app.
Weddings have always been a significant milestone in most cultures around the world. They're a time to celebrate the love of the couple that has made the commitment to each other in the precesence of their families and loved ones, **and what is a celebration without music?**

Whether it be during the ceremeony, during the cocktail hour, the first dance, or the party that ensues once the rituals are out of the way, every part of a wedding is filled with music. Thus, the orgainsation of the wedding musicians can truely make or break the day.

One of the problems a band leader will encounter is that (with very few exceptions, and at nearly every level of the industry) musicians are freelancers. Permanent, salaried positions are nonexistent. Even if you play in Taylor Swift or Paul McCartney band, at best you could be looking at a contract that lasts as long as a single tour. 

Musicians are several tiny, sole-trader entities that work together. Therefore, there is almost never a centralised organisation or staff to deligate tasks or handle the admin side of a wedding booking. This can create a myriad of issues with double-bookings, missed bookings, and particularly in the wedding industry, the wrong music being played for the event.
***

## R2 - Why is it a problem that needs solving?
The Wedding Industry is a highly competative environment where anything short of perfrection is not tolerated. 

**One bad experience from a client accompanied with a bad review on Google can absolutely sink a wedding vendor, leaving them with the expensive choice to either start from scratch with a rebrand, or get a day job!**

The saying amongst musicians is that **"You're only as good as your last gig"**, and that could not be more true than at a wedding. 

**The key to building a lucrative career as a Wedding/Functions musician is prepartion and organisation.**

The Wedding Band API is designed to give a Band Leader fast asscess to all the information they need to compile in the organisation and execution of a Wedding Booking. It allows the user to store a database of musicians and their instruments, contact details for booking agents, venue details, a place to build a setlist, and an archieve of songs. 

This saves the musician from digging through a crowded email inbox and looking through badly routed foulders on a computer. 

**All the crucial data that you need to plan and execute a wedding gig in one spot!**
***

## R3 - Why have you chosen this database system. What are the drawbacks compared to others?
Why PSQL?
Research alternatives

## R4 - Identify and discuss the key functionalities and benefits of an ORM

Research ORM

## R5 - Document all endpoints for your API

I've included an endpoints.json file to make importing my endpoints into insomnia quick and easy.

***
## Users

### `POST /auth/register`
 - Registers a new user with the wedding API. 

- Request Body: 
```json
{
	"name": "User10",
	"email": "user10@weddingband.com",
	"password": "123456"
}
```
- Response: 
```json
{
	"email": "user10@weddingband.com",
	"is_admin": false,
	"name": "User10",
	"id": 5,
}
```
***
### `POST /auth/login`
 - Logs a valid user in and returns a JWT token. 

- Request Body: 
```json
{
    "email": "user10@weddingband.com",
	"password": "123456"
}
```
- Response: 
```json
{
    "email": "user10@weddingband.com",
	"token": "eyJhbGciOiJIUzI (JWT shortened for brevity)",
	"is_admin": false
}
```
## Booking Agents
### `GET /agent`
 - Gets the list of booking agents currently stored in psql. 

- Response: 
```json
	{
		"id": 1,
		"title": "Miller Gold Talent Agency",
		"name": "Ari Gold",
		"email": "ari.gold@mga.com",
		"phone": "0412345678",
		"user": {
			"email": "admin@weddingband.com",
			"name": "Admin"
		}
	},
	{
		"id": 2,
		"title": "Michael Chugg Entertainment",
		"name": "Michael Chugg",
		"email": "chuggy@mce.com.au",
		"phone": "0487654321",
		"user": {
			"email": "admin@weddingband.com",
			"name": "Admin"
		}
	}
```
***
### `POST /agent`
 - Posts a new booking agent to psql. 
- JWT required
- Request: 
```json
{
	"title": "Polymer Entertainment",
	"name": "Artie Fufkin",
	"email": "arthurf@polymer.com",
	"phone": "0412457888"
}
```
- Response: 
```json
{
	"id": 3,
	"title": "Polymer Entertainment",
	"name": "Artie Fufkin",
	"email": "arthurf@polymer.com",
	"phone": "0412457888",
	"user": {
		"name": "Admin",
		"email": "admin@weddingband.com"
	}
}
```
***
### `PATCH /agent/<int:agent_id>`
 - Updates an existing booking agent in psql. 
- JWT required
- Request: 
```json
{
	"name": "Arthur James Fufkin"
}
```
- Response: 
```json
{
	"id": 3,
	"title": "Polymer Entertainment",
	"name": "Arthur James Fufkin",
	"email": "arthurf@polymer.com",
	"phone": "0412457888",
	"user": {
		"name": "Admin",
		"email": "admin@weddingband.com"
	}
}
```
***
### `DELETE /agent/<int:agent_id>`
 - Deletes an existing booking agent from psql. 
- JWT required
- Response: 
```json
{
	"message": "Agent Arthur James Fufkin deleted successfully"
}
```
***
## Aisle Songs
### `GET /aisle`
 - Gets the list of aisle songs currently stored in psql. 

- Response (shortened for brevity): 
```json
	{
		"id": 1,
		"title": "Pachelbel's Canon",
		"artist": "Johann Pachelbel",
		"genre": "Classical",
		"key": "D",
		"tempo": 62,
		"user": {
			"email": "admin@weddingband.com",
			"name": "Admin"
		}
	},
	{
		"id": 2,
		"title": "A Thousand Years",
		"artist": "Christina Perri",
		"genre": "Pop",
		"key": "Bb",
		"tempo": 95,
		"user": {
			"email": "admin@weddingband.com",
			"name": "Admin"
		}
	},
```
***
### `POST /aisle`
 - Posts a new aisle song to psql. 
- JWT required
- Request: 
```json
{
  "title": "Hallelujah",
  "artist": "Leonard Cohen",
  "genre": "Folk",
  "key": "C",
  "tempo": 65
}
```
- Response: 
```json
{
	"id": 6,
	"title": "Hallelujah",
	"artist": "Leonard Cohen",
	"genre": "Folk",
	"key": "C",
	"tempo": 65,
	"user": {
		"name": "Admin",
		"email": "admin@weddingband.com"
	}
}
```
***
### `PATCH /aisle/<int:aisle_song_id>`
 - Updates an existing aisle song in psql. 
- JWT required
- Request: 
```json
{
	"key": "D"
}
```
- Response: 
```json
{
	"id": 6,
	"title": "Hallelujah",
	"artist": "Leonard Cohen",
	"genre": "Folk",
	"key": "D",
	"tempo": 65,
	"user": {
		"name": "Admin",
		"email": "admin@weddingband.com"
	}
}
```
***
### `DELETE /aisle/<int:aisle_song_id>`
 - Deletes an existing aisle song from psql. 
- JWT required
- Response: 
```json
{
	"message": "Aisle Song with Hallelujah deleted successfully"
}
```
***
## First Dance Songs
### `GET /firstdance`
 - Gets the list of first dance songs currently stored in psql. 

- Response (shortened for brevity): 
```json
	{
		"id": 1,
		"title": "At Last",
		"artist": "Etta James",
		"genre": "Soul",
		"key": "F",
		"tempo": 65,
		"user": {
			"name": "Admin",
			"email": "admin@weddingband.com"
		}
	},
	{
		"id": 2,
		"title": "Thinking Out Loud",
		"artist": "Ed Sheeran",
		"genre": "Pop",
		"key": "D",
		"tempo": 79,
		"user": {
			"name": "Admin",
			"email": "admin@weddingband.com"
		}
	},
```
***
### `POST /firstdance`
 - Posts a new first dance song to psql. 
- JWT required
- Request: 
```json
{
  "title": "Perfect",
  "artist": "Ed Sheeran",
  "genre": "Pop",
  "key": "A",
  "tempo": 95
}
```
- Response: 
```json
{
	"id": 6,
	"title": "Perfect",
	"artist": "Ed Sheeran",
	"genre": "Pop",
	"key": "A",
	"tempo": 95,
	"user": {
		"name": "Admin",
		"email": "admin@weddingband.com"
	}
}
```
***
### `PATCH /firstdance/<int:first_dance_song_id>`
 - Updates an existing first dance song in psql. 
- JWT required
- Request: 
```json
{
	"key": "B"
}
```
- Response: 
```json
{
	"id": 6,
	"title": "Perfect",
	"artist": "Ed Sheeran",
	"genre": "Pop",
	"key": "B",
	"tempo": 95,
	"user": {
		"name": "Admin",
		"email": "admin@weddingband.com"
	}
}
```
***
### `DELETE /firstdance/<int:first_dance_song_id>`
 - Deletes an existing first dance song from psql. 
- JWT required
- Response: 
```json
{
	"message": "First Dance Song with Perfect deleted successfully"
}
```
****************************************************************
## Gigs
### `GET /gigs`
 - Gets the list of gigs currently stored in psql. 

- Response (shortened for brevity): 
```json
	{
		"id": 1,
		"date": "2024-01-04",
		"time": "17:00:00",
		"invoice": "1001",
		"venue": {
			"title": "VALHALLA RESTAURANT BAR",
			"address": "3834 Nelson Bay Road,Bobs Farm, NSW 2316"
		},
		"agent": {
			"name": "Ari Gold",
			"phone": "0412345678",
			"email": "ari.gold@mga.com"
		},
		"user": {
			"email": "admin@weddingband.com",
			"name": "Admin"
		},
		"musician": {
			"name": "Grant Green",
			"instrument": "Guitar"
		},
		"aisle_song": {
			"title": "Pachelbel's Canon",
			"key": "D",
			"tempo": 62
		},
		"first_dance_song": {
			"title": "At Last",
			"key": "F",
			"tempo": 65
		}
	},
```
### `POST /gigs`
 - Posts a new gig to psql. 
- JWT required
- Request: 
```json
{
	"date": "03/04/2024",
	"time": "16:30:00",
	"invoice": "1005",
	"venue_id": "1",
	"agent_id": "2",
	"musician_id": "3",
	"aisle_song_id": "4",
	"first_dance_song_id": "3" 
}
```
- Response:
```json
{
	"id": 3,
	"date": "2024-03-04",
	"time": "16:30:00",
	"invoice": "1005",
	"venue_id": 1,
	"agent_id": 2,
	"user_id": 1,
	"musician_id": 3,
	"aisle_song_id": 4,
	"first_dance_song_id": 3
}
```
***
### `PATCH /gig/<int:gig_id>`
 - Updates an existing gig in psql. 
- JWT required
- Request: 
```json
{
	"date": "10/10/2024",
	"time": "15:30:00"
}
```
- Response: 
```json
{
	"id": 1,
	"date": "2024-10-10",
	"time": "15:30:00",
	"invoice": "1001",
	"venue": {
		"title": "VALHALLA RESTAURANT BAR",
		"address": "3834 Nelson Bay Road,Bobs Farm, NSW 2316"
	},
	"agent": {
		"name": "Ari Gold",
		"phone": "0412345678",
		"email": "ari.gold@mga.com"
	},
	"user": {
		"name": "Admin",
		"email": "admin@weddingband.com"
	},
	"musician": {
		"name": "Grant Green",
		"instrument": "Guitar"
	},
	"aisle_song": {
		"title": "Pachelbel's Canon",
		"key": "D",
		"tempo": 62
	},
	"first_dance_song": {
		"title": "At Last",
		"key": "F",
		"tempo": 65
	}
}
```
***
### `DELETE /gig/<int:gig_id>`
 - Deletes an existing gig from psql. 
- JWT required
- Response: 
```json
{
	"message": "Gig on 2024-10-10 deleted successfully"
}
```
****************************************************************
## Musicians
### `GET /musician`
 - Gets the list of musicians currently stored in psql. 

- Response (shortened for brevity): 
```json
	{
		"id": 1,
		"name": "Grant Green",
		"instrument": "Guitar",
		"email": "info@grantgreen.net",
		"phone": "0455566899",
		"user": {
			"name": "Admin",
			"email": "admin@weddingband.com"
		}
	},
	{
		"id": 2,
		"name": "Wes Montgomery",
		"instrument": "Guitar",
		"email": "info@wes.net",
		"phone": "0455566888",
		"user": {
			"name": "Admin",
			"email": "admin@weddingband.com"
		}
	},
	{
		"id": 3,
		"name": "Guthrie Goven",
		"instrument": "Guitar",
		"email": "guthrie@guthriegoeven.com",
		"phone": "0455566887",
		"user": {
			"name": "Admin",
			"email": "admin@weddingband.com"
		}
	},
	{
		"id": 4,
		"name": "Jaco Pastorius",
		"instrument": "Bass",
		"email": "j@jaco.com",
		"phone": "0444587189",
		"user": {
			"name": "Admin",
			"email": "admin@weddingband.com"
		}
	},
```
### `POST /musician`
 - Posts a new musician to psql. 
- JWT required
- Request: 
```json
{
	"name": "Mark Knopfler",
	"email": "mark@moneyfornothing.com",
	"phone": "0401234567",
	"instrument": "Guitar"
}
```
- Response:
```json
{
	"id": 18,
	"name": "Mark Knopfler",
	"instrument": "Guitar",
	"email": "mark@moneyfornothing.com",
	"phone": "0401234567",
	"user": {
		"email": "admin@weddingband.com",
		"name": "Admin"
	}
}
```
***
### `PATCH /musician/<int:musician_id>`
 - Updates an existing musician in psql. 
- JWT required
- Request: 
```json
{
	"email": "mark@direstraights.com"
}
```
- Response: 
```json
{
	"id": 18,
	"name": "Mark Knopfler",
	"instrument": "Guitar",
	"email": "mark@direstraights.com",
	"phone": "0401234567",
	"user": {
		"email": "admin@weddingband.com",
		"name": "Admin"
	}
}
```
***
### `DELETE /musician/<int:musician_id>`
 - Deletes an existing musician from psql. 
- JWT required
- Response: 
```json
{
	"message": "Musician Mark Knopfler deleted successfully"
}
```
****************************************************************
## Venues
### `GET /venues`
 - Gets the list of venues currently stored in psql. 

- Response (shortened for brevity): 
```json
	{
		"id": 1,
		"title": "VALHALLA RESTAURANT BAR",
		"manager": "Trevor Odinson",
		"address": "3834 Nelson Bay Road,Bobs Farm, NSW 2316",
		"phone": "0454234556",
		"user": {
			"email": "admin@weddingband.com",
			"name": "Admin"
		}
	},
	{
		"id": 2,
		"title": "Lovedale Wedding Chapel and Reception",
		"manager": "Cyril Lovedale",
		"address": "842 Lovedale Road, Allandale, NSW 2320",
		"phone": "0412457889",
		"user": {
			"email": "admin@weddingband.com",
			"name": "Admin"
		}
	},
	{
		"id": 3,
		"title": "Fort Scratchley Function Centre",
		"manager": "Cletus Scratchley",
		"address": "1/3 Nobbys Road, Newcastle East, NSW 2300",
		"phone": "0415234556",
		"user": {
			"email": "admin@weddingband.com",
			"name": "Admin"
		}
	}
```
### `POST /venues`
 - Posts a new venue to psql. 
- JWT required
- Request: 
```json
{
	"title": "Ravalla",
	"manager": "Jerome O'Connor",
	"address": "48 Watt St, Newcastle NSW 2300",
	"phone": "0415121316"
}
```
- Response:
```json
{
	"id": 4,
	"title": "Ravalla",
	"manager": "Jerome Connors",
	"address": "48 Watt St, Newcastle NSW 2300",
	"phone": "0415121316",
	"user": {
		"name": "Admin",
		"email": "admin@weddingband.com"
	}
}
```
***
### `PATCH /venues/<int:venue_id>`
 - Updates an existing venue in psql. 
- JWT required
- Request: 
```json
{
	"phone": "0404050607"
}
```
- Response: 
```json
{
	"id": 4,
	"title": "Ravalla",
	"manager": "Jerome Connors",
	"address": "48 Watt St, Newcastle NSW 2300",
	"phone": "0404050607",
	"user": {
		"email": "admin@weddingband.com",
		"name": "Admin"
	}
}
```
***
### `DELETE /venues/<int:venue_id>`
 - Deletes an existing venue from psql. 
- JWT required
- Response: 
```json
{
	"message": "Venue Ravalla deleted successfully"
}
```
## R6 - An ERD for your app
ERD

## R7 - Detail any third party services that your app will use
Modules used. SQLALchemy etc.

## R8 - Describe your projects models in terms of the relationships they have with each other
Relationships between tables

## R9 - Discuss the database relations to be implemented in your application
How the relationships will work?

## R10 - Describe the way tasks are allocated and tracked in your project
Trello