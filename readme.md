# AI Fitness Assistant - Internship Project

## Project Overview
A Django web application that generates personalized fitness and nutrition plans using Google's Gemini AI. Users input their health metrics and preferences, and the app creates customized diet and exercise routines through AI integration.

## Features Implemented
- ✅ User input form for personal health data
- ✅ Food preference selection (Indian, American, Mexican, etc.)
- ✅ Workout location preference (Home, Gym, Park)
- ✅ Google Gemini AI integration for plan generation
- ✅ PDF report download functionality
- ✅ Responsive, clean UI with loading animations
- ✅ Form validation and error handling
- ✅ Rate limiting to respect API quotas
- ✅ PythonAnywhere deployment ready

## Tech Stack
- **Backend**: Django 4.2.7
- **Frontend**: HTML, CSS, JavaScript
- **AI**: Google Gemini API (gemini-1.5-flash)
- **PDF Generation**: xhtml2pdf + ReportLab
- **Database**: SQLite
- **Static Files**: WhiteNoise for serving
- **Environment**: python-dotenv

## Project Structure
```
AI-Fitness-Assistant/
├── Personal_Fitness_Assistant/
│   ├── manage.py
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── fitness_app/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── ai_client.py
│   ├── assistant/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   └── templates/
│   └── requirements.txt
└── .env
```

## Setup Instructions

### 1. Prerequisites
- Python 3.8+
- Google Gemini API key (free from Google AI Studio)

### 2. Local Development Installation
```bash
# Clone repository
git clone <repository-url>
cd AI-Fitness-Assistant/Personal_Fitness_Assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env
# Edit .env with your API key and secret key

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Start development server
python manage.py runserver
```

### 3. Gemini API Setup
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with Google account
3. Generate an API key
4. Add to your `.env` file:
```
GEMINI_API_KEY=your_actual_api_key_here
SECRET_KEY=your-django-secret-key
DEBUG=True
```

## Deployment on PythonAnywhere

### 1. Prepare Project for Deployment
```bash
# Ensure DEBUG is False in production
# Collect static files
python manage.py collectstatic

# Test locally
python manage.py runserver
```

### 2. PythonAnywhere Setup
1. **Sign up** at [pythonanywhere.com](https://www.pythonanywhere.com/)

2. **Upload Project**:
   - Open bash console
   - Clone your Git repository or upload files
   - Or use: `git clone https://github.com/yourusername/ai-fitness-assistant.git`

3. **Setup Virtual Environment**:
```bash
cd ai-fitness-assistant/Personal_Fitness_Assistant
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. **Environment Variables**:
   - Add in WSGI file or PythonAnywhere Web App environment variables:
```python
import os
os.environ['SECRET_KEY'] = 'your-secret-key'
os.environ['DEBUG'] = 'False'
os.environ['GEMINI_API_KEY'] = 'your-gemini-api-key'
```

5. **Web App Configuration**:
   - Go to Web tab → Add a new web app
   - Manual configuration → Python 3.10
   - Virtualenv: `/home/username/ai-fitness-assistant/Personal_Fitness_Assistant/venv`
   - Source code: `/home/username/ai-fitness-assistant/Personal_Fitness_Assistant`

6. **WSGI Configuration**:
```python
import os
import sys

path = '/home/username/ai-fitness-assistant/Personal_Fitness_Assistant'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'fitness_app.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

7. **Static Files Configuration**:
   - In Web tab → Static files:
   - URL: `/static/`
   - Directory: `/home/username/ai-fitness-assistant/Personal_Fitness_Assistant/staticfiles`

8. **Final Steps**:
```bash
# Run migrations
python manage.py migrate

# Reload web app
```
Visit: `yourusername.pythonanywhere.com`

## Key Components

### AI Integration (`fitness_app/ai_client.py`)
- `GeminiClient`: Manages Google Gemini API communication
- Smart rate limiting without CPU blocking
- Error handling for API limits and connectivity issues
- Structured prompts for balanced fitness plans

### Models (`assistant/models.py`)
- `FitnessAssessment`: Stores user data, preferences, and AI responses
- Food preferences: Indian, American, Mexican, Vegetarian, etc.
- Workout locations: Home, Gym, Park, etc.

### Views (`assistant/views.py`)
- `index()`: Form handling and AI processing
- `result()`: Display generated fitness plans
- `download_pdf()`: PDF report generation

### Features
- **Non-blocking loader**: Smooth UX during AI processing
- **PDF export**: Professional report generation
- **Responsive design**: Works on mobile and desktop
- **Rate limiting**: Respects Gemini API quotas (60 requests/minute)
- **Error handling**: User-friendly error messages

## API Rate Limiting
The app implements smart rate limiting:
- Uses Django cache for request tracking
- No CPU-blocking sleep calls
- User-friendly messages when limits approached
- Respects Gemini free tier limits (60 RPM)

## Environment Variables
Create `.env` file:
```env
SECRET_KEY=your-django-secret-key
DEBUG=False
GEMINI_API_KEY=your-gemini-api-key-from-google-ai-studio
```

## What I Learned
- Django deployment on PythonAnywhere
- Google Gemini API integration
- Static file management in production
- Rate limiting implementation
- PDF generation in web applications
- Environment-based configuration
- Error handling for external APIs

## Challenges & Solutions
1. **API Rate Limiting**: Implemented cache-based limiting without blocking
2. **Static Files**: Configured WhiteNoise for efficient static file serving
3. **PDF Generation**: Used xhtml2pdf with custom templates
4. **Deployment**: Adapted settings for PythonAnywhere environment

## Notes for Mentor
- Uses free Google Gemini API (60 requests/minute limit)
- SQLite database (can upgrade to PostgreSQL if needed)
- All environment variables properly configured
- Static files correctly set up for production
- Rate limiting implemented to avoid API quota issues
- Error handling for common deployment scenarios

## Testing the Deployment
1. Visit your PythonAnywhere URL
2. Fill out the fitness assessment form
3. Verify AI plan generation works
4. Test PDF download functionality
5. Check responsive design on mobile

## Troubleshooting
- **Static files not loading**: Run `collectstatic` and check PythonAnywhere static config
- **API errors**: Verify Gemini API key in environment variables
- **Database issues**: Run migrations in PythonAnywhere console
- **Import errors**: Check virtual environment and requirements

---
*Internship Project - Shubham Mandal*