import os
import tempfile
from typing import Dict

from django.core.files import File
from matplotlib.backends.backend_pdf import PdfPages
from rest_framework import serializers

from .models import Dataset
from .types import TransformedData
from .utils import transform_dataframe, filter_by_numeric_columns, load_csv


class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = ["id", "size", "dataframe"]
        read_only_fields = ["id", "size"]

    def create(self, validated_data: Dict):
        csv = validated_data["dataframe"]
        print(csv)
        dataframe = load_csv(csv)
        data = transform_dataframe(
            filename=csv.name,
            dataframe=dataframe,
            new_extension=".feather",
            transform_function="to_feather",
        )
        feather_data = File(data.data, name=data.filename)
        validated_data["dataframe"] = feather_data
        validated_data["size"] = dataframe.size
        return super().create(validated_data)

    def to_excel(self) -> TransformedData:
        dataframe = self.instance.load_dataframe()
        return transform_dataframe(
            filename=os.path.basename(self.instance.dataframe.name),
            dataframe=dataframe,
            new_extension=".xlsx",
            transform_function="to_excel",
        )

    def get_stats(self) -> Dict:
        dataframe = self.instance.load_dataframe()
        return dataframe.to_dict()

    def get_histograms_pdf(self) -> TransformedData:
        dataframe = self.instance.load_dataframe()
        numeric_columns = filter_by_numeric_columns(dataframe.dtypes.items())
        filename = os.path.basename(self.instance.dataframe.name)
        with tempfile.TemporaryDirectory() as tmp_dirname:
            tmp_path = os.path.join(tmp_dirname, "multi_histogram.pdf")
            with PdfPages(tmp_path) as pdf:
                for column in numeric_columns.keys():
                    dataframe.plot(kind="hist")
                    figure = dataframe.plot.hist(column=column)
                    pdf.savefig(figure.figure)
            data = open(tmp_path, "rb")

        return TransformedData(filename=filename, data=data)
