import PyPDF2

with open('', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)


    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(page)

        with open(f'pagina_{page_num+1}.pdf', 'wb') as output_file:
            pdf_writer.write(output_file)
