from rest_framework.permissions import BasePermission

from .models import Course, Lecture, Homework


class IsAddedToCourse(BasePermission):
    def has_object_permission(self, request, view, obj):
        auth_user = request.user
        lecturers = Course.objects.get(id=obj.id).users.filter(is_staff=True)
        students = Course.objects.get(id=obj.id).users.filter(is_staff=False)
        return (auth_user in lecturers) or (auth_user in students)


class IsHasPermissionToLecture(BasePermission):
    def has_object_permission(self, request, view, obj):
        course = Lecture.objects.get(id=obj.id).course
        return IsAddedToCourse.has_object_permission(self, request, view, course)


class IsOwnerStudentOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        hw = Homework.objects.get(id=obj.id)
        course = Lecture.objects.get(id=hw.lecture.id).course
        course_staff = Course.objects.get(id=course.id).users.filter(is_staff=True)
        return request.user == hw.student or request.user in course_staff


class IsAccessedToComments(BasePermission):
    def has_object_permission(self, request, view, obj):
        hw = Homework.objects.get(id=obj.homework.id)
        return IsOwnerStudentOrStaff.has_object_permission(self, request, view, hw)