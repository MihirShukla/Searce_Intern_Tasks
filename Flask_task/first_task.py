import json
import copy
from datetime import datetime, timedelta

with open("static_json.json", "r") as read_file:
    final_dict = json.load(read_file)

def orijson():
    json_dict = {}
    print("1st",json_dict)
    json_dict = final_dict
    print("2nd",json_dict)
    with open("static_json.json", "w") as write_file:
        json.dump(json_dict, write_file, indent=2)

#orijson()

print(final_dict)
my_data_dict = {}

inputlist = ["profile_id", "start_date", "end_date"]
'''
user_id = input("Enter user id:-")
user_profile = int(input("Enter user profile id:-"))
user_start_date = input("Enter start_date:-")
user_end_date = input("Enter end_date:-")
'''
tempdict = {}

def calculate(user_id,user_profile,user_start_date,user_end_date):
    if user_id in final_dict:
        templist = copy.deepcopy(final_dict[user_id])
        my_data_dict.update({inputlist[0]: user_profile})
        my_data_dict.update({inputlist[1]: user_start_date})
        my_data_dict.update({inputlist[2]: user_end_date})
        cnt = -1
        for x in final_dict[user_id]:
            cnt += 1
            sd_profile_id = x["profile_id"]
            sd_json = datetime.strptime(x["start_date"], "%d-%m-%Y").date()
            ed_json = datetime.strptime(x["end_date"], "%d-%m-%Y").date()
            sd_user = datetime.strptime(user_start_date, "%d-%m-%Y").date()
            ed_user = datetime.strptime(user_end_date, "%d-%m-%Y").date()
            if sd_user > ed_user:
                print("You entered invalid dates")

            else:
                if user_profile != sd_profile_id:
                    if sd_json < sd_user and sd_json < ed_user and sd_user <= ed_json and ed_json < ed_user:
                        print("Test case 1")
                        templist[cnt]["end_date"] = (sd_user - timedelta(days=1)).strftime("%d-%m-%Y")

                    elif sd_user < sd_json and ed_user < ed_json and sd_user < ed_json and sd_json <= ed_user:
                        print("Test case 2")
                        templist[cnt]["start_date"] = (ed_user + timedelta(days=1)).strftime("%d-%m-%Y")

                    elif sd_json < sd_user and sd_json < ed_user and ed_json > sd_user and ed_json > ed_user:
                        print("Test case 3")
                        temp_ed_json = ed_json.strftime("%d-%m-%Y")
                        sd_user_input_end_dates = (ed_user + timedelta(days=1)).strftime("%d-%m-%Y")
                        changed_ed_json = sd_user - timedelta(days=1)
                        templist[cnt]["end_date"] = changed_ed_json.strftime("%d-%m-%Y")
                        tempdict.update({inputlist[0]: sd_profile_id})
                        tempdict.update({inputlist[1]: sd_user_input_end_dates})
                        tempdict.update({inputlist[2]: temp_ed_json})
                        templist.append(tempdict)

                    elif sd_json == sd_user and sd_json < ed_user and sd_user < ed_json and ed_user < ed_json:
                        print("Test case 4")
                        templist[cnt]["start_date"] = (ed_user + timedelta(days=1)).strftime("%d-%m-%Y")

                    elif sd_json < sd_user and sd_json < ed_user and sd_user <= ed_json and ed_user == ed_json:
                        print("Test case 5")
                        templist[cnt]["end_date"] = (sd_user - timedelta(days=1)).strftime("%d-%m-%Y")

                    elif sd_json > sd_user and sd_json < ed_user and ed_json > sd_user and ed_json < ed_user:
                        print("Test case 6")
                        templist.remove(x)

                    elif sd_json == sd_user and sd_json < ed_user and ed_json > sd_user and ed_json < ed_user:
                        print("Test case 7")
                        templist.remove(x)

                    elif sd_json > sd_user and sd_json < ed_user and ed_json > sd_user and ed_json == ed_user:
                        print("Test case 8")
                        templist.remove(x)

                    elif sd_json == sd_user and ed_json == ed_user and sd_json < ed_user and ed_json > sd_user:
                        print("Test case 9")
                        templist.remove(x)
                    elif sd_json < sd_user and sd_json < ed_user and ed_json < sd_user and ed_json < sd_user:
                        print("Test case 10")

                    elif sd_user < sd_json and sd_user < ed_json and ed_user < sd_json and ed_user < ed_json:
                        print("Test case 11")

                    elif sd_user == ed_json and sd_user == sd_json and ed_user == ed_user and ed_user == sd_user:
                        print("Test case 21")
                        templist.remove(x)

                    elif ed_user < sd_json:
                        break

                else:
                    print("similar profiles")
                    if sd_json <= sd_user and sd_json < ed_user and sd_user <= ed_json and ed_json < ed_user:
                        print("Test case 12")
                        templist.remove(x)
                        my_data_dict["profile_id"]=user_profile
                        my_data_dict["start_date"] = sd_json.strftime("%d-%m-%Y")
                        cnt -=1

                    elif sd_user < sd_json and ed_user < ed_json and sd_user < ed_json and sd_json <= ed_user:
                        print("Test case 13")
                        templist.remove(x)
                        my_data_dict["profile_id"] = user_profile
                        my_data_dict["end_date"] = ed_json.strftime("%d-%m-%Y")
                        cnt -= 1

                    elif sd_json < sd_user and sd_json < ed_user and ed_json > sd_user and ed_json > ed_user:
                        print("Test case 14")
                        templist.remove(x)
                        my_data_dict["profile_id"] = user_profile
                        my_data_dict["start_date"] = sd_json.strftime("%d-%m-%Y")
                        my_data_dict["end_date"] = ed_json.strftime("%d-%m-%Y")
                        cnt -= 1

                    elif sd_json > sd_user and sd_json < ed_user and ed_json > sd_user and ed_json < ed_user:
                        print("Test case 15")
                        templist.remove(x)
                        cnt -= 1

                    elif sd_json <= sd_user and sd_json < ed_user and sd_user < ed_json and ed_user < ed_json:
                        print("Test case 16")
                        templist.remove(x)
                        my_data_dict["end_date"] = ed_json.strftime("%d-%m-%Y")
                        cnt -= 1

                    elif sd_json >= sd_user and sd_json < ed_user and ed_json > sd_user and ed_json < ed_user:
                        print("Test case 17")
                        templist.remove(x)
                        cnt -= 1

                    elif sd_json == sd_user and ed_json == ed_user and sd_json < ed_user and ed_json > sd_user:
                         print("Test case 18")
                         templist.remove(x)
                         cnt -= 1

                    elif sd_user < sd_json and sd_user < ed_json and ed_user < sd_json and ed_user < ed_json:
                        print("Test case 19")
                        if int((sd_json - ed_user).days) == 1:
                            templist.remove(x)
                            my_data_dict["profile_id"] = user_profile
                            my_data_dict["start_date"] = sd_user.strftime("%d-%m-%Y")
                            my_data_dict["end_date"] = ed_json.strftime("%d-%m-%Y")
                            cnt -= 1
                        else:
                            my_data_dict["profile_id"] = user_profile
                            my_data_dict["start_date"] = sd_user.strftime("%d-%m-%Y")
                            my_data_dict["end_date"] = ed_user.strftime("%d-%m-%Y")

                    elif sd_user > sd_json and sd_user > ed_json and ed_user > sd_json and ed_user > ed_json:
                        print("Test case 20")
                        if int((sd_user - ed_json).days) == 1:
                            templist.remove(x)
                            my_data_dict["profile_id"] = user_profile
                            my_data_dict["start_date"] = sd_json.strftime("%d-%m-%Y")
                            my_data_dict["end_date"] = ed_user.strftime("%d-%m-%Y")
                            cnt -= 1
                        else:
                            my_data_dict["profile_id"] = user_profile
                            my_data_dict["start_date"] = sd_user.strftime("%d-%m-%Y")
                            my_data_dict["end_date"] = ed_user.strftime("%d-%m-%Y")

                    elif sd_user == ed_json and sd_user == sd_json and ed_user == ed_user and ed_user == sd_user:
                        print("Test case 22")
                        templist.remove(x)
                        cnt -= 1

                    elif ed_user < sd_json:
                        break

        templist.append(my_data_dict)
        final_dict[user_id] = sorted(templist[:],key=lambda dates: datetime.strptime(dates["start_date"], "%d-%m-%Y"))
    

    else:
        print("added successfully")
        newdict = {}
        newlist = []
        newdict.update({inputlist[0]:user_profile})
        newdict.update({inputlist[1]: user_start_date})
        newdict.update({inputlist[2]: user_end_date})
        newlist.append(newdict)
        print(newlist)
        final_dict.update({user_id: newlist})
        print(final_dict)

    with open("static_json.json", "w") as write_file:
        json.dump(final_dict, write_file, indent=2)

   
    
    




