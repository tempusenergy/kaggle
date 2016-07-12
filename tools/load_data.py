import os

import pandas as pd


GRUPO_URL = 'https://www.kaggle.com/c/grupo-bimbo-inventory-demand/download/'


class NoFileError(Exception):
        pass


class GrupoBimboData(object):
    """Loads the data for the Kaggle Grupo Bimbo comp.
    Data file names:
    - train.csv.zip
    - test.csv.zip
    - cliente_tabla.csv.zip
    - producto_tabla.csv.zip
    - town_state.csv.zip

    Attributes:
    - data (dict): dict containing a pandas dataframe corresponding
                   to each data filename (without file extension)
    - data_load_args (dict): dict of dicts containing additional args to pass
                             to pandas read_csv for each data filename
    """

    data_load_args = {
        'train': {'nrows': 1000},
    }

    def __init__(self, data_dir):
        """Args:
        - data_dir (str): full path to directory containing data files
        """
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        self._data_dir = data_dir
        self.data = {
            'train': None,
            'test': None,
            'cliente_tabla': None,
            'producto_tabla': None,
            'town_state': None,
        }

    def _get_path(self, data_name):
        data_file = data_name + '.csv.zip'
        return '/'.join([self._data_dir, data_file])

    def _load_data(self, data_name, load_args):
        filename = self._get_path(data_name)
        if not os.path.isfile(filename):
            raise NoFileError('{} does not exist'.format(filename))

        self.data[data_name] = pd.read_csv(filename, **load_args)

    def load_all(self, load_arg_override=None):
        """Load all the data files into a dict of pandas dataframes.

        Note:
        - Data files should not be unzipped, pandas can handle this.

        Args:
        - load_arg_override (dict): Dict of dicts that overrides
                                    self.data_load_args (see class docstring)
                                    e.g. {'train': {'nrows': 2000}}
        """
        if load_arg_override:
            self.data_load_args.update(load_arg_override)

        for data_name in self.data:
            load_args = {}
            if data_name in self.data_load_args:
                load_args = self.data_load_args[data_name]

            self._load_data(data_name, load_args)
