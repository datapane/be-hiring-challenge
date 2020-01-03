import pandas as pd
from io import BytesIO


class PandasInMemoryMixin:
    buf, df = None, None

    def __init__(self, path):
        self.buf = BytesIO()
        self.df = pd.read_csv(path)

    def __del__(self):
        self.buf.close()

    def read_buf(self):
        self.buf.seek(0)
        return self.buf.read()


class ExcelConverter(PandasInMemoryMixin):
    def __init__(self, path):
        super().__init__(path)

    def convert(self):
        writer = pd.ExcelWriter(self.buf, engine='xlsxwriter')
        self.df.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        return self.read_buf()


class PlotToPDF(PandasInMemoryMixin):
    def __init__(self, path):
        super().__init__(path)

    def pdf(self):
        plot = self.df.hist()
        fig = plot[0][0].get_figure()
        fig.savefig(self.buf, format='pdf')
        return self.read_buf()
