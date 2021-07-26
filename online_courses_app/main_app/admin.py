from django.contrib import admin
from .models import Lecture, Course, Homework, Comment

# Register your models here.
admin.site.register(Lecture)
admin.site.register(Course)
admin.site.register(Homework)
admin.site.register(Comment)