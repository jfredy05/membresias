from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View

from .models import Course, Chapter, Lesson


class CourseDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        course = get_object_or_404(Course, slug=slug)
        context={
            'course':course
        }
        return render(request, 'courses/pages/course/detail.html', context)