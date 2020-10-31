def avg(*list_numbers:float)->float: #* zeby dać wiecej argumentów
    # print(type(list_numbers)) #<class 'tuple'>
    total = 0
    for num in list_numbers:
        if isinstance(num, (int, float)):
            total += num
        else:
            raise TypeError("Wrong input data. Please make sure tha evertyhing is a number.")

    return total/len(list_numbers)




if __name__ == "__main__":
    # print(avg(1,2,3,4,5)) # 1,2,3,4,5 jest przez pythona jako tupla traktowane
    # print(avg(1,2,3,4,5, "Mohammad")) # 1,2,3,4,5 jest przez pythona jako tupla traktowane
    print(avg(1,2,3,4,5, True)) # 1,2,3,4,5 jest przez pythona jako tupla traktowane