import requests

while True:
    url= input("Enter the correct url of the site you want to scrape(q to quit): ")
    if url == 'q':
        break
    elif url == 'Q':
        break
    responses = requests.get(url)

    print(responses.text)