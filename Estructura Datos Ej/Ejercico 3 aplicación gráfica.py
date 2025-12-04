import tkinter as tk

class EditorGrafico:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor con Undo/Redo")

        # Text widget
        self.text = tk.Text(root, width=50, height=15)
        self.text.pack(pady=10)

        # Pilas para undo/redo
        self.undo_stack = []
        self.redo_stack = []

        # Botones
        frame = tk.Frame(root)
        frame.pack()

        tk.Button(frame, text="Guardar Estado", command=self.guardar_estado).pack(side="left", padx=5)
        tk.Button(frame, text="Undo", command=self.undo).pack(side="left", padx=5)
        tk.Button(frame, text="Redo", command=self.redo).pack(side="left", padx=5)

    def guardar_estado(self):
        contenido = self.text.get("1.0", tk.END)
        self.undo_stack.append(contenido)
        self.redo_stack.clear()
        print("Estado guardado.")

    def undo(self):
        if not self.undo_stack:
            print("Nada que deshacer.")
            return
        estado_actual = self.text.get("1.0", tk.END)
        self.redo_stack.append(estado_actual)

        estado_prev = self.undo_stack.pop()
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, estado_prev)
        print("Undo ejecutado.")

    def redo(self):
        if not self.redo_stack:
            print("Nada que rehacer.")
            return
        estado_actual = self.text.get("1.0", tk.END)
        self.undo_stack.append(estado_actual)

        estado_sig = self.redo_stack.pop()
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, estado_sig)
        print("Redo ejecutado.")


# Ejecutar app
root = tk.Tk()
app = EditorGrafico(root)
root.mainloop()
