import requests
import base64

# Define the URL of the endpoint
url = "http://localhost:80/process-pano"

# Read the image file and encode it in base64
with open("C:/Users/colin/Downloads/demo4/@391092.52@5819576.17@33@U@52.51541@13.39505@284@@325.56@90.00@0.00@52.58@@art_prob_0.0000@.jpg", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Prepare the JSON payload
# payload = {
#     "image_path": "C:/Users/colin/Downloads/demo4/@391092.52@5819576.17@33@U@52.51541@13.39505@284@@325.56@90.00@0.00@52.58@@art_prob_0.0000@.jpg",
#     "image": encoded_image,
#     "dataset_name": "Test"
# }

# # Send the POST request
# response = requests.post(url, json=payload)

# # Print the response from the server
# print(response.status_code)
# print(response.json())

url = "http://localhost:80/search-image"

# Prepare the JSON payload
payload = {
    "image": encoded_image,
    "limit": 5,  # Set the limit for the number of results you want
    "offset": 0,  # Set the offset if needed
    "dataset_names": ["Test"]  # Replace with your actual dataset names
}

# Send the POST request
response = requests.post(url, json=payload)

# Print the response from the server
print(response.status_code)
print(response.json())
