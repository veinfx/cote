def solution(num_list):
    last = num_list[-1]
    last_2 = num_list[-2]
    if last > last_2:
        add_item = last - last_2
    else:
        add_item = last *2
    num_list.append(add_item)
    return num_list
