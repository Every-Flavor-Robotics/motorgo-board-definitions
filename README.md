# motorgo-board-definitions
This repository contains the board definitions for the MotorGo boards. These board definitions are compatible with the Arduino IDE and PlatformIO and tell the IDE how to compile and upload code to the MotorGo boards.

## Installation
Since the MotorGo boards are based on the ESP32, you'll have to first install the ESP32 board definition.

**Arduino IDE 2.X**
* Go to `Tools > Board > Boards Manager...`
* Search for `ESP32`
* Install `esp32` by Espressif Systems

**Arduino IDE 1.X**
* Go to `Tools > Board > Boards Manager...`
* Search for `ESP32`
* Install `esp32` by Espressif Systems
*

**PlatformIO**
* Navigate to PlatformIO Home
* Go to `Platforms`
* Search for `Espressif 32`
* Click `Install`


Next, you'll have to install the MotorGo board definition, which is available in this respository.

**Arduino IDE 2.X**
* Go to `File > Preferences`
* Add `https://raw.githubusercontent.com/Every-Flavor-Robotics/motorgo-arduino/main/board_definitions/package_motorgo_index.json` to `Additional Boards Manager URLs`
* Go to `Tools > Board > Boards Manager...`
* Search for `MotorGo`
* Click `Install`

**Arduino IDE 1.X**
* Go to `File > Preferences`
* Add `https://raw.githubusercontent.com/Every-Flavor-Robotics/motorgo-arduino/main/board_definitions/package_motorgo_index.json` to `Additional Boards Manager URLs`
* Go to `Tools > Board > Boards Manager...`
* Search for `MotorGo`
* Click `Install`

**PlatformIO**
* Clone this respotory
* Navigate to board_definitions/
* Run the python script `python3 setup_platformio.py`