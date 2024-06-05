import random
import sys

# Question bank for levels
LEVEL1_QUESTIONS = [
    ["Which of these food items has different varieties such as: 'Sujika _______', 'Aateka _______', 'Moong dal ka _________' and 'Gajarka _________'?",
     "A. Sharbat", "B. Halwa", "C. Pakora", "D. Chaat", "B", "b"],
    ["Which of these is the name of a type of women’s clothing?",
     "A. Padmini", "B. Man Bai", "C. Jodha", "D. Anarkali", "D", "d"],
    ["Which of these foods would complete the name of these three common dishes: Kadhai _______, Shahi _______, and Matar ______?",
     "A. Dahi", "B. Ghee", "C. Paneer", "D. Khoya", "C", "c"],
    ["Which of these is a board game which can normally be played by only two opponents at a time?",
     "A. Snakes and Ladders", "B. Chess", "C. Ludo", "D. Monopoly", "B", "b"],
    ["Which organization is the birthplace of World Wide Web?",
     "A. CERN", "B. NASA", "C. IUPAP", "D. University of Cambridge", "A", "a"],
    ["What do koalas like to eat?",
     "A. Carrots", "B. Yogurt", "C. Eucalyptus leaves", "D. Chives", "C", "c"],
    ["What is the correct synonym of 'DEMENTED'?",
     "A. Noisy", "B. Insane", "C. Dangerous", "D. Happy", "B", "b"],
    ["How many states make up the United States of America?",
     "A. 39", "B. 49", "C. 27", "D. 50", "D", "d"]
]

LEVEL2_QUESTIONS = [
    ["Which state is known as ‘The Empire State’?",
     "A. Washington DC", "B. The New York City", "C. California State", "D. Chicago", "B", "b"],
    ["Which is the executive office and residence of the Korean President?",
     "A. White House", "B. Blue House", "C. Golden House", "D. Green House", "B", "b"],
    ["Grand Central Terminal, Park Avenue, New York is the",
     "A. Largest railway station", "B. Highest railway station", "C. Longest railway station", "D. None of the above", "A", "a"],
    ["For which of the following disciplines is Nobel Prize awarded?",
     "A. Physics and Chemistry", "B. Physiology and Medicine", "C. Literature, Peace and Economics", "D. All of the above", "D", "d"],
    ["Which country invented football?",
     "A. England", "B. USA", "C. Africa", "D. Germany", "A", "a"],
    ["Which place on earth is the coldest to live?",
     "A. Oymyakon-Russia", "B. Antarctica", "C. Gobi desert", "D. Ireland", "A", "a"],
    ["How many squares are there in the chessboard?",
     "A. 48", "B. 56", "C. 64", "D. 128", "C", "c"],
    ["Which blood type is known as the universal blood donor?",
     "A. B-", "B. O-", "C. O+", "D. A-", "B", "b"],
    ["Name two countries that allow taking a nap during work?",
     "A. Italy and Spain", "B. Australia and Austria", "C. Mexico and Texas", "D. America and France", "A", "a"],
    ["Which country developed the Skype software?",
     "A. Estonia", "B. Japan", "C. Germany", "D. USA", "A", "a"]
]

