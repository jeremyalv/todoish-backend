from django.contrib import admin
from django.db import models
from datetime import datetime

from todoish.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ('title',)

    list_display = ('title', 'is_finished', 'due_date', 'created_at', 'author', 'category')
    
    list_filter = ('title', 'is_finished', 'due_date', 'created_at', 'updated_at', 'category')

    # Pure fields without any sections
    # fields = ['title', 'description', 'is_finished', 'author', 'category']

    # When we need to create fields with custom sections
    fieldsets = (
        ('General', {
            'fields': ('title', 'description', 'is_finished', 'due_date', 'author', 'category')
        }),
        # ('History', {
        #     'fields': ('created_at', 'updated_at')
        # })
    )

# admin.site.register(Task, TaskAdmin)
