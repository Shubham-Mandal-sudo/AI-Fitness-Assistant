# AI Fitness Assistant - Internship Project

## Project Overview
A Django web application that generates personalized fitness and nutrition plans using AI. Users input their health metrics and preferences, and the app creates customized diet and exercise routines through local AI integration.

## Features Implemented
- ✅ User input form for personal health data
- ✅ Food preference selection (Indian, American, Mexican, etc.)
- ✅ Workout location preference (Home, Gym, Park)
- ✅ AI integration with LMStudio for plan generation
- ✅ PDF report download functionality
- ✅ Responsive, clean UI with loading animations
- ✅ Form validation and error handling

## Tech Stack
- **Backend**: Django 4.2.7
- **Frontend**: HTML, CSS, JavaScript
- **AI**: LMStudio Local API
- **PDF Generation**: xhtml2pdf
- **Database**: SQLite

## Project Structure
```
fitness_assistant/
├── fitness_app/          # Django project settings
├── assistant/           # Main application
├── templates/          # HTML templates
├── static/            # CSS and JavaScript
└── requirements.txt   # Dependencies
```

## Setup Instructions

### 1. Prerequisites
- Python 3.8+
- LMStudio installed and running on port 1234

### 2. Installation
```bash
# Clone repository
git clone <repository-url>
cd ai-fitness-assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

### 3. LMStudio Setup
1. Install LMStudio from https://lmstudio.ai/
2. Load a suitable model (7B+ parameters recommended)
3. Start local server on port 1234
4. Ensure API is accessible at `http://localhost:1234/v1`

## Key Components

### Models (`assistant/models.py`)
- `FitnessAssessment`: Stores user data and AI responses
- Fields: personal info, preferences, goals, timestamps

### Views (`assistant/views.py`)
- `index()`: Handles form submission and AI processing
- `result()`: Displays generated fitness plan
- `download_pdf()`: Generates PDF report

### AI Integration (`fitness_app/ai_client.py`)
- `LMStudioClient`: Manages API communication
- Custom prompts for fitness plan generation
- Error handling for API connectivity

### Templates
- `index.html`: User input form
- `result.html`: Plan display with PDF download
- `pdf_template.html`: PDF report layout

## What I Learned
- Django form handling and model management
- API integration with local AI services
- PDF generation in web applications
- Frontend development with CSS animations
- Error handling and user experience design

## Challenges & Solutions
1. **AI Response Formatting**: Implemented custom formatting for consistent output
2. **PDF Generation**: Used xhtml2pdf with custom CSS for styling
3. **Loading States**: Created overlay loader for better UX during AI processing
4. **Form Validation**: Added client and server-side validation

## Future Improvements
- [ ] User authentication and history
- [ ] Progress tracking over time
- [ ] More AI model options
- [ ] Exercise demonstration videos
- [ ] Meal plan shopping lists

## Notes for Mentor
- The app currently uses SQLite for simplicity (can be switched to PostgreSQL)
- LMStudio must be running locally for AI features to work
- Form includes comprehensive validation
- Error handling implemented for API failures
- UI is fully responsive for mobile devices

## Running the Project
1. Start LMStudio with a loaded model
2. Run `python manage.py runserver`
3. Navigate to `http://localhost:8000`
4. Fill out the form and generate a fitness plan

---
*Internship Project - Shubham Mandal*
*shubhammandal205@gmail.com*
