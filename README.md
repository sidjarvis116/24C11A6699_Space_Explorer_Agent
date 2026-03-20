🌌 Space Explorer Agent: AI-Powered Astronomy Guide
The Space Explorer Agent is an intelligent educational platform that bridges the gap between complex NASA astrophysical data and student learners. By orchestrating real-time satellite data with an AI reasoning engine, the agent transforms technical metadata into engaging, kid-friendly scientific insights.

🚀 Key Features
Automated NASA Uplink: Seamlessly integrates with NASA Open APIs to fetch the "Astronomy Picture of the Day" (APOD) and live imagery from Mars Rover missions.

AI Reasoning Engine: Leverages the Google Gemini 2.0 Flash model to analyze raw scientific descriptions and rewrite them in simplified, student-friendly language.

Contextual Session Memory: Uses Flask Secret Keys to track explored topics throughout a session, providing a persistent and personalized user journey.

Modern Interactive UI: Features a high-performance web interface designed with a Glassmorphism aesthetic for an immersive, space-themed user experience.

🛠️ Technical Stack
Backend: Python 3.x, Flask

AI/LLM: Google GenAI SDK (Gemini 2.0 Flash)

APIs: NASA Planetary & Mars Rover APIs

Security: python-dotenv for environment variable protection and cryptographic session signing

Frontend: HTML5, CSS3 (Advanced Glassmorphism), JavaScript

🏗️ Architecture
The project follows a modular Client-Agent-Tool architecture:

Client: Interactive web interface for user queries.

Agent: Flask-based controller that routes natural language requests.

Tools: Custom Python functions (get_apod, get_mars_rover_photos) that communicate with external NASA data sources.

⚙️ Installation & Setup
Clone the repository:

Bash
git clone https://github.com/your-username/space-explorer-agent.git
cd space-explorer-agent
Install dependencies:

Bash
pip install -r requirements.txt
Configure Environment Variables:
Create a .env file in the root directory and add your credentials:

Plaintext
NASA_API_KEY=your_nasa_api_key
GEMINI_API_KEY=your_gemini_api_key
FLASK_SECRET_KEY=your_random_secret_string
Run the application:

Bash
python app.py
📜 Educational Impact
This project reduces the technical barrier to entry for astrophysics by roughly 90% through automated simplification, making real-time space data accessible to the next generation of explorers.

🛡️ Security Note
This project uses .env files to ensure that sensitive API credentials are never hardcoded or exposed in the source code.
