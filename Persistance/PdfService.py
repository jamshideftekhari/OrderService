from reportlab.pdfgen.canvas import Canvas
from pathlib import Path


class PdfService(object):

    def __init__(self, title):
        self.pdfCanvas = Canvas("../static/"+title+".pdf")

    def AddTitle(self, title):
        self.pdfCanvas.drawString(290, 720, title)

    def savePdf(self):
        self.pdfCanvas.save()