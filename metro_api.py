import board
import busio
import neopixel
from digitalio import DigitalInOut
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi.adafruit_esp32spi_wifimanager import WiFiManager
from config import config

# Setup the raw hardware pins
esp32_cs = DigitalInOut(board.ESP_CS)
esp32_ready = DigitalInOut(board.ESP_BUSY)
esp32_reset = DigitalInOut(board.ESP_RESET)
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

# Initialize the onboard NeoPixel
status_pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)

# Pass it to the WiFiManager
wifi = WiFiManager(esp, config["wifi_ssid"], config["wifi_password"], status_pixel=status_pixel)

class MetroApiOnFireException(Exception):
    pass

class MetroApi:
    @staticmethod
    def fetch_train_predictions(station_code: str, group: str) -> list:
        api_url = config['metro_api_url'] + station_code
        
        try:
            # wifi.get() automatically checks if the chip is alive and resets it if not!
            response = wifi.get(
                api_url, 
                headers={'api_key': config['metro_api_key']},
                timeout=15
            )
            
            with response: # This ensures the socket is closed automatically
                train_data = response.json()
                print('Received response from WMATA api...')
                
                # Safer access: defaults to empty list if 'Trains' key is missing
                all_trains = train_data.get('Trains', [])
                
                trains = filter(lambda t: t['Group'] == group, all_trains)
                return list(map(MetroApi._normalize_train_response, trains))

        except Exception as e:
            print(f"WiFiManager caught an error: {e}")
            # If WiFiManager couldn't fix it after its internal retries:
            raise MetroApiOnFireException()

    @staticmethod
    def _normalize_train_response(train: dict) -> dict:
        line = train.get('Line', '--')
        destination = train.get('Destination', 'Unknown')
        arrival = train.get('Min', '--')

        # Clean up long destination names for the matrix
        map_dest = {
            'No Passenger': 'No Psngr',
            'NoPssenger': 'No Psngr',
            'ssenger': 'No Psngr',
            'Greenbelt': 'Grnbelt',
            'Branch Av': 'Brnch Av'
        }
        destination = map_dest.get(destination, destination)

        return {
            'line_color': MetroApi._get_line_color(line),
            'destination': destination,
            'arrival': arrival
        }

    @staticmethod
    def _get_line_color(line: str) -> int:
        colors = {
            'RD': 0xFF0000,
            'OR': 0xFF5500,
            'YL': 0xFFFF00,
            'GR': 0x00FF00,
            'BL': 0x0000FF,
            'SV': 0xAAAAAA # Silver Line
        }
        return colors.get(line, 0x444444)