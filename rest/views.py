from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd

from rest.models import DatasetModel


class DatasetView(APIView):
    # noinspection PyUnusedLocal
    @staticmethod
    def get(*args, **kwargs):
        datasets = DatasetModel.objects.all()
        return Response(datasets)

    # noinspection PyShadowingBuiltins
    @staticmethod
    def post(request):
        file_obj = request.data['file']
        csv = pd.read_csv(file_obj)
        csv.to_pickle('/media/'+request.FILES['file'].name+'.pkl')
        print('csv', csv)
        pickle = pd.read_pickle('/media/'+request.FILES['file'].name+'.pkl')
        print('pickle', pickle)
        pickle.to_csv('/media/'+request.FILES['file'].name)
        export = open('/media/'+request.FILES['file'].name, 'r')
        print('export', export)
        return Response([export])
