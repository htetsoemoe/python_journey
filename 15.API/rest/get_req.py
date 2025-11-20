import requests

import json     # for working with JSON data (requests often handles this automatically)

def get_random_joke():
    """Function to get a random joke from the Joke API"""
    api_url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=racist,sexist&type=single"

    print(f"Sending API Request to: {api_url}")

    try:
        # Send a GET Request
        response = requests.get(api_url)

        # Check the HTTP Status Code (200 means success)
        if response.status_code == 200:
            # Convert the JSON Response to a Python Dictionary
            joke_data = response.json()

            # Check the joke type and display it
            if joke_data['type'] == 'single':
                print("\n--- Joke ---")
                print(joke_data['joke'])
            elif joke_data['type'] == 'twopart':
                print("\n--- Joke ---")
                print(joke_data['setup'])
                print(joke_data['delivery'])
            else:
                print("Unknown joke type.")
        elif response.status_code == 404:
            print("Error: API Endpoint not found.")
        else:
            print(f"API Request failed. Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")

    except requests.exceptions.ConnectionError:
        print("Network Connection Error: No internet connection or API Server is down.")
    except requests.exceptions.Timeout:
        print("Request Timeout: API Server did not respond in time.")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except json.JSONDecodeError:
        print("JSON Parsing Error: API Response is not in JSON format.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# Call the function to test
get_random_joke()