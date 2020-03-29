from django.shortcuts import render
from .models import Result


def home(request):
    """
    Returns HTTP Response for the home/landing page.
    """
    context = {
        'results': Result.objects.all()
    }
    return render(request, 'landing/index.html', context)
