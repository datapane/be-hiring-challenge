# pylint: disable=no-member
import os
from io import BytesIO
import pandas as pd
from django.db import models
from picklefield.fields import PickledObjectField


class Dataset(models.Model):
    file_name = models.CharField(max_length=60, null=True, blank=True)
    csv_data = models.FileField(upload_to='uploads/', null=True, blank=True)
    dataframe = PickledObjectField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.file_name)

    @property
    def size(self):
        return self.dataframe.size

    # pylint: disable=abstract-class-instantiated
    def get_excel(self):
        file = BytesIO()
        writer = pd.ExcelWriter(
            file,
            engine='xlsxwriter',
            options={'encoding': 'utf-8'}
        )
        self.dataframe.to_excel(writer, 'sheet')

        writer.save()
        writer.close()
        file.seek(0)
        file_bytes = file.read()

        return file_bytes

    def get_histogram_pdf(self):
        pdf_path = os.path.join('.', 'hist_plot.pdf')
        df = self.dataframe.select_dtypes('number')
        ax = df.plot.hist()
        fig = ax.get_figure()
        fig.savefig(pdf_path)

        file = open(pdf_path, "rb")
        file_bytes = file.read()
        os.remove(pdf_path)

        return file_bytes
