from zeep import Client

client = Client('http://localhost:7777/ws/AcademicoWebService?wsdl')


#Funciones que llaman a los servicios del cliente.
def getEstudiantes(servicio):
    return {
        servicio: client.service.getAllEstudiante()
    }[servicio]


def getAsignatura(id):
    return {"asignatura": client.service.getAsignatura(id)}["asignatura"]


def getProfesor(id):
    return {"profesor": client.service.getProfesor(id)}["profesor"]


while True:
    opcion = int(input("1- Listar estudiantes. \n"
                   "2- Buscar asignatura. \n"
                   "3- Buscar Profesor. \n"
                   "0- Salir. \n"
                   "Opcion: "))
    if opcion == 0:
        break
    elif opcion == 1:
        print(getEstudiantes("estudiantes"))
    elif opcion == 2:
        asignatura = input("Digite el id de la asignatura a consultar: ")
        print(getAsignatura(asignatura))
    elif opcion == 3:
        profesor = input("Digite el id del profesor a consultar: ")
        print(getProfesor(profesor))
