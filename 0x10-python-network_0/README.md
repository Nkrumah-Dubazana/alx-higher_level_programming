# Python - Network #0

This networking project involves utilizing `curl` in Bash scripts to interact with a server set up on a container. Through these tasks, I gained knowledge about various HTTP headers, URL structure, domain names, different HTTP request/response header fields, status codes, and cookies. Additionally, an algorithm challenge in Python was included as task six.

## Tasks :page_with_curl:

**0. cURL body size**
  * [0-body_size.sh](./0-body_size.sh): Bash script that sends a `GET` request to a specified URL and displays the size of the response body in bytes.

**1. cURL to the end**
  * [1-body.sh](./1-body.sh): Bash script that sends a `GET` request to a specified URL and displays the response body for a `200` status code response.

**2. cURL Method**
  * [2-delete.sh](./2-delete.sh): Bash script that sends a `DELETE` request to a specified URL and displays the response body.

**3. cURL only methods**
  * [3-methods.sh](./3-methods.sh): Bash script that displays all HTTP methods accepted by the server of a specified URL.

**4. cURL headers**
  * [4-header.sh](./4-header.sh): Bash script that sends a `GET` request to a specified URL with a header variable `X-HolbertonSchool-User-Id=98` and displays the response body.

**5. cURL POST parameters**
  * [5-post_params.sh](./5-post_params.sh): Bash script that sends a `POST` request to a specified URL with the variables `email=test.gmail.com` and `subject=I will always be here for PLD` and displays the response body.

**6. Find a peak**
  * [6-peak.py](./6-peak.py): [Technical interview preparation] - Python program that finds a peak in a list of unsorted integers.
  * [6-peak.txt](./6-peak.txt): Text file containing the complexity of the algorithm.

**7. Only status code**
  * [100-status_code.sh](./100-status_code.sh): Bash script that sends a `GET` request to a specified URL and displays the status code of the response without using pipes, redirections, `;`, or `&&`.

**8. cURL a JSON file**
  * [101-post_json.sh](./101-post_json.sh): Bash script that sends a JSON `POST` request with the contents of a provided file to a specified URL and displays the response body.

**9. Catch me if you can!**
  * [102-catch_me.sh](./102-catch_me.sh): Bash script that sends a request to `0.0.0.0:5000/catch_me` causing the server to respond with a message containing `You got me!` in the response body.
