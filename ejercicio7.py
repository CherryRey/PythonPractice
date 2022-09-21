'''Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.'''

listaord = []
for n in range(1,101):
   listaord.append(n)
    
listaord = sorted(listaord, reverse=True)
print(listaord)