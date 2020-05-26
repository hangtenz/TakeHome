Run Api
	- venv\Scripts\activate
	- python app.py
Database 
	- sqlite3 (in memory database)
	- flask
url of api
	- port = 5565
	- path = /cards

HTTP method
	- POST
		add cards in database, pass data by json body like this
		{
			"name" : "Alice",
			"content":"abcc",
			"status":"OK",
			"catagory":"test",
			"author":"hangtenz"
		}
		- return json message ok
	- PUT
	 	update card in database when specify author, pass data by json body
		{
			"name" : "Ahhh",
			"content":"abcc",
			"status":"OK",
			"catagory":"test",
			"author":"hangtenz"
		}
		- return json message ok
	- DELETE
		delete card in database when specify author, pass data by json body
		{
			"author" : "hangtenz"
		}		
		- return json message author
	- GET
		get all cards in database 
		- return json list