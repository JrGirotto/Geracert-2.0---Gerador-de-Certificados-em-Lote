# Geracert 2.0 - Gerador de Certificados em Lote

## Descrição

O **Geracert 2.0** é uma aplicação que permite a geração em lote de certificados personalizados em formato PDF. Este projeto é ideal para instituições de ensino, empresas ou eventos que desejam automatizar o processo de criação de certificados, facilitando a distribuição e aumentando a eficiência.

## Funcionalidades

- Geração em lote de certificados em PDF
- Personalização de certificados com nome, data e outras informações
- Interface simples e fácil de usar
- Exportação de certificados para um diretório especificado

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal
- **Fpdf**: Biblioteca para criação de arquivos PDF
- **Pandas**: Para manipulação de dados em lote

## Como Usar

1. Clone o repositório:
    ```bash
    git clone https://github.com/JrGirotto/Geracert-2.0---Gerador-de-Certificados-em-Lote.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd Geracert-2.0---Gerador-de-Certificados-em-Lote
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Prepare um arquivo CSV com as informações dos certificados, seguindo o formato especificado no projeto.

5. Execute a aplicação:
    ```bash
    python main.py caminho_para_o_seu_arquivo.csv
    ```

   Exemplo:
    ```bash
    python main.py dados_certificados.csv
    ```

6. Os certificados serão gerados e salvos no diretório especificado.

## Requisitos

- Python 3.x
- Dependências listadas no arquivo `requirements.txt`

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir _issues_ ou enviar _pull requests_.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
