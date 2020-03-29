from django.shortcuts import render
from django.http import HttpResponse

results = [
    {
        'address': 'Hospital Drive, Calgary',
        'patient_capacity': '250',
        'wait_time': '20',
        'drive_time': '10',
    },
    {
        'address': '2nd Hospital Drive, Calgary',
        'patient_capacity': '69',
        'wait_time': '30',
        'drive_time': '20',
    }
]


def home(request):
    """
    Returns HTTP Response for the home/landing page.
    """
    context = {
        'results': results
    }
    return render(request, 'landing/index.html', context)
