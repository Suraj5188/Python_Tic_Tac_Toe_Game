# Python Tic Tac Toe Game 

def main():
          print("--------------------------------Welcome to the Tic Tac Toe Game----------------------------------")

          # Print The Tic Tac Board Game
          print("\nThe Tic Tac Board Game")
          print("0 | 1 | 2")
          print("------------")
          print("3 | 4 | 5")
          print("------------")
          print("6 | 7 | 8")

          print("\n ^^^ Remember You have to enter this number when your turn is came ^^^")
          print("\n Let's Play Game Now----")


def prinboard():
          print("0 | 1 | 2")
          print("------------")
          print("3 | 4 | 5")
          print("------------")
          print("6 | 7 | 8")

def printboard_main(x_state, y_state):
          zero='X' if x_state[0] else ('0' if y_state[0] else 0)
          one='X' if x_state[1] else ('0' if y_state[1] else 1)
          two='X' if x_state[2] else ('0' if y_state[2] else 2)
          three='X' if x_state[3] else ('0' if y_state[3] else 3)
          four='X' if x_state[4] else ('0' if y_state[4] else 4)
          five='X' if x_state[5] else ('0' if y_state[5] else 5)
          six='X' if x_state[6] else ('0' if y_state[6] else 6)
          seven='X' if x_state[7] else ('0' if y_state[7] else 7)
          eight='X' if x_state[8] else ('0' if y_state[8] else 8)

          
          print(f"{zero} | {one} | {two}")
          print(f"------------")
          print(f"{three} | {four} | {five}")
          print(f"------------")
          print(f"{six} | {seven} | {eight}")
                  

def sum(a,b,c):
        return a+b+c

def check_win(x_state, y_state):

          wins=[ [0,1,2], [0,3,6], [0,4,8], [1,4,7], [2,5,8], [3,4,5], [6,7,8], [2,4,6] ]
          
          for win in wins:
                    if sum(x_state[win[0]],x_state[win[1]],x_state[win[2]])==3:
                              print("X WON The Match!")
                              return 1
                    if sum(y_state[win[0]],y_state[win[1]],y_state[win[2]])==3:
                              print("Y Won The Match!")
                              return 0
                    
          return -1

def play_game():  
          x_state=[0,0,0,0,0,0,0,0,0]
          y_state=[0,0,0,0,0,0,0,0,0]

          turn=1
          while(True):
                    printboard_main(x_state, y_state)
                    
                    if turn==1:
                              print("X's chance")
                              player1=int(input("Enter Player1 Choice : "))
                              x_state[player1]=1                 
                    else:
                              print("Y's chance")
                              player2=int(input("Enter Player2 Choice : "))
                              y_state[player2]=1

                    winner=check_win(x_state,y_state)
                    if(winner!=-1):
                            print("Match Over")
                            break
                              
                    turn=1-turn

if __name__ =="__main__":
          main()
          play_game()