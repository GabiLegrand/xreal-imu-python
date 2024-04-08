from XrealIMU import XrealIMU
import time 

if __name__ == "__main__":
    imu = XrealIMU()
    imu.start_connection()
    for i in range(1000):
        time.sleep(round(1/9,3))
        for j in range(4):
            print ("\033[A                                  \033[A")
        print("Iteration : ",i)
        print("Eurler : ", [round(v,3) for v in imu.get_euler()])
        print("Quaternion : ", [round(v,3) for v in imu.get_quaternion()])
        print("Brightness : ", imu.get_brightness())

    imu.stop_connection()