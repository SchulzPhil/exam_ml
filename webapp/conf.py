import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv(dotenv_path="webapp/webapp.env")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config['UPLOAD_FOLDER'] = os.getenv("UPLOAD_FOLDER")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/filipp/PycharmProjects/exam_ml/webapp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class MlModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    path = db.Column(db.String)

    def __repr__(self):
        return "".join(self.name)


db.create_all()




