import requests

BASE_URL = "http://127.0.0.1:8080"
INDEX_NAME = "incidents"

def discover_endpoint():
    print("--- Searching for the correct API Route ---")
    
    # Intha 3 paths-la ethavathu onnu kandippa JSON tharum
    test_paths = [
        f"/api/v1/index/{INDEX_NAME}/search",
        f"/api/v1/search/{INDEX_NAME}",
        f"/api/v1/index/{INDEX_NAME}/vector/search"
    ]
    
    for path in test_paths:
        url = f"{BASE_URL}{path}"
        try:
            # Simple GET request without complex vectors first
            res = requests.get(url, params={"top_k": 1}, timeout=5)
            content_type = res.headers.get('Content-Type', '')
            
            print(f"Testing {path} -> Status: {res.status_code} | Type: {content_type}")
            
            # JSON response vandha adhu thaan namma endpoint
            if "application/json" in content_type:
                print(f"FOUND IT! Correct API Path: {path}")
                print(f"Response: {res.text[:100]}")
                return path
        except:
            continue
    
    print("\nNo JSON endpoint found. Dashboard-la 'Search' click pannumpothu URL bar-la enna irukkunu check pannunga.")

if __name__ == "__main__":
    discover_endpoint()