# No. 1
def Hashtag(string):
    z = '#'
    for i in string.split():
        z += i.capitalize()
    if len(z) > 140 or len(z) < 2:
        print(False)
    else:
        print(z)
Hashtag("Hello there how are you doing")
Hashtag("  Hello   World   ")
Hashtag("")

# No. 2
def create_phone_number(number):
    if len(number) < 10 or len(number) > 10:
        print('Nomor anda salah')
    else:
        print("({}{}{}) {}{}{}-{}{}{}{}".format(number[0],number[1],number[2],number[3],number[4],number[5],number[6],number[7],number[8], number[9]))

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

# No. 3
def sort_odd_even(num):
    odd = [a for a in sorted(num) if a % 2 == 1]
    even = [b for b in sorted(num, reverse= True) if b % 2 == 0]
    for key, val in enumerate(num):
        if val % 2 == 0:
            num[key] = even[0]
            del even[0]
        elif val % 2 == 1:
            num[key] = odd[0]
            del odd[0]
    print(num)
sort_odd_even([5,3,2,8,1,4])

# No. 4
def hollow_triangle(row):
    z= ''
    for i in range (0,row,1): 
        for j in range (1, row*2):
            if j != row+i and j != row-i and i != row-1:
                z += '___'
            else: 
                z += ' # '    
        z += '\n'
    print(z)
hollow_triangle(1)
hollow_triangle(2)
hollow_triangle(3)
hollow_triangle(4)
hollow_triangle(5)
hollow_triangle(10)