import socket
from datetime import datetime

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
print ("Socket Sucessfully Created")
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


port = 8000
host_ip = '0.0.0.0'
requests = 0 
path_requests = {"/": 0, "/resume": 0, "/projects" : 0, "/metrics": 0}
status_counts = {"200": 0, "404": 0}
s.bind((host_ip, port))
print(f"Socket binded to {host_ip} on port {port}")

s.listen(5)
print(f"Socket is listening")


while True:
    c, addr = s.accept()
    print(f'got connection from {addr}')
    request_bytes = c.recv(1024)
    if not request_bytes:
        c.close()
        continue
    request = request_bytes.decode(errors="ignore")

    parts = request.split()
    path = parts[1] if len(parts) > 1 else "/"
    requests += 1

    if path == "/":
        try:
            file_requested = "static/index.html"
            status_code = 200
            status_counts["200"] += 1 
            path_requests["/"] += 1
            with open(file_requested, "rb") as f:
                html_content = f.read()
            response_headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode('utf-8')
            c.sendall(response_headers + html_content)
        except FileNotFoundError:
            status_code = 404
            html = "<html><body><h1>404 - File Not Found</h1></body></html>"
            response = f"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n{html}"
            c.send(response.encode())

    elif path == "/projects":
        try:
            file_requested = "static/projects.html"
            status_code = 200
            status_counts["200"] += 1 
            path_requests["/projects"] += 1
            with open(file_requested, "rb") as f:
                html_content = f.read()
            response_headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode('utf-8')
            c.sendall(response_headers + html_content)
        except FileNotFoundError:
            status_code = 404
            html = "<html><body><h1>404 - File Not Found</h1></body></html>"
            response = f"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n{html}"
            c.send(response.encode())

    elif path == "/resume":
        try:
            file_requested = "static/resume.html"
            status_code = 200
            status_counts["200"] += 1 
            path_requests["/contact"] += 1
            with open(file_requested, "rb") as f:
                html_content = f.read()
            response_headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode('utf-8')
            c.sendall(response_headers + html_content)
        except FileNotFoundError:
            status_code = 404
            html = "<html><body><h1>404 - File Not Found</h1></body></html>"
            response = f"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n{html}"
            c.send(response.encode())

    elif path == "/metrics":
        status_code = 200 
        status_counts["200"] += 1 
        path_requests["/metrics"] += 1

        metrics = f"http_requests_total {requests}\n"

        for path, count in path_requests.items():
            metrics += f'http_requests_by_path{{path="{path}"}} {count}\n'

        for status, count in status_counts.items():
            metrics += f'http_status_codes{{code="{status}"}} {count}\n'

        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n{metrics}"
        c.send(response.encode()) 
    else:
        status_code = 404
        status_counts["404"] += 1
        html = """
            <html>
            <head><title></title></head>
            <body>
                <h1>ERROR 404 PAGE NOT FOUND</h1>
            </body
            </html>
        """
        response = f"HTTP/1.1 404 Not Found\r\nContent-type: text/html\r\n\r\n{html}"
        c.send(response.encode()) 


    timestamp = datetime.now()
    address = addr
    method = parts[0] if len(parts) > 0 else "Unknown"
    print(f" Ip Address:{address} \n Time:{timestamp} \n Method:{method} \n Path:{path} ")

    c.close()
    


