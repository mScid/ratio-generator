from random import sample

#import of list
textlist = open('textlist.txt', 'r')
data = textlist.read()
data_into_list = data.split("\n")

#max value depending on length of text list
val_max = len(data_into_list)

#print title
print("L+ratio generator")

#ask for no. of values
n = int(input("how many do you want? (max " + str(val_max+2) + "):  "))

#error checking
if n > (val_max+2):
    print("error. too many xD")
    exit()
else:
    print()

#produces a non-repeating list
randomlist = sample(data_into_list, n-2)

#prints list
print(f"L + Ratio + {' + '.join(map(str,randomlist))}")