import pandas as pd
from io import BytesIO


class ExcelConverter:
    def __init__(self, path):
        self.bio = BytesIO()
        self.df = pd.read_csv(path)
        self.writer = pd.ExcelWriter(self.bio, engine='xlsxwriter')

    def convert(self):
        self.df.to_excel(self.writer, sheet_name='Sheet1')
        self.writer.save()
        self.bio.seek(0)
        return self.bio.read()
