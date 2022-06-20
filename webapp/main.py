import os
from flask import request, render_template, flash, redirect
from forms import PredictForm, MlModelForm
from utils import model_predict, allowed_file
from werkzeug.utils import secure_filename
from conf import app, db, MlModel
from utils import learning_model


@app.route("/", methods=["GET", "POST"])
async def upload_file_and_learning_model():
    form = MlModelForm(request.form)
    result = None
    if request.method == 'POST':

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            path = app.config["UPLOAD_FOLDER"] + f"/{filename}"
            model_path = learning_model(path=path, model_name=form.model_name.data)

            note = MlModel(path=model_path, name=form.model_name.data)
            db.session.add(note)
            db.session.commit()

            result = "Model has been trained"
            return render_template("learning_model.html", form=form, result=result)

    return render_template("learning_model.html", form=form)


@app.route("/model", methods=["GET", "POST"])
def predict():
    form = PredictForm()
    data = form.data
    result = None
    if request.method == "POST" and form.validate_on_submit():

        model_path = MlModel.query.filter_by(name=data["model_version"]).first()
        model_path = model_path.path

        result = model_predict(path=model_path, data=data)

    return render_template("index.html", form=form, result=result)


if __name__ == '__main__':
    app.run(debug=True)
