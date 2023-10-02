import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage you want to scrape
url = 'https://ramjeetsingh.github.io/Drum-Kit/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Define a function to print the element type and its content
    def print_element_type_and_content(element):
        element_type = element.name  # Get the HTML tag name
        element_content = element.get_text()  # Get the text content within the element
        print(f"Element Type: {element_type}")
        print(f"Element Content: {element_content}")
        print("\n")

    # Find all HTML elements in the soup and print their type and content
    all_elements = soup.find_all()
    for element in all_elements:
        print_element_type_and_content(element)
else:
    print('Failed to retrieve the webpage')
