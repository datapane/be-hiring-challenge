from io import BytesIO

import matplotlib.pyplot as plt
import pandas as pd
from picklefield.fields import PickledObjectField

from django.db import models
from django.urls import reverse


class Dataset(models.Model):
    name = models.CharField(max_length=128)
    dataframe = PickledObjectField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @property
    def size(self):
        return self.dataframe.size

    def to_excel(self):
        excel_file = BytesIO()
        xlwriter = pd.ExcelWriter(
            excel_file,
            engine='xlsxwriter',
            options={'encoding':'utf-8'}
        )
        self.dataframe.to_excel(xlwriter, 'sheet')

        xlwriter.save()
        xlwriter.close()
        excel_file.seek(0)

        return excel_file.read()

    def to_pdf(self):
        pdf_file = BytesIO()
        self.dataframe.hist(bins=8)
        plt.savefig(pdf_file, format='pdf')
        pdf_file.seek(0)

        return pdf_file.read()
