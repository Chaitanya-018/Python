# #to add data in json ==> dump()
# #to read data from json file ==> load
# #if we want to perform curd operations on data structures like list,tuple,dict.
# #we can json
#
# import json
# from xml.etree.ElementTree import indent
#
# # data={'name':'john','age':24,'gender':'male'}
# # print(type(data)) #data type dict
#
# # with open('json_file.json', mode='w') as f:  #create json file and dump python data into json string
# #     json.dump(data,f,indent=4)  #we run again it will override json data
#
# # op=json.dumps(data,indent=4)  #it will convert python object to json object
# # print(op)
# # print(type(op))  #str
#
# # with open('json_file.json',mode='r') as R:
# #     read_data=json.load(R)    #read from json file & convert it into python object
# #     print(read_data)
# #     print(type(read_data))  #dict
#
#
# data={'name':'john','age':24,'gender':'male'}
# print(type(data))  #python dict
# op1=json.dumps(data,indent=4)
# print(op1)
# print(type(op1))  #json string
#
#
# op2=json.loads(op1)
# print(op2)
# print(type(op2))  #back to python dictionary
# print(op2['name'])
#
#
#
#
# import json
# names=['harish','kiran','abdul','vikas']
# with open('json_file.json',mode='w') as f:
#     dt=json.dumps(list)
#     f.write(dt)

# with open('json_file.json',mode='r') as f:
#     res=f.read()
#     convt=json.loads(res)
#     print(res)
#     print(convt[1])

#----------------------------------------------------------------------------------------------------
#07-10-2025 task

#add few names into the existing list in the file
#remove any name

# General Steps==>
# Load data from the JSON file → json.load()
# Modify the data in Python (add / remove / edit)
# Write back the updated data → json.dump()


# import json
# names=['harish','kiran','abdul','vikas']
#
# with open('json_file.json', 'r') as f:
#     data = json.load(f)  # data is a Python list
#     print(data)
#
# new_name = input("Enter name to add: ")
# data.append(new_name)
#
# with open('json_file.json', 'w') as f:
#     json.dump(data, f, indent=4)
# print("Name added successfully!")
#
# #remove name
#
# with open('json_file.json', 'r') as f:
#     data = json.load(f)
# remove_name = input("Enter name to remove: ")
# if remove_name in data:
#     data.remove(remove_name)
#     print(f"Removed '{remove_name}'")
# else:
#     print(f"'{remove_name}' not found")
# with open('json_file.json', 'w') as f:
#     json.dump(data, f, indent=4)


#8-10-25 task
import json
user=input("enter user name: ")
file_name='json_file.json'
#remove operation only for authorised persons
# remove_element=input("enter fruit name: ")
# with open(file_name,'r') as h:
#     data=json.load(h)
#     if user in data["users"]:
#         if remove_element not in data["fruits"]:
#             print(f"{remove_element} is not available")
#         else:
#             data["fruits"].remove(remove_element)
#             print(f"{remove_element} is removed successfully")
#     else:
#         print("u r not authorised to perform remove operation")
# with open(file_name,'w')as f:
#     json.dump(data,f)

#adding operation only for authorised persons
adding_element=input("enter fruit name to be add : ")
with open(file_name,'r') as h:
    data=json.load(h)
    if user in data["users"]:
        if adding_element in data["fruits"]:
            print(f"{adding_element} is already exists")
        else:
            data["fruits"].append(adding_element)
            print(f"{adding_element} is added successfully")
    else:
        print("u r not authorised to perform adding operation")
with open(file_name,'w')as f:
    json.dump(data,f,indent=4)












