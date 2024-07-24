questions_and_options = [
["What is the Capital of India?","Delhi","Mumbai","Goa","Bangalore","a"],
["How many moon(s) does Earth have?",2,1,3,5,"b"],
["When was India's constitution implemented?",1950,2005,1947,1856,"a"],
["Who was the former Indian prime minister who was murdered by his/her bodyguard?","Jawaharlal Nehru","Mahatma Gandhi","Indira Gandhi","Savitribai Phule","c"],
["How many vowels in English?",3,1,4,5,"d"],
["How many planets in solar system?",2,4,7,8,"d"],
["How many bones in humans?",103,206,306,305,"b"],
["How many palyers in cricket team?",5,7,9,11,"d"],
["How many tentacles does an octopus has?",1,12,24,8,"d"],
["Most populated country?","India","China","America","Russia","a"],
["No of legs in a chair",1,2,3,4,"d"],
["No of teeth humans have",45,65,34,32,"d"],
["President is the _____citizen of the country","third","first","second","last","b"],
["When was pakistan created?",1967,1934,1947,1957,"c"],
["What is name of H20","water","chemical","diesel","petrol","a"]
]

prize = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1000000,2500000,5000000,10000000]

money = 0
for i in range(len(questions_and_options)):
    print(f"Question for Rs {prize[i]}/-")
    q = questions_and_options[i]
    print(f"{q[0]}")
    print(f"a.{q[1]}         b.{q[2]}")
    print(f"c.{q[3]}         d.{q[4]}")
    ans = input("Enter your option or press 0 to quit:")
    if(ans=="0"):
        print("You quit the game")
        money = prize[i-1]
        print("You've won Rs",money)
        break
    elif(ans.lower()==q[-1]):
        print(f"\nRight answer, you won Rs{prize[i]}\n")
        if(i==4):
            money = 10000
        elif(i==9):
            money = 320000
        elif(i==14):
            money = 1000000
    else:
        print(f"Wrong answer, you lose")
        break



