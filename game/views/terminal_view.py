import pyfiglet
from beautifultable import BeautifulTable
from data.settings import BOARD_LENGTH
from game.utils.list_utils import reverse_matrix

class TerminalView:
    def print_logo(self) -> None:
        logo = pyfiglet.Figlet(font='stop')
        print(logo.renderText('Connecta'))

    def display_move(self, player) -> None:
        print(f'\n{player.name} ({player.char}) ha movido en la columna #{player.last_move}\n')

    def display_board(self, board) -> None:
        matrix = board.columns_as_lists()
        matrix = reverse_matrix(matrix)
        bt = BeautifulTable()
        for col in matrix:
            bt.columns.append(col)
        bt.columns.header = [str(i) for i in range(BOARD_LENGTH)]
        print(bt)

    def display_result(self, winner, match) -> None:
        if winner is not None:
            print(f'\n{winner.name} ({winner.char}) gana!!!')
        else:
            print(f'\nEmpate entre {match.get_player("x")} (x) y {match.get_player("o")} (o)!')

    def select_round_type(self) -> str:
        print("""
        Selecciona el tipo de ronda:

        1) Computadora vs Computadora
        2) Computadora vs Humano
        """)
        response = ''
        while response != '1' and response != '2':
            response = input('Por favor, escribe 1 o 2:  ')
        return response
    
    def select_difficulty_level(self) -> str:
        print("""
        Chose your opponent, human:

        1) Bender: for clowns and wimps
        2) T-800: you may regret it
        3) T-1000: Don't even think about it!
        """)
        response = ''
        while response not in ['1', '2', '3']:
            response = input('Please type 1, 2 or 3: ').strip()
        return response

    def ask_human_name(self) -> str:
        return input('Introduce tu nombre, humano: ')

    def ask_column(self) -> str:
        return input('Selecciona una columna: ')
