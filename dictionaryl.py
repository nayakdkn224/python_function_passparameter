person= {"first_name":"deepsk" , "last_name":"nayak","age":'30',"Gender":"Male","place":"bhubaneswar"}
print(person)
print(len(person))     
                  #use for loop for a set of data transer at a time 
for dictionaryitem in person:
    print("the key name and item value pairs in the dictionary are:", person[dictionaryitem ]])
    print(type(person))
    firstname= person["first_name"]
    print(firstname)
    lastname= person["last_name"]
    print("this last name is :",lastname)
    gender =person["Gender"]
    print(gender)
    age =person["age"]
    place =person["place"]
    print("the place is he living:",place)
    print(person.get("age"))
    print(person.get("Gender"))
                                    #add one more item into person dictionary name 
    person["hobby"]= "playing cricket"
    print(person)
    print(person.get("hobby"))
                    #remove age details from the person dictionary 
    person.pop("age")
    print(person)
    del person["hobby"]
    print(person)
                                         #use if condition for checking the item is availabe or not 
    if "place" in person:
        print("the key name 'place' is exit")
    else:
        print("the key name 'place' is not existed")

        if "place" not in person:
            print("the key name 'place'is exist")
        else:
            print("the key name 'place' is not existed")



