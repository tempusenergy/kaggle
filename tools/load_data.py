import pandas as pd


class GrupoBimboData(object):
    train = None
    test = None
    cliente_tabla = None
    producto_tabla = None
    town_state = None
    all_data = [train, test, cliente_tabla, producto_tabla, town_state]

    def __init__(self, data_dir):
        self._data_dir = data_dir

    def _get_path(self, data_name):
        data_file = data_name + '.csv'
        return '/'.join([self._data_dir, data_file])

    def _load_train(self, nrows=1000):
        self.train = pd.read_csv(self._get_path('train'), nrows=nrows)

    def _load_test(self):
        self.test = pd.read_csv(self._get_path('test'))

    def _load_cliente_tabla(self):
        self.cliente_tabla = pd.read_csv(self._get_path('cliente_tabla'))

    def _load_producto_tabla(self):
        self.producto_tabla = pd.read_csv(self._get_path('producto_tabla'))

    def _load_town_state(self):
        self.town_state = pd.read_csv(self._get_path('town_state'))

    def load_all(self, num_train_rows=1000):
        self._load_train(nrows=num_train_rows)
        self._load_test()
        self._load_cliente_tabla()
        self._load_producto_tabla()
        self._load_town_state()
        self.all_data = [
            self.train,
            self.test,
            self.cliente_tabla,
            self.producto_tabla,
            self.town_state,
        ]
