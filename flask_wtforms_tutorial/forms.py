"""Form class declaration."""
import csv
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    DateField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from datetime import date
from wtforms.fields.html5 import DateField
from wtforms.validators import URL, DataRequired, Email, EqualTo, Length




class StockForm(FlaskForm):
    """Generate Your Graph."""
    #THIS IS WHERE YOU WILL IMPLEMENT CODE TO POPULATE THE SYMBOL FIELD WITH STOCK OPTIONS
    chart_choices = []
    with open('listing_status.csv','r') as file:
            Listings = csv.reader(file)
            for row in Listings:
                chart_choices.append((row[0], row[0]))
    print(len(chart_choices))
    symbol = SelectField("Choose Stock Symbol",[DataRequired()],
        choices = list(chart_choices),

    )


    chart_type = SelectField("Select Chart Type",[DataRequired()],
        choices=[
            ("1", "1. Bar"),
            ("2", "2. Line"),
        ],
    )

    time_series = SelectField("Select Time Series",[DataRequired()],
        choices=[
            ("1", "1. Intraday"),
            ("2", "2. Daily"),
            ("3", "3. Weekly"),
            ("4", "4. Monthly"),
        ],
    )

    start_date = DateField("Enter Start Date")
    end_date = DateField("Enter End Date")
    submit = SubmitField("Submit")