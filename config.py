# - Samanvitha Matta (G01252738)
# - Akshaya Reddy Dundigalla (G01482843)
# - Tarun Naga Sai Chadaram (G01445928)
# Flask application configuration class to connect to Amazon RDS MySQL database

class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://admin:database645swe@database-645.cylxhmwgst1w.us-east-1.rds.amazonaws.com/stusurvec"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
