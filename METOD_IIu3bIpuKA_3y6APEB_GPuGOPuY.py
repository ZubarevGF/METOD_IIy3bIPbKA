x = [5,4,3,2,1]
print("*****Значения массива до сортировки*****")
print(x)
n = len(x)

#Текущее число и следующее(При сравнении)
tek = 0
next = 0

b = 0
while(b < (n - 1)):

######## Перед входом в цикл обнулить значение а и ind (Если убрать решётки ниже, то будет виден полный процесс обмена)
    ind = 0
    a = 0
    while(a < (n - 1)):
        tek = x[ind]
        next = x[ind + 1]
        #print("tek =",tek)
        #print("next =",next)
        if (next < tek):
            #print("next < tek")
            #print(x)
            x[ind] = next
            x[ind + 1] = tek
            ind = ind + 1
        #print(x)
        a = a + 1
    b = b + 1
print("*****Значения массива после сортировки*****")
print(x)