from random import shuffle
card01=['01','03','05','07','09',11,13,15,17,19,21,23,25,27,29,31]
card02=['02','03','06','07',10,11,14,15,18,19,22,23,26,27,30,31]
card04=['04','05','06','07',12,13,14,15,20,21,22,23,28,29,30,31]
card08=['08','09',10,11,12,13,14,15,24,25,26,27,28,29,30,31]
card16=range(16,32)
card_list=[card01,card02,card04,card08,card16]
loopvar0=1
while loopvar0==1:
    result=0
    turn=1
    shuffle(card_list)
    raw_input('Think of an integer between 1 and 31 (inclusive) and press any key!')
    for card in card_list:
        loopvar1=1
        shuffle(card)
        print [str(card[0]),str(card[1]),str(card[2]),str(card[3])]
        print [str(card[4]),str(card[5]),str(card[6]),str(card[7])]
        print [str(card[8]),str(card[9]),str(card[10]),str(card[11])]
        print [str(card[12]),str(card[13]),str(card[14]),str(card[15])]
#This output is ugly as sin, but it's either this or printing single-digit
#numbers as single characters, which throws off the alignment of the numbers,
#and I think keeping the lists aligned is worth the quotes.
        if turn==1:
            print 'Is your number in this set? Look carefully!'
        elif turn==2:
            print 'How about this set?'
        elif turn==3:
            print 'And this set?'
        elif turn==4:
            print 'And this one?'
        else:
            print 'Finally, is your number in this set?'
        while loopvar1==1:
            answer=raw_input('Y/N:')
            if answer=='y' or answer=='Y':
                if card==card01:
                    result+=1
                elif card==card02:
                    result+=2
                elif card==card04:
                    result+=4
                elif card==card08:
                    result+=8
                else:
                    result+=16
                loopvar1=0
            elif answer=='n' or answer=='N':
                loopvar1=0
            else:
                print 'I\'m sorry, what was that? (Please type "y" or "n".)'
        turn+=1
    loopvar2=1
    loopvar3=1
    print 'Was your number '+str(result)+'?'
    while loopvar2==1:
        answercheck=raw_input('Y/N:')
        if answercheck=='y' or answercheck=='Y':
            print 'Of course it was. I\'m great at my job.'
            loopvar2=0
        elif answercheck=='n' or answercheck=='N':
            print 'Huh. Then one or both of us made a mistake.'
            loopvar2=0
        else:
            print 'I\'m sorry, what was that? (Please type "y" or "n".)'
    print 'Would you like to try again?'
    while loopvar3==1:
        playagain=raw_input('Y/N:')
        if playagain=='y' or playagain=='Y':
            loopvar3=0
        elif playagain=='n' or playagain=='N':
            loopvar0=0
            loopvar3=0
        else:
            print 'I\'m sorry, what was that? (Please type "y" or "n".)'
            
