import pandas as pd
from io import BytesIO


class ExcelConverter:
    def __init__(self, path):
        self.buf = BytesIO()
        self.df = pd.read_csv(path)
        self.writer = pd.ExcelWriter(self.buf, engine='xlsxwriter')

    def convert(self):
        self.df.to_excel(self.writer, sheet_name='Sheet1')
        self.writer.save()
        self.buf.seek(0)
        return self.buf.read()


class PlotToPDF:
    def __init__(self, path):
        self.buf = BytesIO()
        self.df = pd.read_csv(path)

    def pdf(self):
        plot = self.df.hist()
        fig = plot[0][0].get_figure()
        fig.savefig(self.buf, format='pdf')
        self.buf.seek(0)
        return self.buf.read()
