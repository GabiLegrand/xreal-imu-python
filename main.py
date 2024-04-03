from XrealIMU import XrealIMU


if __name__ == "__main__":
    imu = XrealIMU()
    imu.start_connection()

    print("Eurler : ", imu.get_euler())
    print("Quaternion : ", imu.get_quaternion())
    print("Brightness : ", imu.get_brightness())

    imu.stop_connection()