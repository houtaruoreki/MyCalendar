import datetime
from datetime import datetime
from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    current_date = datetime.now().strftime('%d %B %Y')
    return HttpResponse(current_date)
