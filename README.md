# 1 - OCR Lista Escolar e
# 2 - Reconhecimento da data de vencimento de remédios [^1].

Projeto usado para exemplificar o uso do [AWS Textract](https://docs.aws.amazon.com/pt_br/textract/latest/dg/API_DetectDocumentText.html) na extração de textos em imagens simples.

## Pré requisitos

- Python
- Uv
- Conta AWS

## Configuração do ambiente

É necessário configurar um usuário no IAM com acesso ao serviço Textract.

## Instalação

Para instalar as dependências do projeto utilize o comando:

```sh
uv install
```

## Execução

```

uv run main.py
```
# 2 - reconhecimento_dataVencimento_remdios
Para Analisar imagens de caixas de remédios e extrair a data de validade. Como eu não posso usar a AWS, eu substitui o Amazon Rekognition pelo Tesseract OCR, que é uma ferramenta de reconhecimento óptico de caracteres (OCR) de código aberto.

Este novo código irá:

Ler a imagem da caixa do remédio.
Extrair a data de validade usando OCR (Tesseract).
Verificar se o medicamento está vencido, próximo do vencimento ou válido.
Gerar um alerta para o responsável pelo estoque.

Pré-requisitos:
Instalar o Tesseract OCR (se ainda não tiver instalado):
No Windows: Baixe e instale Tesseract OCR.

No Linux (Ubuntu/Debian):
sudo apt update && sudo apt install tesseract-ocr -y

No MacOS:
brew install tesseract

Instalar as dependências do Python:
pip install pytesseract pillow

Como funciona:
O código lê a imagem da caixa do remédio.
Usa OCR para extrair a data de validade.
Analisa a data e dá um alerta:
Vencido → Exibe ⚠️ "Medicamento VENCIDO!"
Menos de 30 dias para vencer → Exibe ⚠️ "Medicamento PRÓXIMO DO VENCIMENTO!"
Data válida → Exibe ✅ "Medicamento dentro do prazo de validade."

[^1]: 1° Projeto exemplo do código do expert Guilherme Carvalho e o 2ª código, eu ao invés de fazer com a imagens de jogadores eu fiz com caixas de remédios para ver as datas e validades dos mesmos.
