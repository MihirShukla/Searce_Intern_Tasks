import json
import os
file_name = os.path.basename('find_line.py')
def taskqueue_schedule():
    a = input('Search what you want: ')
    file_dict = {}
    file_list = []
    final_list = []

    f=open('task1.py','r')
    for x in f:
        if a in x:
            print('Statement exist')
            print(x)
            file_list.append(x)
            
    for i in file_list:
        final_list.append(i.strip())
    file_dict.update({file_name : final_list})
    with open("abc.json","w") as write_file:
        json.dump(file_dict,write_file,indent=2)

taskqueue_schedule()
