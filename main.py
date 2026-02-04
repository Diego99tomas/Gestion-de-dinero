#regsitrar monto 

lista_de_gastos= []

def registrar_gasto():
    try:
        gasto=float(input("ingrese monto: "))
        if gasto <= 0:
            print("\n El monto debe ser positivo y mayor que cero \n")
            return
        
    except ValueError:
        print("\n Debe ingresar un número \n")
        return

    categoria=input("ingrese categoria: ").lower().strip()
    descripcion=input("ingrese descripcion: ")

    lista_de_gastos.append({"gasto":gasto,"categoria":categoria,"descripcion":descripcion})
    print(f"\n Gasto añadido! \n" )
    

def mostrar_todos_los_gastos():
    if len(lista_de_gastos)==0:
        print("No hay gastos registrados")
    else:    
        for posicion,i in enumerate(lista_de_gastos):
            posicion+=1
            print(f"{posicion}. Gasto: {i['gasto']} | categoria : {i['categoria']} | descripcion: {i['descripcion']}")
        
        print("------------------------- \n")


def total_gastos():
    total=0
    for elemento in lista_de_gastos:
        monto=elemento["gasto"]
        total=total+monto
        
    print(f"\n Gasto total: {total} \n")

   
def filtrar_por_categoria(categoria):
    total_de_elementos_filtrados=[]

    for elemento in lista_de_gastos:
       if elemento["categoria"]==categoria:
           total_de_elementos_filtrados.append(elemento)

    if len(total_de_elementos_filtrados)==0: 
        print("\n No hay elementos que coincidan \n")           
    else:   
        for i in total_de_elementos_filtrados:
            print(f"gasto: {i['gasto']} | categoria : {i['categoria']} | descripcion: {i['descripcion']}")   


def mostrar_menu():
    while True:
            opcion = int(input(
                "1. Registrar Gasto\n"
                "2. Mostrar Gastos\n"
                "3. Total de Gastos\n"
                "4. Filtrar por categoria\n"
                "0. Salir\n"
            ))

            match opcion:
                case 1:
                    registrar_gasto()
                case 2:
                    mostrar_todos_los_gastos()
                case 3:
                    total_gastos()
                case 4:
                    busqueda = input("Ingrese categoria: ").lower().strip()
                    filtrar_por_categoria(busqueda)
                case 0:
                    print("Gracias")
                    break


mostrar_menu()
