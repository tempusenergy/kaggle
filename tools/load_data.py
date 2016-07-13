import os

import pandas as pd


GRUPO_URL = 'https://www.kaggle.com/c/grupo-bimbo-inventory-demand/download/'


def check_data(data):
    if type(data) != pd.DataFrame:
        return False
    if len(data) == 0:
        return False
    return True


class NoFileError(Exception):
        pass


class DataLoadError(Exception):
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

    def combine_data(self, parent='train', keep_index_cols=True):
        data = getattr(self, parent)
        child_table_keys = [
            ('cliente_tabla', 'Cliente_ID'),
            ('producto_tabla', 'Producto_ID'),
            ('town_state', 'Agencia_ID'),
        ]

        for child, key in child_table_keys:
            child_df = getattr(self, child)
            if not check_data(child_df):
                raise DataLoadError(child + ' data has not been loaded')
            data = pd.merge(data, child_df, on=key)

        if not keep_index_cols:
            keys = [child[1] for child in child_table_keys]
            data = data.drop(keys, axis=1)

        return data
