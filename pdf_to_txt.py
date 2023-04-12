import PyPDF4
import PySimpleGUI as sg

# Define o layout da janela
layout = [
    [sg.Text('Selecione o arquivo PDF para converter')],
    [sg.Input(key='file_path'), sg.FileBrowse(file_types=(('PDF Files', '*.pdf'),))],
    [sg.Text('Selecione o local para salvar o arquivo de texto')],
    [sg.Input(key='txt_path'), sg.FolderBrowse()],
    [sg.Button('Converter'), sg.Button('Cancelar')]
]

# Cria a janela
window = sg.Window('Conversor de PDF para Texto', layout)

# Loop de eventos
while True:
    event, values = window.read()

    # Verifica se o usuário clicou no botão "Cancelar" ou fechou a janela
    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        break

    # Verifica se o usuário selecionou um arquivo PDF e um local para salvar o arquivo de texto
    if values['file_path'] != '' and values['txt_path'] != '':
        # Abre o arquivo PDF em modo de leitura binária
        with open(values['file_path'], 'rb') as pdf_file:

            # Cria um objeto PDFReader e passe o objeto de arquivo PDF para ele
            pdf_reader = PyPDF4.PdfFileReader(pdf_file)

            # Crie uma lista vazia para armazenar o texto extraído
            text = []

            # Para cada página do PDF, extraia o texto e adicione-o à lista de texto
            for page in range(pdf_reader.getNumPages()):
                text.append(pdf_reader.getPage(page).extractText())

        # Feche o arquivo PDF
        pdf_file.close()

        # Salva o arquivo de texto no local especificado pelo usuário
        txt_path = values['txt_path'] + '/output.txt'
        with open(txt_path, 'w', encoding='utf-8') as txt_file:

            # Escreva o texto extraído do PDF no arquivo de texto
            txt_file.write('\n'.join(text))

        # Exibe uma mensagem informando que a conversão foi concluída
        sg.popup('Conversão concluída. O arquivo de texto foi salvo em "{}".'.format(txt_path))

# Fecha a janela
window.close()
