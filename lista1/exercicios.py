####### programa 1 #######
def verifica_idade_eleitor(ano_nascimento):
    if(2022 - ano_nascimento >= 16):
        return('Apto a ser eleitor')
    else:
        return('Inapto a ser eleitor')

