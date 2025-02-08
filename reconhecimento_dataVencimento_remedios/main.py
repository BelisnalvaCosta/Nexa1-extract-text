import pytesseract
from PIL import Image
import re
from datetime import datetime

# Se estiver no Windows, defina o caminho do executável do Tesseract:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extrair_data_validade(imagem_path: str):
    """ Extrai a data de validade da imagem da caixa do remédio """
    imagem = Image.open(imagem_path)
    texto_extraido = pytesseract.image_to_string(imagem)

    # Expressão regular para encontrar datas no formato DD/MM/AAAA ou MM/AAAA
    padrao_data = r"(\d{2}/\d{2}/\d{4}|\d{2}/\d{4})"
    datas_encontradas = re.findall(padrao_data, texto_extraido)

    if datas_encontradas:
        return datas_encontradas[0]  # Retorna a primeira data encontrada
    else:
        return None

def verificar_validade(data_validade: str):
    """ Verifica se o medicamento está vencido, próximo do vencimento ou válido """
    try:
        if len(data_validade) == 7:  # Se a data estiver no formato MM/AAAA
            data_validade = "01/" + data_validade  # Assume o primeiro dia do mês

        validade = datetime.strptime(data_validade, "%d/%m/%Y")
        hoje = datetime.today()

        if validade < hoje:
            return "⚠️ Medicamento VENCIDO!"
        elif (validade - hoje).days <= 30:
            return "⚠️ Medicamento PRÓXIMO DO VENCIMENTO!"
        else:
            return "✅ Medicamento dentro do prazo de validade."
    except ValueError:
        return "Erro: Formato de data inválido."

if __name__ == "__main__":
    imagem_remedio = "reconhecimento_dataVencimento_remedios/images/aeroSplay-data.jpg"  # Substitua pelo nome da imagem do medicamento
    data_validade = extrair_data_validade(imagem_remedio)

    if data_validade:
        print(f"Data de validade extraída: {data_validade}")
        alerta = verificar_validade(data_validade)
        print(alerta)
    else:
        print("⚠️ Não foi possível detectar a data de validade na imagem.")
