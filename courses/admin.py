from django.contrib import admin

from .models import Author, Course, Chapter, Lesson


admin.site.register(Author)
admin.site.register(Chapter)
admin.site.register(Course)
admin.site.register(Lesson)
