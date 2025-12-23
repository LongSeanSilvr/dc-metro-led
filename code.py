import board
import time
import gc
import microcontroller
import watchdog
from config import config
from train_board import TrainBoard
from metro_api import MetroApi, MetroApiOnFireException

# --- 1. SETUP WATCHDOG (Dead Man's Switch) ---
wdt = microcontroller.watchdog
wdt.timeout = 15  # Reboots the board if not "fed" for 15 seconds
wdt.mode = watchdog.WatchDogMode.RESET

# --- 2. TRAIN LOGIC ---
STATION_CODE = config['metro_station_code']
REFRESH_INTERVAL = config['refresh_interval']

def refresh_trains(train_group: str) -> list:
    try:
        return MetroApi.fetch_train_predictions(STATION_CODE, train_group)
    except MetroApiOnFireException:
        print('WMATA Api is currently on fire. Retrying...')
        return None

train_group = config['train_group_1']
train_board = TrainBoard(lambda: refresh_trains(train_group))

# --- 3. MAIN LOOP ---
while True:
    try:
        # "Pet the dog" - Reset the timer so the board knows we are alive
        wdt.feed() 
        
        # Refresh the LED Matrix
        train_board.refresh()
        
        # Clean up memory to prevent fragmentation
        gc.collect()
        
        # Toggle train group for the next cycle
        if train_group == config['train_group_1']:
            train_group = config['train_group_2']
        else:
            train_group = config['train_group_1']
        
        # Sleep logic: Feed the dog every second during the wait interval
        # This prevents the WDT from triggering while we are just waiting
        for _ in range(REFRESH_INTERVAL):
            wdt.feed()
            time.sleep(1)

    except Exception as e:
        # If any unexpected software error occurs, force a hard reset 
        # to clear the SPI bus and start fresh.
        print(f"Unexpected error: {e}")
        microcontroller.reset()