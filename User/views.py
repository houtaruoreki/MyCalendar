from datetime import datetime

from django.shortcuts import render
from .models import User


def calculate_age(birth_date, current_year):
    return current_year - birth_date.year - ((current_year, birth_date.month, birth_date.day) < (
        current_year, datetime.now().month, datetime.now().day))


def index(request):
    users = User.objects.all()
    current_year = datetime.now().year

    # Calculate age for each user
    for user in users:
        user.age = calculate_age(user.birth_date, current_year)

    return render(request, 'index.html', {'users': users, 'current_year': current_year})
