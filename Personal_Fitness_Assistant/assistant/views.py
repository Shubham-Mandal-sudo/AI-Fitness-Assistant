from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import FitnessAssessment
from Personal_Fitness_Assistant.ai_client import GeminiClient  
from .utils import render_to_pdf, generate_pdf_filename
import json

def index(request):
    if request.method == 'POST':
        try:
            # Get form data
            user_data = {
                'gender': request.POST.get('gender'),
                'age': int(request.POST.get('age')),
                'weight': float(request.POST.get('weight')),
                'height': float(request.POST.get('height')),
                'waist_circumference': float(request.POST.get('waist_circumference')),
                'health_goal': request.POST.get('health_goal'),
                'duration': request.POST.get('duration'),
                'food_preference': request.POST.get('food_preference', 'ANY'),
                'workout_place': request.POST.get('workout_place', 'ANY'),
            }
            
            # Generate AI response using Gemini
            ai_client = GeminiClient()  # Changed to GeminiClient
            ai_response = ai_client.generate_fitness_plan(user_data)
            
            # Save to database
            assessment = FitnessAssessment(
                gender=user_data['gender'],
                age=user_data['age'],
                weight=user_data['weight'],
                height=user_data['height'],
                waist_circumference=user_data['waist_circumference'],
                health_goal=user_data['health_goal'],
                duration=user_data['duration'] if user_data['duration'] else None,
                food_preference=user_data['food_preference'],
                workout_place=user_data['workout_place'],
                ai_response=ai_response
            )
            assessment.save()
            
            return render(request, 'assistant/result.html', {
                'assessment': assessment,
                'bmi': assessment.calculate_bmi()
            })
            
        except Exception as e:
            return render(request, 'assistant/index.html', {
                'error': f"Error processing your request: {str(e)}"
            })
    
    return render(request, 'assistant/index.html',{'assessment':FitnessAssessment})

def result(request, assessment_id):
    try:
        assessment = FitnessAssessment.objects.get(id=assessment_id)
        return render(request, 'assistant/result.html', {
            'assessment': assessment,
            'bmi': assessment.calculate_bmi()
        })
    except FitnessAssessment.DoesNotExist:
        return redirect('index')
    
def download_pdf(request, assessment_id):
    try:
        assessment = FitnessAssessment.objects.get(id=assessment_id)
        bmi = assessment.calculate_bmi()
        
        context = {
            'assessment': assessment,
            'bmi': bmi,
            'generated_date': assessment.created_at.strftime("%B %d, %Y"),
        }
        
        pdf = render_to_pdf('assistant/pdf_template.html', context)
        
        if pdf:
            response = HttpResponse(pdf.getvalue(), content_type='application/pdf')
            filename = generate_pdf_filename(assessment)
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
        
        return HttpResponse("Error generating PDF", status=500)
        
    except FitnessAssessment.DoesNotExist:
        return redirect('index')