import requests
import json

def get_github_user_data(username):
    """Function to get a user's profile data from the GitHub API"""
    api_url = f"https://api.github.com/users/{username}"

    print(f"\nSending GitHub API Request to: {api_url}")

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            user_data = response.json()
            print("\n--- GitHub User Profile ---")
            print(f"Name: {user_data.get('name', 'N/A')}")
            print(f"Username: {user_data.get('login', 'N/A')}")
            print(f"Followers: {user_data.get('followers', 'N/A')}")
            print(f"Following: {user_data.get('following', 'N/A')}")
            print(f"Public Repos: {user_data.get('public_repos', 'N/A')}")
            print(f"Location: {user_data.get('location', 'N/A')}")
            print(f"Bio: {user_data.get('bio', 'N/A')}")
        elif response.status_code == 404:
            print(f"Error: GitHub User '{username}' not found.")
        else:
            print(f"GitHub API Request failed. Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")

# Call the function to test
# get_github_user_data("octocat")
# GitHub's Demo User
get_github_user_data("realpython")


# get_github_user_data("nonexistentuser12345")
# Test a non-existent user