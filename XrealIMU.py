import ctypes


class XrealIMU:
    """
    Simple class extracting IMU data from Xreals using the AirAPI_Windows dll.
    Require hidapi.dll 
    """
    def __init__(self, dll_path='./AirAPI_Windows.dll'):
        self.path = dll_path
        self.api = ctypes.CDLL(dll_path)
    
    def start_connection(self):
        self.api.StartConnection()
        self.api.GetQuaternion.restype = ctypes.POINTER(ctypes.c_float)
        self.api.GetEuler.restype = ctypes.POINTER(ctypes.c_float)
        return 1
    
    def get_euler(self):
        elr_ptr =  self.api.GetEuler()
        euler = [elr_ptr[i] for i in range(3)]
        return euler
    def get_quaternion(self):
        quats = self.api.GetQuaternion()
        quaternion = [quats[i] for i in range(4)]
        return quaternion

    def get_brightness(self):        
        brigthness = self.api.GetBrightness()
        return brigthness
    
    def stop_connection(self):
        self.api.StopConnection()
        return 1
    