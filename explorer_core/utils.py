from os.path import join

from explorer.settings import MEDIA_ROOT


def get_file_path(id):
    file_path = join(MEDIA_ROOT, f'{id}.pkl')
    return file_path
