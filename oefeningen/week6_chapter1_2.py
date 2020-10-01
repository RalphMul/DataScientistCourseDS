def greet(lang):
  if lang == 'es':
      return ('Hola')
  elif lang == 'fr':
      return ('Bonjour')
  elif lang == 'nl':
     return ('Hallo')
  else:
      return ('Hello')

#greet('en')
#greet('fr')
#greet('es')
#greet('nl')

#def greet():
#    return "Hello"

print(greet('en'), "Glenn")
print(greet('es'), "Sally")
print(greet('fr'), "Michael")
print(greet('nl'), "Ralph")
