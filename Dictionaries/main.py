dic={
    # "Sanjana":"Human Being",
    # "Spoon":"Object"
    705:"Sanju",
    456:"Shreya",
    725:"Yogita",
    775:"Supriya"

}
# print(dic)
# print(dic[765]) 
# print(dic.get(900))
# print(dic.values())
# for key in dic.keys():
#     # print(dic[key])
#     print(f"The value corresponding to the key {key} is {dic[key]}")

print(dic.items())
for key,value in dic.items():
    print(f"The value corresponding to the key {key} is {dic[key]}" )
    