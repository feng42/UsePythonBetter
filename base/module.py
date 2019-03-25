def dayofyear():
    import datetime
    year = input("Please input year: ")
    month = input("Please input Month: ")
    day = input("Please input day: ")
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    date2 = datetime.date(year=int(year), month=1, day=1)
    return (date1-date2).days + 1




if __name__ == '__main__':
    #print(dayofyear())
    import random
    alist = [8,23,42, 82, 53, 167, 42]
    random.shuffle(alist)
    print(alist)