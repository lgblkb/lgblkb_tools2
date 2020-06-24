import diskcache
from lgblkb_tools import Folder, logger
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from box import Box
import itertools as it
import more_itertools as mit
from lgblkb_tools.geometry import FieldPoly

sns.set()
# region pandas options:
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 25)
# endregion

this_folder = Folder(__file__)
data_folder = this_folder['data']
cache = diskcache.Cache(this_folder['.cache'])


@logger.trace()
def main():
    FieldPoly.synthesize(10).plot()
    plt.show()
    pass


if __name__ == '__main__':
    main()
