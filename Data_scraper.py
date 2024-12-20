import requests
import pandas as pd
import time

# Replace with your actual API key
api_key = "AIzaSyBRrYsvEEAapuiR9KMLs3g-6wv4gAoJr_Q"

# Function to fetch Google Places data
def get_places_data(query, num_results=40):
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    details_url = "https://maps.googleapis.com/maps/api/place/details/json?"
    places = []
    
    try:
        # Send request to Google Places API
        response = requests.get(f"{base_url}query={query}&key={api_key}")
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        results = response.json().get("results", [])
        
        # Extract the required details from the first batch of results
        while len(places) < num_results:
            # Process the current results
            for result in results:
                place_id = result.get("place_id")
                name = result.get("name", "N/A")
                address = result.get("formatted_address", "N/A")
                rating = result.get("rating", "N/A")
                
                # Fetch additional details using Place Details API
                details_response = requests.get(f"{details_url}place_id={place_id}&key={api_key}")
                details_response.raise_for_status()
                details = details_response.json().get("result", {})
                
                phone_number = details.get("formatted_phone_number", "N/A")
                website = details.get("website", "N/A")
                
                # Get the type or industry (type of business)
                types = details.get("types", [])
                industry = ", ".join(types) if types else "N/A"
                
                places.append({
                    "Name": name,
                    "Address": address,
                    "Rating": rating,
                    "Phone Number": phone_number,
                    "Website": website,
                    "Industry": industry 
                })
            
            # Check if there are more pages of results
            next_page_token = response.json().get("next_page_token")
            if next_page_token and len(places) < num_results:
                # Wait before sending the next request due to API rate limits
                time.sleep(2)
                response = requests.get(f"{base_url}query={query}&key={api_key}&pagetoken={next_page_token}")
                response.raise_for_status()
                results = response.json().get("results", [])
            else:
                break

    except requests.exceptions.RequestException as e:
        print(f"Error during the request: {e}")
    
    return pd.DataFrame(places)

# Query for businesses
query = "restaurants in Mumbai"  # Replace with your search query
data = get_places_data(query, num_results=40)

# Data cleaning (e.g., remove duplicates, handle missing values)
data.drop_duplicates(subset=["Name", "Address"], inplace=True)
data.fillna("N/A", inplace=True)

# Save results to a CSV on your desktop
data.to_csv(r"C:\Users\tripa\OneDrive\Desktop\Data science\google_business_results.csv", index=False)
print(f"Data saved to google_business_results.csv with {len(data)} entries.")