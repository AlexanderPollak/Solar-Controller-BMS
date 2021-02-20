#START OF MAIN:

from SCP.control import *

if __name__ == '__main__':

    Serial_Port = '/dev/ttyUSB0'  # Serial Port for Communication with Pylontech
    Modbus_Host = '192.168.0.210'  # Modbus Server Address for Communication with Inverter

    Battery_Modules = 6  # Number of Installed Modules
    Cadance = 5  # Control Loop refresh rate in seconds
    Max_Com_Error = 1000 # Number of Communication errors before program stops
    Display = True  # Enable Terminal SoC Print
    Log = True  # Enable BMS logging
    Control = True  # Enable Inverter Control Loop

    SoC_high = 90  # Percent
    SoC_low = 50  # Percent
    Battery_low = 45.5  # Volt
    Battery_hysteresis = 2.0  # Voltc


    main(Serial_Port=Serial_Port, Modbus_Host=Modbus_Host, Battery_Modules=Battery_Modules, Cadance=Cadance,\
         Display=Display, Log=Log, Control=Control, SoC_high=SoC_high, SoC_low=SoC_low, Battery_low=Battery_low,\
         Battery_hysteresis=Battery_hysteresis, Error_counter_max=Max_Com_Error)
