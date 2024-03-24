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


## R4 - Identify and discuss the key functionalities and benefits of an ORM


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
### `PATCH /aisle/<int:agent_id>`
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
### `DELETE /aisle/<int:agent_id>`
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
### `PATCH /firstdance/<int:agent_id>`
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
### `DELETE /firstdance/<int:agent_id>`
 - Deletes an existing first dance song from psql. 
- JWT required
- Response: 
```json
{
	"message": "First Dance Song with Perfect deleted successfully"
}
```
## R6 - An ERD for your app


## R7 - Detail any third party services that your app will use


## R8 - Describe your projects models in terms of the relationships they have with each other


## R9 - Discuss the database relations to be implemented in your application


## R10 - Describe the way tasks are allocated and tracked in your project

