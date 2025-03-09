start_list = [6]

#v1
result = 0
if len(start_list) == 0:
    print(result)
else:
    for i in start_list[::2]:
        result += i
    print(result * start_list[-1])
#v2
if start_list:
    result = int(sum(start_list[::2]) * start_list[-1])
    print(result)
else:
    print(0)
