# 🧪 Study Scripts

Small standalone scripts for practicing networking and CLI tooling in Python — outside the main topic-by-topic folders.

---

## 📂 Example Scripts & Guides

### 1. Minimal HTTP Server
* **File**: [server_connect.py](file:///d:/python/python-study-notes/study_scripts/server_connect.py)
* **Guide**: [server_connect.md](file:///d:/python/python-study-notes/study_scripts/server_connect.md)
* **Description**: A local server built with `http.server` that replies to every GET request.

### 2. API Client with Exception Handling
* **File**: [client_api_connect.py](file:///d:/python/python-study-notes/study_scripts/client_api_connect.py)
* **Description**: Fetches from a public test API using `requests`, handling `Timeout`, `HTTPError`, and the base `RequestException`. See [`exception/exception_hierarchy.md`](file:///d:/python/python-study-notes/exception/exception_hierarchy.md) for the full exception reference.

### 3. Simple Math CLI Tool
* **File**: [simple_cli_tool.py](file:///d:/python/python-study-notes/study_scripts/simple_cli_tool.py)
* **Description**: An `argparse`-based CLI that performs `sum`, `minus`, `multiply`, or `divide` across a list of numbers.

```bash
uv run simple_cli_tool.py multiply 5 6 7 8
# Output: Operation: MULTIPLY / Numbers: [5.0, 6.0, 7.0, 8.0] / Result: 1680.0
```
