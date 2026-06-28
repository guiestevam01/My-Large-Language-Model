aluno = {
    "nome": "Guilherme",
    "idade": 19
}
print(aluno.get('nome'))
aluno["cidade"] = "Maringá"
print(aluno.get('cidade'))

print(f"Nome do aluno: {aluno.get('nome')}")
aluno["idade"] = 23
print(aluno.get('idade'))

#sets
numeros = {1,2,3,4}
print(numeros)
numeros_2 = {1,1,2,3,6,7}
print(numeros_2)
uniao = numeros.union(numeros_2)
print(uniao)

lista = [1,2,34,2,32,3,4,2,]
lista_set = set(lista)
print(lista_set)