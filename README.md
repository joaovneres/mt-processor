# Simulador de Máquina de Turing

Este repositório contém a implementação de um simulador de Máquinas de Turing (MT). O programa processa arquivos de entrada no formato `.txt` e gera arquivos de saída de acordo com os resultados da execução das máquinas de turing.

## Estrutura do Projeto

- **Turing_Machines/**: Contém arquivos `.jff` que representam as máquinas de turing, que podem ser abertos e visualizados utilizando o software **JFLAP**.
  - `MT_1.jff`, `MT_2.jff`, etc.: Representam diferentes máquinas de turing que podem ser utilizados para teste ou análise.

- **Implementação/**: Contém os arquivos principais do código e arquivos de entrada e saída.
  - `main.py`: Código-fonte principal do simulador. Esse arquivo implementa a lógica para simulação das máquinas de turing e processamento dos arquivos de entrada.
  - `entradaX.txt`: Arquivos de entrada contendo as cadeias que serão processadas pelo programa.
  - `saidaX.txt`: Arquivos de saída gerados pelo programa após o processamento das entradas.

- **Raiz do projeto**:
  - `main.exe`: Arquivo executável para Windows. Pode ser executado diretamente conforme as instruções no arquivo `manualT2.txt`.
  - `manualT2.txt`: Instruções detalhadas para a execução do programa, tanto via interface gráfica quanto pelo terminal (CMD ou PowerShell).
  - `README.md`: Este arquivo, que contém uma visão geral do projeto.

## Como Executar o Programa

### Opção 1: Executando o código Python

Se você desejar executar o código diretamente em Python:

1. Certifique-se de que o Python esteja instalado em seu sistema.
2. Navegue até a pasta **Implementação**.
3. Execute o arquivo `main.py` passando os arquivos de entrada e saída:
   ```bash
   python main.py entrada.txt saida.txt
   ```

### Opção 2: Executando o executável (Windows)

Para executar o arquivo **main.exe**, siga as instruções detalhadas no arquivo `manualT2.txt` localizado na raiz do projeto.

Basicamente, basta garantir que o arquivo de entrada esteja no mesmo diretório que o **main.exe** e seguir as orientações de execução. Você pode também passar o nome dos arquivos de entrada e saída como parâmetros, caso deseje utilizar diferentes arquivos de entrada e gerar novos arquivos de saída.

## Visualizando as Máquinas de Turing

Os arquivos dentro da pasta **Turing_Machines/** são representações de máquinas de turing que podem ser abertos utilizando o software **JFLAP**. Para visualizar e interagir com as máquinas de turing:

1. Baixe o [JFLAP](https://www.jflap.org/).
2. Abra qualquer um dos arquivos `.jff` na pasta **Turing_Machines/** no JFLAP para visualizar o máquina de turing correspondente.

## Observações

- O arquivo de entrada deve seguir o formato especificado no enunciado do trabalho para que o programa funcione corretamente.
- Caso o arquivo de entrada esteja mal formatado ou não atenda às especificações, mensagens de erro serão exibidas no terminal (CMD ou PowerShell) ao executar o **main.exe**.
  
## Requisitos

- Python 3.x (para execução do `main.py`)
- Windows (para o executável `main.exe`)
- JFLAP (para visualização das máquinas de turing)