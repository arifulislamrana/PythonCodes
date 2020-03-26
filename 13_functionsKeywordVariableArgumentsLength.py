def person(name, **data):
    print(name)
    for k, v in data.items():
        print(k, v)


person('arif', age=24, phn='0172018')
person('arif', age=24, vill='musapur', phn='017201')