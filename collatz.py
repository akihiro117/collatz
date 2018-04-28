#collatz.py
#Created by Akihiro Yamada on 2018/04/28.
#Copyright (c) 2018. All Rights Reserved.

#コラッツ数列

import sys

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

def input_number():
    is_ended = False
    while is_ended == False:
        print('整数を入力してください:')
        try:
            inputted_number = int(input())
            is_ended = True
        except ValueError:
            print('エラー：整数以外が入力されました。')
            is_ended = False
    while True:
        inputted_number = collatz(inputted_number)
        print(inputted_number)
        if inputted_number == 1:
            break

input_number()