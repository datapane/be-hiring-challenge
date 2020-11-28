from io import BytesIO
import pandas as pd
from matplotlib import pyplot
from picklefield.fields import PickledObjectField

from django.db import models


class DatasetModel(models.Model):
    name = models.CharField(max_length=50)
    dataframe = PickledObjectField()
    created_at = models.DateTimeField(auto_now_add=True)

    def size(self):
        """
        Returns dataframe size

        :return: int
        """
        return self.dataframe.size

    def get_excel(self):
        """
        Returns Excel for export

        :return: bytes
        """
        excel = BytesIO()
        # noinspection PyTypeChecker,SpellCheckingInspection
        writer = pd.ExcelWriter(excel, 'xlsxwriter')
        self.dataframe.to_excel(writer)
        writer.save()
        excel.seek(0)

        return excel.read()

    def get_plot(self):
        """
        Returns Plot on PDF

        :return: bytes
        """
        pdf = BytesIO()
        self.dataframe.hist()
        pyplot.savefig(pdf, format='pdf')
        pdf.seek(0)

        return pdf.read()

    def __str__(self):
        return self.name
