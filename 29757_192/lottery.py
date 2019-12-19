from random import randint
#해외취업을 목표로 하고 있기때문에, 코멘트를 영어로 달아보았습니다.
#이상한 영어표현이 있어도 양해 부탁드립니다.

def generate_numbers(): #select ramdom number between 1 to 45 
    random_number = []  #randomized number list
    count = 0           #count for list room number
    while count < 6:
        number = randint(1, 45)
        if number in random_number:
            continue
        else:
            random_number.append(number)
            count = count + 1

    for num1 in range(0,len(random_number)):
        for num2 in range(num1+1,len(random_number)):
            if random_number[num1]>random_number[num2]:
                temp=random_number[num1]
                random_number[num1]=random_number[num2]
                random_number[num2]=temp

    return random_number

def draw_winning_numbers():  #plus bonus number to random list
    test=generate_numbers()
    while True:
        number = randint(1, 45)
        if number in test:
            continue
        else:
            test.append(number)
            break

    return test

def count_matching_numbers(list1,list2): #count how much matched number
    count=0
    for temp in list1:
        if temp in list2:
           count = count +1

    return count

def check(numbers, winning_numbers): #check how much you can get the money

    count =0                         #count match number
    for num in numbers:
        if num in winning_numbers[0:6]:
            count = count +1

    if count==6:
        return 100000000
    elif count==5:
        if winning_numbers[6] in numbers:
            return 50000000
        return 1000000
    elif count==4:
        return 50000
    elif count==3:
        return 5000
    else:
        return 0

