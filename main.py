import tkinter as tk
from tkinter import messagebox
from unit_test import Test

class CaesarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Шифр Цезаря")
        self.geometry("520x170")
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Сообщение
        tk.Label(frame, text="Сообщение:").grid(row=0, column=0, sticky=tk.W, pady=5, padx=(0, 20))
        self.message_entry = tk.Entry(frame, width=50)
        self.message_entry.grid(row=0, column=1, columnspan=3, sticky=tk.EW, pady=5)

        # Сдвиг
        tk.Label(frame, text="Сдвиг:").grid(row=1, column=0, sticky=tk.W, pady=5, padx=(0, 20))
        self.shift_entry = tk.Entry(frame, width=10)
        self.shift_entry.grid(row=1, column=1, sticky=tk.W, pady=5)

        # Расшифровка и дешифровка для русского и английского алфавита
        self.action_var = tk.StringVar(value="encrypt")
        tk.Radiobutton(frame, text="Зашифровать", variable=self.action_var, value="encrypt").grid(row=1, column=2, sticky=tk.W, padx=(0, 60))
        tk.Radiobutton(frame, text="Расшифровать", variable=self.action_var, value="decrypt").grid(row=1, column=3, sticky=tk.W)

        # Действие
        tk.Button(frame, text="Действие", command=self.execute).grid(row=3, column=1, columnspan=3, pady=10, sticky=tk.EW)

        # Результат
        tk.Label(frame, text="Результат:").grid(row=4, column=0, sticky=tk.W, pady=5, padx=(0, 20))
        self.result_entry = tk.Entry(frame, width=50)
        self.result_entry.grid(row=4, column=1, columnspan=3, sticky=tk.EW, pady=5)

        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)
        frame.columnconfigure(3, weight=1)

    def execute(self):
        message = self.message_entry.get()
        try:
            shift = int(self.shift_entry.get())
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Сдвиг должен быть числом")
            return

        choice = self.action_var.get()
        test = Test(message, shift, choice)
        result = test.testing()
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, result)

if __name__ == "__main__":
    app = CaesarApp()
    app.mainloop()
