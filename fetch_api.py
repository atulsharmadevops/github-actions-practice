import requests #Loads the Requests library to make HTTP calls (GET/POST).
import json #Provides tools to convert Python data to/from JSON.

def fetch_api_data():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()
    except Exception as e:
        print("API request failed: ",e)
        return
    
    try:
        users = response.json()
    except Exception as e:
        print("Error reading JSON: ",e)
        return

    processed_data = []
    for user in users[:5]:
        processed_data.append({
            "id": user["id"],
            "name" : user["name"],
            "email" : user["email"],
            "city" : user["address"]["city"],
            "company" : user["company"]["name"]
        })

    print("---Processed API Data---")
    for item in processed_data:
        print(f"ID: {item['id']} | Name: {item['name']} | Email: {item['email']} | City: {item['city']} | Company: {item['company']}")

    try:
        with open("output.json", "w") as f:
            json.dump(processed_data, f, indent=4)
        print("\nData saved to output.json")
    except Exception as e:
        print("Error saving file: ",e)

fetch_api_data()
