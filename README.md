# XREAL Air 2 Pro IMU Data Extractor

This Python module provides a simple interface for extracting raw IMU (Inertial Measurement Unit) data from XREAL Air 2 Pro glasses. Utilizing the AirAPI_Windows.dll, this module allows for easy access to quaternion and Euler angle data, as well as device brightness levels.

## Features

- Fetch quaternion and Euler angles in real-time.
- Retrieve the device's brightness level.
- Start and stop the connection.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Windows operating system (due to the DLL dependencies).
- Python 3.6 or later.
- The [hidapi.dll](https://github.com/libusb/hidapi/releases) is required for low-level USB communication.
- AirAPI_Windows.dll - Although originally sourced from [MSmithDev's GitHub](https://github.com/MSmithDev/AirAPI_Windows), i had to use the version from [IVideoGameBoss's PhoenixHeadTracker project](https://github.com/iVideoGameBoss/PhoenixHeadTracker/tree/main?tab=readme-ov-file) to make it work.

## Installation

1. Clone this repository to your local machine.
2. Put `hidapi.dll` and `AirAPI_Windows.dll` in the same directory as this module
3. Plug your glasses.
4. Call `start_connection` (see example)

## Devices 

This should work with the Air, Air 2 and Air 2 pro.

## Usage

Here is a simple example of how to use the `XrealIMU` class to extract IMU data:

```python
from xreal_imu import XrealIMU

# Initialize the class with the path to AirAPI_Windows.dll
imu = XrealIMU('./AirAPI_Windows.dll')

# Start the connection
imu.start_connection()

# Get Euler angles
euler = imu.get_euler()
print(f"Euler Angles: {euler}")

# Get Quaternion
quaternion = imu.get_quaternion()
print(f"Quaternion: {quaternion}")

# Get Brightness
brightness = imu.get_brightness()
print(f"Brightness: {brightness}")

# Stop the connection
imu.stop_connection()
```

## API Reference

The `XrealIMU` class provides the following methods:

- `start_connection()`: Initializes the connection to the device. Must be called before fetching data.
- `get_euler()`: Returns the Euler angles as a list of three floats.
- `get_quaternion()`: Returns the quaternion as a list of four floats.
- `get_brightness()`: Returns the device's brightness level as an integer.
- `stop_connection()`: Closes the connection to the device.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
