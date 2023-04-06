from django.contrib import admin
from todoish.models import Task

# admin.site.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_finished', 'created_at', 'author', 'category')
    
    list_filter = ('title', 'is_finished', 'created_at', 'updated_at', 'category')

    # Pure fields without any sections
    # fields = ['title', 'description', 'is_finished', 'author', 'category']

    # When we need to create fields with custom sections
    fieldsets = (
        ('General', {
            'fields': ('title', 'description', 'is_finished', ('author', 'category'))
        }),
        # ('History', {
        #     'fields': ('created_at', 'updated_at')
        # })
    )


admin.site.register(Task, TaskAdmin)
