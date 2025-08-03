from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class BoardView(TemplateView):
    template_name = "game_page.html"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.symbols = ["x", "0"]
        self.current_symbol = self.symbols[0]

    def post(self, request, *args, **kwargs):
        cell_id = request.POST.get("cell_id")
        print(f"cell clicked: {cell_id}")

        return self.get(request, *args, **kwargs)
