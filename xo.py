#!/Users/hekate/anaconda3/bin/python3.7

class State:  
   def __init__(self, previous = None):
      if previous:
         self.turn = previous.turn
         self.move_counter = previous.move_counter
         self.result = previous.result
         self.board = previous.board
      else:
         self.turn = ""
         self.move_counter = 0
         self.result = "ambiguous"
         self.board = []

   def next_turn(self):
      self.turn = "o" if self.turn == "x" else "x"

   def empty_fields(self):
      return [i for i, f in enumerate(self.board) if f == "e"]

   def is_settled(self):
      for i in range(3,10,3):
         if self.board[i - 1] != "e" and len(set(self.board[:i])) == 1:
            self.result = self.board[i-1] + " wins"
            return True
      for i in range(3):
         if self.board[i] != "e" and len(set(self.board[i:9:3])) == 1:
            self.result = self.board[i] + " wins"
            return True
      if self.board[0] != "e" and len(set(self.board[0:9:4])) == 1:
         self.result = self.board[0] + " wins"
         return True
      if self.board[2] != "e" and len(set(self.board[2:7:2])) == 1:
         self.result = self.board[2] + " wins"
         return True
      if len(self.empty_fields()) == 0:   
         self.result = "draw"
         return True
      return False

class Action:   
   def __init__(self, field):
      self.letter_index = field

   def move(self, state):
      next = State(state)
      next.board[int(self.letter_index)] = state.turn
      if state.turn == "o":
         next.move_counter += 1
      next.next_turn()
      return next

class Game:  
   def __init__(self, auto_player = None):
      self.auto_player = auto_player
      self.current_state = State()
      self.current_state.board = ["e", "e", "e",
                                  "e", "e", "e",
                                  "e", "e", "e"]
      self.current_state.turn = "x"
      self.status = "beggin"

   def advance_turn(self, state):
      self.current_state = state
      if state.is_settled():
         self.status = "end"
         print(state.result)
      else:
         print(self.current_state.board[:3])
         print(self.current_state.board[3:6])
         print(self.current_state.board[6:9])
         if self.current_state.turn == "x":
            letter_index = input("Choose x field: ")
         else:
            letter_index = input("Choose o field: ")
         action = Action(letter_index)
         self.advance_turn(action.move(self.current_state))

   def start(self):
      if self.status == "beggin":
         self.advance_turn(self.current_state)
         self.status = "run"

print("These are fields keys: \n[0, 1, 2]\n[3, 4, 5]\n[6, 7, 8]")
new_game = Game()
new_game.start()
