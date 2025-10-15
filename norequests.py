# norequests.py

class NoRequests:
    def get(self, url):
        return "No response from {url}".format(url=url)

    def post(self, url, data):
        return "No response from {url} with data {data}".format(url=url, data=data)

# Example usage
if __name__ == '__main__':
    client = NoRequests()
    print(client.get('http://example.com'))
    print(client.post('http://example.com', {'key': 'value'}))
