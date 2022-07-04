# # Task 1

# # from math import sqrt
# # def func():
# #     a = int(input('Enter number a: '))
# #     perimetr = a ** 2
# #     kvadrat = a * a * a
# #     diagonal = sqrt(a ** 2)
# #     return perimetr, kvadrat, diagonal
# # print(func())

# # Task 2

# # a = 0
# # b = 2
# # c = 5

# # a1 = a + b
# # b1 = c - b 
# # c = a + b + c 

# # a = a1
# # b = b1

# # print(a, b, c)


# # Task 3



# #number = '9123'
# #if number[-1] < number[-2] : 
# #    if number[-3] < number[-4]:
#  #@       print('yes')
#  #else:
#  #   print('No')


# # for i in range(10000, 100000):
# #     if i % 2 == 0:
# #         i = str(i)
# #         # Правильно, но можно было так: if i[2] in '13579' или так if int(i[2]) % 2 == 1
# #         if i[2] == '1' or i[2] == '3' or i[2] == '5'or i[2] == '7'or i[2] == '9' :
# #             answer = (int(i[0])) + (int(i[1])) +(int(i[2])) +(int(i[3])) + (int(i[4]))
# #             if answer % 4 == 0:
# #                 print(i) # Здесь должен быть i, в нем храниться само число, в answer сумма его отдельных чисел


# # Task 5
# # number = '12345'
# # max number


# # Task 8
# # for i in range(1,51):
# #     if i % 3 == 0 and i % 5 == 0:
# #         print('FizzBuzz')
# #     elif i % 3 == 0:
# #         print('Fizz')
# #     elif i % 5 == 0:
# #         print('buzz')
# #     else:
# #        print(i)
    


# # 1 --- 1
# # 2 --- 1
# # 3 --- 1
# # 4 --- 0.9
# # 5 --- 0
# # 6, 7 --- 0
# # 8 --- 1

# # Общий балл = 4.9
# '''


# '''


# '''
# import random
 
# WORDS = [  # СПИСОК
#     'python',
#     'javascript',
#     'ruby',
#     'dota'

# ]
# MAX_ERRORS = 10
 
 
# def return_random_word():  # ФУНКЦИЯ РАНДОМА
#     return random.choice(WORDS)
 
 
# def handle_user_input():  # ФУНКЦИЯ ВВОДА ЛИТЕРАЛА
#     user_input = input('Пожалуйста, введите букву: ')
#     return user_input.lower()
 
 
# def get_initial_statuses(word):  # ФУНКЦИЯ "СПИСОК FALSE = литера" [FALSE,FALSE,FALSE...]
#     statuses = []
#     for letter in word:
#         statuses.append(False)
#     return statuses
 
 
# def is_game_finished(statuses, current_errors):  # ФУНКЦИЯ "КОНЕЦ ИГРЫ или ПРОДОЛЖЕНИЕ" True или False
#     if current_errors >= MAX_ERRORS:
#         return True
#     for status in statuses:
#         if not status:
#             return False
#     return True
 
 
# def perfom_check_action(word, statuses, letter):  # ФУНКЦИЯ "БУКВА В СЛОВЕ" [FALSE, TRUE, FALSE...]
#     if letter not in word:
#         return False
 
#     for index, l in enumerate(word):
#         if letter == l:
#             statuses[index] = True
 
#     return True
 
 
# def print_word(word, statuses):  # ФУНКЦИЯ "ПЕЧАТЬ БУКВЫ В СЛОВЕ" _ _ _ Б _ _
#     for index, letter in enumerate(word):
#         if statuses[index]:
#             print(letter, end='')
#         else:
#             print('_', end=' ')
#     print()
 
 
# def main():  # ФУНКЦИЯ main()
#     word = return_random_word()
#     statuses = get_initial_statuses(word)
#     current_errors = 0
#     while not is_game_finished(statuses, current_errors):
#         print_word(word, statuses)
#         print('Осталось попыток:', MAX_ERRORS - current_errors)
#         letter = handle_user_input()
#         result = perfom_check_action(word, statuses, letter)
 
#         if not result:
#             current_errors += 1
 
