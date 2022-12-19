from functools import reduce

def suma(*arguments):
   total_add = 0
   for e in arguments:
      total_add += e
   print(total_add)

def resta(*arguments):
   total_substract = reduce(lambda a,b: a - b, arguments)
   print(total_substract)

def multiplicacion(*arguments):
   total_multi = reduce(lambda a,b: a*b, arguments)
   print(total_multi)

def division(*arguments): 
   total_div = reduce(lambda a,b: a/b, arguments)
   print(total_div)
