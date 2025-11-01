from django.shortcuts import render
from .models import AboutMe, LearningJourney

# View for Learning Journey page (index)
def index(request):
    journey_entries = LearningJourney.objects.all()  # Fetch all learning journey items
    about = AboutMe.objects.first()  # Fetch About Me entry
    context = {
        'journey_entries': journey_entries,
        'about': about,
    }
    return render(request, 'index.html', context)

# View for About Me page
def about_me(request):
    about = AboutMe.objects.first()  # Assuming only one AboutMe entry
    context = {
        'about': about
    }
    return render(request, 'aboutMe.html', context)