#     if current_errors >= MAX_ERRORS:
#         print('Вы проиграли!')
#     else:
#         print('Вы выиграли!')
        
# main()'''

# '''for i in range(1,51):
#      if i % 3 == 0 and i % 5 == 0:
#          print('FizzBuzz')
#      elif i % 3 == 0:
#          print('Fizz')
#      elif i % 5 == 0:
#          print('buzz')
#      else:
#         print(i)'''

# with open('numbers.txt', 'w') as file1:
#     for number in range(1,21):
#         file1.write(str(number)+ '\n')

# with open('squares.txt', 'w') as  file2:
#     with open('numbers.txt') as file1:
#         data = file1.read().split('\n')
#         data.pop()
#         new_data = list(map(int, data))
#         for number in new_data:
#             file2.write(str(number ** 2) + '\n')
#             print(file2)

# def count_symbols(str_):
#     vowels = 0
#     consonants = 0
#     symbols = 0
    
#     for l in str_.lower():
#         if l in "eyuoia":
#             vowels += 1 
#         elif l in "qwrtpsdfghjklzxcvbnm":
#             consonants += 1
#         else:
#             symbols += 1
#     return f'Количество гласных: {vowels}, согласных: {consonants}, остальных символов: {symbols}'
# print(count_symbols('dota'))

# import random

# def main():
#     computer_choise = ['1', '2', '3', '4']
#     objects = {'1': 'Камень', '2': 'Ножницы', '3': 'Бумага'}
#     count = [0, 0]

#     print('Привет, давай сразимся в игру "Камень, Ножницы, Бумага"!')
#     name1 = input("Введите ваше имя: ")
#     print("Привет, меня звать", name1, "и я принимаю твой вызов!!!")
#     while True:
#         t = input('''Выберите действие (число от 1 до 4): 
#                 1) Камень
#                 2) Ножницы
#                 3) Бумага
#                 4) Выход
# '''
#         )
#         if t == '4':
#             print("До свидания!")
#             break
#         elif t not in ['1', '2', '3']:
#             print("ОШИБКА! ВВОДИТЬ МОЖНО ТОЛЬКО ЧИСЛА ОТ 1 ДО 4!")
#             break
#         else:
#             computer_turn = random.choice(computer_choise)
#             print('%s, ты выбрал %s, я выбрал %s!' % (name1, objects[t], objects[computer_turn]))
#             if t == '1' and computer_turn == '2' or t == '2' and computer_turn == '3' or t == '3' and computer_turn == '1':
#                 print('%s, ты победил!' % name1)
#                 count[0] += 1
#             elif t == '2' and computer_turn == '1' or t == '3' and computer_turn == '2' or t == '1' and computer_turn == '3':
#                 print('%s, ты проиграл!' % name1)
#                 count[1] += 1
#             else:
#                 print('%s, ничья!' % name1)
#             print('Счёт: %d:%d' % (count[0], count[1]))
#             if 5 in count:
#                 break

# if __name__ == '__main__':
#     main()
import random
import sys
name = input("Please enter your name to play Hangman! ")

print("Welcome "+name+" !. Lets play Hangman.")

wrong_attempt = int(input("How many incorrect attempts do you want ? "))

f = open('words.csv',"r")

secret_word = f.readline()
#print(secret_word)
guesses = ''
word = []
for i in secret_word.strip("\n"):
    word.append("*")
while wrong_attempt > 0 :
    word_str = ''.join([str(elem) for elem in word])

    #print(word_str)
    c = 0
    letter = input("\nGuess a word : ")
    for char in secret_word :
        if char == letter :
            word.pop(c)
            word.insert(c,char)
            c += 1
        else :
            c += 1
            if c == len(secret_word) :
                wrong_attempt -= 1
                print("Bad Luck. You have ",wrong_attempt," attempts left.")
                print("The secret word is ",secret_word)
    c=0

    word_str = ''.join([str(elem) for elem in word])
    print(word_str)
    if word_str == secret_word.strip("\n"):
        print("Yeee, you won")
        sys.exit()
if wrong_attempt == 0 :
    print("You LOSE.")