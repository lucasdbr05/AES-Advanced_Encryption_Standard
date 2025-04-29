# AES - Advanced Encryption Standard

Este projeto implementa o algoritmo AES (Advanced Encryption Standard) em diferentes modos de operação, além de uma versão simplificada chamada S-AES. Ele também inclui funcionalidades para criptografia e descriptografia no modo ECB usando o S-AES.

## Como executar

Para instalar as dependências e executar o programa principal, utilize os seguintes comandos:

```shell
pip install pycryptodome numpy scipy
py main.py
```

## Funcionalidades

1. **S-AES**:
   - Criptografia e descriptografia usando o algoritmo S-AES.
   - Suporte para entrada de chaves e dados em formato hexadecimal.

2. **Modo ECB com S-AES**:
   - Criptografia e descriptografia de blocos de texto no modo ECB usando o S-AES.

3. **AES em diferentes modos de operação**:
   - Implementação dos modos de operação: ECB, CBC, CFB, OFB e CTR.
   - Cálculo de entropia aproximada e tempo de execução para cada modo.

## Opções do Menu

- `0`: Encerrar o programa.
- `1A`: Criptografar usando S-AES.
- `1B`: Descriptografar usando S-AES.
- `2A`: Criptografar no modo ECB usando S-AES.
- `2B`: Descriptografar no modo ECB usando S-AES.
- `3`: Executar o AES nos diferentes modos de operação.


## Estrutura do Projeto

- `main.py`: Arquivo principal que gerencia o menu e as interações do usuário.
- `AES.py`: Implementação do AES com suporte a diferentes modos de operação.
- `S_AES.py`: Implementação do algoritmo simplificado S-AES.
- `ECB.py`: Funções para criptografia e descriptografia no modo ECB usando S-AES.
- `Logger.py`: Classe utilitária para exibir informações formatadas no console.

## Exemplo de Uso

### Criptografia com S-AES
1. Escolha a opção `1A` no menu.
2. Insira a chave em formato hexadecimal.
3. Insira o texto a ser criptografado.

### S-AES em Electronic Code Book Mode (ECB)
1. Escolha a opção `2A` no menu.
2. Insira a chave em formato hexadecimal.
3. Insira o texto a ser criptografado.

### AES em Modos de Operação
1. Escolha a opção `3` no menu.
2. O programa exibirá os resultados para cada modo de operação, incluindo o tempo de execução e a entropia.


<h2>💻 Autores</h2>

<table>
  <tr>
    <td align="center"><a href="https://github.com/lucasdbr05" target="_blank"><img style="border-radius: 50%;" src="https://github.com/lucasdbr05.png" width="100px;" alt="Lucas Lima"/><br /><sub><b>Lucas Lima - 231003406</b></sub></a><br /></td>
</table>
