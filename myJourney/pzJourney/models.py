from django.db import models # type: ignore

# Create your models here.

# Model for About Me page
class AboutMe(models.Model):
    name = models.CharField(max_length=100)  # Your full name
    email = models.EmailField()             # Your email
    bio = models.TextField()                # Short biography
    skills = models.TextField(blank=True)   # Optional: list your skills

    def __str__(self):
        return self.name

# Model for Learning Journey page
class LearningJourney(models.Model):
    title = models.CharField(max_length=200)   # Title of a learning step
    description = models.TextField()           # Description of what you learned
    date = models.DateField(auto_now_add=True) # Optional: date when you learned

    def __str__(self):
        return self.title
