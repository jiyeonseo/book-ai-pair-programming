class WordDocument:
   def create(self):
       print("Word document created.")


   def get_property(self):
       print("Font, size, color")

class ExcelDocument:
   def create(self):
       print("Excel document created.")


   def get_property(self):
       print("Row, column, cell")




class DocumentEditor:
   def new_document(self, doc_type):
       if doc_type == "word":
           return WordDocument()
       elif doc_type == "excel":
           return ExcelDocument()
       else:
           raise ValueError("Unknown document type")




editor = DocumentEditor()
word_doc = editor.new_document("word")
word_doc.create()
word_doc.get_property()


excel_doc = editor.new_document("excel")
excel_doc.create()
excel_doc.get_property()