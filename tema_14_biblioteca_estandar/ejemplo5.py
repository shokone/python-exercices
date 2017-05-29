from subprocess import PIPE, Popen
proceso = Popen(['ls', '-la'], stdout=PIPE, stderr=PIPE)
error = proceso.stderr.read()
lista = proceso.stdout.read()
proceso.stderr.close()
proceso.stdout.close()
if not error:
    print(lista)
else:
    print("Se produjo el error: \n%s" % error)
