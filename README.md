# DC Metro Train Board (CircuitPython 10 Edition)

A real-time WMATA train prediction display for the Adafruit Matrix Portal M4. This version has been specifically modernized for CircuitPython 10.x and features a robust "self-healing" network stack to prevent common hardware freezes and SPI timeouts.

## 🚀 Key 2025 Updates
- Improved Stability: Uses WiFiManager to automatically detect and fix "SPI Timeout" errors.
- Modern Firmware: Optimized for CircuitPython 10.x and NINA Firmware 1.7.4+.
- Memory Efficient: Automated socket management and garbage collection to prevent crashes.
- Heartbeat Indicator: Uses the onboard NeoPixel to show connection status at a glance.

## Hardware Requirements
- Adafruit Matrix Portal M4
- 64x32 RGB LED matrix compatible with the Matrix Portal
- USB-C power supply (15w+ phone adapters recommended)
- USB-C cable

## Part 1: Prepare the Hardware
1. Glue Screws: Use hot glue to cover the sharp screws on the right-hand side of the matrix to prevent wire chafing.
2. Mount Portal: Lightly screw the phillips head screws into the posts on the Matrix Portal. 
3. Power Wiring: Connect the red power cable to 5V and the black power cable to GND on the Matrix Portal screw terminals.
4. Data Connection: Plug the Matrix Portal into the 16-pin HUB75 connector on the back of the matrix.

## Part 2: Loading the Software
1. Update NINA Firmware: Your board MUST be running NINA firmware 1.7.4 or higher.
2. Install CircuitPython: Double-click RESET on the board and drag the latest CircuitPython 10.x .uf2 file onto the MATRIXBOOT drive.
3. Install Libraries: Copy the following folders from the Adafruit Bundle into a /lib folder on your CIRCUITPY drive:
   - adafruit_matrixportal
   - adafruit_esp32spi
   - adafruit_requests
   - adafruit_connection_manager
   - adafruit_display_text
   - neopixel
4. Copy Source Code: Copy all .py files from the /src folder of this repository into the root of the CIRCUITPY volume.

## Part 3: Configuration
All configuration for this board—including WiFi and API keys—is handled in the config.py file.

1. Get a WMATA API Key: Sign up at the WMATA Developer Portal.
2. Open config.py: Locate this file in the root of your board.
3. Network Configuration: Fill in your 'wifi_ssid' and 'wifi_password'.
4. Metro Configuration: 
   - 'metro_station_code': Enter your station code (e.g., 'F04').
   - 'train_group_1' & 'train_group_2': Set which platforms to display.
   - 'metro_api_key': Paste your Primary Key from the WMATA dashboard.

Note: The secrets.py file is a bridge required by the hardware libraries; it automatically pulls the credentials you enter in config.py.

## Troubleshooting & Heartbeat
The onboard NeoPixel (near the USB port) provides real-time status:
- Blue Flashing: Actively connecting to Wi-Fi.
- Green Flash: Data successfully retrieved.
- Red/Yellow: A network error occurred; the board is automatically performing a hardware reset.

---

