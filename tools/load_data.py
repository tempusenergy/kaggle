import os

import pandas as pd


GRUPO_URL = 'https://www.kaggle.com/c/grupo-bimbo-inventory-demand/download/'


class NoFileError(Exception):
        pass


class GrupoBimboData(object):
    """Loads the data for the Kaggle Grupo Bimbo comp.

    Attributes:
    - train (pandas data_frame)
    - test (pandas data_frame)
    - cliente_tabla (pandas data_frame)
    - producto_tabla (pandas data_frame)
    - town_state (pandas data_frame)
    """

    def __init__(self, data_dir):
        """Args:
        - data_dir (str): full path to directory containing data files
        """
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        self._data_dir = data_dir

        self.train = None
        self.test = None
        self.cliente_tabla = None
        self.producto_tabla = None
        self.town_state = None

    def _get_path(self, data_name):
        data_file = data_name + '.csv.zip'
        return os.path.join(self._data_dir, data_file)

    def load_data(self, data_name, **kwargs):
        """Load the data for a specific data_file into the similiarly named
        class attribute.

        Args:
        - data_name (str): name of the data file, without extension ('train')
        - **kwargs : any supported by pandas read_csv
        """
        filename = self._get_path(data_name)
        if not os.path.isfile(filename):
            raise NoFileError('{} dataset does not exist'.format(filename))

        data_frame = pd.read_csv(filename, **kwargs)
        setattr(self, data_name, data_frame)
