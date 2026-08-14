import requests
import json

BASE_URL = "http://127.0.0.1:8000"

print("--- 🎓 PROFESSOR LIVE CONTROL DASHBOARD SIMULATOR ---")

# --- SIMULATING PROFESSOR CLICKING START ACTIVATION WINDOW ---
print("\n[ACTION] Professor triggers single-click interface parameters switch activation loop...")

professor_payload_url = f"{BASE_URL}/api/v1/professor/create-session?classroom_id=ROOM-LH302&professor_id=PROF-STAFF-409"

try:
    response = requests.post(professor_payload_url)
    result_data = response.json()
    
    print(f"Server Response Status Code: {response.status_code}")
    print("\n--- ⏱️ LIVE COUNTDOWN MONITOR GRIDS ---")
    print(json.dumps(result_data, indent=4))
    
except Exception as network_error:
    print(f"Connection Failed: Please ensure your local FastAPI uvicorn server engine is actively running! Error: {network_error}")
