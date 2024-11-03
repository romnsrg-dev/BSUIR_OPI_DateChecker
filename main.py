import tkinter as tk

# Функция для определения времени года по дате
def get_season():
    try:
        # Разбиваем введённую строку на день и месяц
        day, month = map(int, entry_date.get().split('.'))

        # Инициализируем переменную для сообщения об ошибке
        error_messages = []

        # Проверяем диапазон дня и месяца
        if day < 1 or day > 31:
            error_messages.append("День должен быть от 01 до 31.")
        if month < 1 or month > 12:
            error_messages.append("Месяц должен быть от 01 до 12.")

        # Если есть ошибки, выводим их
        if error_messages:
            result.set("\n".join(error_messages))
            result_label.config(fg="red")
            return

        # Определяем время года
        if month in [12, 1, 2]:
            result.set("Зима")
            result_label.config(fg="blue")
        elif month in [3, 4, 5]:
            result.set("Весна")
            result_label.config(fg="green")
        elif month in [6, 7, 8]:
            result.set("Лето")
            result_label.config(fg="orange")
        elif month in [9, 10, 11]:
            result.set("Осень")
            result_label.config(fg="brown")

    except ValueError:
        result.set("Неверный формат. Используйте ДД.ММ.")
        result_label.config(fg="red")

# Настройка основного окна
root = tk.Tk()
root.title("Определение времени года по дате")
root.geometry("450x250")  # Увеличили высоту окна для лучшего отображения
root.configure(bg="#f0f0f0")

# Помещаем окно по центру экрана
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_width()) // 2
y = (root.winfo_screenheight() - root.winfo_height()) // 2
root.geometry(f"+{x}+{y}")

# Заголовок
label = tk.Label(root, text="Введите дату (ДД.ММ):", bg="#f0f0f0", font=("Arial", 14))
label.pack(pady=10)

# Поле для ввода даты
entry_date = tk.Entry(root, font=("Arial", 14), justify="center", width=10)
entry_date.pack(pady=5)

# Кнопка для определения времени года
button = tk.Button(root, text="Определить время года", command=get_season, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
button.pack(pady=10)

# Поле для вывода результата
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 16), bg="#f0f0f0", wraplength=400)  # wraplength для переноса строк
result_label.pack(pady=10)

root.mainloop()
