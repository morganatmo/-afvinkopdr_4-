#AFVINKOPDRACHT 4 - OPDRACHT 1
#Morgan Atmodimedjo BIN1a

#1st method
#td stands for total days
#bugs_total = 0
#td = 1

#while td <= 5:
    #bugs_per_day = int(input("How many bugs were collected today? (day", td, ")" )
    #bugs_total = bugs_total + bugs_per_day
    #td += 1

#print(bugs_total, "bugs were collected in the past 5 days")


#2nd method
bugs_day1 = int(input("How many bugs were collected at day 1? "))
bugs_day2 = int(input("How many bugs were collected at day 2? "))
bugs_day3 = int(input("How many bugs were collected at day 3? "))
bugs_day4 = int(input("How many bugs were collected at day 4? "))
bugs_day5 = int(input("How many bugs were collected at day 5? "))

bugs_total = bugs_day1 + bugs_day2 + bugs_day3 + bugs_day4 + bugs_day5

print(bugs_total, "bugs were collected in the past 5 days")
