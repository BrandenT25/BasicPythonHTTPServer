import requests
import pytest

url = 'http://localhost:8000'

class TestHTTPserver:

    def test_Home_Page(self):
        response = requests.get(f"{url}/")
        assert response.status_code == 200

    def test_About_Page(self):
        response = requests.get(f"{url}/about")
        assert response.status_code == 200

    def test_Contact_Page(self):
        response = requests.get(f"{url}/contact")
        assert response.status_code == 200

    def test_Metric_Page(self):
        response = requests.get(f"{url}/about")
        assert response.status_code == 200

    def test_Metric_Format(self):
        response = requests.get(f"{url}/metrics")
        assert response.headers['Content-Type'] == "text/plain"

    def test_Metric_Incrementation(self):
        initial = requests.get(f"{url}/metrics")
        initial_num = initial.text
        
        requests.get(f"{url}/metrics")
        
        next_num = (requests.get(f"{url}/metrics")).text
        assert initial_num != next_num

    def test_Concurrent_Users_On_Server(self):
        import concurrent.futures
        def makeRequests():
            return requests.get(f"{url}/")
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executer:
            futures = [executer.submit(makeRequests) for _ in range(10)]
            results = [f.result() for f in futures]
        assert all(r.status_code == 200 for r in results)

    def test_invalid_pages(self):
        response = requests.get(f"{url}/invalid-page")
        assert response.status_code == 404

            
