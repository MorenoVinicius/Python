import os
import PyPDF2

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
folder_path = os.path.join(desktop_path, 'Arquivos Separados')

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

with open('holerites.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file) # substituir PdfReader por PdfFileReader
    num_pages = len(pdf_reader.pages)


    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        pdf_writer = PyPDF2.PdfWriter() # substituir PdfWriter por PdfFileWriter
        pdf_writer.add_page(page)

        output_path = os.path.join(folder_path, f'pagina_{page_num+1}.pdf')
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)


