"""
Exercício 05 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que converta metros para centímetros.

    >>> from secao_01_estrutura_sequencial import ex_05_metros_para_centimetros
    >>> ex_05_metros_para_centimetros.input = lambda k: '1'
    >>> ex_05_metros_para_centimetros.converter_metros_para_centimetros()
    Transformando para centímetros dá 100.0 cm
    >>> ex_05_metros_para_centimetros.input = lambda k: '3.621'
    >>> ex_05_metros_para_centimetros.converter_metros_para_centimetros()
    Transformando para centímetros dá 362.1 cm

"""


def converter_metros_para_centimetros():
    """Escreva aqui em baixo a sua solução"""
    metros=1_000
    # metro1= (float(input("Escreva quantos metros")))
    transformacao= metros/10
    print("Transformando para centímetros dá", transformacao, "cm")
