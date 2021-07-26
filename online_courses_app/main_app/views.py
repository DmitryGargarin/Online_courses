from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import FormView

from .forms import CourseForm, LectureForm, CourseDeleteForm, CourseUpdateForm, LectureDeleteForm, LectureUpdateForm, \
    MessageForm, HomeworkAddForm, AddDeleteUserForm, UpdateMarkForm
from .models import Course, Lecture, validate_file_extension, Homework, Comment


def index(request):
    courses = Course.objects.all()
    course_form = CourseForm()
    course_delete_form = CourseDeleteForm()

    if request.method == "POST":
        if "del_course" in request.POST:
            course = CourseDeleteForm(request.POST)
            if course.is_valid():
                instance = Course.objects.get(name=course.cleaned_data.get('name'))
                instance.delete()
        elif "add_course" in request.POST:
            course = CourseForm(request.POST)
            if course.is_valid():
                course.save()
    else:
        course_form = CourseForm()
        course_delete_form = CourseDeleteForm()

    data = {"courses": courses,
            "course_add_form": course_form,
            "course_delete_form": course_delete_form}
    return render(request, "index.html", context=data)


def personal(request):
    return render(request, "personal.html")


def course(request):
    course = Course.objects.get(id=request.GET.get("id", 0))
    lecturers = Course.objects.get(id=course.id).users.filter(is_staff=True)
    students = Course.objects.get(id=course.id).users.filter(is_staff=False)
    lectures = Lecture.objects.filter(course_id=course)
    lecture_add = LectureForm()
    lecture_delete = LectureDeleteForm()
    course_update_form = CourseUpdateForm()
    add_delete_user_form = AddDeleteUserForm()

    if request.method == "POST":
        if "upd_course" in request.POST:
            curr_course = CourseUpdateForm(request.POST, instance=course)
            if curr_course.is_valid():
                curr_course.save()
        elif "del_lecture" in request.POST:
            lecture = LectureDeleteForm(request.POST)
            if lecture.is_valid():
                instance = Lecture.objects.get(name=lecture.cleaned_data.get('name'))
                instance.delete()
        elif "add_lecture" in request.POST:
            lecture_new = LectureForm(request.POST, request.FILES)
            lecture_new.course_id = course.id
            if lecture_new.is_valid():
                lecture_new.save()
        elif "add_user" in request.POST:
            new_user = User.objects.get(username=request.POST.get("username", ""))
            course.users.add(new_user)
        elif "del_user" in request.POST:
            new_user = User.objects.get(username=request.POST.get("username", ""))
            course.users.remove(new_user)
    else:
        lecture_add = LectureForm()
        course_update_form = CourseUpdateForm()
        add_delete_user_form = AddDeleteUserForm()

    data = {
        "course": course,
        "lects": lecturers,
        "studs": students,
        "lectures": lectures,
        "lecture_add_form": lecture_add,
        "lecture_delete_form": lecture_delete,
        "course_update_form": course_update_form,
        "add_delete_user_form": add_delete_user_form
    }
    return render(request, "course.html", context=data)


def lecture(request):
    lecture = Lecture.objects.get(id=request.GET.get("id", 0))
    homeworks = Homework.objects.filter(lecture_id=request.GET.get("id", 0))
    lecture_update_form = LectureUpdateForm()
    homeworks_user = Homework.objects.filter(lecture_id=request.GET.get("id", 0), student=request.user)
    homework_add_form = HomeworkAddForm()

    if request.method == 'POST':
        if "upd_lecture" in request.POST:
            curr_lecture = LectureUpdateForm(request.POST, instance=lecture)
            if curr_lecture.is_valid():
                curr_lecture.save()
        if "add_homework" in request.POST:
            hw = Homework(lecture=lecture,
                          student=request.user,
                          answer=request.POST.get('answer', ''),
                          mark=0)
            hw_user_lectures = Homework.objects.filter(student=request.user)
            lectures = []
            for hws in hw_user_lectures:
                lectures.append(hws.lecture.id)
            if hw.lecture.id not in lectures:
                hw.save()
    else:
        lecture_update_form = LectureUpdateForm()
        homework_add_form = HomeworkAddForm()

    data = {"lecture": lecture,
            "homeworks": homeworks,
            "lecture_update_form": lecture_update_form,
            "homework_add_form": homework_add_form,
            "homeworks_user": homeworks_user}
    return render(request, "lecture.html", context=data)


def homework(request):
    hm = Homework.objects.get(id=request.GET.get("id", 0))
    msgForm = MessageForm()
    latest_msgs = Comment.objects.all().filter(homework__exact=hm.id).order_by('-pubdate')
    update_mark_form = UpdateMarkForm()
    if request.method == 'POST':
        if "msgpost" in request.POST:
            msg = Comment(homework=hm,
                                 user=request.user,
                                 message=request.POST.get("message", 0))
            msg.save()
        if "upd_mark" in request.POST:
            updated_mark = UpdateMarkForm(request.POST, instance=hm)
            if updated_mark.is_valid():
                updated_mark.save()
    else:
        msgForm = MessageForm()
        update_mark_form = UpdateMarkForm()
    data = {"homework": hm, 
            "msgs": latest_msgs, 
            "msgForm": msgForm, 
            "update_mark_form": update_mark_form}
    return render(request, "homework.html", context=data)


app_url = "/"


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = app_url + "login"
    template_name = "reg/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "reg/login.html"
    success_url = app_url

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(app_url)
