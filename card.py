
class Card:
    def __init__(self, name, power, element):
        self.name = name
        self.power = power
        self.element = element

    def beats(self, other):
        wins_against = {
            'fire': 'snow',
            'snow': 'water',
            'water': 'fire'
        }

        if self.element == other.element:
            if self.power > other.power:
                return "Win"
            elif self.power < other.number:
                return "Lose"
            else:
                return "Tie"
        elif wins_against[self.element] == other.element:
            return "Win"
        elif wins_against[other.element] == self.element:
            return "Lose"

    def __str__(self):
        return f"{self.name} ({self.element.capitalize()} {self.power})"

deck = [
     Card("Margueritas on the Beach", 3, "fire"),
    Card("Snowboarding the Mountain", 9, "snow"),
    Card("Diving into the Unknown", 6, "water"),
    Card("Dancing Under Fireworks", 8, "fire"),
    Card("Meditation in the Snow", 5, "snow"),
    Card("Raindrops on the Window", 2, "water"),
    Card("Campfire Secrets", 7, "fire"),
    Card("Icy Silence", 10, "snow"),
    Card("River of Thought", 4, "water"),
]

