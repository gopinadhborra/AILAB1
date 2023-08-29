from collections import defaultdict
import math;
jug1=int(input("enter the jug1 value"))
jug2=int(input("enter the jug2 value"))
aim=int(input("enter the aim"))
   
visited = defaultdict(lambda: False)
def waterJugSolver(amt1, amt2):
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(amt1, amt2)
        return True
    if visited[(amt1, amt2)] == False:
        print(amt1, amt2)
        visited[(amt1, amt2)] = True
        return (waterJugSolver(0, amt2) or
                waterJugSolver(amt1, 0) or
                waterJugSolver(jug1, amt2) or
                waterJugSolver(amt1, jug2) or
                waterJugSolver(amt1 + min(amt2, (jug1-amt1)),
                amt2 - min(amt2, (jug1-amt1))) or
                waterJugSolver(amt1 - min(amt1, (jug2-amt2)),
                amt2 + min(amt1, (jug2-amt2))))
    else:
        return False
def check():
    if (jug1<=aim) and (jug2<=aim):
        print("Not Possible")
        return True
   
    elif (jug1/2==jug2 or jug2/2==jug1) and (jug1!=aim and jug2!=aim):
        print("Not Possible")
        return True
    elif(aim%(math.gcd(jug1,jug2))!=0):
        print("Not Possible")
        return True
result=check();
if result!=True:
    print("Steps: ")
    waterJugSolver(0, 0)
