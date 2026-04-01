import os
import requests
from flask import Flask, request, jsonify, render_template, session
from dotenv import load_dotenv
from google import genai

# Bulletproof .env loading
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=env_path) 

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "space-explorer-secret")
# ... (load_dotenv stuff) ...

# Fetch API keys
NASA_API_KEY = os.getenv("NASA_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the modern Gemini Client
client = genai.Client(api_key=GEMINI_API_KEY)

# --- NASA Tools (From Architecture Diagram) ---

def get_apod(date=None):
    """Fetch Astronomy Picture of the Day."""
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    if date: url += f"&date={date}"
    response = requests.get(url)
    return response.json()

def get_mars_rover_photos(date="2023-01-01", rover="curiosity", camera="navcam"):
    """Fetch Mars Rover photos."""
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?earth_date={date}&camera={camera}&api_key={NASA_API_KEY}"
    response = requests.get(url)
    return response.json()

def explain_science(title, description):
    """Reasoning Engine: Student-friendly explanations."""
    prompt = f"Explain the science of '{title}' for a student using plain English: {description}"
    try:
        response = client.models.generate_content(
            model='gemini-3.1-flash-lite-preview', # Latest stable for 2026
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Mission Control error: {str(e)}"

# --- Routes ---

@app.route('/')
def home():
    """Serves the frontend. REQUIRES a 'templates' folder."""
    return render_template('index.html')

@app.route('/api/ask', methods=['POST'])
def ask_agent():
    data = request.json
    user_query = data.get('query', '').lower()
    
    # Simple tool routing logic
    if any(word in user_query for word in ["today", "apod", "picture"]):
        nasa_data = get_apod()
        if 'error' in nasa_data:
            return jsonify({"error": "NASA uplink failed."})
            
        explanation = explain_science(nasa_data.get('title'), nasa_data.get('explanation'))
        
        # Track session state as per diagram
        session['last_topic'] = nasa_data.get('title')
        
        return jsonify({
            "title": nasa_data.get('title'),
            "image_url": nasa_data.get('url'),
            "explanation": explanation,
            "media_type": nasa_data.get('media_type', 'image')
        })
    
    elif "mars" in user_query:
        # Mars Rover logic
        mars_data = get_mars_rover_photos()
        if not mars_data.get('photos'):
            return jsonify({"explanation": "No Mars photos found for this date."})
        
        photo = mars_data['photos'][0]
        return jsonify({
            "title": f"Mars through the eyes of {photo['rover']['name']}",
            "image_url": photo['img_src'],
            "explanation": "This is a direct raw image from the Martian surface.",
            "media_type": "image"
        })

    return jsonify({"explanation": "I'm ready! Ask about 'today's picture' or 'Mars photos'."})

if __name__ == '__main__':
    app.run(debug=True)
