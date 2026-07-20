```
BaseException
└── Exception
    └── RequestException
        ├── HTTPError
        ├── ConnectionError
        │   ├── ProxyError
        │   └── SSLError
        ├── Timeout
        │   ├── ConnectTimeout
        │   └── ReadTimeout
        ├── TooManyRedirects
        ├── URLRequired
        ├── InvalidURL
        ├── MissingSchema
        ├── InvalidSchema
        ├── InvalidHeader
        ├── ChunkedEncodingError
        ├── ContentDecodingError
        ├── StreamConsumedError
        ├── RetryError
        └── UnrewindableBodyError
```

RequestException is the parent class of all requests exceptions.

## 1. RequestException

The base exception for all exceptions raised by requests.

**When does it occur?**

Whenever any request-related error occurs.

**Example**

```python
import requests

try:
    requests.get("https://example.com")
except requests.RequestException as e:
    print(e)
```

**When to use?**

Use it as the last except block to catch everything.

## 2. HTTPError

Raised when an HTTP request returns an error status code after calling raise_for_status().

Important: A 404 or 500 does NOT automatically raise an exception.

```python
response = requests.get(url)
print(response.status_code)    # 404

# No exception yet

response.raise_for_status()    # Now HTTPError is raised
```

**Example**

```python
import requests

try:
    response = requests.get("https://httpbin.org/status/404")
    response.raise_for_status()

except requests.HTTPError as e:
    print(e)
```

**Output**

```
404 Client Error: Not Found
```

Use when you want to treat HTTP errors separately.

## 3. Timeout

Raised when the request exceeds the timeout value.

```python
requests.get(url, timeout=5)
```

If the request takes longer than 5 seconds, `Timeout` will be raised.

**Example**

```python
try:
    requests.get(url, timeout=1)

except requests.Timeout:
    print("Request timed out")
```

Think of it as

> "I waited too long."

## 4. ConnectTimeout

A subclass of Timeout.

Occurs while connecting to the server.

```
Your Computer
      |
      |  (trying...)
      |
Internet
      |
Server
```

The connection itself never gets established.

**Example**

```python
try:
    requests.get(url, timeout=(2, 10))
except requests.ConnectTimeout:
    print("Couldn't connect")
```

Usually caused by

- server offline
- firewall
- blocked IP
- network issues

## 5. ReadTimeout

Connection succeeds.

```
Computer  --------> Server
            Connected ✔
```

But the server never sends data back.

```
Waiting...
Waiting...
Waiting...
Timeout
```

**Example**

```python
try:
    requests.get(url, timeout=(5,2))
except requests.ReadTimeout:
    print("Server is too slow")
```

**Difference**

```
ConnectTimeout
↓
Cannot connect


ReadTimeout
↓
Connected
↓
Waiting for response
↓
Timeout
```

## 6. ConnectionError

Raised when a connection cannot be made.

Examples

- No Internet
- DNS failed
- Connection refused
- Host unreachable

```python
try:
    requests.get("https://abcxyz123456.com")

except requests.ConnectionError:
    print("Connection failed")
```

Think of

> No road to the destination.

## 7. ProxyError

Occurs when using a proxy server.

```
Computer
   |
Proxy
   X
Internet
```

The proxy fails.

**Example**

```python
proxies = {
    "https": "http://wrongproxy:8080"
}

requests.get(url, proxies=proxies)
```

**Result**

```
ProxyError
```

## 8. SSLError

Occurs when SSL/TLS verification fails.

**Example**

```python
requests.get("https://expired.badssl.com/")
```

Possible reasons

- expired certificate
- invalid certificate
- certificate mismatch

**Example**

```python
except requests.SSLError:
    print("SSL verification failed")
```

## 9. TooManyRedirects

Suppose

```
A -> B
B -> C
C -> A
```

This becomes an infinite loop.

```
A
↓
B
↓
C
↓
A
↓
B
↓
...
```

Eventually

```
TooManyRedirects
```

## 10. MissingSchema

Schema means

```
http://
https://
ftp://
```

**Example**

```python
requests.get("google.com")
```

**Output**

```
MissingSchema
```

