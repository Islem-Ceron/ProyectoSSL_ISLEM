import http.server
import ssl
import os

HOST = "localhost"
PORT = 8443
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CERT = os.path.join(BASE_DIR, "ssl", "server.crt")
KEY = os.path.join(BASE_DIR, "ssl", "server.key")


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)


def main():
    server = http.server.ThreadingHTTPServer((HOST, PORT), Handler)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=CERT, keyfile=KEY)
    server.socket = context.wrap_socket(server.socket, server_side=True)
    print(f"Servidor HTTPS corriendo en https://{HOST}:{PORT}")
    print("Abre esa URL en tu navegador. Si aparece una advertencia,")
    print("haz clic en Avanzado -> Continuar/Proceder para ver la pagina.")
    print("Presiona Ctrl+C para detener.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")


if __name__ == "__main__":
    main()
