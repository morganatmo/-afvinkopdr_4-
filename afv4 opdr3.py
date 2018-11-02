#AFVINKOPDRACHT 4 - OPDRACHT 3
#Morgan Atmodimedjo BIN1a

laps = 1
L = int(input("How many laps do u want to run? "))   #L stands for laps
fastest = 0     #name fastest lap
FL = 0  #FL stands for fastest lap
FLT = 0     #fastest laptime
slowest = 0     #name slowest lap
SL = 100000  #SL stands for slowest lap
SLT = 0     #slowest laptime

while laps <= L:
    print("lap", L)
    LapTime = int(input("Enter the laptime of lap", L))
    if LapTime > FL:
        fastest = L
        FL = fastest
        FLP = LapTime
    if LapTime < SL:
        slowest = L
        SL = slowest
        SLP = LapTime
    Sum_Laptime += LapTime
    L += 1
    
Average_LapTime = Sum_Laptime / L   
print ("The fastest lap: lap ", fastest," With the time being: ", FL,"\n The slowest lap: lap ", slowest,
       "With the time being: ", SL,"\n The average laptime: ",Average_LapTime)
