class Pet():
    def __init__(
        self, 
        portrait="asserts/calm.png",
        name="",
        fullness=100,
        activity=100,
        cheerfulness=100,
        mood=100,
        fullness_change=1,
        activity_change=1,
        cheerfulness_change=1,
        mood_change=1
        ):

        self.portrait = portrait
        self.name = name
        self.fullness = fullness
        self.activity = activity
        self.cheerfulness = cheerfulness
        self.mood = mood
        self.fullness_change = fullness_change
        self.activity_change = activity_change
        self.cheerfulness_change = cheerfulness_change
        self.mood_change = mood_change


    def decrease_stats(self):
        self.fullness -= self.fullness_change
        self.activity -= self.activity_change
        self.cheerfulness -= self.cheerfulness_change
        self.mood -= self.mood_change

    def feed(self, calories):
        self.fullness += calories
        print(f'{self.name} съел {calories} калорий,'
        f' и теперь у него {self.fullness} очков сытости.')

    def play(self, time):
        self.activity += time
        print(f'Вы поиграли с питомцем и теперь'
        f' у него {self.activity} очков активности.')

    def sleep(self, time):
        self.cheerfulness += time
        print(f'Питомец поспал и теперь у него'
        f' {self.cheerfulness} очков бодрости.')