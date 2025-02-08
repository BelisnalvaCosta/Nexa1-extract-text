Analisar imagens de caixas de remédios e extrair a data de validade. Se caso você não pode usar a AWS, vamos substituir o Amazon Rekognition pelo Tesseract OCR, que é uma ferramenta de reconhecimento óptico de caracteres (OCR) de código aberto.

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