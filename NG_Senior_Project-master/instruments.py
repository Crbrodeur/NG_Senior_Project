import random
from abc import ABC, abstractmethod
from alicat import FlowController
import visa
import pyvisa.constants

class SimulatedResponses:
    @staticmethod
    def simulated_temp_query():
        """ simulates response from Lakeshore

        Returns:
            temp_data: (list) three random values between 0-100

        todo: Implement this function with real data

        """
        temp_data = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100)]
        return temp_data

    @staticmethod
    def simulated_pvf_query():
        """ simulates response from proportional flow valve (pfv)

        Returns:
            head_pressure: (double) random value between 0-100

        todo: Implement this function with real data

        """
        head_pressure = random.uniform(0, 100)
        return head_pressure


class Instrument:
    def __init__(self, instrument_name="", instrument_id=None):
        """ Instrument parent class

        Args:
            instrument_name: (str) name of instrument
            instrument_id: (str) id of instrument
        """
        self._instrument_name = instrument_name
        self._instrument_id = int(instrument_id)
        self._init_flag = False
        self.initialize_instrument()

    @abstractmethod
    def initialize_instrument(self):
        pass
        print("parent class init used")

    @abstractmethod
    def check_status(self):
        pass
        print("parent class check status used ")

    def get_instrument_name(self):
        """ gets instrument name

        Returns:
            self._instrument_name: (str) instruments name

        """
        return self._instrument_name

    def get_instrument_id(self):
        """ gets instrument ID

        Returns:
            self._instrument_id: (str) instruments id

        """
        return self._instrument_id

    def set_init_flag(self):
        """ sets initialization flag

        Returns:
            N/A

        """
        self._init_flag = True

    def get_init_flag(self):
        """get initialization flag

        Returns:
            self._init_flag: (bool) True if devices is active, false otherwise.

        """
        return self._init_flag


class Lakeshore(Instrument):
    
    def __init__(self, instrument_name="", instrument_id=None, num_of_sensors=3, usbAddress=-1):
        """Lakeshore Temperature Controller

            port settings are initialized

        Args:
            instrument_name: (str) name of the instrument
            instrument_id: (str) id of the instrument
            num_of_sensors:number of sensors in use
            usbAddress: the address of the connected USB, 'COM4'
        """
        Instrument.__init__(self, instrument_name, instrument_id)
        self.set_point = None
        self.num_of_temp_sensors = num_of_sensors

        self._rm = visa.ResourceManager()
        self._instrument = self._rm.open_resource(usbAddress)
        self._instrument.baud_rate = 57600
        self._instrument.data_bits = 7
        self._instrument.stop_bits = pyvisa.constants.StopBits.one
        self._instrument.parity = pyvisa.constants.Parity.odd


    """
        Don't really need this code because we are doing
        all the initialization in __int__
    """
    """
    def initialize_instrument(self):
         Initializes Proportional Flow Valve

        Returns:
            0: successful
            1: Failure

        todo: Implement this function

        
        try:
            #  initialization code goes here

            self.set_init_flag()
        except BaseException:  # Change exception accordingly
            print("Lakeshore temperature controller failed to Initialized ")
            return 1
        return 0
    """



    def check_status(self):
        """ Checks the status of the Lakeshore Temperature controller

        Returns:
            0: the device is active
            1: the device is not active

        """
        print("Lakeshore Active ")
        print(self._instrument.query('*IDN?'))
        return 0

    def get_temperature_data(self):
        """ gets data from Lakeshore

        Returns:
            data: (list) Temperature data off the Lakeshore

        todo: implement this function
        """
        print(self._instrument.query('KRDG?'))

        if self.get_init_flag():
            data = SimulatedResponses.simulated_temp_query()
            return data
        else:
            return 1


class PropFlowValve(Instrument):

    def __init__(self, instrument_name="", instrument_id=None, max_head_pressure=10):
        """ Alicat Proportional Flow Valve

        Args:
            instrument_name: (str) name of instrument
            instrument_id: (str) id of instrument
            max_head_pressure: (double) maximum desired head pressure
        """
        Instrument.__init__(self, instrument_name, instrument_id)
        self.MAX_HEAD_PRESSURE = max_head_pressure

    def initialize_instrument(self):
        """ Initializes Proportional Flow Valve

            connects to COM3 port

        Returns:
            0: successful
            1: Failure
        """
        try:
            prop_flow_valve = FlowController(port='COM3')
            print("Alicat PFV Initialized.\nDevice info:\n ")
            print(prop_flow_valve.get())
            self.set_init_flag()
        except BaseException:  # Change exception accordingly
            print("Alicat PFV failed to Initialized ")
            return 1
        return 0

    def check_status(self):
        """ Checks the status of the Proportional Flow Valve

        Returns:
            0: the device is active
            1: the device is not active

        todo: Implement this function

        """
        if (self.get_init_flag() == True):
            print("Alicat PFV Active ")
            return 0
        else:
            print("Alicat PFV not Active")
            return 1

    def set_pressure(self, pressure_set_point):
        """

        Args:
            pressure_set_point:

        Returns:

        todo: Implement this function

        """
        try:
            #  self._set_point = pressure_set_point
            self._instrument_name.set_flow_rate(pressure_set_point)
            print("Pressure set to " + pressure_set_point)
        except BaseException:
            print("failure to set pressure")
            return 1

        return 0

    @staticmethod
    def get_head_pressure():
        """ Gets head pressure from PFV

        Returns:
            head_pressure = (double) current head pressure

        todo: implement this function

        """
        try:

            head_pressure = SimulatedResponses.simulated_pvf_query()
            return head_pressure

        except IOError:
            print("failure to get head pressure")


lake_shore = Lakeshore(instrument_name="lake_shore", instrument_id= "009099696", num_of_sensors=3, usbAddress='COM4')
lake_shore.check_status()
lake_shore.get_temperature_data()

pf_valve = PropFlowValve(instrument_name="Proportional_Flow_Valve", instrument_id="090900")
pf_valve.set_pressure(0.0)

