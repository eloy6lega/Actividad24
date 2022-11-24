def PedirCositas():
    print('-------------------------------------')  # separador
    print('Crea una lista, un tuple, un set y un dictonary')
    lista=['Esto es una lista. Mutable y admite repetición y añadir valores. SIEMPRE es ordenada']
    tuple=('Esto es un tuple. Inmutable y no permite añadir valores')
    set={'Esto es un set. Mutable y NO admite repetición de valores. NUNCA está ordenado'}
    dictonary={'Esto es un diccionario, donde hay que metyer una key':'y un value. Es Mutable'}
    print(lista)
    print(tuple)
    print(set)
    print(dictonary)
PedirCositas()

def Apartado3y5():
    print('-------------------------------------')  # separador
    listavalores=['juan',9.95,False,'Madrid',15]
    listavalores.reverse() #ordena los valores al revés porque al haber números no puede alfabéticamente (APARTADO 5)
    for i in listavalores:
        print(i)
    listavalores.append(25.95) #Se añade al final de la lista
    print(listavalores)
Apartado3y5()

def Apartado4y5():
    print('-------------------------------------')  # separador
    tuplavalores=['juan',9.95,False,'Madrid',15]
    tuplavalores.reverse() #ordena la lista al revés porque no se puede ordenar por orden alfabético los números (APARTADO 5)
    for t in tuplavalores:
        print(t)
    #tuplavalores.append(25.95) #Las tuplas no permiten añadir valores. Dará error
    print(tuplavalores)
Apartado4y5()

def Apartado6():
    print('-------------------------------------')  # separador
    setciudades={'Madrid','Malaga','CiudadReal','Teruel','Valencia'}
    #no se puede hacer un set.sort() porque los set son unordered.
    print(setciudades)
Apartado6()

def Apartado7():
    print('-------------------------------------') #separador
    ap7={'Lunes':7,'Martes':8.5,'Miercoles':6,'Jueves':7,'Viernes':9}
    for apes in ap7:
        print(apes)
    #suma
    totalsum=0
    print(sum(ap7.values()))
    #media
    totalmed=0
    for value in ap7.values():
        #total=total+precio
        totalmed += value
        print(value)
    print(f'El total es {value}')
    print(f'El total es {value / len(ap7)}')
Apartado7()