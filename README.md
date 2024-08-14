# Clone do Crunch em Python

Este é um script Python que replica a funcionalidade básica da ferramenta Crunch encontrada no Kali Linux, que gera wordlists baseadas em conjuntos de caracteres especificados e intervalos de comprimento.

## Funcionalidades

- Gere wordlists com conjuntos de caracteres personalizáveis.
- Especifique comprimentos mínimos e máximos das palavras.
- Salve as wordlists geradas em um arquivo especificado.

## Instalação

Você só precisa ter o Python 3.x instalado na sua máquina.

Opcionalmente, você pode criar um ambiente virtual:

   python -m venv venv


   source venv/bin/activate

## Uso

1. Para usar o script, execute o seguinte comando:

   python3 crunch.py <min_length> <max_length> <'charset'> <output_file>

   <min_length>: Comprimento mínimo das palavras.

   <max_length>: Comprimento máximo das palavras.

   <'charset'> : Conjunto de caracteres a ser utilizado na wordlist.

   <output_file>: Arquivo onde a wordlist gerada será salva.


## Como usar

   chmod +x crunch.py

   ./crunch.py 2 4 abcd123 wordlist.txt
