import os.path
from sklearn.model_selection import train_test_split as tts
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import pandas as pd
import pickle
from dotenv import load_dotenv

load_dotenv(dotenv_path="webapp/webapp.env")

MODEL_SAVE_PATH = os.getenv("MODEL_SAVE_PATH")


def model_predict(path: str, data: dict) -> int:
    data.pop("csrf_token")
    data.pop("model_version")

    df = pd.DataFrame.from_dict([data])
    model = pickle.load(file=open(path, "rb"))

    result = model.predict(df)
    return int(result)


ALLOWED_EXTENSIONS = {'csv'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def learning_model(path: str, model_name: str):
    df = pd.read_csv(path)

    x = df.drop('price', axis=1)
    y = df[['price']]

    x_train, x_test, y_train, y_test = tts(x, y, test_size=0.2, random_state=22)

    model = RandomForestRegressor()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    ts = r2_score(y_train, model.predict(x_train))  # train score
    vs = r2_score(y_test, y_pred)  # validation score

    complete = os.path.join(MODEL_SAVE_PATH, f"{model_name}.sav")

    pickle.dump(model, open(complete, 'wb'))

    absolute_path = f"{MODEL_SAVE_PATH}/{model_name}.sav"

    return absolute_path



