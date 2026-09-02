# 🌐 Minimal Local HTTP Server

`HTTPServer` creates a web server that listens on a port; `BaseHTTPRequestHandler` defines how your server responds to requests. `MyHandler` inherits from it to implement its own `do_GET()`.

```text
HTTPServer
    │
    ├── Waits for connections on localhost:3000
    │
    └── When a request arrives
            │
            ▼
    MyHandler.do_GET()
```

```text
BaseHTTPRequestHandler
          ▲
          │ inherits
          │
      MyHandler
```

See [server_connect.py](file:///d:/python/python-study-notes/study_scripts/server_connect.py) for the runnable server.
