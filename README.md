# Reece Doyle T2A2 -  Wedding Band API
## R1 - Identification of the problem you are trying to solve by building this particular app.
Weddings have always been a significant milestone in most cultures around the world. They're a time to celebrate the love of the couple that has made the commitment to each other in the precesence of their families and loved ones, **and what is a celebration without music?**

Whether it be during the ceremeony, during the cocktail hour, the first dance, or the party that ensues once the rituals are out of the way, every part of a wedding is filled with music. Thus, the orgainsation of the wedding musicians can truely make or break the day.
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


## R6 - An ERD for your app


## R7 - Detail any third party services that your app will use


## R8 - Describe your projects models in terms of the relationships they have with each other


## R9 - Discuss the database relations to be implemented in your application


## R10 - Describe the way tasks are allocated and tracked in your project

CREATE TABLE VENUES(
venue_id integer PRIMARY KEY,
address text NOT NULL,
phone integer NOT NULL,
manager text NOT NULL
);

CREATE TABLE MUSICIANS(
muso_id integer PRIMARY KEY,
name text NOT NULL,
phone integer NOT NULL,
instrument_1 text NOT NULL,
instrument_2 text,
instrument_3 text
);

CREATE TABLE BOOKING_AGENT(
agent_id integer PRIMARY KEY,
name text NOT NULL,
email text NOT NULL,
phone integer NOT NULL
);

