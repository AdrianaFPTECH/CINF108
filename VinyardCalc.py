'''
Adriana Frias
A program that calculates the size of a vineyard
'''
R = float(input('Please input the length of the row, in feet. '))
E = float(input('Please input space, in feet, used by end post assembly. '))
S = float(input('Please input the space between the vines. '))

V = (R-2*E)/S

print(V)
