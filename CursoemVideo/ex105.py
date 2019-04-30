def notas(*n, sit=False):
    """
    -> Funcao para analisar notas e situacoes de varios alunos
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou nao adicionar a situacao
    :return: dicionario com varias informacoes sobre a situacao da turma
    """
    alunos = dict()
    alunos['total'] = len(n)
    alunos['maior'] = max(n)
    alunos['menor'] = min(n)
    alunos['media'] = sum(n)/len(n)
    if sit:
        if alunos['media'] >= 7:
            alunos['situacao'] = 'BOA'
        elif alunos['media'] < 5:
            alunos['situacao'] = 'RUIM'
        else:
            alunos['situacao'] = 'RAZOAVEL'
    return alunos


resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
help(notas)