**Correct**

```python
requests.get("https://google.com")
```

## 11. InvalidSchema

The protocol exists but Requests doesn't support it.

**Example**

```python
requests.get("ftp://example.com")
```

**Output**

```
InvalidSchema
```

## 12. InvalidURL

Malformed URL.

**Example**

```python
requests.get("ht!tp://abc")
```

**Output**

```
InvalidURL
```

## 13. InvalidHeader

Occurs when an HTTP header has an invalid value.

**Example**

```python
headers = {
    "Authorization": None
}

requests.get(url, headers=headers)
```

This may raise

```
InvalidHeader
```

## 14. ChunkedEncodingError

Some servers send responses in chunks.

```
Chunk 1 ✔
Chunk 2 ✔
Chunk 3 ❌ Corrupted
```

Requests cannot reconstruct the response.

**Result**

```
ChunkedEncodingError
```

Mostly seen while downloading large files.

## 15. ContentDecodingError

The server says

```
Content-Encoding: gzip
```

But sends corrupted compressed data.

Requests cannot decompress it.

```
ContentDecodingError
```

## 16. StreamConsumedError

Occurs when trying to consume a streamed response more than once.

**Example**

```python
response = requests.get(url, stream=True)

data = response.raw.read()

# Reading again may raise
response.raw.read()
```

The stream has already been consumed.

## 17. RetryError

Raised when retries are configured (typically using urllib3's Retry with a Session and HTTPAdapter) and all retry attempts fail.

For example, if you configure 3 retries and the server remains unavailable, Requests may raise RetryError.

## 18. UnrewindableBodyError

Occurs when Requests needs to resend a request body (for example, after a redirect or retry), but the body comes from a non-seekable stream that can't be rewound.

**Example**

```python
file = open("large_file.bin", "rb")

requests.post(url, data=file)
```

If Requests needs to resend the body but can't seek back to the beginning of the file or stream, it may raise UnrewindableBodyError.

## Summary Table

| Exception               | Meaning                                        | Common Cause                      |
| ----------------------- | ----------------------------------------------- | ---------------------------------- |
| `RequestException`      | Base class for all Requests exceptions         | Catch-all                         |
| `HTTPError`             | HTTP status error (after `raise_for_status()`) | 404, 500, 403                     |
| `Timeout`               | Request took too long                          | Slow network or server            |
| `ConnectTimeout`        | Couldn't establish a connection                | Server down, firewall             |
| `ReadTimeout`           | Connected but no response received             | Slow server                       |
| `ConnectionError`       | Failed to connect                              | DNS failure, no internet          |
| `ProxyError`            | Proxy server failed                            | Bad proxy configuration           |
| `SSLError`              | SSL/TLS verification failed                    | Invalid or expired certificate    |
| `TooManyRedirects`      | Redirect loop                                  | Misconfigured server              |
| `MissingSchema`         | URL missing `http://` or `https://`            | Incomplete URL                    |
| `InvalidSchema`         | Unsupported protocol                           | `ftp://`, custom schemes          |
| `InvalidURL`            | Malformed URL                                  | Invalid URL syntax                |
| `InvalidHeader`         | Bad HTTP header                                | Invalid header value              |
| `ChunkedEncodingError`  | Corrupted chunked response                     | Server/network issue              |
| `ContentDecodingError`  | Failed to decode compressed content            | Corrupted gzip/deflate data       |
| `StreamConsumedError`   | Stream already read                            | Reading a streamed response twice |
| `RetryError`            | All configured retries failed                  | Persistent network/server failure |
| `UnrewindableBodyError` | Request body couldn't be resent                | Non-seekable upload stream        |

## Quick Recap

- RequestException – catch-all base exception.
- HTTPError – HTTP 4xx/5xx responses after raise_for_status().
- ConnectionError – network connectivity problems.
- Timeout – request took too long.
- ConnectTimeout – connection couldn't be established.
- ReadTimeout – server didn't send data in time.
- SSLError – HTTPS certificate problems.
- TooManyRedirects – redirect loop.
- InvalidURL, MissingSchema, and InvalidSchema – invalid URL formats.
