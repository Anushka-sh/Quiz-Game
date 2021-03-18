from Easy import Easy
from Medium import Medium
from Hard import Hard

Easy_prompts = 'Easy Level'
Medium_prompts = 'Medium Level'
Hard_prompts = 'Hard Level'
Questions = [Easy_prompts, Medium_prompts, Hard_prompts]


quiz = { Easy_prompts : [
    "What Color are eggs?\n(a) White\n (b) Red\n (c) Orange\n (d) Yellow\n\n",
    "What Color are leaves?\n (a) Red\n (b) Pink\n (c) Green\n (d) Peach\n\n",
    "What Color are strawberries?\n (a) Purple\n (b) Yellow\n (c) Black\n (d) Pink\n\n",
    "What Color are Brinjal?\n (a) Pink\n (b) Purple\n (c) White\n (d) Orange\n\n"
],
Medium_prompts : [
    "Who is the Prime Minister of India?\n (a) Rahul Gandhi\n (b) Manmohan Singh\n (c) Narendra Modi\n (d) Akhilesh Yadav\n\n",
    "Who is the CEO of Facebook?\n (a) Elon Musk\n (b) Mark Zuckerberg\n (c) Jack Ma\n (d) Bill Gates\n\n",
    "Who is the Owner of Tata Consultancy Sevices?\n (a) Ratan Tata\n (b) Azim Premji\n (c) Salil Parekh\n (d) Brian Humphires\n\n",
    "Which is the largest Continent?\n (a) Europe\n (b) Antarctica\n (c) Africa\n (d) Asia\n\n"
],
Hard_prompts : [
    "What is the name of the biggest planet in our Solar System?\n (a) Mars\n (b) Uranus\n (c) Earth\n (d) Jupiter\n\n",
    "Who discovered Penicillin?\n (a) Thomas Alva Edison\n (b) Alexander Fleming\n (c) Alexander Graham Bell\n (d) Johannes Gutenberg\n\n",
    "Which is the largest living animal in the world?\n (a) The Blue Whale\n (b) Lion\n (c) Elephant\n (d) Giraffe\n\n",
    "Which movie is to be the first Bollywood film to go Plastic-Free?\n (a) Baazigar\n (b) Sholay\n (c) Coolie No. 1\n (d) Chak De India\n\n"
]
}
def get_quiz_choice():
    while True:
        try:
            quiz_number = int(input('Choose the level of quiz you like\n1 for {}\n2 for {}\n3 for {}\nYour choice:'.format(Easy_prompts, Medium_prompts, Hard_prompts)))
        except ValueError:
            print("Not a number, please try again\n")
        else:
            if 0 >= quiz_number or quiz_number > len(quiz):
                print("Invalid value, please try again\n")
            else:
                return quiz_number

questions = [
    Easy(Easy_prompts[0], "a"),
    Easy(Easy_prompts[1], "c"),
    Easy(Easy_prompts[2], "d"),
    Easy(Easy_prompts[3], "b")]

questions1 = [
    Medium(Medium_prompts[0], "c"),
    Medium(Medium_prompts[1], "b"),
    Medium(Medium_prompts[2], "a"),
    Medium(Medium_prompts[3], "d"),
]

questions2 = [
    Hard(Hard_prompts[0], "d"),
    Hard(Hard_prompts[1], "b"),
    Hard(Hard_prompts[2], "a"),
    Hard(Hard_prompts[3], "c")
]
choice = get_quiz_choice()
quiz_name = Questions[choice - 1]
print("\nYou chose the {}\n".format(quiz_name))
quiz_questions = quiz[quiz_name]
for q in (quiz_questions):
    if(choice==Easy_prompts):
        def run_test(questions):
            score = 0
            for question in Questions:
                answer = input(Easy_prompts)
                if answer == question:
                    score += 1;
                    if(score==5):
                        print("You got " + str(score) + str(len(Easy_prompts)) + "Correct: " + "Very Strong")
                    elif(score==4):
                        print("You got " + str(score) + str(len(Easy_prompts)) + "Correct: " + "Strong")
                    elif(score==3):
                        print("You got " + str(score) + str(len(Easy_prompts)) + "Correct: " + "Good")
                    elif(score==2):
                        print("You got " + str(score) + str(len(Easy_prompts)) + "Correct: " + "Bad")
                    elif(score==1):
                        print("You got " + str(score) + str(len(Easy_prompts)) + "Correct: " + "Poor")

        run_test(Easy_prompts)

    if (choice == Easy_prompts):
        def run_test(questions):
            score = 0
            for question in questions:
                answer = input(Medium_prompts)
                if answer == question:
                    score += 1;
                    if (score == 5):
                        print("You got " + str(score) + str(len(Medium_prompts)) + "Correct: " + "Very Strong")
                    elif (score == 4):
                        print("You got " + str(score) + str(len(Medium_prompts)) + "Correct: " + "Strong")
                    elif (score == 3):
                        print("You got " + str(score) + str(len(Medium_prompts)) + "Correct: " + "Good")
                    elif (score == 2):
                        print("You got " + str(score) + str(len(Medium_prompts)) + "Correct: " + "Bad")
                    elif (score == 1):
                        print("You got " + str(score) + str(len(Medium_prompts)) + "Correct: " + "Poor")

        run_test(Medium_prompts)
    if(choice==Hard_prompts):
        def run_test(questions):
            score = 0
            for question in questions:
                answer = input(Hard_prompts)
                if answer == question:
                    score += 1;
                    if(score==5):
                        print("You got " + str(score) + str(len(Hard_prompts)) + "Correct: " + "Very Strong")
                    elif(score==4):
                        print("You got " + str(score) + str(len(Hard_prompts)) + "Correct: " + "Strong")
                    elif(score==3):
                        print("You got " + str(score) + str(len(Hard_prompts)) + "Correct: " + "Good")
                    elif(score==2):
                        print("You got " + str(score) + str(len(Hard_prompts)) + "Correct: " + "Bad")
                    elif(score==1):
                        print("You got " + str(score) + str(len(Hard_prompts)) + "Correct: " + "Poor")

        run_test(Hard_prompts)

