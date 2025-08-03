from django.views.generic import TemplateView


class BoardView(TemplateView):
    template_name = "game_page.html"

    def get_moves(self):
        return self.request.session.get("moves", [])

    def set_moves(self, moves):
        self.request.session["moves"] = moves

    def get_current_player(self):
        return self.request.session.get("current_player", 0)

    def set_current_player(self, player):
        self.request.session["current_player"] = player

    def get_playing_cell(self):
        return self.request.session.get("playing_cell")

    def set_playing_cell(self, cell):
        self.request.session["playing_cell"] = cell

    def post(self, request, *args, **kwargs):
        moves = self.get_moves()
        current_player = self.get_current_player()
        playing_cell = self.get_playing_cell()

        cell_id = request.POST.get("cell_id")

        # Set state variables for logic
        self.moves = moves
        self.current_player = current_player
        self.playing_cell = playing_cell

        valid_move = self.check_move(cell_id)
        if valid_move:
            self.moves.append(cell_id)
            self.turn()

        # Save updated state back to session
        self.set_moves(self.moves)
        self.set_current_player(self.current_player)
        self.set_playing_cell(self.playing_cell)

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.moves = self.get_moves()
        self.current_player = self.get_current_player()
        self.playing_cell = self.get_playing_cell()

        symbols = ["0", "x"]
        cell_symbols = {}
        for i, cell in enumerate(self.moves):
            player = i % 2
            cell_symbols[cell] = symbols[player]

        context["cell_symbols"] = cell_symbols
        return context

    def check_move(self, id):
        try:
            played = self.moves.index(id)
        except ValueError:
            # Move hasn't been played
            bcell, scell = id.split("-")

            if self.playing_cell is None:
                self.playing_cell = scell
                return True
            else:
                if self.playing_cell != bcell:
                    # Invalid move: must play in the correct big cell
                    return False
                else:
                    return True
        else:
            # Move already played
            return False

    def turn(self):
        self.current_player = 1 - self.current_player

