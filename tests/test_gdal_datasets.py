from lgblkb_tools import Folder, logger
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from box import Box
import itertools as it
import more_itertools as mit

# region pandas options:
# pd.set_option('display.max_rows', None)
from lgblkb_tools.gdal_datasets import DataSet, GdalMan

pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 25)
# endregion

this_folder = Folder(__file__)
data_folder = this_folder['data']


@logger.trace()
def main():
    input_file = r'/home/lgblkb/PycharmProjects/imagination/results/S2A_MSIL2A_20200607T064631_N0214_R020_T41UQU_20200607T094817/e2228d01bfb0b58d12695592b06db8fd/clgreen.tiff'
    ds = DataSet(input_file)
    logger.debug("ds.epsg: %s", ds.epsg)
    gm = GdalMan()
    gm.gdalwarp(input_file, out_filepath=data_folder['kor.tiff'], t_srs='epsg:3857')

    pass


if __name__ == '__main__':
    main()
