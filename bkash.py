import datetime
while True:
    a=(input('Enter Bkash USSID:\n'))
    if a == '*247#':
        print('1.Send Meny \t')
        print('2.Mobile Recherge\t')
        print('3.Payment\t')
        print('4.Cash out\t')
        print('5.Pay Bill\t')
        print('6.My Bkash\t')
        print('7.Helpline\t')
        op=int(input('Select Opation:\n'))
        if op == 1:
            print('--------------carrier info--------------\n')
            num=int(input('Enter The Bkash Number:\t'))
            am=int(input('Enter The Amount:\t'))
            re=int(input('Enter The Reference:\t'))
            pin=int(input('Enter The Pin Number:\t'))
            if pin == 8888:   
                print('\n Received Send maney request of Number',num, 'for', am,'Tk', datetime.datetime.now(),'Wait for Caonfirmation.')
            else:
                print('sorry,wrong your pin no.')
        if op == 2:
            print('---------------carrier info---------------\n')
            num=int(input('Enter mobile Number:\n'))
            am=int(input('Enter The Amount:\n'))
            re=int(input('Enter The Reference:\t'))
            pin=int(input('Enter The Pin Number:\n'))
            if pin == 8888:
                print('\n Received Recherge request of Number',num, 'for', am,'Tk', datetime.datetime.now(),'Wait for Caonfirmation.')
            else:
                print('sorry.wrong your pin no.')
        if op == 3:
            print('---------------carrier info---------------\n')
            num=int(input('Enter A Machant Number:\n'))
            am=int(input('Enter The Amount:\n'))
            re=int(input('Enter The Reference:\t'))
            pin=int(input('Enter The Pin Number:\n'))
            if pin == 8888:
                 print('\n Received payment request of Number',num, 'for', am,'Tk', datetime.datetime.now(),'Wait for Caonfirmation.')
            else:
                print('sorry.wrong your pin no.')
        if op == 4:
            print('----------------carrier info----------------\n')
            num=int(input('plese enter cash out Number:\n'))
            print('bkash\n 1. Form Agent\n 2. From ATM\n 0. Main menu\n')
            op=int(input('Please Enter Your Opation'))
            am=int(input('Enter The Amount:\n'))
            re=int(input('Enter The Reference:\t'))
            pin=int(input('Enter The Pin Number:\n'))
            if pin == 8888:
                print('\n Received Cash out request of Number',num, 'for', am,'Tk', datetime.datetime.now(),'Wait for Caonfirmation.')
            else:
                print('sorry.wrong your pin no.')
        if op == 5:
             print('---------------Pay BIll---------------\n')
             num=int(input('plese enter Pay Bill Number:\n')) 
             print('bkash\n 1 Electricity\n 2 Gas\n 3 Internet,TV and Phone\n 4 Education\n 5 Holding Tax\n 6 Other\n 0 Main Menu\n')
             op=int(input('Please Enter Your Opation'))               
             am=int(input('Enter The Amount:\n'))
             re=int(input('Enter The Reference:\t'))
             pin=int(input('Enter The Pin Number:\n'))
             if pin == 8888:
                print('\n Received Pay Bill request of Number',num, 'for', am,'Tk', datetime.datetime.now(),'Wait for Caonfirmation.')
             else:
                 print('sorry.wrong your pin no.')
        if op == 6:
             print('---------------My Bkash---------------\n')
             print('bkash\n 1 Cheak Balance\n 2 Request Statement\n 3 change Mobile Menu PIN\n 4 Manage Beneficiary\n 5 Update MNP Info\n 0 Main Menu')
             op=int(input('Please Enter Your Opation:\n'))
             pin=int(input('Enter The Pin Number:\n'))
             if pin == 8888:
                print('\n Received My Bkash request of Number',num, 'for', am,'Tk', datetime.datetime.now(),'Wait for Caonfirmation.')
             else:
                 print('sorry.wrong your pin no.')
        if op == 7:
             print('---------------Helpline---------------\n')
             print('bkash\n 1 Call 16247 or visit www.bkash.com for more info.\n 0 Main Menu')
             op=int(input('Please Enter Your Opation'))
             pin=int(input('Enter The Pin Number:\n'))
             if pin == 8888:
                 print('\n Received Helpline request of Number',num, 'for', am,'Tk', datetime.datetime.now(),'Wait for Caonfirmati.')
             else:
                 print('sorry. wrong your pin no.')
                
                
            
            
            
            
