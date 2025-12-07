print("menu de utilidades")
print("1 - Calculadora (sumar , restar, multiplicar)")
print("2 - Comprobar de edad")
print("3 - Clasificar de notas")

opcion =input("elige una opcion (1/2/3):")




if opcion   == "1":
    print("calculadora")
    numero1 = int(input("escribe el primer numero: "))
    numero2 = int(input("escribe el segundo numero: "))


    print("que quieres hacer?")
    print("1 - sumar")
    print("2 - restar")
    print("3 - multiplicar")
    op_calc = input("Elige una opcion (1/2/3): ")

    if op_calc == "1":
        resultado = numero1 + numero2
        print("el resultado de la suma es", resultado )

    elif op_calc == "2":
        resultado= numero1 - numero2
        print("el resultado de la resta es ", resultado)
    elif op_calc == "3":
        resultado = numero1 * numero2
        print (" el resultado de la multiplicacion es", resultado)

    else:
        print( "opcion no valida")


elif opcion == "2":
    print("comprobador de edad")
    edad = int(input("escribe tu edad:"))

    if edad >= 18:
        print(" eres mayor de edad")
    else:
        print(" eres menos de edad")


elif opcion == "3":
    print ("clasificador de notas")
    nota = float(input("escribe tu nota (0-10):"))

    if nota >= 9:
        print("sobresaliente")
    elif nota >=7 and nota <9:
        print ("notable")
    elif nota >= 5:
        print ("aprobado")
    else:
        print("suspenso")
else:
    print("opcion del menu no valida")
