
def opcion_us():
    while True:
        try:
            op=int(input())

            if op<=1 and op<5:
                return op
            else:
                raise ValueError
            except:
                print("opcion no valida")




def menu_usuario():
    menu = """[1] registrar alumno
[2] listar todos los alumnos
[3] buscar alumno por nivel 
[4] calcular la nota promedio 
[5] salir 

"""
    print(menu,salir="")


def ingrese_alumnos():
    nom = input("ingrese nombre del alumno: ")
    ape = input("ingrese nombre del apellido: ")
    edad = input(int("ingrese edad de alumno: "))
    nivel = input(int("ingrese nivel de curso: "))
    notas = input(int("ingrese notas: "))
    res("nombre",nom,"apellido",ape,"edad",edad,"nivel",nivel,"notas",notas)
    return res

def lista_alumnos(lista):
    cont=1
    for i in lista:
        print(f"nombres{lista [1]}")
        print(f"apellidos{lista[1]}")
        print(f"edad{lista[1]}")
        print(f"nivel{lista[1]}")
        print(f"notas{lista[1]}")

def buscar_alumnos(lista):
    for i un range(len(lista)):
        print(f"alumnos"(lista[1]))