LEVEL3_QUESTIONS = [
    ["The language spoken by people in Pakistan is?",
     "A. Hindi", "B. Sindhi", "C. Palaun", "D. Naraun", "B", "b"],
    ["Which animal has three hearts?",
     "A. Whale", "B. Dolphin", "C. Starfish", "D. None of these", "D", "d"],
    ["Which country is Prague in?",
     "A. Czech Republic", "B. Croatia", "C. Finland", "D. Guyana", "A", "a"],
    ["Who was the First Commander in Chief of the Kaurava Army?",
     "A. Drona", "B. Bheeshma", "C. Karna", "D. Ashvathama", "B", "b"],
    ["The language of Lakshadweep, a Union Territory of India, is",
     "A. Tamil", "B. Hindi", "C. Malayalam", "D. Telugu", "C", "c"],
    ["The western ghats in Maharashtra is known as?",
     "A. Nilgiris", "B. Sahyadri", "C. Cardomom Hills", "D. Anamalai Hills", "B", "b"],
    ["Researchers of which institute has designed a paper-based sensor to detect the quality of milk?",
     "A. IIT Hyderabad", "B. IIT Bombay", "C. IIT Guwahati", "D. IIT Delhi", "C", "c"],
    ["Which is the longest snake in the world?",
     "A. Anaconda", "B. Reticulated Python", "C. Black Mamba", "D. Puffer Adder", "B", "b"],
    ["How many bones are in the human adult body?",
     "A. 202", "B. 204", "C. 200", "D. 206", "D", "d"],
    ["Which of the following is radioactive?",
     "A. Caesium", "B. Germanium", "C. Aluminium", "D. Magnesium", "A", "a"],
    ["Who is the founder of AIADMK?",
     "A. M.G. Ramachandran", "B. Jayalalitha", "C. Annadurai", "D. None of the above", "A", "a"],
    ["What is the name of the disease that arises due to vitamin B1 deficiency?",
     "A. Scurvy", "B. Beriberi", "C. Pellagra", "D. Gingivitis", "B", "b"]
]

def welcome_user():
    name = input('Hey there, enter your name: ')
    print(f'Welcome to the quiz, {name}!!!')
    print('''
    These are the guidelines of the game:
       - There are 3 levels - easy, moderate, and hard.
       - Each of the 8 questions in Level 1 has 1 point.
       - To clear Level 1 and proceed to Level 2 you must score a minimum of 4 points.
       - Each of the 10 questions in Level 2 has 3 points.
       - To clear Level 2 and proceed to Level 3 you must score a minimum of 12 points.
       - Each of the 12 questions in Level 3 has 5 points.
       - To clear Level 3 you must score a minimum of 20 points.
       - In all three levels, each wrong answer warrants 1 negative point.
    Enjoy the quiz!
    ''')

def ask_to_start():
    response = input('Are you ready to start? (yes or no): ')
    if response.lower() != 'yes':
        print('Ok cool! See you later!!')
        sys.exit()

# def ask_question(question):
#     print(question[0])
#     for i in range(1, 5):
#         print(question[i])
#     print()
#     answer = input("Answer: ").strip()
#     return answer.lower() in (question[5], question[6])
# def ask_question(question):
#     print(question[0])
#     for i in range(1, 5):
#         print(question[i])
#     print()
#     answer = input("Answer: ").strip().lower()

#     if answer in (question[5], question[6]):
#         print('CORRECT ANSWER!!!')
#         return True
#     else:
#         print(f'WRONG ANSWER. The correct answer is: {question[int(question[5])]}')
#         return False
def ask_question(question):
    print(question[0])
    for i in range(1, 5):
        print(question[i])
    print()
    answer = input("Answer: ").strip().lower()

    if answer in (question[5], question[6]):
        print('CORRECT ANSWER!!!')
        return True
    else:
        correct_answer_index = 5 if question[5].isalpha() else 6
        correct_answer = question[correct_answer_index]
        print(f'WRONG ANSWER. The correct answer is: {correct_answer}')
        return False



def run_level(questions, num_questions, points_per_correct, required_score):
    score = 0
    questions = random.sample(questions, num_questions)
    
    for question in questions:
        if ask_question(question):
            score += points_per_correct
        else:
            score -= 1
        print(f'You have a total of {score} points.')
        print()
    
    if score >= required_score:
        return score
    else:
        print(f'You needed {required_score} points to pass this level. Thank you for playing!')
        sys.exit()

def main():
    welcome_user()
    ask_to_start()

    # Level 1
    score = run_level(LEVEL1_QUESTIONS, 8, 1, 4)
    print(f'Congrats, you passed Level 1 with {score} points! Here is your first question for Level 2...')

    # Level 2
    score += run_level(LEVEL2_QUESTIONS, 10, 3, 12)
    print(f'Congrats, you passed Level 2 with a total of {score} points! Here is your first question for Level 3...')

    # Level 3
    score += run_level(LEVEL3_QUESTIONS, 12, 5, 20)
    print(f'Congrats, you passed Level 3 with a total of {score} points! You are a quiz master!')

if __name__ == "__main__":
    main()
