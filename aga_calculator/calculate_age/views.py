from datetime import datetime, timedelta, date
# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view()
def calculate_age(request):
    year = int(request.GET['year'])
    month = int(request.GET['month'])
    day = int(request.GET['day'])
    dob = date(year, month, day)
    age = datetime.now().date() - dob
    age_years = age // timedelta(days=365)
    return Response({'year': year, 'month': month, 'day': day, 'age': age_years})
