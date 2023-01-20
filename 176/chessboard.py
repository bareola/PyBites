WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
   """Create a chessboard with of the size passed in.
   Don't return anything, print the output to stdout"""
   for row in range(size):
      if row % 2 == 0:
            print(f'{WHITE}{BLACK}' * int(size/2))
      else:
            print(f'{BLACK}{WHITE}' * int(size/2))