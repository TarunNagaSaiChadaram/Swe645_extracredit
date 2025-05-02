# - Samanvitha Matta (G01252738)
# - Akshaya Reddy Dundigalla (G01482843)
# - Tarun Naga Sai Chadaram (G01445928)
# Sets up the SQLAlchemy database object for the Flask application.
# To manage ORM activities, this will be imported into the main application.
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
