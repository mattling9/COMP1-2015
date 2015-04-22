# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment

BOARDDIMENSION = 8

def CreateBoard():
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):
      Board[Count].append("  ")
  return Board

def DisplayWhoseTurnItIs(WhoseTurn):
  if WhoseTurn == "W":
    print("It is White's turn")
  else:
    print("It is Black's turn")

def GetTypeOfGame():
  TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
  ValidInput = False
  AcceptableInputs = ['Y','YES','NO','N']
  while ValidInput == False:
    for item in AcceptableInputs:
      if TypeOfGame.upper() == item:
          ValidInput = True
    if ValidInput == False:
      print("Please Enter Y or N")
      TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
  TypeOfGame = TypeOfGame[0]
  return TypeOfGame

def DisplayWinner(WhoseTurn):
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured.  White wins!")
  else:
    print("White's Sarrum has been captured.  Black wins!")

def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  if Board[FinishRank][FinishFile][1] == "S":
    return True
  else:
    return False

def DisplayBoard(Board):
  print()
  for RankNo in range(1, BOARDDIMENSION + 1):
    print("     _______________________")
    print(("R"+  str(RankNo)), end="   ")
    for FileNo in range(1, BOARDDIMENSION + 1):
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
  print("     _______________________")
  print()
  print("      F1 F2 F3 F4 F5 F6 F7 F8")
  print()
  print()    

def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  CheckRedumMoveIsLegal = False
  if ColourOfPiece == "W":
    if FinishRank == StartRank - 1:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
        CheckRedumMoveIsLegal = True
  elif FinishRank == StartRank + 1:
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True
  return CheckRedumMoveIsLegal

def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckSarrumMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = True
  return CheckSarrumMoveIsLegal

def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  if RankDifference == 0:
    if FileDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, FileDifference):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
    elif FileDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
  elif FileDifference == 0:
    if RankDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    elif RankDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  return GisgigirMoveIsLegal

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckNabuMoveIsLegal = False
  if abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1:
    CheckNabuMoveIsLegal = True
  return CheckNabuMoveIsLegal

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1):
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) == 2):
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  MoveIsLegal = True
  if (FinishFile == StartFile) and (FinishRank == StartRank):
    MoveIsLegal = False

  Positions = [StartFile, StartRank, FinishFile, FinishRank]
  for position in Positions:
    if position < 1 or position > 8:
      MoveisLegal = False
      
  else:
    try:
      PieceType = Board[StartRank][StartFile][1]
      PieceColour = Board[StartRank][StartFile][0]
      if WhoseTurn == "W":
        if PieceColour != "W":
          MoveIsLegal = False
        if Board[FinishRank][FinishFile][0] == "W":
          MoveIsLegal = False
      else:
        if PieceColour != "B":
          MoveIsLegal = False
        if Board[FinishRank][FinishFile][0] == "B":
          MoveIsLegal = False
      if MoveIsLegal == True:
        if PieceType == "R":
          MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
        elif PieceType == "S":
          MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "M":
          MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "G":
          MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "N":
          MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "E":
          MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
    except:
      pass
  return MoveIsLegal

def InitialiseBoard(Board, SampleGame):
  if SampleGame == "Y":
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        Board[RankNo][FileNo] = "  "
    Board[1][2] = "BG"
    Board[1][4] = "BS"
    Board[1][8] = "WG"
    Board[2][1] = "WR"
    Board[3][1] = "WS"
    Board[3][2] = "BE"
    Board[3][8] = "BE"
    Board[6][8] = "BR"
  else:
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        if RankNo == 2:
          Board[RankNo][FileNo] = "BR"
        elif RankNo == 7:
          Board[RankNo][FileNo] = "WR"
        elif RankNo == 1 or RankNo == 8:
          if RankNo == 1:
            Board[RankNo][FileNo] = "B"
          if RankNo == 8:
            Board[RankNo][FileNo] = "W"
          if FileNo == 1 or FileNo == 8:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"
          elif FileNo == 2 or FileNo == 7:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
          elif FileNo == 3 or FileNo == 6:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
          elif FileNo == 4:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
          elif FileNo == 5:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
        else:
          Board[RankNo][FileNo] = "  "    
                    
