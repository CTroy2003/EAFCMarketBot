EAFC Market Bot is an Agent who, under user direction will navigate the EAFC Ultimate Team Online Marketplace. The user instructs the agent to search for players under market value, where using auotmation our bot sucessfully "snipes" or buys the players before other people can.
The backend is hosted on a flask server where we use selenium to automate navigation on the EAFC Ultimate Team Marketplace, our agent is able to cycle the search until a succesfull purchase is made.
The frontend is a simple react webpage where we are able to select and send our filters to the backend through JSON, we also receive and react to the statuses of our search based on updates sent from the server.

Files --

marketpull.py - this file contains the logic associated with navigating through the marketplace using selenium.

apipull.py - Flask application that runs our agent code and uses endpoints to communicate with frontend

requirements.txt - list of necessary dependancies.

Procfile - boilerplate for server deployment service (using Render here)

index.js & index.css handle our frontend webpage and styling.

NOTE: This is for personal testing and learning, please do not actually use this in any meaningful capacity, EA might ban your account if you do.


