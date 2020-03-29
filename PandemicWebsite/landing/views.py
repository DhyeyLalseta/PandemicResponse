from django.shortcuts import render
from .models import Result


def home(request):
    """
    Returns render for the home/landing page.

    Includes rendering of results and hospital information form.
    """
    context = {
        "results": Result.objects.all()
        .filter(patient_capacity__gt=0)
        .order_by("drive_time")[:4],
    }
    return render(request, "landing/index.html", context)
