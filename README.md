Phase-4-Code-Challenge-lateshow
Date, 2024/10/15
By Mbithi Evans

# lateshow
Welcome to the Late Show project! This Flask application is designed to manage episodes, guests, and their appearances on a late-night talk show. It provides a RESTful API for CRUD operations on episodes, guests, and their respective appearances.

Features

View all episodes and guests
Retrieve detailed information about a specific episode, including its guests and ratings
Add new appearances for guests on specific episodes
Easy to extend with additional features


Technologies Used
Python 3.8+
Flask
Flask-SQLAlchemy
Flask-Migrate
Flask-Marshmallow
SQLite
SQLAlchemy

Installation

Clone the repository:
git clone https://github.com/34Mbithi/lateshow.git

cd lateshow

Set up a virtual environment:

python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

Install the required packages:
pip install -r requirements.txt

Late Show
Welcome to the Late Show project! This Flask application is designed to manage episodes, guests, and their appearances on a late-night talk show. It provides a RESTful API for CRUD operations on episodes and guests, as well as their respective appearances.


Technologies Used

Python 3.8+
Flask
Flask-SQLAlchemy
Flask-Migrate
Flask-Marshmallow
SQLite
SQLAlchemy

Installation

Python 3.8 or higher
pip (Python package installer)


Steps

Clone the repository:

git clone https://github.com/34Mbithi/lateshow.git

cd lateshow


Set up a virtual environment:

python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

Install the required packages:

pip install -r requirements.txt

Run the Application:
python run.py

The application will start and be accessible at http://127.0.0.1:5000/.

API Testing: You can use tools like Postman or CURL to interact with the API endpoints.

API Endpoints
Episodes
GET /episodes: Retrieve a list of all episodes.
GET /episodes/<int:id>: Retrieve details for a specific episode by ID.
DELETE /episodes/<int:id>: Delete a specific episode by ID.
Guests
GET /guests: Retrieve a list of all guests.
Appearances
POST /appearances: Create a new appearance for a guest on an episode.


License
The content of this site is licensed under the MIT license Copyright (c) 2018.
