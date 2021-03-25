tasks = []

no_tasks = int(input())

for i in range(0, no_tasks):
    single_task = []
    a, b = input().split(',')

    single_task.append(int(a))
    single_task.append(int(b))

    tasks.append(single_task)

def min_max (lst):
    min_lst = []
    max_lst = []
    for element in lst:
        minimum = min(element)
        maximum = max(element)
        min_lst.append(minimum)
        max_lst.append(maximum)

    min_final = min(min_lst)
    max_final = max(max_lst)

    return min_final, max_final

 
min_hr, max_hr = min_max(tasks)
# print('min:', min_hr)
# print('max:', max_hr)

total_hours = max_hr - min_hr
# print('Total Hours:', total_hours)

work_hr_lst = []
for element in tasks:
    work_hr = element[1] - element[0] 
    work_hr_lst.append(work_hr)

# print(work_hr_lst)

if max(work_hr_lst) >= total_hours :
    # print(max(work_hr_lst))
    print(0)

elif sum(work_hr_lst) >= total_hours :
    print(sum(work_hr_lst))
    print(0)
else :
    print(total_hours- sum(work_hr_lst))