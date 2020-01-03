from cement import Controller, ex
import re


class DataSets(Controller):
    class Meta:
        label = 'datasets'
        stacked_type = 'embedded'
        stacked_on = 'base'

    @staticmethod
    def _get_filename(response):
        return re.findall("filename=\"(.+)\"", response.headers['content-disposition'])[0]

    def id(self):
        if self.app.pargs.id is not None:
            return self.app.pargs.id
        else:
            print("please provide an `id` with -i or --id")
            exit(1)

    @ex(help='list all datasets')
    def list(self):
        print(self.app.apiservice.list())

    @ex(
        help='create a new dataset',
        arguments=[
            (['-f', '--file'],
             {'help': 'input CSV file',
              'action': 'store',
              'dest': 'file'}),
        ],
    )
    def create(self):
        if self.app.pargs.file is None:
            print("please provide a `file` with -f or --file")
            exit(1)
        with open(self.app.pargs.file, 'r') as f:
            print(self.app.apiservice.create({'blob': f}))

    @ex(help='fetch an existing dataset')
    def view(self):
        print(self.app.apiservice.view(self.id()))

    @ex(help='delete a dataset')
    def delete(self):
        success = self.app.apiservice.delete(self.id())
        print("Successfully deleted") if success else print("Failed to delete")

    @ex(help='export a dataset to excel')
    def excel(self):
        self._save_file_response(self.app.apiservice.excel(self.id()))

    @ex(help='generate stats for a dataset')
    def stats(self):
        print(self.app.apiservice.stats(self.id()))

    @ex(help='plot histograms for a dataset')
    def plot(self):
        self._save_file_response(self.app.apiservice.plot(self.id()))

    def _save_file_response(self, response):
        fname = self._get_filename(response)
        open(fname, 'wb').write(response.content)
        print("Downloaded {}".format(fname))
