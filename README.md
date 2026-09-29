# 📚 AI Study Assistant

An AI-powered study tool that generates concept explanations, structured notes, and quizzes using the Google Gemini API. Built as a simple, focused project to explore prompt engineering and AI-integrated web apps.

🔗 **Live Demo:** https://ai-study-assistant-ecpo.onrender.com

## Features

- **Concept Explanation** – explains any topic at a beginner, intermediate, or advanced level, with a simple analogy
- **Notes Generation** – turns pasted text (or an uploaded `.txt` file) into structured notes with headings and bullet points
- **Quiz Generation** – creates multiple-choice quizzes on any topic, with instant grading and explanations
- **Prompt Library** – all AI prompts are stored as reusable templates in `prompts.py`, separated from app logic

## Tech Stack

- **Language:** Python
- **Frontend/App:** Streamlit
- **AI Model:** Google Gemini API (`google-genai`)
- **Other:** python-dotenv (for environment variables)

  
## Run It Locally

1. Clone this repository:
git clone https://github.com/GoliSravani0306/ai-study-assistant.git
cd ai-study-assistant


2. Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # Mac/Linux


3. Install dependencies:

pip install -r requirements.txt


4. Add your Gemini API key:
   - Create a `.env` file in the project root
   - Add this line: `GEMINI_API_KEY=your_key_here`
   - Get a free key at [Google AI Studio](https://aistudio.google.com/apikey)

5. Run the app:

streamlit run app.py


## Project Structure

ai-study-assistant/
├── app.py # Streamlit UI and feature logic
├── gemini_helper.py # Gemini API connection and JSON parsing
├── prompts.py # Prompt Library — reusable prompt templates
├── requirements.txt
└── README.md


## Author

**Sravani Goli**
