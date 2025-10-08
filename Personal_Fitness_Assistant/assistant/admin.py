from django.contrib import admin
from .models import FitnessAssessment

@admin.register(FitnessAssessment)
class FitnessAssessmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'gender', 'age', 'weight', 'health_goal', 'created_at']
    list_filter = ['gender', 'created_at']
    search_fields = ['health_goal']