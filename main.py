import tkinter as tk
from pet import Pet

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.pet = Pet(
            name="Парво",
            portrait="asserts/calm.png"
        )
        # п.с. мой тигр - итальянец, 
        # у него классное имя и усы 
        # (но он их сбрил, на фото их нет)
        self.canvas = tk.Canvas(self)
        self.canvas.pack()
        self.pet_image = tk.PhotoImage(file=self.pet.portrait)
        self.canvas.create_image(0, 0, image=self.pet_image)

        """
        TODO:
            кнопки:
                - покормить,
                - поиграть,
                - уложить спать,
                ((помыть));

            лейблы:
                - атрибуты питомца,
            
            портрет:
                - как изменяется картинка портрета?
                    - нужен муд?
                
                - состояние питомца
                    - например, не сможет спать, если объелся
        """


if __name__ == '__main__':
    window = App()
    window.mainloop()