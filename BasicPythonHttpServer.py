iimport socket


s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
print ("Socket Sucessfully Created")
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


port = 8000
host_ip = '0.0.0.0'


s.bind((host_ip, port))
print(f"Socket binded to {host_ip} on port {port}")

s.listen(5)
print(f"Socket is listening")


while True:
    c, addr = s.accept()
    print(f'got connection from {addr}')
    request = c.recv(1024).decode()

    parts = request.split()
    path = parts[1] if len(parts) > 1 else "/"


    if path == "/":
        html = """
            <html>
            <head><title>/</title></head>
            <body>
                <h1>Hello welcome to my basic https server in python</h1>
                <a href="/about"><button type="button">about</button></a>
                <a href="/contact"><button type="button">contact me</button></a>
            </body
            </html>
        """
    elif path == "/about":
        html = """
            <html>
            <head><title>/</title></head>
            <body>
                <h1>I am a freshmen CS major at Texas a&m wanting to go into devops cloud. I made this basic http server so i can containerize, dockerize, and deploy onto the cloud.</h1>
                <a href="/contact"><button type="button">contact me</button></a>
                <a href="/"><button type="button">home</button></a>
            </body
            </html>
        """
    elif path == "/contact":
        html = """
            <html>
            <head><title>/</title></head>
            <body>
                <a href="https://www.linkedin.com/in/brandentoddturner/">LinkedIn</a> <h4>email: brandenturner7@gmail.com">email</h4>
                <a href="/about"><button type="button">about</button></a> 
                <a href="/"><button type="button">home</button></a>
            </body
            </html>
        """
    else:
        html = """
            <html>
            <head><title></title></head>
            <body>
                <h1>ERROR 404 PAGE NOT FOUND</h1>
            </body
            </html>
        """



    response = f"HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n{html}"
    c.send(response.encode())
    c.close()
    


