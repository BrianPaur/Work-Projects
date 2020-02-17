#stamp PDF writer

from pdfrw import PdfReader, PdfWriter, PageMerge

#define the files

trade_ticket = "Trade_Ticket.pdf"
signature_file = "Sig.pdf"
signed_ticket = "Signed.pdf"

#define the reader and writer objects

reader_input = PdfReader(trade_ticket)
writer_output = PdfWriter()
signature_input = PdfReader(signature_file)
signature = signature_input.pages[0]

#loop through pages

for i in range(len(reader_input.pages)):
    merger = PageMerge(reader_input.pages[i])
    merger.add(signature).render()

#write file

writer_output.write(signed_ticket, reader_input)
