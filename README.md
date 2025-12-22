# DC Metro Train Board (CircuitPython 10 Edition)

A real-time WMATA train prediction display for the Adafruit Matrix Portal M4.

## 🚀 Key Improvements in this Version
This version has been specifically optimized for modern CircuitPython and hardware stability:
* **CircuitPython 10.x Support:** Updated syntax and pin management.
* **NINA Firmware 1.7.4+:** Requires the updated Wi-Fi co-processor firmware to prevent SPI timeouts.
* **Auto-Recovery:** Uses `WiFiManager` and hardware reset logic to prevent "SPI Char" crashes.
* **Socket Management:** Explicitly closes network connections to prevent memory leaks.

## 🛠 Setup
1. Copy the contents of this repo to your `CIRCUITPY` drive.
2. Create a `secrets.toml` or `secrets.py` with your WiFi credentials and WMATA API key.
3. Ensure your `/lib` folder contains the latest `adafruit_esp32spi` and `adafruit_matrixportal` libraries.
