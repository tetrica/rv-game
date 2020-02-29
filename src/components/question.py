import tcod as libtcod

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        self.answered = False

    def get_answer(self, answer=None):
        self.answered = answer == self.answer