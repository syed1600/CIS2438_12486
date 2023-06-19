print("Davy's auto shop services") 
print("Oil change -- $35") 
print("Tire rotation -- $19") 
print("Car wash -- $7") 
print("Car wax -- $12") 
print("")  

print("Select first service:") 
serv1 = input() 
print("Select second service:") 
serv2 = input()  
total = 0 
print("") 
 
print("Davy's auto shop invoice") 
print("")  

dic = {"Oil change":35,"Tire rotation":19,"Car wash":7,"Car wax":12} 
 
if(serv1 in dic):  
    
    print("Service 1: {0}, ${1}".format(serv1,dic[serv1]))   
    total =+ dic[serv1] 

if(serv1 == "-"): 
    print("Service 1: No service")
if(serv2 in dic): 
    print("Service 2: {0}, ${1}".format(serv2,dic[serv2]))   
    total += dic[serv2]
if(serv2 =="-"): 
    print("Service 2: No service")  
print("") 

print("Total: ${0}".format(total))