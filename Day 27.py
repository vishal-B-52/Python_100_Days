# KBC Quiz Program

import random

print("\nWelcome to the the Kaun Banega Crorepati Quiz deviyo aur sajjano. Mai hu Shamitabh Chhappan aur aap khel "
      "rahe hai KBC.Let's PLAY THE GAME!!!!\n")

qna_og = [["____ is capital of India", "Delhi", ["Mumbai", "Delhi", "Lucknow", "Pune"]],
          ["Which year was the first ever IPL held?", "2008", ["2005", "2014", "2015", "2008"]],
          ["Who was the main actor in DDLJ ?", "Shahrokh Khan",
           ["Shahrokh Khan", "Pankaj Tripathi", "Salman Khan", "Ajay Devgan"]],
          ["T-Series is a ___ company", "Music", ["Pharmaceuticals", "Biscuit", "Music", "Packers & Movers"]],
          ["Why is 8 scared of 7?", "Because 7 ate(8) 9",
           ["Because 7 ate(8) 9", "Ye raaz usi ke saath chala gaya", "YES", "Mujhe kya malum"]],
          ["What to say when the task ahead is difficult and you are lazy?", "Angoor khatte hai",
           ["Angoor khatte hai", "Bhai 200 rupay lele par mera ye kaam karde", "It's too hard",
            "Ye to syllabus mein hai hi nahi"]],
          ["Which day is celebrated as Indian Independence day?", "15th August",
           ["13rd may", "12th April", "27th May", "15th August"]],
          ["Aasmaan se gire aur ____ mein atke", "Khajoor", ["Khejroliya", "Khajuraho", "Khajoor", "Khandesh"]],
          ["Which one of these cities do not have an IIT?", "Dholakpur",
           ["Madras", "Roorkee", "Dholakpur", "Kharagpur"]],
          ["\"God of Cricket\" is referred to whom all the time?", "Sachin Tendulkar",
           ["MS Dhoni", "Don Bradman", "Kapil Dev", "Sachin Tendulkar"]],
          ["____ starts with \'We, the people of India\'", "Indian Constitution",
           ["Shaktimaan", "Indian Constitution", "Panchtantra", "Kumkum Bhagya"]]]


def randomize_list(qna_og):
    n = len(qna_og)
    for i in range(n):
        j = random.randint(0, n - 1)
        element = qna_og.pop(j)
        qna_og.append(element)
    return qna_og


ANSWER = True
amt = 0
curr_question = 1
qna = randomize_list(qna_og)

for q in qna:
    while True:
        print(curr_question, ".", q[0])
        A = q[2][0].ljust(22 - len(q[2][0]))
        C = q[2][2].ljust(21 - len(q[2][2]))
        print("A", ".", A, "\t\tB", ".", q[2][1])
        print("C", ".", C, "\t\tD", ".", q[2][3])
        my_option = input("Lock Option (Enter option, not answer):- ")
        if len(my_option) > 1 or len(my_option) < 1:
            print("Invalid Option. Let me repeat question.\n")
            continue
        else:
            if my_option.isalpha():
                my_option = my_option.upper()
                if my_option == "A":
                    ANSWER = q[2][0] == q[1]
                elif my_option == "B":
                    ANSWER = q[2][1] == q[1]
                elif my_option == "C":
                    ANSWER = q[2][2] == q[1]
                elif my_option == "D":
                    ANSWER = q[2][3] == q[1]
                else:
                    print("Invalid Option. Let me repeat question.\n")
                    continue
                break
            else:
                print("Invalid Option. Let me repeat question.\n")
                continue

    if ANSWER:
        if curr_question == 1:
            amt += 1000
        elif 2 <= curr_question < 5:
            amt += 3000
        elif 5 <= curr_question <= 9:
            amt *= 2
        elif curr_question == 10:
            print("\n\n10 LAKH!!!!")
            print("Adbhut!! Aaap jeet chuke hai 10 Lakh ki dhanrashi. Very well played!!")
            print("\nHamare saath ye adbhut khel khelne ke liye dhanyavaad.")
            break
        print("Sahi Jawab!! Aapne jeete hai --> ₹", amt, "\n")

    else:
        print("\nYe jawaab..... galat hai. Aapka khel yahi sampath hota hai.")
        print("Aap ghar le ja sakte hai ₹", amt, "dhanrashi.")
        print("\nHamare saath bane rahane ke liye shukriya")
        break
    curr_question += 1
