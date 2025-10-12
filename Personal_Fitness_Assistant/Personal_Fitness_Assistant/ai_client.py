import google.generativeai as genai
import os
from decouple import config
import time
import markdown2
from markdown_it import MarkdownIt

class GeminiClient:
    def __init__(self):
        self.api_key = config('GEMINI_API_KEY')
        genai.configure(api_key=self.api_key)
        
        # Use a balanced model - gemini-2.5-flash-lite is free and fast
        self.model = genai.GenerativeModel('gemini-2.5-flash-lite')
    
    def generate_fitness_plan(self, user_data):
        prompt = self._build_prompt(user_data)
        
        try:
            
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    top_p=0.8,
                    top_k=40,
                    max_output_tokens=2000,
                )
            )
            
            return self._format_response(response.text)
            
        except Exception as e:
            return f"❌ **Error generating fitness plan**: {str(e)}\n\nPlease try again in a moment."
    
    def _build_prompt(self, user_data):
        food_pref_text = f"Food Preference: {user_data['food_preference']}" if user_data.get('food_preference') and user_data['food_preference'] != 'ANY' else "Food Preference: No specific preference"
        workout_place_text = f"Workout Location Preference: {user_data['workout_place']}" if user_data.get('workout_place') and user_data['workout_place'] != 'ANY' else "Workout Location: No specific preference"
        
        return f"""
        You are a professional fitness and nutrition expert. Create a comprehensive, balanced fitness and nutrition plan.

        USER INFORMATION:
        - Gender: {user_data['gender']}
        - Age: {user_data['age']} years
        - Weight: {user_data['weight']} kg
        - Height: {user_data['height']} cm
        - Waist Circumference: {user_data['waist_circumference']} cm
        - {food_pref_text}
        - {workout_place_text}
        - Health Goal: {user_data['health_goal']}
        - Duration: {user_data.get('duration', 'Not specified')} weeks

        CREATE A BALANCED PLAN WITH THESE SECTIONS:

        🎯 **Goal Overview & Timeline**
        [Provide realistic expectations and main focus areas]

        📊 **Health Metrics & Target**
        [Calculate BMI, suggest healthy weight range, set measurable targets]

        🍽️ **Personalized Nutrition Plan**
        - Daily Calorie Target: [Calculate based on goals]
        - Macronutrient Breakdown: [Carbs/Protein/Fat percentages]
        - Sample Daily Meal Plan (adjust for food preferences):
          * Breakfast: [Specific foods with portions]
          * Lunch: [Specific foods with portions]
          * Dinner: [Specific foods with portions]
          * Snacks: [Healthy options]

        💪 **Weekly Exercise Routine**
        [Create balanced workout schedule considering location preference]
        - Include: Cardio, Strength Training, Flexibility
        - Specify: Exercises, Sets, Reps, Duration
        - Rest days included

        📈 **Progress Tracking**
        [Weekly checkpoints and metrics to track]

        ⚠️ **Important Health Notes**
        [Safety precautions and when to consult healthcare provider]

        GUIDELINES:
        - Be realistic and sustainable
        - Focus on balanced nutrition
        - Include both cardio and strength training
        - Consider the user's preferences and limitations
        - Emphasize consistency over intensity
        - Include hydration and sleep recommendations
        """
    
    def _format_response(self, response):
        # Enhance formatting for better display
        md = MarkdownIt()
        formatted = markdown2.markdown(response)
        
        return formatted