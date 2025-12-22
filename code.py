import board
import time
import gc
from config import config
from train_board import TrainBoard
from metro_api import MetroApi, MetroApiOnFireException

STATION_CODE = config['metro_station_code']
REFRESH_INTERVAL = config['refresh_interval']

def refresh_trains(train_group: str) -> list:
    try:
        return MetroApi.fetch_train_predictions(STATION_CODE, train_group)
    except MetroApiOnFireException:
        print('WMATA Api is currently on fire. Trying again later ...')
        return None

train_group = config['train_group_1']
train_board = TrainBoard(lambda: refresh_trains(train_group))

while True:
    # 1. Update the display
    train_board.refresh()
    
    # 2. Force a memory cleanup to prevent crashes over time
    gc.collect()
    print(f"Free memory: {gc.mem_free()}")
    
    # 3. Wait
    time.sleep(REFRESH_INTERVAL)
    
    # 4. Toggle the train group for the next run
    if train_group == config['train_group_1']:
        train_group = config['train_group_2']
    else:
        train_group = config['train_group_1']