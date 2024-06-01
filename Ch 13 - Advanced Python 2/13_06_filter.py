def greater_than_5(num):
    if(num>5):
        return True

    else:
        return False

l = [1, 2 , 3, 67, 47, 98]
print(list(filter(greater_than_5, l)))