from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'has_started', 'has_ended',)


admin.site.register(Course, CourseAdmin)