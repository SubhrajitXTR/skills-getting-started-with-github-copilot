from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_unregister_and_signup():
    # 1. Setup: Register a participant
    # Note: Use an existing activity name from the database
    activity = "Chess Club"
    email = "test@example.com"
    # Using the correct endpoint /activities/{activity_name}/signup
    client.post(f"/activities/{activity}/signup", params={"email": email})
    
    # 2. Test: Unregister existing participant
    # Using /activities/{activity_name}/participants
    response = client.delete(f"/activities/{activity}/participants", params={"email": email})
    print(f"DELETE existing: {response.status_code}")
    assert response.status_code == 200
    
    # 3. Test: Unregister missing participant
    response = client.delete(f"/activities/{activity}/participants", params={"email": email})
    print(f"DELETE missing: {response.status_code}")
    assert response.status_code == 404
    
    # 4. Test: POST signup still works
    response = client.post(f"/activities/{activity}/signup", params={"email": "new@example.com"})
    print(f"POST new: {response.status_code}")
    assert response.status_code == 200

if __name__ == "__main__":
    test_unregister_and_signup()
