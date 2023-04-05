ACL = int(input("Cuál es el número de IPV4 ACL? "))
if ACL >= 1 and ACL <= 99:
	print("Este es un ACL IPV4 Estándar.")
elif ACL >=100 and ACL <= 199:
	print("Este es una ACL IPV4 Extendida")
else:
	print("Esta ACL IPV4 no es Extendida o Estándar. ")
