from django import forms
from django.contrib.auth.models import User

from .models import Course, Lecture, Comment, Homework


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            'name': 'Название',
            'users': 'Пользователи'
        }


class CourseDeleteForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']
        labels = {
            'name': 'Название'
        }


class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']
        labels = {
            'name': 'Название'
        }


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['name', 'presentation', 'task']
        labels = {
            'name': 'Название',
            'presentation': 'Презентация',
            'task': 'Задание'
        }


class LectureDeleteForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['name']
        labels = {
            'name': 'Название'
        }


class LectureUpdateForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['name', 'presentation', 'task']
        labels = {
            'name': 'Название',
            'presentation': 'Презентация',
            'task': 'Задание'
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        labels = {
            'message': 'Комментарий'
        }


class HomeworkAddForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['answer']
        labels = {
            'answer': 'Решение'
        }


class AddDeleteUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        labels = {
            'username': 'Псевдоним пользователя'
        }


class UpdateMarkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['mark']
        labels = {
            'mark': 'Отметка'
        }
