from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Course, Lecture, Comment, Homework


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password']


class CourseSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class LectureSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    def create(self, validated_data):
        course = Course.objects.get(name=validated_data.pop('course')['name'])
        lecture = Lecture.objects.create(course=course, **validated_data)
        return lecture

    def update(self, instance, validated_data):
        instance.course = validated_data.get('course', instance.course)
        instance.presentation = "static/uploads/presentations/" + str(validated_data.get('presentation', instance.presentation))
        instance.name = validated_data.get('name', instance.name)
        instance.task = validated_data.get('task', instance.task)
        instance.save()
        return instance

    class Meta:
        model = Lecture
        fields = '__all__'


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
