from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Terminal log-la kedaicha correct endpoint
ENDEE_URL = "http://127.0.0.1:8080/api/v1/index/incidents/search"

@app.route('/search', methods=['POST'])
def career_search():
    try:
        data = request.json
        user_query = data.get('query', '')
        
        print(f"DEBUG: Processing request for: {user_query}")

        # Terminal-la 'k' missing-nu vandhadhaala, 'top_k' replace panroam
        payload = {
            "query": user_query,
            "k": 1,
            "include_metadata": True
        }

        # POST request to Endee
        response = requests.post(ENDEE_URL, json=payload, timeout=5)
        print(f"DEBUG: Endee Response Code: {response.status_code}")

        if response.status_code == 200:
            res_data = response.json()
            # Endee response structure-ah safe-aa handle panroam
            results = res_data.get("results") or res_data.get("matches", [])

            if results:
                meta = results[0].get("metadata", {})
                return jsonify({
                    "status": "success",
                    "results": [{
                        "role": meta.get("role") or meta.get("Role") or "Career Match Found",
                        "path": meta.get("path") or meta.get("Path") or "Skills loading...",
                        "brief": meta.get("brief") or meta.get("Brief") or "Description found in database."
                    }]
                })


    except Exception as e:
        print(f"CRITICAL ERROR: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
