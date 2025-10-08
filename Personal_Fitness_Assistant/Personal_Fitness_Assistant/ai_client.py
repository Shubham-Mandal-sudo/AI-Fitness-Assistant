import requests
import json
import re
import markdown2
from markdown_it import MarkdownIt

class LMStudioClient:
    def __init__(self, base_url="http://localhost:1234/v1"):
        self.base_url = base_url
        self.chat_completions_url = f"{base_url}/chat/completions"
    
    def generate_fitness_plan(self, user_data):
        prompt = self._build_prompt(user_data)
        
        messages = [
            {
                "role": "system",
                "content": """You are a professional fitness and nutrition expert. Provide detailed, personalized diet and exercise plans based on user information.

IMPORTANT FORMATTING INSTRUCTIONS:
- Use clear section headers with emojis
- Use bullet points for lists
- Make it visually appealing and easy to read
- Do not use tables
- Reduce spaces between line
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
        
        payload = {
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 2500,
            "stream": False
        }
        
        try:
            response = requests.post(
                self.chat_completions_url,
                headers={"Content-Type": "application/json"},
                json=payload,
                timeout=600
            )
            response.raise_for_status()
            
            result = response.json()
            return self._format_response(result['choices'][0]['message']['content'])
            
        except requests.exceptions.RequestException as e:
            return f"❌ **Error connecting to AI service**: {str(e)}\n\nPlease make sure LMStudio is running on localhost:1234"
        except Exception as e:
            return f"❌ **Error generating fitness plan**: {str(e)}"
    
    def _build_prompt(self, user_data):
        food_pref_text = f"Food Preference: {user_data['food_preference']}" if user_data.get('food_preference') and user_data['food_preference'] != 'ANY' else "Food Preference: No specific preference"
        workout_place_text = f"Workout Location Preference: {user_data['workout_place']}" if user_data.get('workout_place') and user_data['workout_place'] != 'ANY' else "Workout Location: No specific preference"
        
        return f"""
        Create a comprehensive fitness and nutrition plan for the following user:
        
        **Personal Information:**
        - Gender: {user_data['gender']}
        - Age: {user_data['age']} years
        - Weight: {user_data['weight']} kg
        - Height: {user_data['height']} cm
        - Waist Circumference: {user_data['waist_circumference']} cm
        
        **Preferences:**
        - Food: {food_pref_text}
        - Workout place: {workout_place_text}
        
        **Health Goal:** {user_data['health_goal']}
        **Duration:** {user_data.get('duration', 'Not specified')} weeks
        
        Please provide a detailed plan including:
        
        🎯 **Goal Overview** - Summary of the plan
        📊 **Health Metrics Analysis** - Analysis of current metrics and targets
        🍽️ **Personalized Diet Plan** - Daily meal plan with specific foods and portions
        💪 **Exercise Routine** - Weekly workout schedule with specific exercises
        📈 **Progress Tracking** - How to monitor progress
        ⚠️ **Important Notes** - Health considerations and tips
        
        Make the plan realistic, sustainable, and tailored to the user's specific metrics, goals, and preferences.
        """
    
    def _format_response(self, response):
        # Enhance formatting for better display
        md = MarkdownIt()
        formatted = markdown2.markdown(response)
        
        return formatted