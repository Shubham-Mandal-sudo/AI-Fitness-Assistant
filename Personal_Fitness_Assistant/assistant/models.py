from django.db import models

class FitnessAssessment(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    FOOD_PREFERENCES = [
        ('ANY', 'No Preference'),
        ('INDIAN', 'Indian'),
        ('CHINESE', 'Chinese'),
        ('AMERICAN', 'American'),
        ('MEXICAN', 'Mexican'),
        ('ASIAN', 'Asian'),
        ('MEDITERRANEAN', 'Mediterranean'),
        ('VEGETARIAN', 'Vegetarian'),
        ('VEGAN', 'Vegan'),
    ]
    
    WORKOUT_PLACES = [
        ('ANY', 'No Preference'),
        ('HOME', 'At Home'),
        ('GYM', 'Gym'),
        ('PARK', 'Park/Outdoors'),
        ('ANY_OUTDOOR', 'Any Outdoor'),
        ('ANY_INDOOR', 'Any Indoor'),
    ]
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    weight = models.FloatField(help_text="Weight in kg")
    height = models.FloatField(help_text="Height in cm")
    waist_circumference = models.FloatField(help_text="Waist circumference in cm")
    health_goal = models.TextField()
    duration = models.IntegerField(null=True, blank=True, help_text="Duration in weeks (optional)")
    food_preference = models.CharField(max_length=20, choices=FOOD_PREFERENCES, default='ANY')
    workout_place = models.CharField(max_length=20, choices=WORKOUT_PLACES, default='ANY')
    created_at = models.DateTimeField(auto_now_add=True)
    ai_response = models.TextField()
    
    def calculate_bmi(self):
        return self.weight / ((self.height / 100) ** 2)
    
    def __str__(self):
        return f"Assessment {self.id} - {self.health_goal}"