from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import File, Lab, Lecture, LabGrade, MidtermGrade
from django_gitolite.models import Repo

class LecturesView(generic.ListView):
    template_name = 'cs111/lectures.html'
    context_object_name = 'lectures'

    def get_queryset(self):
        return Lecture.objects.order_by('number')

class LabsView(generic.ListView):
    template_name = 'cs111/labs.html'
    context_object_name = 'labs'

    def get_queryset(self):
        return Lab.objects.order_by('number')

def index(request):
    return render(request, 'cs111/index.html', {})

def labs(request):
    return render(request, 'cs111/labs.html', {})

@login_required
def repository(request):
    user = request.user
    repo = Repo.objects.get(path=f'spring21/{user.username}/cs111')
    lab_grades = LabGrade.objects.filter(student__user=user).order_by('lab__number')
    midterm_grade = None
    try:
        midterm_grade = MidtermGrade.objects.get(student__user=user)
    except Exception as e:
        print(e)
        print('ok')
        pass
    return render(request, 'cs111/repository.html', {
        'repo': repo,
        'lab_grades': lab_grades,
        'midterm_grade': midterm_grade,
    })

def resources(request):
    try:
        syllabus = File.objects.get(file='cs111/syllabus.pdf')
    except File.DoesNotExist:
        syllabus = None
    try:
        vm = File.objects.get(file='cs111/vm.ova')
    except File.DoesNotExist:
        vm = None
    try:
        vm_no_gui = File.objects.get(file='cs111/vm-no-gui.ova')
    except File.DoesNotExist:
        vm_no_gui = None
    return render(request, 'cs111/resources.html', {
        'syllabus': syllabus,
        'vm': vm,
        'vm_no_gui': vm_no_gui,
    })
