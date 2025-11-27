
# Função principal do cifrador de César
def cesar(texto, deslocamento, criptografar=True):
    if not isinstance(deslocamento, int):
        return 'O deslocamento deve ser um valor inteiro.'
    if deslocamento < 1 or deslocamento > 25:
        return 'O deslocamento deve ser um inteiro entre 1 e 25.'
    if not criptografar:
        deslocamento = -deslocamento
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    d = deslocamento % len(alfabeto)
    alfabeto_deslocado = alfabeto[d:] + alfabeto[:d]
    tabela_traducao = str.maketrans(
        alfabeto + alfabeto.upper(),
        alfabeto_deslocado + alfabeto_deslocado.upper()
    )
    return texto.translate(tabela_traducao)

def criptografar(texto, deslocamento):
    return cesar(texto, deslocamento)

def descriptografar(texto, deslocamento):
    return cesar(texto, deslocamento, False)

texto_criptografado = "Pbhentr vf sbhaq va hayvxryl cynprf."
texto_descriptografado = descriptografar(texto_criptografado, 13)
print(texto_descriptografado)
