def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    kev_scr = 0 # kevin's score
    stu_scr = 0 # stuart's score
    
    for i in range(len(string)):
        if string[i] == vowels:
            kev_scr += (len(string) - i)
        else:
            stu_scr += (len(string) - i)
            
    if kev_scr > stu_scr:
        print('Kevin', kev_scr)
    elif stu_scr > kev_scr:
        print('Stuart', stu_scr)
    else:
        print('DRAW')

if __name__ == '__main__':
    s = input()
    minion_game(s)