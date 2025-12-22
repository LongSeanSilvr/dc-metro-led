import board
import busio
import digitalio
import time
from adafruit_esp32spi import adafruit_esp32spi

# 1. Initialize SPI
spi = board.SPI()

# 2. Setup pins correctly for CircuitPython 10
esp32_cs = digitalio.DigitalInOut(board.ESP_CS)
esp32_ready = digitalio.DigitalInOut(board.ESP_BUSY)
esp32_reset = digitalio.DigitalInOut(board.ESP_RESET)

# 3. Initialize the ESP32 connection
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

print("Connecting to ESP32...")
time.sleep(0.5) # Give it a moment to wake up

# 4. Fetch and display the version safely
ver = esp.firmware_version

# Handle both bytearray (old) and string (new) returns
if isinstance(ver, (bytearray, bytes)):
    version_string = "".join([chr(b) for b in ver if 32 <= b <= 126])
else:
    version_string = str(ver)

print("\n" + "="*30)
print(f" CURRENT NINA VERSION: {version_string}")
print("="*30)

if "1.7.4" in version_string:
    print("SUCCESS: You are on the stable version!")
else:
    print("NOTE: If this still says 1.2.2, the flash did not take.")