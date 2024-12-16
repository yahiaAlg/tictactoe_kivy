from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from random import choice

class TicTacToeApp(App):
    def build(self):
        # Changer la couleur d'arrière-plan de l'application
        Window.clearcolor = (0.9, 0.95, 1, 1)  # Bleu ciel très clair
        
        self.title = "Morpion - Bleu ciel et Blanc"
        
        # Mode de jeu : 1 joueur ou 2 joueurs
        self.mode = int(input("Choisissez le mode de jeu (1 pour joueur vs IA, 2 pour joueur vs joueur) : "))
        
        # Layout principal : Grille de 3x3
        self.layout = GridLayout(cols=3, padding=15, spacing=10)
        self.board = [[None for _ in range(3)] for _ in range(3)]  # Stocke les valeurs X, O ou None
        self.current_player = 'X'

        # Ajout des boutons
        for row in range(3):
            for col in range(3):
                button = Button(
                    text='',
                    font_size=36,
                    background_color=(1, 1, 1, 1),  # Blanc initial
                    background_normal='',  # Enlever le style par défaut
                    color=(0.2, 0.2, 0.2, 1),  # Texte gris foncé
                    border=(2, 2, 2, 2),  # Bordure subtile
                )
                button.bind(on_press=lambda btn, x=row, y=col: self.on_button_press(btn, x, y))
                self.layout.add_widget(button)
                self.board[row][col] = button

        self.status_label = Label(
            text="C'est au tour de X",
            font_size=24,
            size_hint_y=None,
            height=50,
            color=(0.1, 0.1, 0.5, 1)  # Texte bleu foncé
        )

        # Layout global
        main_layout = GridLayout(rows=2, spacing=10, padding=20)
        main_layout.add_widget(self.layout)
        main_layout.add_widget(self.status_label)

        return main_layout

    def on_button_press(self, button, row, col):
        if button.text == '':  # Vérifie si la case est vide
            button.text = self.current_player
            button.background_color = (0.4, 0.7, 1, 1) if self.current_player == 'X' else (1, 1, 1, 1)  # Bleu ciel pour X, blanc pour O

            if self.check_winner(self.current_player):
                self.status_label.text = f"{self.current_player} a gagné !"
                self.disable_board()
            elif self.check_draw():
                self.status_label.text = "Match nul !"
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.status_label.text = f"C'est au tour de {self.current_player}"

                if self.mode == 1 and self.current_player == 'O':  # Mode 1 joueur et tour de l'IA
                    self.ai_move()

    def ai_move(self):
        valid_moves = [(row, col) for row in range(3) for col in range(3) if self.board[row][col].text == '']
        row, col = choice(valid_moves)
        self.on_button_press(self.board[row][col], row, col)

    def check_winner(self, player):
        # Vérifie les lignes, colonnes et diagonales
        for row in range(3):
            if all(self.board[row][col].text == player for col in range(3)):
                return True

        for col in range(3):
            if all(self.board[row][col].text == player for row in range(3)):
                return True

        if all(self.board[i][i].text == player for i in range(3)) or all(self.board[i][2-i].text == player for i in range(3)):
            return True

        return False

    def check_draw(self):
        return all(self.board[row][col].text != '' for row in range(3) for col in range(3))

    def disable_board(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col].disabled = True

if __name__ == "__main__":
    TicTacToeApp().run()


