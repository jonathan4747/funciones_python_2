# cuenta Regresiva
def cuentaRegresiva(num):
    arr=[]
    for i in range(num,-1,-1):
        arr.append(i)
    return arr
num=cuentaRegresiva(5)
print(num)

#imprimir y devolver
def imprimir_y_devolver(arr):
    print(arr[0])
    return arr[1]
arr=imprimir_y_devolver([1,2])
print(arr)
#primero mas longitud
def primero_mas_longitud(arr):
    sum = arr[0]+len(arr)
    return sum
arry=primero_mas_longitud([1,2,3,4,5])
print(arry)

#valore mayores que el segundo
def valore_mayores_que_el_segundo(arr):
    if(len(arr)<=2):
        return False
    elif (len(arr)>2):
        Arry=[]
        print(arr[2])
        for i in range(0,len(arr)):
            if arr[i]>=arr[2]:
                Arry.append(arr[i])
        return Arry
array1=valore_mayores_que_el_segundo([5,2,3,2,1,4])
print(array1) 
array2=valore_mayores_que_el_segundo([3])
print(array2)     

#esta longitud,ese valor
def length_and_valuer(long,num):
    arr=[]
    for i in range(0,long):
        arr.append(num)
    return arr
array3=length_and_valuer(4,7)
print(array3)
array4=length_and_valuer(6,2)
print(array4)