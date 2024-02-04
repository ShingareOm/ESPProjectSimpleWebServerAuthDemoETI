# ESP32 Web Server with MicroPython

## Overview

This project demonstrates the creation of a simple web server using the ESP32 microcontroller and MicroPython. The web server allows users to remotely control an LED connected to the ESP32 through a web interface.

## Getting Started

### Prerequisites

- ESP32 microcontroller
- MicroPython firmware flashed onto the ESP32
- Python development environment
- [AMPy](https://github.com/scientifichackers/ampy) tool for uploading files to ESP32
- Network credentials (SSID and PASSWORD)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/ShingareOm/ESPProjectSimpleWebServerAuthDemoETI.git
   ```

2. Upload the `main.py` file and `networkcredentials.py` (containing SSID and PASSWORD) to your ESP32 using AMPy or any other preferred method.

## Usage

1. Connect the ESP32 to the power source.
2. Open the serial console to view the ESP32's IP address.
3. Open a web browser and enter the ESP32's IP address.
4. Use the web interface to control the LED.

## Project Structure

- `main.py`: The main MicroPython script for the web server.
- `networkcredentials.py`: File containing network credentials.
- `assets/`: Folder containing favicon and other static assets.

## Author

- **Om Shingare**
  - GitHub: Shingare Om
  - Website: www.omshingare.me

## Acknowledgments

- [MicroPython](http://micropython.org/)
- [ESP32](https://www.espressif.com/en/products/socs/esp32)
- [AMPy](https://github.com/scientifichackers/ampy)

## License

This project is licensed under the [MIT License](LICENSE).

