import struct

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
arquivo = open("cep.dat","rb")
line = arquivo.read(registroCEP.size)
i = 0

# Loop para a verificacao da quantidade de valores
while line != " ":
    arquivo.readlines()

    # insere os valores na lista
    registroCEP.unpack(line)
    i += 1
arquivo.close()

# ordena a lista de uma vez usando o metodo sort()
registroCEP.sort()

# imprime os valores ordenados
print(registroCEP)

# Atualiza o arquivo para inserir os valores ordenados
arquivo = open("cep.dat", "w")
i = 0
while i < registroCEP.size:
    # escreve os valores no arquivo
    arquivo.write(("%s" % (registroCEP[i])))
    i += 1
arquivo.close()
