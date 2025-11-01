from django.contrib import admin # type: ignore
from .models import AboutMe, LearningJourney
# Register your models here.


admin.site.register(AboutMe)
admin.site.register(LearningJourney)
