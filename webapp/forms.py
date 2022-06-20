from flask_wtf import FlaskForm
from conf import MlModel
from wtforms import SelectField, FloatField, validators, StringField
from choices import (
    car_brand_list, car_model_list,
    fuel_type_list, transmission_type_list
)


class PredictForm(FlaskForm):
    company_name = SelectField(choices=car_brand_list)
    model = SelectField(choices=car_model_list)
    fuelType = SelectField(choices=fuel_type_list)
    transmission = SelectField(choices=transmission_type_list)
    engineSize = FloatField(validators=[validators.DataRequired()])
    mileage = FloatField(validators=[validators.DataRequired()])
    mpg = FloatField(validators=[validators.DataRequired()])
    tax = FloatField(validators=[validators.DataRequired()])
    year = FloatField(validators=[validators.DataRequired()])
    model_version = SelectField(choices=MlModel.query.order_by(MlModel.name).all())


class MlModelForm(FlaskForm):
    model_name = StringField(label="Model name",
                             validators=[validators.DataRequired()])



