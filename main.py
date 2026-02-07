import json


class Gasto:
    def __init__(self, monto:float, categoria:str,descripcion:str):
        if monto<=0:
            raise ValueError("Monto invalido")
        
        self.monto=monto         
        self.categoria=categoria.lower().strip()
        self.descripcion=descripcion
    
    def to_dict(self):
        return {
            "monto": self.monto,
            "categoria":self.categoria,
            "descripcion":self.descripcion
        }
    
    @staticmethod
    def from_dict(datos):
        return Gasto(datos["monto"],datos["categoria"],datos["descripcion"])

    def __str__(self):
        return f"Monto: {self.monto} | Categoria : {self.categoria} | Descripcion: {self.descripcion}"
    

class GestorDeGastos:
    ARCHIVO="gastos.json"

    def __init__(self):
        self.lista_de_gastos= []
        self.cargar_lista_de_gastos()


    def cargar_lista_de_gastos(self):
        try:
            with open(self.ARCHIVO,"r") as leer_archivo:
                datos_cargados=json.load(leer_archivo)
                for i in datos_cargados:
                    elemento=Gasto.from_dict(i)
                    self.lista_de_gastos.append(elemento)   
                print("archivo cargado exitosamente")
        except FileExistsError:
            print("No se encontro el archivo")


    def registrar_gasto(self):
        try:
            gasto=float(input("ingrese monto: "))
            categoria=input("ingrese categoria: ").lower().strip()
            descripcion=input("ingrese descripcion: ")

        except ValueError:
            print(f"\n Debe ingresar un número mayor que cero \n")
            return
        
        nuevo_gasto=Gasto(gasto,categoria,descripcion)
        self.lista_de_gastos.append(nuevo_gasto.to_dict()) 
           
        with open(self.ARCHIVO,"w") as escribir_archivo:
            json.dump(self.lista_de_gastos,escribir_archivo,indent=4)
            print("Gasto añadido correctamente")
        
        

    def mostrar_todos_los_gastos(self):
        if len(self.lista_de_gastos)==0:
            print("No hay gastos registrados \n")
            return 
        else:    
            for posicion,gasto in enumerate(self.lista_de_gastos):
                posicion+=1
                print(f"{posicion}.",gasto)
            
            print("------------------------- \n")


    def total_gastos(self):
        total=0
        for gasto in self.lista_de_gastos:
            total=total+gasto["monto"]
            
        print(f"\n Gasto total: {total} \n")


    def eliminar_gasto(self):
        if len(self.lista_de_gastos)==0:
            print("No hay gastos registrados \n")
            return
        
        self.mostrar_todos_los_gastos()
        try:
            posicion_del_gasto_a_eliminar=int(input("Ingrese la posicion del gasto a eliminar: "))
            if posicion_del_gasto_a_eliminar<=0 or posicion_del_gasto_a_eliminar > len(self.lista_de_gastos):
                print("posicion no valida, verifique porfavor")
                return
        except ValueError:
            print("\n Debe ingresar un número \n")
            return

        confirmacion=input("¿Seguro? s/n: ")
        if confirmacion == "s":
            self.lista_de_gastos.pop(posicion_del_gasto_a_eliminar-1)
            print("Se elimino correctamente")
            with open(self.ARCHIVO,"w") as escribir_archivo:
                json.dump(self.lista_de_gastos,escribir_archivo,indent=4)
        else:
            return    
                
        
    def filtrar_por_categoria(self,categoria):
        lista_de_elementos_filtrados=[]

        for gasto in self.lista_de_gastos:
            if gasto.categoria==categoria:
                lista_de_elementos_filtrados.append(gasto)

        cantidad_de_elemtos_filtrados=len(lista_de_elementos_filtrados)       

        if cantidad_de_elemtos_filtrados==0: 
            print("\n No hay elementos que coincidan \n")           
        else:   
            print(f"Se encontraron {cantidad_de_elemtos_filtrados} coincidencias: \n")
            for i in lista_de_elementos_filtrados:
                print(i)   


    def mostrar_menu(self):
        while True:
                try:
                    opcion = int(input(
                        "1. Registrar Gasto\n"
                        "2. Mostrar Gastos\n"
                        "3. Total de Gastos\n"
                        "4. Filtrar por categoria\n"
                        "5. Eliminar gasto\n"
                        "0. Salir\n"
                    ))
                except ValueError:
                    print("Opción invalida")
                    continue

                match opcion:
                    case 1:
                        self.registrar_gasto()
                    case 2:
                        self.mostrar_todos_los_gastos()
                    case 3:
                        self.total_gastos()
                    case 4:
                        busqueda = input("Ingrese categoria: ").lower().strip()
                        self.filtrar_por_categoria(busqueda)
                    case 5:
                        self.eliminar_gasto()
                    case 0:
                        print("Gracias")
                        break


gasto=GestorDeGastos()
gasto.mostrar_menu()
