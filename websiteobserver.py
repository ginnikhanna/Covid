import requests
class WebsiteObserver:
    def __init__(self):
        pass

    def request_answer(self, url):
        page = requests.get(url)
        return page.status_code

    def request_text(self, url):
        page = requests.get(url)
        text = page.text
        return text


