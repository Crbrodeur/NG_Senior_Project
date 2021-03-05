from abc import ABC, abstractmethod
import time
import threading
# from python_sandbox import johns_library as jl
import random
class DataEntry:
    """

    """
    def __init__(self, time, temp):
        self.__time = time
        self.__temp = jl.get_time_stamp()

    def get_time(self):
        return self.__time

    def get_temp(self):
        return self.__temp


class DataStream:
    """

    """
    def __init__(self, units="kelvin", rate=1):
        """

        Args:
            units:
            rate:

        Returns:

        """
        self._units = units
        self._sampling_rate = 1/rate
        self._collect = False

    def start_data_collector(self):
        """

        Returns:

        """
        self._collect = True
        t1 = threading.Thread(target=self.data_collector)
        t1.start()
        return 0

    def stop_data_collector(self):
        """

        Returns:

        """
        self._collect = False

    @abstractmethod
    def data_collector(self):
        pass

    @abstractmethod
    def clear_data_collector(self):
        pass


    def get_units(self):
        """

        Returns:

        """
        return self._units

    def get_sampling_rate(self):
        """

        Returns:

        """
        return self._sampling_rate


class TempData(DataStream):
    """

    """
    def __init__(self, temp_controller,  units="", rate=1):
        """

        Args:
            temp_controller:
            units:
            rate:
        """
        DataStream.__init__(self, units, rate)
        self.temp_controller = temp_controller
        self.temp_dict = {'Time': [], 'Chuck': [], "Radiation Shield": [], "Probe Card": []}
        self.count = 0


    def clear_data_collector(self):
        """

        Returns:

        """
        self.temp_dict = {'Time': [], 'Chuck': [], "Radiation Shield": [], "Probe Card": []}

    def data_collector(self):
        """

        Returns:

        """
        while self._collect:
            self.count += 1
            print("collecting temp data " + str(self.count))

            data = self.temp_controller.get_temperature_data()

            # self.temp_dict['Time'].append(jl.get_time_stamp())
            self.temp_dict['Chuck'].append(data[0])
            self.temp_dict["Radiation Shield"].append(data[1])
            self.temp_dict["Probe Card"].append(data[2])
            time.sleep(self._sampling_rate)


class PFVData(DataStream):
    def __init__(self, pfv, units="", rate=1):
        DataStream.__init__(self, units, rate)
        self.pfv = pfv
        self.pressure_dict = {'Time': [], 'Head_pressure': []}
        self.count = 0


    def data_collector(self):
        """

        Returns:

        """
        while self._collect:
            self.count += 1
            print("collecting pfv data " + str(self.count))
            head_pressure =self.pfv.get_head_pressure()
            # self.pressure_dict['Time'].append(jl.get_time_stamp())
            self.pressure_dict['Head_pressure'].append(head_pressure)
            time.sleep(self._sampling_rate)
