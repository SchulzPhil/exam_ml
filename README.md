# Flask car price prdeiction app

Hi there. This is a Flask app that helps you to train your own model and then predict the certain car price.

## Run locally

**Clone project with SSH**
    
     git clone git@github.com:SchulzPhil/exam_ml.git

**Get project folder**
    
     cd exam_ml/webapp
    
**Create virtual environment**

    python -m venv venv
    
**Acrivate virtual Environment**

    source venv/bin/activate
    
**Install dependencies**

    pip install -r requirements.txt

**Create additional folder for your models and data**

    mkdir ml_model

    mkdir ml_data

**Add the absolute path to conf.py and utils.py modules**

***SECRET_KEY could be any*** 

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "ANY")

***Paste there the absolute path to previously created ml_data folder***

    app.config['UPLOAD_FOLDER'] = os.getenv("UPLOAD_FOLDER", "/home/user/exam_ml/webapp/ml_data")

***Paste there the absolute path to test.db DB***

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:////home/user/exam_ml/webapp/test.db")
    
***Paste there the absolute path to previously created ml_model folder***
    
    MODEL_SAVE_PATH = os.getenv("MODEL_SAVE_PATH", "/home/user/exam_ml/webapp/ml_model)

**Run server**

    python3 main.py

---
After this you could do anything on your local server. 

For example you could test the model training on the test dataset cars.csv. After this test the model's prediction.
