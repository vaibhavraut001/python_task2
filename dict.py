dict1={
    "name":"vaibhav",
    "subject":["math","bio","chem","phy"],
    "surname":"raut",
    "age":21
}
print(dict1)

dict2={
    "name":"vaibhav",
    "subject":["math","bio","chem","phy"],
    "surname":"raut",
    "age":21
}
print(dict2["name"])

dict3={
    "name":"vaibhav",
    "subject":["math","bio","chem","phy"],
    "surname":"raut",
    "age":21,
    "dict":{
        "phy":33,
        "chem":55,
        "math":55

    }
}
dict3["name"]="rahul"
print(dict3)

dict4={
    "name":"vaibhav",
    "subject":["math","bio","chem","phy"],
    "surname":"raut",
    "age":21,
    "dict":{
        "phy":33,
        "chem":55,
        "math":55

    }
}
dict4["city"]="nagpur"
print(dict4)

dict5={
    "name":"vaibhav",
    "subject":["math","bio","chem","phy"],
    "surname":"raut",
    "age":21,
    "dict":{
        "phy":33,
        "chem":55,
        "math":55

    }
}
print(dict5["dict"]["math"])

null6={}
null6["name"]="vaibahv"
print(null6)

dict6={
    "name":"rahu",
    "surname":"gandhi",
    "party":"congress",
    "member":[33,44,67,87,42]
}
print(dict6.keys())

dict7={
    "name":"rahu",
    "surname":"gandhi",
    "party":"congress",
    "member":[33,44,67,87,42]
}
print(dict7.values())

dict8={
    "name":"rahu",
    "surname":"gandhi",
    "party":"congress",
    "member":[33,44,67,87,42]
}
print(dict8.items())

dict9={
    "name":"vaibhav",
    "surname":"raut",
    "college":"raicsit",
    "age":21

}
print(dict9.get("name"))

dict10={
    "name":"vaibhav",
    "surname":"raut",
    "college":"raicsit",
    "age":21
}
dict10.update({"city":"wardha"})
print(dict10)

