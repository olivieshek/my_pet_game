import tkinter as tk
from pet import Pet
import time

"""
TODO:
    кнопки:
        - покормить,
        - поиграть,
        - уложить спать,
        ((помыть));

    лейблы:
        - атрибуты питомца;
    
    портрет:
        - как изменяется картинка портрета?
            - нужен муд? - результат 3х атрибутов :
                                        fullness,
                                        activity,
                                        cheerfulness;
        
        - состояние питомца
            # например, не сможет спать, если объелся
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
        self.fullness_lbl = tk.Label(self)
        self.fullness_lbl.pack()
        self.activity_lbl = tk.Label(self)
        self.activity_lbl.pack()
        self.cheerfulness_lbl = tk.Label(self)
        self.cheerfulness_lbl.pack()

        # изображение питомца
        self.canvas = tk.Canvas(self, height=256, width=256)
        self.canvas.pack()
        self.pet_image = tk.PhotoImage(file=self.pet.portrait)
        self.pet_image = self.pet_image.subsample(2) # 512 / 2 = 256
        self.canvas.create_image(128, 128, image=self.pet_image)

    def renew(self):
        self.pet.decrease_stats()
        print('Атрибуты снизились')
        self.after(1000, self.renew)


if __name__ == '__main__':
    window = App()
    window.renew()
    window.mainloop()