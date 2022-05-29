# Taller N1 - Modulo 2
# Autor: Jonnier Andres Teran Morales
# Correo= Jonnier.teran@upb.edu.co
# ID No. 502195
# id: 1003064599
# Cel: 3245644212
    
# Creamos las Variables a Utilizar con valores de prueba
a=2
b=3
c=5
d=7
e=8
f=1

# Realizamos 2 funciones para las ecuaciones
def ecuacion1():
    return (a+(b/c))/(d+(e/f))


def ecuacion2():
    return a-(b/(c-d))

# Asignamos las Ecuaciones a 2 nuevas variables
ecu1= ecuacion1()
Ecu2= ecuacion2()



# Reasignamos valores entre las variables (invertimos su valor)
ecu1,Ecu2 =Ecu2,ecu1

# Imprimimos por pantalla la Solucion Obtenida
print("Resultados Luego de Reasignar variables ecu1 -> Ecu2 y Ecu2 -> ecu1")
print("De la Expresion matematica a-(b/(c-d)) obtenemos Ecu1= ",ecu1)
print("De la Expresion matematica (a+(b/c))/(d+(e/f)) Ecu2: ",Ecu2) 

