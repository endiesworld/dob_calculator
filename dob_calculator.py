from datetime import datetime, timedelta, date


def calculate_age(dob: list):
    dob = date(dob[0], dob[1], dob[2])
    age = datetime.now().date() - dob
    age_years = age // timedelta(days=365)
    print(age_years)


calculate_age([1986, 12, 17])
