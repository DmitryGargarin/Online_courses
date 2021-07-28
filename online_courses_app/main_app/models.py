import os
from shutil import copy, copyfile

from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.pptx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


# user будет использоваться дефолтная

class Course(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User)
    pubdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.name


class Lecture(models.Model):
    name = models.CharField(max_length=50)
    presentation = models.FileField(upload_to="static/uploads/presentations/", validators=[validate_file_extension])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    task = models.CharField(max_length=300, default="")
    pubdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.name + " - " + str(self.presentation) + " - " + str(self.course) + " - " + str(self.task)


class Homework(models.Model):
    MARKS = [
        (5, "Awesome"),
        (4, "Very good"),
        (3, "Good"),
        (2, "Bad"),
        (1, "Awful"),
        (0, "Not checked")
    ]
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name="lecture_name")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='name')
    pubdate = models.DateTimeField(auto_now_add=True)
    answer = models.CharField(max_length=100)
    mark = models.IntegerField(choices=MARKS)

    def __str__(self):
        return str(self.id) + " - " + self.student.first_name + self.student.last_name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    message = models.CharField(max_length=100, default="")
    pubdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + str(self.user) + " " + str(self.pubdate)
