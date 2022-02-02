import tempfile
from io import BytesIO, StringIO
from pathlib import Path

import pandas as pd
from django.core.files import File
from rest_framework import serializers

from .models import DatasetModel
import logging

logger = logging.getLogger(__name__)

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetModel
        fields = ["id", "file", "obj_size"]
        read_only_fields = ["id", "obj_size"]

    def validate_file(self, value):
        filename = value.name
        logger.warn(f"filename: {filename}")
        if not str(filename).endswith(".csv"):
            raise serializers.ValidationError("The only supported file type is .csv")
        return value

    def create(self, validated_data):
        csv = validated_data["file"]
        filename = csv.name
        decoded_file = csv.read().decode()
        io_str = StringIO(decoded_file)
        with tempfile.TemporaryDirectory() as tmpdirname:
            tmp_filepath = Path(filename).with_suffix(".csv")
            tmp_filepath = tmpdirname / tmp_filepath

            pd.read_csv(io_str).to_csv(tmp_filepath)
            with open(tmp_filepath, "rb") as ft:
                feather_data = ft.read()
                feather_data = BytesIO(feather_data)
            validated_data["obj_size"] = tmp_filepath.stat().st_size
            validated_data["file"] = File(feather_data, name=filename)
        return super().create(validated_data)
