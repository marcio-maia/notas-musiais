
NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maio': (0,2,4,5,7,9,11)}
def  escalas(tonica: str, tonalidade:str)-> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tônica e uma tonalidade
    
    Parameters:
        tonica: Nota que será a tônica da escala
        tonalidade: Tonalidade da empresa
    
    Returns:
        Um dicionário com as notas da esala e o grau

    Examples:    
        >>> escalas('C', 'maior')
        {'notas':['C','D','E','F','G','A','B'],graus:['I','II','III','IV','V','VI','VII']}

        >>> escalas('A','maior')
        {'notas':['A','B','C','D','E','F','G'],graus:['I','II','III','IV','V','VI','VII']}
    """
    intervalos = ESCALAS[tonalidade]
    tonica_pos = NOTAS.index(tonica)

    temp =[]

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) %12
        temp.append(NOTAS[nota])
    
    return {'notas':temp, 'graus':['I','II','III','IV','V','VI','VII']}    
 