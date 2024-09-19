nomes = []
notas = []
aprovacao = []
quantidade = int(input("Quantos alunos(as)? ")) #pede a quantidade de alunos, definido como int pra não aceitar input errado
for i in range (quantidade): #define a repetições conforme input do usuário
    nomeAtual = input("Digite o nome do(a) aluno(a): ")
    nomes.append(nomeAtual.title()) #separa em outra variavel para poder ajustar maiusculas e minusculas
    notaAtual = float(input("Digite a nota para este(a) aluno(a): ")) #só aceita float porque estava dando erro por ler como str

    #comparação de notas com status de aprovação:
    notas.append(notaAtual)
    if notaAtual >= 7.0:
        aprovacao.append('APROVADO')
    elif notaAtual < 3.0:
        aprovacao.append('REPROVADO')
    else:
        aprovacao.append('RECUPERAÇÃO')

aprovacaoTurma = 'SIM' if all(situacao == "APROVADO" for situacao in aprovacao) else "NÃO"
recuperacaoTurma = "SIM" if any(rec == "RECUPERAÇÃO" for rec in aprovacao) else 'NÃO'
#tupla com nome, nota e status do aluno, para ser impresso com função for
for nome, nota, status in zip(nomes, notas, aprovacao):
    sorted(len(nomes))
    tamanhoNome = len(nomes[0])
    print(f"Nome: {nome:{tamanhoNome}} | Nota: {nota} \t| {status}")
print(f'Resumo da turma:\nTodos estão aprovados? {aprovacaoTurma}\nAlguém está em recuperação? {recuperacaoTurma}')
