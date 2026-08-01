import os
import threading
import time
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler


def start_server():

    os.chdir("web")

    server = HTTPServer(
        ("localhost", 8000),SimpleHTTPRequestHandler)

    thread = threading.Thread(target=server.serve_forever,daemon=True)

    thread.start()

    time.sleep(1)

    webbrowser.open("http://localhost:8000")

    print("Dashboard running at http://localhost:8000")

    input("Press Enter to stop server...")

    server.shutdown()