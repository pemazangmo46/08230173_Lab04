from django.shortcuts import render  # Import render function to render HTML templates
from .models import AboutMe, LearningJourney  # Import models from the current app

# ---------------------------
# View for Learning Journey page (Home Page)
# ---------------------------
def index(request):
    # Fetch all LearningJourney entries from the database
    journey_entries = LearningJourney.objects.all()

    # Fetch the first AboutMe entry to display brief bio info
    about = AboutMe.objects.first()

    # Pass data to the template using a context dictionary
    context = {
        'journey_entries': journey_entries,
        'about': about,
    }

    # Render the 'index.html' template with context data
    return render(request, 'index.html', context)


# ---------------------------
# View for About Me page
# ---------------------------
def about_me(request):
    # Get the first AboutMe record (assuming there’s only one entry)
    about = AboutMe.objects.first()

    # Pass the AboutMe data to the template
    context = {
        'about': about
    }

    # Render the 'aboutMe.html' template with context data
    return render(request, 'aboutMe.html', context)
