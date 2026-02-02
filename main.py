#regsitrar monto 

registroDeGastos=[]

def registrar_gasto():
    gasto=input("ingrese monto: ")
    categoria=input("ingrese categoria: ")
    descripcion=input("ingrese descripcion: ")

    registroDeGastos.append({"gasto":gasto,"categoria":categoria,"descripcion":descripcion})
    print(f"\n Gasto añadido! \n" )

def mostrar_gastos():
    for i in registroDeGastos:
        print(f"gasto: {i["gasto"]}, categoria : {i["categoria"]}, descripcion: {i["descripcion"]}")
    
    print("------------------------- \n")

def total_gastos():
    total=0
    for elemento in registroDeGastos:
        monto=float(elemento["gasto"])
        total=total+monto
        
    print(f"\n {total} \n")
   
def filtrar_por_categoria(categoria):
    total_de_elementos_filtrados=[]
    for elemento in registroDeGastos:
       if elemento["categoria"]==categoria:
           total_de_elementos_filtrados.append(elemento)

    if len(total_de_elementos_filtrados)==0: 
        print("\n No hay elementos que coincidan \n")           
    else:   
        for i in total_de_elementos_filtrados:
            print(" \n ")
            print(f"gasto: {i["gasto"]}, categoria : {i["categoria"]}, descripcion: {i["descripcion"]}")   
        


def mostrar_menu():
    entrada=input("1. Registrar Gasto \n 2. Mostrar Gasto \n 3. Total de Gastos \n 4. Filtrar por categoria \n 0. Salir \n " )
    opcion=int(entrada)
    match opcion:
        case 1:
            registrar_gasto()
            mostrar_menu()
        case 2:
            mostrar_gastos()
            mostrar_menu()
        case 3:
            total_gastos()
            mostrar_menu()
        case 4:
            busqueda=input("Ingrese categoria: ")
            filtrar_por_categoria(busqueda)
            mostrar_menu()

        case 0:
            return

                       

mostrar_menu()
print("Gracias")