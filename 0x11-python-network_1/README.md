# 0x11. Python - Network #1

## Introduction
This project focuses on network programming in Python, utilizing the `urllib` and `requests` packages to interact with URLs. The tasks involve making HTTP requests, handling responses, and working with JSON data.

## Tasks

### 0. What's my status? #0
- File: [0-hbtn_status.py](./0-hbtn_status.py)
- Description: 
  - Fetches `https://alx-intranet.hbtn.io/status`.
  - Uses the `urllib` package.
  - Displays the body of the response with specific formatting.

### 1. Response header value #0
- File: [1-hbtn_header.py](./1-hbtn_header.py)
- Description:
  - Takes a URL as input, sends a request to it, and displays the value of the `X-Request-Id` variable found in the response header.
  - Uses the `urllib` and `sys` packages.

### 2. POST an email #0
- File: [2-post_email.py](./2-post_email.py)
- Description:
  - Takes a URL and an email address as input, sends a `POST` request to the URL with the email as a parameter, and displays the body of the response.
  - Uses the `urllib` and `sys` packages.

### 3. Error code #0
- File: [3-error_code.py](./3-error_code.py)
- Description:
  - Takes a URL as input, sends a request to it, and displays the body of the response.
  - If the HTTP status code is greater than or equal to 400, prints an error message.
  - Uses the `urllib` and `sys` packages.

### 4. What's my status? #1
- File: [4-hbtn_status.py](./4-hbtn_status.py)
- Description:
  - Fetches `https://alx-intranet.hbtn.io/status`.
  - Uses the `requests` package.
  - Displays the body of the response with specific formatting.

### 5. Response header value #1
- File: [5-hbtn_header.py](./5-hbtn_header.py)
- Description:
  - Takes a URL as input, sends a request to it, and displays the value of the `X-Request-Id` variable found in the response header.
  - Uses the `requests` and `sys` packages.

### 6. POST an email #1
- File: [6-post_email.py](./6-post_email.py)
- Description:
  - Takes a URL and an email address as input, sends a `POST` request to the URL with the email as a parameter, and displays the body of the response.
  - Uses the `requests` and `sys` packages.

### 7. Error code #1
- File: [7-error_code.py](./7-error_code.py)
- Description:
  - Takes a URL as input, sends a request to it, and displays the body of the response.
  - If the HTTP status code is greater than or equal to 400, prints an error message.
  - Uses the `requests` and `sys` packages.

### 8. Search API
- File: [8-json_api.py](./8-json_api.py)
- Description:
  - Takes a letter as input, sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter, and displays the response.
  - Displays the user ID and name if the response is properly JSON formatted and not empty.
  - Uses the `requests` and `sys` packages.

