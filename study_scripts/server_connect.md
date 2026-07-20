```
HTTPServer
    │
    ├── Waits for connections on localhost:3000
    │
    └── When a request arrives
            │
            ▼
    MyHandler.do_GET()
```

HTTPServer → Creates a web server that listens on a port.
BaseHTTPRequestHandler → Defines how your server should respond to requests.

```
BaseHTTPRequestHandler
          ▲
          │ inherits
          │
      MyHandler
```
