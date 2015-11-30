def task_3(my_list):
    if my_list:
        elements_sum = 0
        for element in my_list[::2]:
            elements_sum += element
        result = elements_sum * my_list[len(my_list)-1]
    else:
        result = 0
    return result
