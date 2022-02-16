import tkinter as tk
from pet import Pet
import time

"""
TODO:
    портрет:
        - как изменяется картинка портрета?
            - нужен муд? - результат 3х атрибутов :
                                        fullness,
                                        activity,
                                        cheerfulness;
        
        - состояние питомца
            # например, не сможет спать, если объелся

        блокировать кнопки, когда питомец что-то делает
            вместе с тем, изменять портрет питомца в процессе активности

        mood????? должен влиять на портрет
        mood = sum(fullness, activity, cheerfulness) // 3
        -- то есть, ищем среднее арифмитическое
"""


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # настройка окна
        self.geometry("500x500")
        # питомец
        self.pet = Pet(
            name="Парво",
            portrait="assets/calm.png"
        )
        # интерфейс с атрибутами питомца
        self.title(f'Питомец {self.pet.name}')
        self.fullness_lbl = tk.Label(self)
        self.fullness_lbl.pack()
        self.activity_lbl = tk.Label(self)
        self.activity_lbl.pack()
        self.cheerfulness_lbl = tk.Label(self)
        self.cheerfulness_lbl.pack()
        self.mood_lbl = tk.Label(self)
        self.mood_lbl.pack()

        # изображение питомца
        self.canvas = tk.Canvas(self, height=256, width=256)
        self.canvas.pack()
        self.pet_image = tk.PhotoImage(file=self.pet.portrait)
        self.pet_image = self.pet_image.subsample(2) # 512 / 2 = 256
        self.canvas.create_image(128, 128, image=self.pet_image)

        # кнопки
        self.feed_btn = tk.Button(
            self, 
            text='Покормить', 
            command=lambda: self.pet.feed(calories=5)
        )
        self.feed_btn.pack()
        self.play_btn = tk.Button(
            self, 
            text='Поиграть',
            command=lambda: self.pet.play(5)
        )
        self.play_btn.pack()
        self.sleep_btn = tk.Button(
            self, 
            text='Уложить спать',
            command=lambda: self.pet.sleep(5)
        )
        self.sleep_btn.pack()

    # FIXME: кнопки срабатывают не мнгновенно
    def renew(self):
        self.pet.decrease_stats()
        print('Атрибуты снизились')
        self.fullness_lbl.config(text=f'Сытость: {self.pet.fullness}')
        self.activity_lbl.config(text=f'Активность: {self.pet.activity}')
        self.cheerfulness_lbl.config(text=f'Бодрость: {self.pet.cheerfulness}')
        self.mood_lbl.config(text=f'Настроение: {self.pet.mood}')
        self.after(1000, self.renew)


if __name__ == '__main__':
    window = App()
    window.renew()
    window.mainloop()