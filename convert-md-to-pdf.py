import markdown
import pdfkit

# Ler arquivo Markdown
with open("arquivo.md", "r") as md_file:
    md_content = md_file.read()

# Converter para HTML
html_content = markdown.markdown(md_content)

# Converter para PDF
pdfkit.from_string(html_content, "arquivo.pdf")
print("PDF gerado com sucesso!")
