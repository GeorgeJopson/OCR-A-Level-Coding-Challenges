#I know this is some horrible code that could be far more clean, but I don't want
#to spend ages on this challenge.
#And there might be some bugs I haven't spotted due to not testing all possible board combinations.
#I might come back later and make it clean, but for now I'm not worrying about it.

#Answer:
#1: white king is in check
#2: black king is in check
#3: no king is in check

file=open("chess.txt","r")
chessFile=file.readlines()
file.close()
counter=0
chessGames=[]
while True:
    chessGame=[]
    emptyLines=0
    for index in range(counter,counter+8):
        chessGame.append(chessFile[index][:-1].split(" "))
        if(chessFile[index]==". . . . . . . .\n"):
            emptyLines+=1
    chessGames.append(chessGame)
    if(emptyLines==8):
        del chessGames[-1]
        break
    counter+=9
##Get black kings x,y coordinates and then use that with the peices coordinates
##to see if they are checking it
##Black Peices Are Uppercase. white peices are lowercase
def isWhiteInCheck(game):
    for y in range(8):
        for x in range(8):
            if(game[y][x]=="king"):
                whiteKingY=y
                whiteKingX=x

    inCheck=False
    for y in range(8):
        for x in range(8):
            if(game[y][x]=="Pawn"):
                pawnY=y
                pawnX=x
                possiblePositions=[[pawnX-1,pawnY+1],[pawnX+1,pawnY+1]]
                for position in possiblePositions:
                    if(position[0]==whiteKingX and position[1]==whiteKingY):
                        inCheck=True
            elif(game[y][x]=="Castle"):
                castleY=y
                castleX=x
                if(whiteKingX==castleX or whiteKingY==castleY):
                    inCheck=True
            elif(game[y][x]=="Bishop"):
                bishopY=y
                bishopX=x
                for diagonal in range(1,9):
                    if(bishopY+diagonal==whiteKingY and bishopX+diagonal==whiteKingX):
                        inCheck=True
                    elif(bishopY-diagonal==whiteKingY and bishopX+diagonal==whiteKingX):
                        inCheck=True
                    elif(bishopY+diagonal==whiteKingY and bishopX-diagonal==whiteKingX):
                        inCheck=True
                    elif(bishopY-diagonal==whiteKingY and bishopX-diagonal==whiteKingX):
                        inCheck=True
            elif(game[y][x]=="Queen"):
                queenY=y
                queenX=x
                if(whiteKingX==queenX or whiteKingY==queenY):
                    inCheck=True
                for diagonal in range(1,9):
                    if(queenY+diagonal==whiteKingY and queenX+diagonal==whiteKingX):
                        inCheck=True
                    elif(queenY-diagonal==whiteKingY and queenX+diagonal==whiteKingX):
                        inCheck=True
                    elif(queenY+diagonal==whiteKingY and queenX-diagonal==whiteKingX):
                        inCheck=True
                    elif(queenY-diagonal==whiteKingY and queenX-diagonal==whiteKingX):
                        inCheck=True
            elif(game[y][x]=="Knight"):
                knightY=y
                knightX=x
                possiblePositions=[[knightX-2,knightY+1],[knightX-1,knightY+2],[knightX+2,knightY+1],[knightX+1,knightY+2],[knightX-2,knightY-1],[knightX-1,knightY-2],[knightX+2,knightY-1],[knightX+1,knightY-2]]
                for position in possiblePositions:
                    if(position[0]==whiteKingX and position[1]==whiteKingY):
                        inCheck=True
    return inCheck

def isBlackInCheck(game):
    for y in range(8):
        for x in range(8):
            if(game[y][x]=="King"):
                blackKingY=y
                blackKingX=x

    inCheck=False
    for y in range(8):
        for x in range(8):
            if(game[y][x]=="pawn"):
                pawnY=y
                pawnX=x
                possiblePositions=[[pawnX-1,pawnY+1],[pawnX+1,pawnY+1]]
                for position in possiblePositions:
                    if(position[0]==blackKingX and position[1]==blackKingY):
                        inCheck=True
            elif(game[y][x]=="castle"):
                castleY=y
                castleX=x
                if(blackKingX==castleX or blackKingY==castleY):
                    inCheck=True
            elif(game[y][x]=="bishop"):
                bishopY=y
                bishopX=x
                for diagonal in range(1,9):
                    if(bishopY+diagonal==blackKingY and bishopX+diagonal==blackKingX):
                        inCheck=True
                    elif(bishopY-diagonal==blackKingY and bishopX+diagonal==blackKingX):
                        inCheck=True
                    elif(bishopY+diagonal==blackKingY and bishopX-diagonal==blackKingX):
                        inCheck=True
                    elif(bishopY-diagonal==blackKingY and bishopX-diagonal==blackKingX):
                        inCheck=True
            elif(game[y][x]=="queen"):
                queenY=y
                queenX=x
                if(blackKingX==queenX or blackKingY==queenY):
                    inCheck=True
                for diagonal in range(1,9):
                    if(queenY+diagonal==blackKingY and queenX+diagonal==blackKingX):
                        inCheck=True
                    elif(queenY-diagonal==blackKingY and queenX+diagonal==blackKingX):
                        inCheck=True
                    elif(queenY+diagonal==blackKingY and queenX-diagonal==blackKingX):
                        inCheck=True
                    elif(queenY-diagonal==blackKingY and queenX-diagonal==blackKingX):
                        inCheck=True
            elif(game[y][x]=="knight"):
                knightY=y
                knightX=x
                possiblePositions=[[knightX-2,knightY+1],[knightX-1,knightY+2],[knightX+2,knightY+1],[knightX+1,knightY+2],[knightX-2,knightY-1],[knightX-1,knightY-2],[knightX+2,knightY-1],[knightX+1,knightY-2]]
                for position in possiblePositions:
                    if(position[0]==blackKingX and position[1]==blackKingY):
                        inCheck=True
    return inCheck
counter=1
for game in chessGames:
    if(isWhiteInCheck(game)):
        print("#{0}: white king is in check".format(counter))
    elif(isBlackInCheck(game)):
        print("#{0}: black king is in check".format(counter))
    else:
        print("#{0}: no king is in check".format(counter))
    counter+=1
