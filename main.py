import random as r
import os

try:
    f = open('input.txt', 'r+')
except EnvironmentError:
    f = open('input.txt', 'w')
    s = [['16', ' ', '+', ' ', '2'], ['12', ' ', '-', ' ', '3'], ['16', ' ', '*', ' ', '3'], ['24', ' ', '/', ' ', '4']]
    for i in s:
        for k in i:
            f.write(str(k))
        f.write('\n')
    f.close()
    f = open('input.txt', 'r+')

try:
    k = open('output.txt', 'r+')
except EnvironmentError:
    k = open('output.txt', 'w')

for i in f:
    i = i.replace('\n', '')
    s = i.split(' ')
    if s[1] == '+':
        a = int(s[0]) + int(s[2])
        k.write(str(a) + '\n')
    if s[1] == '-':
        k.write(str(int(s[0]) - int(s[2])) + '\n')
    if s[1] == '*':
        k.write(str(int(s[0]) * int(s[2])) + '\n')
    if s[1] == '/':
        k.write(str(int(s[0]) / int(s[2])) + '\n')
k.close()
