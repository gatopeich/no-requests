# no-requests

A lightweight, safe, dependency-free HTTP client for Python 3, inspired by `requests`, but with no dependencies outside the standard library.

## Features

- Only the most-used API: `get`, `post`, `put`, `delete`
- No dependencies outside Python 3 standard library
- Default timeout is 9 seconds
- Warns (but does not fail) on non-SSL (non-HTTPS) requests
- Simple `Response` object with `.status_code`, `.headers`, `.url`, `.content`, `.text`, `.json()`

## Usage

```python
import norequests as requests

resp = requests.get('https://httpbin.org/get')
print(resp.status_code)
print(resp.json())
```

## License

MIT
