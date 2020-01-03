from cement import Controller, ex


class DataSets(Controller):
    class Meta:
        label = 'datasets'
        stacked_type = 'embedded'
        stacked_on = 'base'

    @ex(help='list all datasets')
    def list(self):
        pass

    @ex(help='create a new dataset')
    def create(self):
        pass

    @ex(help='fetch an existing dataset')
    def view(self):
        pass

    @ex(help='delete a dataset')
    def delete(self):
        pass

    @ex(help='export a dataset to excel')
    def excel(self):
        pass

    @ex(help='generate stats for a dataset')
    def stats(self):
        pass

    @ex(help='plot histograms for a dataset')
    def plot(self):
        pass
