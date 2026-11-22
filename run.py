#!/usr/bin/env python3
"""Локальный сервер СтройРасчёт."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import threading
import webbrowser

ROOT = Path(__file__).resolve().parent
HOST, PORT = "127.0.0.1", 8000

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

def main():
    url = f"http://{HOST}:{PORT}"
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"СтройРасчёт запущен: {url}")
    print("Для остановки нажмите Ctrl+C")
    threading.Timer(0.7, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
    finally:
        server.server_close()

if __name__ == "__main__":
    main()
