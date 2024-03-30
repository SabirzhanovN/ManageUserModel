from django.shortcuts import render

from agreements.models import Agreement
from .models import House, Company


def index(request):
    return render(request, "index.html")


def houses(request):
    companies = Company.objects.all()
    houses = House.objects.all()
    agreements = Agreement.objects.all()

    exists = [i.house.house_number for i in agreements]

    context = {
        "companies": companies,
        "houses": houses,
        "agreements": agreements,
        "exists": exists
    }

    return render(request, "houses.html", context)