## Appendix: DC Metro Station Codes
| Name | Lines | Code |
|------|-------|------|
| Addison Road-Seat Pleasant | BL, SV | G03 |
| Anacostia | GR | F06 |
| Archives-Navy Memorial-Penn Quarter | GR, YL | F02 |
| Arlington Cemetery | BL | C06 |
| Ballston-MU | OR, SV | K04 |
| Benning Road | BL, SV | G01 |
| Bethesda | RD | A09 |
| Braddock Road | BL, YL | C12 |
| Branch Ave | GR | F11 |
| Brookland-CUA | RD | B05 |
| Capitol Heights | BL, SV | G02 |
| Capitol South | BL, OR, SV | D05 |
| Cheverly | OR | D11 |
| Clarendon | OR, SV | K02 |
| Cleveland Park | RD | A05 |
| College Park-U of Md | GR | E09 |
| Columbia Heights | GR, YL | E04 |
| Congress Heights | GR | F07 |
| Court House | OR, SV | K01 |
| Crystal City | BL, YL | C09 |
| Deanwood | OR | D10 |
| Dunn Loring-Merrifield | OR | K07 |
| Dupont Circle | RD | A03 |
| East Falls Church | OR, SV | K05 |
| Eastern Market | BL, OR, SV | D06 |
| Eisenhower Avenue | YL | C14 |
| Farragut North | RD | A02 |
| Farragut West | BL, OR, SV | C03 |
| Federal Center SW | BL, OR, SV | D04 |
| Federal Triangle | BL, OR, SV | D01 |
| Foggy Bottom-GWU | BL, OR, SV | C04 |
| Forest Glen | RD | B09 |
| Fort Totten | RD | B06 |
| Fort Totten | GR, YL | E06 |
| Franconia-Springfield | BL | J03 |
| Friendship Heights | RD | A08 |
| Gallery Pl-Chinatown | RD | B01 |
| Gallery Pl-Chinatown | GR, YL | F01 |
| Georgia Ave-Petworth | GR, YL | E05 |
| Glenmont | RD | B11 |
| Greenbelt | GR | E10 |
| Greensboro | SV | N03 |
| Grosvenor-Strathmore | RD | A11 |
| Huntington | YL | C15 |
| Judiciary Square | RD | B02 |
| King St-Old Town | BL, YL | C13 |
| L'Enfant Plaza | BL, OR, SV | D03 |
| L'Enfant Plaza | GR, YL | F03 |
| Landover | OR | D12 |
| Largo Town Center | BL, SV | G05 |
| McLean | SV | N01 |
| McPherson Square | BL, OR, SV | C02 |
| Medical Center | RD | A10 |
| Metro Center | RD | A01 |
| Metro Center | BL, OR, SV | C01 |
| Minnesota Ave | OR | D09 |
| Morgan Boulevard | BL, SV | G04 |
| Mt Vernon Sq 7th St-Convention Center | GR, YL | E01 |
| Navy Yard-Ballpark | GR | F05 |
| Naylor Road | GR | F09 |
| New Carrollton | OR | D13 |
| NoMa-Gallaudet U | RD | B35 |
| Pentagon | BL, YL | C07 |
| Pentagon City | BL, YL | C08 |
| Potomac Ave | BL, OR, SV | D07 |
| Prince George's Plaza | GR | E08 |
| Rhode Island Ave-Brentwood | RD | B04 |
| Rockville | RD | A14 |
| Ronald Reagan Washington National Airport | BL, YL | C10 |
| Rosslyn | BL, OR, SV | C05 |
| Shady Grove | RD | A15 |
| Shaw-Howard U | GR, YL | E02 |
| Silver Spring | RD | B08 |
| Smithsonian | BL, OR, SV | D02 |
| Southern Avenue | GR | F08 |
| Spring Hill | SV | N04 |
| Stadium-Armory | BL, OR, SV | D08 |
| Suitland | GR | F10 |
| Takoma | RD | B07 |
| Tenleytown-AU | RD | A07 |
| Twinbrook | RD | A13 |
| Tysons Corner | SV | N02 |
| U Street/African-Amer Civil War Memorial | GR, YL | E03 |
| Union Station | RD | B03 |
| Van Dorn Street | BL | J02 |
| Van Ness-UDC | RD | A06 |
| Vienna/Fairfax-GMU | OR | K08 |
| Virginia Square-GMU | OR, SV | K03 |
| Waterfront | GR | F04 |
| West Falls Church-VT/UVA | OR | K06 |
| West Hyattsville | GR | E07 |
| Wheaton | RD | B10 |
| White Flint | RD | A12 |
| Wiehle-Reston East | SV | N06 |
| Woodley Park-Zoo/Adams Morgan | RD | A04 |

## Silver Line Phase II Stations
| Name | Lines | Code |
|------|-------|------|
| Reston Town Center | SV | N07 |
| Herndon | SV | N08 |
| Innovation Center | SV | N09 |
| Dulles Airport | SV | N10 |
| Loudoun Gateway | SV | N11 |
| Ashburn | SV | N12 |

## Train Group Explanations
| Line | Train Group | Destination |
|------|-------------|-------------|
| RD | "1" | Glenmont |
| RD | "2" | Shady Grove |
| BL, OR, SV | "1" | New Carrollton, Largo Town Center |
| BL, OR, SV | "2" | Vienna, Franconia-Springfield, Ashburn |
| GR, YL | "1" | Greenbelt |
| GR, YL | "2" | Huntington, Branch Avenue |
| N/A | "3" | Center Platforms (National Airport, West Falls Church) |

## Credits
Based on the original project by [ScottKekoaShay/dc-metro](https://github.com/ScottKekoaShay/dc-metro/tree/main). Updated for modern hardware and firmware stability.
