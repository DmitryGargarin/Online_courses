from django import forms
from django.contrib.auth.models import User

from .models import Course, Lecture, Comment, Homework


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDeleteForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']


class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = '__all__'


class LectureDeleteForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['name']


class LectureUpdateForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['name', 'presentation', 'task']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']


class HomeworkAddForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['answer']


class AddDeleteUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class UpdateMarkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['mark']