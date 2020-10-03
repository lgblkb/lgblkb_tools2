from functools import partial

from lgblkb_tools import Folder, logger
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from box import Box
import itertools as it
import more_itertools as mit
from lgblkb_tools.telegram_notify import TheChat
from telegram import Bot
from dynaconf import settings

# region pandas options:
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 25)
# endregion

this_folder = Folder(__file__)
data_folder = this_folder['data']
notify = partial(TheChat(r'-432356237', bot=Bot('1084990340:AAFCm3odQOHCPDTqTStT_KQwidCaOrXwJNc')).send_message)


@logger.trace()
def main():
    logger.debug("settings.X: %s", settings.X)
    pass


if __name__ == '__main__':
    main()
