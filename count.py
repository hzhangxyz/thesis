import fitz


def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text


def count_chinese_characters(text):
    count = 0
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            count += 1
    return count


print(count_chinese_characters(extract_text_from_pdf("main.pdf")))
