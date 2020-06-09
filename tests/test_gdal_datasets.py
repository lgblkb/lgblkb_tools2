from lgblkb_tools import Folder, logger
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from box import Box
import itertools as it
import more_itertools as mit

# region pandas options:
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 25)
# endregion

this_folder = Folder(__file__)
data_folder = this_folder['data']


@logger.trace()
def main():
    pd.DataFrame(np.random.rand(10, 2)).plot()
    plt.show()

    pass


if __name__ == '__main__':
    main()
