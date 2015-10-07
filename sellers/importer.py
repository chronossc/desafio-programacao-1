from data_importer import BaseImporter
from data_importer.readers.csv_reader import CSVReader


class TabReader(CSVReader):
    def __init__(self, f, **kwargs):
        kwargs['delimiter'] = '\t'
        super(TabReader, self).__init__(f, **kwargs)


class Importer1(BaseImporter):
    fields = [
        'purchaser_name',
        'item_description',
        'item_price',
        'purchase_count',
        'merchant_address',
        'merchant_name'
    ]
    required_fields = fields
