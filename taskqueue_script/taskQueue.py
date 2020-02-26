import os
import json

def remove_url_dir(my_url):
    l = my_url.split('\\')
    l.pop()
    new_url = '\\'.join(l)
    return new_url


def extract_line(py_file_path):

    f_read = open("abc.json","r")
    lines_list = json.load(f_read)
    f=open(py_file_path,'r')

    try:
        cnt = 1
        for x in f:
            if 'taskqueue.add' in x:
                if py_file_path not in lines_list.keys():
                    lines_list[py_file_path] = [{cnt:x.strip()}]
                else:
                    lines_list[py_file_path].append({cnt:x.strip()})
            cnt += 1
    except:
        print(py_file_path)
            
    f_write = open("abc.json","w")
    json.dump(lines_list,f_write)
    f_write.close()



# f = open('.\HappierWork\happierWork-angular-upgrade-7-GDPR','r')
def myfunc(project_path):
    my_queue = []
    for i in os.listdir(project_path):
        my_queue.append(project_path+"\\"+i)

    file_path = []

    while(len(my_queue)!= 0):
        i = my_queue.pop(0)
        # print(i)
        if os.path.isdir(i): 
            # print("Folder")
            temp = os.listdir(i)
            for j in temp:
                temp = i[:]
                temp += "\\"
                temp += j
                # print(i)
                my_queue.append(temp)
        elif '.py' == i[-3:]:
            # print(i)
            # file_path.append(i)
            extract_line(i)
    return file_path


project_path = 'happierWork'
myfunc(project_path)


