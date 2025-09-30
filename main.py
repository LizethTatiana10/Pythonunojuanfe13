 #creando variables y ciclos en python
menuOpciones=0

#pasos para crear una lista 
#1. se crea la variable y se iguala a corchetes
listaProductos=[]


while menuOpciones!=5:
    print("Bienvenido a la bodega Juanfe")
    print("*****************************")

    print("1. Digita 1 para agregar un producto a la bodega ")
    print("2. Digita 2 para ver todos los productos de la bodega")
    print("3. Digita 3 para calcular el costo total de la bodega ")
    
    menuOpciones=int(input("\nDigita una opcion: "))

    if menuOpciones==1:
        print("😎Comenzaremos a registrar un producto \n")


        #un producto es un diccionario (objeto)
        #pasos para crear un diccionario 
        #1. crearemos la variable utilizando llaves
        diccionarioProducto={}
        #2. agregamos valores y llaves al diccionario
        diccionarioProducto["id"]=int(input("digita al id del producto:"))
        diccionarioProducto["nombre"]=input("digita el nombre del producto:")
        diccionarioProducto["descripcion"]=input("digita la descripcion del producto:")
        diccionarioProducto["precioUnitario"]=int(input("digita el precio unitario del producto:"))
        diccionarioProducto["cantidadbodega"]=int(input("digita la cantidad del producto en bodeega:"))
        #fotografia
        diccionarioProducto["fotografia"]=input("digita una fotografia del producto:")
        #marca
        diccionarioProducto["marca"]=input("digita la marca del producto:")
        #3. AGREGANDO UN DICCIONARIO A UNA LISTA
        listaProductos.append(diccionarioProducto)
        print("\n Producto agregado con exito 😉\n")



    elif menuOpciones==2:
        print("📄Revisaremos nuestro inventario \n")
    elif menuOpciones==3:    
        print("📱estamos calculando \n")
    else:
        print("😓Aun no contamos con esas opcion.... \n")