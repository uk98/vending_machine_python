import vm

li=[]
transaction,tot_a,opt = 0,0,'y'
file1 = open("data.txt","a+")
vm.welcome()
vm.menu()
vm.options()
choice = input('Enter the item number(1-5): ')
while opt=='y':
    if choice in vm.options().keys() or choice=='5':
        if choice == '5':
            print('Exiting')
            break
        else:
            i = vm.options().get(choice)[1]
            li.append(i)
            tot_a+=vm.options().get(choice)[2]
            transaction+=1
            for item in li:
                print(item)
            print('Total Amount: ',tot_a)
            opt = input('Want to buy again?(y/n): ')
            if opt=='n':
                print('\n||||Bill||||')
                print('>Total Amount: ',tot_a)
                print('Pay in denominations of 100,50 and 10\n')
                tot = (int)(input('Enter the amount you want to enter: '))
                if tot<tot_a:
                        a = (int)(input('Enter more money:'))
                        tot+=a
                while not tot%10==0:
                    print('Pay in denominations of 100,50 and 10\n')
                    tot = (int)(input('Enter the amount you want to enter: '))
                    if tot<tot_a:
                        a = (int)(input('Enter more money:'))
                        tot+=a
                        
                print('Refunded : ',tot-tot_a)
                break
                
            while opt not in ('y','n'):
                print('Wrong input! Enter again')
                opt = input('Want to buy again?(y/n): ')
            vm.menu()
            choice = input('Enter the item number(1-5): ')

    else:
        print('Invalid Choice!Enter again!!\n')
        vm.menu()
        choice = input('Enter your choice(1-5): ')
file1.write('\nReceipt: ')
file1.write('\nItems bought:')
file1.write(str(transaction))
file1.write('\n')
file1.write(str(li))  
file1.write('\nTotal Amount : ')
file1.write(str(tot_a))
file1.write('\nAmount Paid : ')
file1.write(str(tot))
file1.write('\nRefunded : ')
file1.write(str(tot-tot_a))
file1.write('\n')
file1.close()
        
    