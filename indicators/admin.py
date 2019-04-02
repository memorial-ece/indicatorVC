from django.contrib import admin
from django.forms import TextInput, Textarea
from .models import *


class IndicatorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows':4, 'cols':40})}
    }
    list_display = ['program', 'tag', 'level', 'course_number', 'assessment_method', 'bins']
    list_filter = ('program', 'GA', 'level')


admin.site.register(Indicator, IndicatorAdmin)
