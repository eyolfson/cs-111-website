from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import File, Lecture

class LecturesView(generic.ListView):
    template_name = 'cs111/lectures.html'
    context_object_name = 'lectures'

    def get_queryset(self):
        return Lecture.objects.order_by('number')

def index(request):
    return render(request, 'cs111/index.html', {})

def labs(request):
    return render(request, 'cs111/labs.html', {})

def resources(request):
    try:
        syllabus = File.objects.get(file='cs111/syllabus.pdf')
    except File.DoesNotExist:
        syllabus = None
    return render(request, 'cs111/resources.html', {'syllabus': syllabus})
