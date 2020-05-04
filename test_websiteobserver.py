import unittest
import websiteobserver

class WebsiteObserverShould(unittest.TestCase):
    def test_if_page_is_alive(self):
        w = websiteobserver.WebsiteObserver()
        url = 'http://web.archive.org/web/20200318095552/https://www.worldometers.info/coronavirus/'
        self.assertEqual(w.request_answer(url), 200)

    def test_if_page_has_text(self):
        w = websiteobserver.WebsiteObserver()
        url = 'http://web.archive.org/web/20200318095552/https://www.worldometers.info/coronavirus/'
        self.assertNotEqual(w.request_text(url), '')

if __name__ == '__main__':
    unittest.main()
