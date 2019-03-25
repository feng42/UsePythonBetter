def reverseint(x:int):
    if -10 < x < 10:
        return x
    str_x = str(x)
    if str_x[0] != "-":
        str_x = str_x[::-1]
        x = int(str_x)
    else:
        str_x = str_x[1:][::-1]
        x = int(str_x)
        x = -x
    return x if - 2**32 < x < 2**32 -1 else 0






if __name__ == "__main__":
    d = {'a':24, 'g':18, 'u':92, '*':42}
    sorted(d.items(), key=lambda x:x[1])
    print(d)
    # dict
    d = {key:value for (key,value) in iterable}
    #reverse
    print("aStr"[::-1])
    # exec string
    str1 = "k:1|k1:2|k2:3|k3:4"
    d1 = {}
    for items in str1.split("|"):
        key,value = items.split(":")
        d1[key] = value
    # sort by age
    alist = [{'name':'a', 'age':20}, {'name':'b','age':30}, {'name':'c','age':42}]
    alist = sorted(alist, key = lambda x:x['age'], reverse=True)
    # arithmetic progression
    print([x*11 for x in range(10)])
    # find diff
    list1 = [1,2,3]
    list2 = [3,4,5]
    set1 = set(list1)
    set2 = set(list2)
    print(set1 & set2, set1 ^ set2)
    # remove duplicates
    l1 = ['b', 'f', 'h', 'b', 'r', 's', 'f']
    l2 = list(set(l1))
    l2.sort(key=l1.index)

    #sum( 1 -- 100 )
    print(sum(range(0, 101)))