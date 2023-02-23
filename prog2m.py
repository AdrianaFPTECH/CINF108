'''
Adriana Frias
A program that calculates the size of a vineyard and makes adjustments based
on the entry.
'''
R = float(input('Please input the length of the row, in feet. ')) # row length
E = float(input('Please input space, in feet, used by end post assembly. ')) # end-post space
S = float(input('Please input the space between the vines. ')) # space between vines


if R <= 50:     # if [row lenth] is less than 50...
    newE = E/2      # mult [end-post space] by 2 and store in variable newE 
    newS = S*2      # mult [end-post space] by 2 and store in var newS
elif R >= 125:  # if [row lenth] is greater than 125...
    newE = E*2      # mult [end-post space] by 2 and store in var newE
    newS = S/2      # div [space between vines] by 2 and store in var newS
else:           # if neither if the above statements are true...
    newE = E        # Don't change E
    newS = S        # Dont change S
                # this is the adjusted formula to calculate the number of vines
V = (R-2*newE)/newS 

print(f'A row {R:.2f} ft long, with {E:.2f} ft end-posts and vines {S:.2f} ft apart')
print(f' has been adjusted to {newE:.2f} ft end-posts {newS:.2f} ft apart and requires {V:.2f} vines')

   

    
