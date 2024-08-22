nombre=input("Digite su nombre")
edad=int(input("Digite su edad"))
ciudad=input("Digite ciudad de residencia")
telefono=input("Digite su telefono")

x={'nombre':nombre,'edad':edad,'ciudad':ciudad,'telefono':telefono}

print(f'{x["nombre"]} tiene {x["edad"]} años, vive en {x["ciudad"]} y su numero de telefono es {x["telefono"]}')
