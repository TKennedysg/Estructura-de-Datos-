class Editor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def insert(self, new_text):
        self.undo_stack.append(("insertar", len(new_text)))
        self.redo_stack.clear()

        self.text += new_text
        print(f"[Insertar] = {self.text}")

    def delete(self, length):
        deleted = self.text[-length:]
        self.undo_stack.append(("Eliminar", deleted))
        self.redo_stack.clear()

        self.text = self.text[:-length]
        print(f"[Eliminar] = {self.text}")

    def undo(self):
        if not self.undo_stack:
            print("Nada que deshacer.")
            return

        action, value = self.undo_stack.pop()

        if action == "insertar":
            deleted = self.text[-value:]
            self.text = self.text[:-value]
            self.redo_stack.append(("insertar", deleted))

        elif action == "eliminar":
            self.text += value
            self.redo_stack.append(("eliminar", len(value)))

        print(f"[desahacer] → {self.text}")

    def redo(self):
        if not self.redo_stack:
            print("Nada que rehacer.")
            return

        action, value = self.redo_stack.pop()

        if action == "insertar":
            self.text += value
            self.undo_stack.append(("insertar", len(value)))

        elif action == "eliminar":
            deleted = self.text[-value:]
            self.text = self.text[:-value]
            self.undo_stack.append(("eliminar", deleted))

        print(f"[Rehacer] → {self.text}")

    def show(self):
        print(f"Texto actual: {self.text}")

editor = Editor()

editor.insert("Hola")
editor.insert(" Mundo")
editor.delete(6)
editor.undo()
editor.undo()
editor.redo()
editor.show()