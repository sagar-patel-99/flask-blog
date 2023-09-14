import requests

API_URL = "http://127.0.0.1:5000/"
CALLS = 5000

def call_api():
    try:
        response = requests.get(API_URL)
        # You can print the response or handle it as needed
        # print(response.text)
    except requests.RequestException as e:
        # Handle the exception or print an error message
        print(f"An error occurred: {e}")

def main():
    for _ in range(CALLS):
        call_api()
        # Optional: Add a delay between requests
        # time.sleep(0.1)

if __name__ == "__main__":
    main()
