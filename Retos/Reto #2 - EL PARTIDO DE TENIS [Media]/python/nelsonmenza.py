p1=0
p2=0
sequence=['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']
print(' P1   -     p2')
def checkPoints(p1,p2):
    score=[]
    players=[p1,p2]
    for p in players:
        if p==0:
            score.append("Love")
        elif p==1:
            score.append(15)
        elif p==2:
            score.append(30)
        elif p==3:
            score.append(40)
        else:
            score.append("WIN")



    if score[0]!="Love" and score[1]!="Love":
        if score[0]==score[1] and score[0]==40:
            return "Deuce"
        elif score[0]=="WIN":
            return "Jugador 1 ha ganado! "
            
        elif score[1]=="WIN":
            return "Jugador 2 ha ganado! "
            
    else:
      return f"{ score[0]}    -    {score[1]}"
        

checkPoints(p1,p2)
def main(p1,p2):
    for i in sequence:
        if i=="P1":
            p1+=1
        else:
            p2+=1

        # if p1==3 or p2==3:
        #     if p1==3:
        #         print("P1 tiene ventaja")
        #     else:
        #         print("P2 tiene ventaja")

            
        check=checkPoints(p1,p2)
        print(check)


main(p1,p2)