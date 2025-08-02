from django.shortcuts import render
from django.views.generic import TemplateView


class BoardView(TemplateView):
    template_name = "game_page.html"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.symbols = ["x", "0"]
        self.current_symbol = self.symbols[0]

    def turn(self):
        pass
