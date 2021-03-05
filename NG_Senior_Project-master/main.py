

import time

# from python_sandbox import johns_library as jl
# import threading
import instruments
import data_collection
import threading

lake_shore = instruments.Lakeshore(instrument_name="lake_shore", instrument_id= "009099696", num_of_sensors=3)


pf_valve = instruments.PropFlowValve(instrument_name="Proportional_Flow_Valve", instrument_id="090900")

print("LAKESHORE ")
print(lake_shore.get_instrument_name())
print(lake_shore.get_instrument_id())
print(lake_shore.get_init_flag())


print("\n\nPROPORTIONAL FLOW VALVE")
print(pf_valve.get_instrument_name())
print(pf_valve.get_instrument_id())
print(pf_valve.get_init_flag())

temp_data_collector = data_collection.TempData(lake_shore, "kelvin", 4)
pressure_data_collector = data_collection.PFVData(pf_valve, "bar", 2)


temp_data_collector.start_data_collector()
pressure_data_collector.start_data_collector()
for i in range(0, 5):
    time.sleep(1)
    print('data collector paused  other work')
temp_data_collector.stop_data_collector()
for i in range(0, 5):
    time.sleep(1)
    print('doing other work')
pressure_data_collector.stop_data_collector()
for i in range(0, 5):
    time.sleep(1)
    print('doing other work')
temp_data_collector.start_data_collector()
pressure_data_collector.start_data_collector()
for i in range(0, 5):
    time.sleep(1)
    print('data collector paused  other work')
temp_data_collector.stop_data_collector()
pressure_data_collector.stop_data_collector()