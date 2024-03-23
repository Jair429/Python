"""Variables."""

player = "Messi world cup"
# print(player)

gol_messi = 100
# print(gol_messi)

messi_goat = True

gol_messi_world = str(gol_messi)
print(gol_messi_world)
print(type(gol_messi_world))

# Concatenación de variables en un print
print(player, gol_messi, messi_goat)
print("Champions legue", player)

# Algunas funciones del sistema
print(len(player))

# Variables en una sola línea
name, surname, alias, age = "Paolo", "Guerrero", "Deprerador", 40
print("Jugador Peruano:", name, surname, "Alias:", alias, "Año:", age)

# Inputs

# first_name = input(' Whats is your name: ')
# age = input(' How old are you? ')
# name = first_name = input(' Whats is your name: ')
# age = age = input(' How old are you? ')

# Cambiamos su tipo
first_name = 16
age = "Endrick"
print(first_name)
print(age)

# Forzamos el tipo
address: str = "Mi dirección"
address = 32
print(type(address))
