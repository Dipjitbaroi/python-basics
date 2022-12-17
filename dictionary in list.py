exampledictionary1 = { "name":"Dip","et":34,"session":"19-20"}
exampledictionary2 = { "name":"Basar","et":46,"session":"19-20"}
exampledictionary3 = { "name":"Ashraful","et":64,"session":"19-20"}

examplelist1 = [exampledictionary1,exampledictionary2,exampledictionary3,]
examplelist2 = ["names of the students:",exampledictionary1["name"],exampledictionary2["name"],exampledictionary3["name"]]
examplelist3 = ["class rolls of the students:",exampledictionary1["et"],exampledictionary2["et"],exampledictionary3["et"]]
studentInput = input("Enter the name or et of the student:",)
for x in range(len(examplelist1)):
    item= examplelist1[x]
    if item["name"]==studentInput:
        print(item)
    elif str(item["et"])==studentInput:
        print(item)