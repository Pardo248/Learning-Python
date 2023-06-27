#VARIABLES
my_string_variable = "My string variable"
print(my_string_variable)
print(my_string_variable,"hi")#Los argumentos se juntan con ","

#CAMBIO DE TIPO DE VARIABLE
my_int_variable = 5
print(type(my_int_variable))

my_str_int_variable = str(my_int_variable)#De esta forma se cambian los tipos de variables
print(type(my_str_int_variable))

#VARIABLES EN UNA SOLA LINEA
name, age = "Diego", 20
#var1 , var2, var3 = 0 // esto no funciona

#FUNCIONES DE PYTHON
print(len(my_string_variable))#"len" cuenta que tan grande es el arreglo

#INPUTS
name = input("what's your name? ")
age = input("how old are you? ")

print(name)
print(age)

name = 35
age = "New Tipe"

print(name)
print(age)