def GetMove(StartSquare, FinishSquare):
  validStartSquare= False
  while validStartSquare == False:
    try:
      StartSquare = int(input("Enter coordinates of square containing piece to move (file first): "))
      validStartSquare = True
    except ValueError:
      print("You must enter intergers here!")
      
    
  while StartSquare < 11:
    print("Please provde both FILE and RANK for this move")
    StartSquare = int(input("Enter coordinates of square containing piece to move (file first): "))
    
  FinishSquare = int(input("Enter coordinates of square to move piece to (file first): "))
  while FinishSquare <11:
    print("Please provde both FILE and RANK for this move")
    FinishSquare = int(input("Enter coordinates of square containing piece to move (file first): "))
    
  return StartSquare, FinishSquare

def ConfirmMove(StartSquare, FinishSquare):
  StartFileRank = list(str(StartSquare))
  FinishFileRank = list(str(FinishSquare))
  
  moveConfirmed = False
  print("Move from Rank {0}, File {1}, to Rank {2}, File {3}".format(StartFileRank[1], StartFileRank[0], FinishFileRank[1], StartFileRank[0]))
  ConfirmationInput = input("Confirm move (Yes/No): ")
  acceptableInputs = ['YES', 'Y', 'NO', 'N']
  while ConfirmationInput.upper() not in acceptableInputs:
    print("Please Enter a valid Input!")
    ConfirmationInput = input("Confirm move (Yes/No): ")

  if ConfirmationInput.upper() == 'Y' or ConfirmationInput.upper() == 'YES':
    moveConfirmed = True
  elif ConfirmationInput.upper() == 'N' or ConfirmationInput.upper() == 'No':
    moveConfirmed = False
  return moveConfirmed
    
def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "WM"
    print("White Redum promoted to Marzaz Pani!")
    Board[StartRank][StartFile] = "  "
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    print("Black Redum promoted to Marzaz Pani!")
    Board[FinishRank][FinishFile] = "BM"
    Board[StartRank][StartFile] = "  "
  else:
    PieceInfo = GetPieceName(Board[StartRank][StartFile])
    Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
    Board[StartRank][StartFile] = "  "
    print()
    print("{0} {1} moves to File:{2}, Rank:{3}".format(PieceInfo[1], PieceInfo[0], FinishFile, FinishRank))
  
    

def GetPieceName(BoardInfo):
                        
  BoardPositionList = list(str(BoardInfo))
  PieceColourInitial = BoardPositionList[0]
  PieceFullColour = ''
  
  PieceNameInitial = BoardPositionList[1]
  PieceFullName = ''

  PieceNameArray = [['G','Gusgigir'],
                    ['E','Etlu'],
                    ['N','Nabu'],
                    ['M','Marzaz Pani'],
                    ['S','Saurum'],
                    ['R','Redum']]

  for piece in PieceNameArray:
    if PieceNameInitial == piece[0]:
      PieceFullName = piece[1]

  if PieceColourInitial == 'W':
    PieceFullColour = 'White'
  elif PieceColourInitial == 'B':
    PieceFullColour = 'Black'

  PieceInfo = [PieceFullName, PieceFullColour]
  return PieceInfo


def GetValidBoardPosition(Rank, File):
  validPosition = False
  validRank = False
  validFile = False
  if Rank > 0 and Rank < 8:
    validRank = True
  elif File >0 and Rank < 8:
    validFile = True

  if (validRank and validFile) == True:
    validPosition = True
  return validPosition

  pass

  pass

  pass

  pass

  pass
    
if __name__ == "__main__":
  Board = CreateBoard() #0th index not used
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = "Y"
  while PlayAgain == "Y":
    WhoseTurn = "W"
    GameOver = False
    SampleGame = GetTypeOfGame()
    if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:
      SampleGame = chr(ord(SampleGame) - 32)
    InitialiseBoard(Board, SampleGame)
    while not(GameOver):
      DisplayBoard(Board)
      DisplayWhoseTurnItIs(WhoseTurn)
      ConfirmMoveDecision = False
      while not ConfirmMoveDecision:
        MoveIsLegal = False
        while not(MoveIsLegal):
          StartSquare, FinishSquare = GetMove(StartSquare, FinishSquare)
          StartRank = StartSquare % 10
          StartFile = StartSquare // 10
          FinishRank = FinishSquare % 10
          FinishFile = FinishSquare // 10
          MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
          if not(MoveIsLegal):
            print("That is not a legal move - please try again")
        GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
        ConfirmMoveDecision = ConfirmMove(StartSquare, FinishSquare)
      MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
      if GameOver:
        DisplayWinner(WhoseTurn)
      if WhoseTurn == "W":
        WhoseTurn = "B"
      else:
        WhoseTurn = "W"
    PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
    if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
      PlayAgain = chr(ord(PlayAgain) - 32)
