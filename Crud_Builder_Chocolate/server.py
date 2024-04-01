from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Base de datos simulada de chocolates
chocolates = {}


class DeliveryChocolate:
    def __init__(self, chocolate_type, peso_number, sabor, relleno):
        self.chocolate_type = chocolate_type
        self.peso_number = peso_number
        self.sabor=sabor
        self.relleno = relleno


class Tabletas(DeliveryChocolate):
    def __init__(self, peso_number, sabor):
        super().__init__("tabletas", peso_number, sabor)

class Bombones(DeliveryChocolate):
    def __init__(self, peso_number, sabor, relleno):
        super().__init__("bombones", peso_number, sabor, relleno)

class Trufas(DeliveryChocolate):
    def __init__(self, peso_number, sabor, relleno):
        super().__init__("trufas", peso_number, sabor, relleno)


class DeliveryFactory:
    @staticmethod
    def create_chocolate(chocolate_type, peso_number, sabor, relleno):
        if chocolate_type == "bombones":
            return Bombones(peso_number, sabor, relleno)
        elif chocolate_type == "tabletas":
            return Tabletas(peso_number, sabor)
        elif chocolate_type == "trufas":
            return Trufas(peso_number, sabor, relleno)
        else:
            raise ValueError("Tipo de chocolate de entrega no válido")


class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


class DeliveryService:
    def __init__(self):
        self.factory = DeliveryFactory()

    def add_chocolate(self, data):
        chocolate_type = data.get("chocolate_type", None)
        peso_number = data.get("peso_number", None)
        sabor=data.get("sabor",None)
        relleno = data.get("relleno", None)

        delivery_chocolate = self.factory.create_chocolate(
            chocolate_type, peso_number, sabor, relleno
        )
        chocolates[len(chocolates) + 1] = delivery_chocolate
        return delivery_chocolate

    def list_chocolates(self):
        return {index: chocolate.__dict__ for index, chocolate in chocolates.items()}

    def update_chocolate(self, chocolate_id, data):
        if chocolate_id in chocolates:
            chocolate = chocolates[chocolate_id]
            peso_number = data.get("peso_number", None)
            sabor=data.get("sabor",None)
            relleno = data.get("relleno", None)
            if peso_number:
                chocolate.peso_number = peso_number
            if sabor:
                chocolate.sabor=sabor
            if relleno:
                chocolate.relleno = relleno
            return chocolate
        else:
            raise None

    def delete_chocolate(self, chocolate_id):
        if chocolate_id in chocolates:
            del chocolates[chocolate_id]
            return {"message": "Chocolate eliminado"}
        else:
            return None


class DeliveryRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.delivery_service = DeliveryService()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/deliveries":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.delivery_service.add_chocolate(data)
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_GET(self):
        if self.path == "/deliveries":
            response_data = self.delivery_service.list_chocolates()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_PUT(self):
        if self.path.startswith("/deliveries/"):
            chocolate_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.delivery_service.update_chocolate(chocolate_id, data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_DELETE(self):
        if self.path.startswith("/deliveries/"):
            chocolate_id = int(self.path.split("/")[-1])
            response_data = self.delivery_service.delete_chocolate(chocolate_id)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )


def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, DeliveryRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()