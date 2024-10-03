"""
Escriba un programa que le pida a un usuario que ingrese un número entero. 
Luego, el programa va a dibujar un triángulo rectángulo en la pantalla, usando asteriscos (*), 
con la altura que corresponda al número que ingresó. 

"""

# Pedir al usuario el ingreso de un número entero
número_entero = int(input("Ingresa un número entero: "))


# Triángulo rectángulo usando asteriscos

for i in range(1, número_entero + 1):
    print('*' * i)


12
