# Appointment Booking Bot

Simple appointment booking chatbot that uses a Flask backend and a lightweight frontend.

Files
- `chatbackend.py` - Flask app exposing /save_appointment (POST) and /appointments (GET).
- `chatbot.html` - Static frontend that drives a small conversational flow and POSTs appointments to the backend.

Requirements
- Python 3.8+
- MongoDB running locally (default URI used: `mongodb://localhost:27017/appointments_db`)

Quick start (Windows PowerShell)

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Start MongoDB (if not running). Example (if you have MongoDB installed as a service):

```powershell
# Start the MongoDB service
Start-Service mongod
```

4. Run the Flask app:

```powershell
python chatbackend.py
```

5. Open `chatbot.html` in a browser (or serve it via a static file server). The frontend posts to `/save_appointment` relative to the host serving the HTML. If you open the HTML file directly (file://) the fetch will fail due to cross-origin restrictions; run the frontend from a simple static server or place it next to the Flask server and serve via Flask.

Notes
- If MongoDB is on a different URI, set the `MONGO_URI` environment variable or edit `chatbackend.py` app.config before starting.
- Consider adding authentication and validation before using in production.


