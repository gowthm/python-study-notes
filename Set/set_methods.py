backend_lang = {'nodejs', 'python', 'java', 'go'}
frontend_lang = {'react', 'python', 'angular'}

backend_lang.add('rust')
backend_lang.remove('go')

print("Back End:", backend_lang)
print('Front End:', frontend_lang)

print("Intersection:", backend_lang.intersection(frontend_lang))
print("Union:", backend_lang.union(frontend_lang))
print("Difference:", backend_lang.difference(frontend_lang))