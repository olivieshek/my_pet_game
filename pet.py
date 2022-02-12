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

        self.portrait = portrait,
        self.name = name,
        self.fullness = fullness,
        self.activity = activity,
        self.cheerfulness = cheerfulness,
        self.mood = mood,
        self.fullness_change = fullness_change,
        self.activity_change = activity_change,
        self.cheerfulness_change = cheerfulness_change,
        self.mood_change = mood_change

    def feed(self, calories):
        self.fullness += calories
        print(f'{self.name} съел {calories} калорий,'
        ' и теперь у него {self.fullness} сытости.')