class Navegador:
    def __init__(self):
        self.actual = None
        self.back_stack = []
        self.forward_stack = []

    def visitar(self, url):
        if self.actual:
            self.back_stack.append(self.actual)
        self.actual = url
        self.forward_stack.clear()
        print(f"Visitando: {self.actual}")

    def back(self):
        if not self.back_stack:
            print("No hay páginas atrás.")
            return
        self.forward_stack.append(self.actual)
        self.actual = self.back_stack.pop()
        print(f"Retrocediendo a: {self.actual}")

    def forward(self):
        if not self.forward_stack:
            print("No hay páginas adelante.")
            return
        self.back_stack.append(self.actual)
        self.actual = self.forward_stack.pop()
        print(f"Avanzando a: {self.actual}")

    def estado(self):
        print("\n--- Estado del Navegador ---")
        print(f"Página actual: {self.actual}")
        print(f"Back stack: {self.back_stack}")
        print(f"Forward stack: {self.forward_stack}")
        print("--------------------------------\n")


# --- Ejemplo de uso ---
nav = Navegador()

nav.visitar("google.com")
nav.visitar("facebook.com")
nav.visitar("youtube.com")

nav.back()
nav.back()
nav.forward()

nav.estado()
