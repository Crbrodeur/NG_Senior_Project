import visa


class TestEquipment():

    def __init__(self, gpibBoardIndex=-1, gpibAddress=-1, usbAddress=-1, ethernetAddress=-1, realTest=True):
        if (gpibBoardIndex != -1):
            self._boardIndex = gpibBoardIndex
            self._gpibAddress = gpibAddress
            self._rm = visa.ResourceManager()
            self._instrument = self._rm.get_instrument('GPIB' + str(self._boardIndex)
                                                       + '::' + str(self._gpibAddress))
        elif (usbAddress != -1):
            self._rm = visa.ResourceManager()
            self._instrument = self._rm.get_instrument(usbAddress)
        elif (ethernetAddress != -1):
            self._rm = visa.ResourceManager()
            self._instrument = self._rm.get_instrument(ethernetAddress)
            # self._instrument = self._rm.open_resource(ethernetAddress)

    def GetIDN(self):
        write = '*IDN?'
        read = self._instrument.ask(write)
        return read

    def GetOPC(self):
        write = '*OPC?'
        read = self._instrument.ask(write)
        return read

    def SetWAI(self):
        write = '*WAI'
        self._instrument.write(write)

    def ReSeT(self):
        write = '*RST'
        self._instrument.write(write)
