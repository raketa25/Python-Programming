"""
- This code uses the `requests` library to fetch the HTML content of a webpage and saves it to a file named 'ars-copy.html'. The URL being accessed is an article from Ars Technica about Sam Altman being back as OpenAI CEO. The `requests.get()` function is used to send a GET request to the specified URL, and the response's text content (the HTML of the page) is stored in the variable `page`. Finally, the HTML content is written to a file using a `with` statement to ensure proper file handling.

"""
import requests

page = requests.get('https://arstechnica.com/information-technology/2023/11/sam-altman-officially-back-as-openai-ceo-we-didnt-lose-a-single-employee/').text

print(page)

with open('ars-copy.html', 'w') as file:
  file.write(page)