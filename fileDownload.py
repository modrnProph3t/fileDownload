import requests

def save_response_body_as_mp3(url, filename, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print("File saved successfully as", filename)
    else:
        print("Failed to retrieve the content")

if __name__ == "__main__":
    url = "https://test.com"  # Replace this with the actual URL
    filename = "audio.mp3"    # Name your file
    
    # Define your custom headers
    custom_headers = {
        "User-Agent": "Custom User Agent",
        "Accept-Language": "en-US,en;q=0.5",
        "Custom-Header-1": "Value1",
        "Custom-Header-2": "Value2",
        "Custom-Header-3": "Value3",
        "Custom-Header-4": "Value4",
        "Custom-Header-5": "Value5",
        "Custom-Header-6": "Value6",
        "Custom-Header-7": "Value7",
        "Custom-Header-8": "Value8",
    }
    
    save_response_body_as_mp3(url, filename, custom_headers)
