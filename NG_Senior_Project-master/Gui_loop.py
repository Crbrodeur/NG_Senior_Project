from PyQt5.QtWidgets import QMainWindow
from PyQt5.Qt import QApplication
from gen1gui import Ui_MainWindow
from dataTab import Ui_DataWindow
from qwt.qt.QtGui import QApplication, QPen
from qwt.qt.QtCore import Qt
from qwt import QwtPlot, QwtScaleDraw, QwtPlotGrid, QwtPlotCurve, QwtPlotItem


# Main Window
class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.data_window = DataWindow()
        self.establish_connections()


    # GUI Button animation
    def establish_connections(self):
        self.btConfirm.clicked.connect(self.write_temp)
        self.btStop.clicked.connect(self.cancel_temp_change)
        self.btEmStop.clicked.connect(self.emergency_stop)
        self.tbDataButton.clicked.connect(self.data_window.show)

    # Confirm Button Function
    def write_temp(self):
        self.desiredTemp.display(self.tempSet.value())
        self.tempSet.setEnabled(False)
        self.btConfirm.setEnabled(False)
        # TODO Implement instrument control... Open valve to start cooldown

    # Cancel Button Function
    def cancel_temp_change(self):
        self.tempSet.setEnabled(True)
        self.btConfirm.setEnabled(True)
        # TODO Implement instrument control... Turn off instruments and end cool down

    # Emergency Stop Button
    def emergency_stop(self):
        self.cancel_temp_change()
        # TODO Implement instrument control... Turn off everything (most should be done in cancel_temp_change)

    # Current Temp Monitor
    def display_temp(self):
        pass
        # TODO display temperature of wafer from lakeshore



# Data Window
class DataWindow(QMainWindow, Ui_DataWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.plot = CartesianPlot()
        self..insertWidget(-1,self.plot)
        # self.establish_connections()

    # TODO make this usable and add data stuff


class CartesianAxis(QwtPlotItem):
    """Supports a coordinate system similar to
    http://en.wikipedia.org/wiki/Image:Cartesian-coordinate-system.svg"""
    def __init__(self, masterAxis, slaveAxis):
        """Valid input values for masterAxis and slaveAxis are QwtPlot.yLeft,
        QwtPlot.yRight, QwtPlot.xBottom, and QwtPlot.xTop. When masterAxis is
        an x-axis, slaveAxis must be an y-axis; and vice versa."""
        QwtPlotItem.__init__(self)
        self.__axis = masterAxis
        if masterAxis in (QwtPlot.yLeft, QwtPlot.yRight):
            self.setAxes(slaveAxis, masterAxis)
        else:
            self.setAxes(masterAxis, slaveAxis)
        self.scaleDraw = QwtScaleDraw()
        self.scaleDraw.setAlignment((QwtScaleDraw.LeftScale,
                                     QwtScaleDraw.RightScale,
                                     QwtScaleDraw.BottomScale,
                                     QwtScaleDraw.TopScale)[masterAxis])

    def draw(self, painter, xMap, yMap, rect):
        """Draw an axis on the plot canvas"""
        xtr = xMap.transform
        ytr = yMap.transform
        if self.__axis in (QwtPlot.yLeft, QwtPlot.yRight):
            self.scaleDraw.move(round(xtr(0.0)), yMap.p2())
            self.scaleDraw.setLength(yMap.p1()-yMap.p2())
        elif self.__axis in (QwtPlot.xBottom, QwtPlot.xTop):
            self.scaleDraw.move(xMap.p1(), round(ytr(0.0)))
            self.scaleDraw.setLength(xMap.p2()-xMap.p1())
        self.scaleDraw.setScaleDiv(self.plot().axisScaleDiv(self.__axis))
        self.scaleDraw.draw(painter, self.plot().palette())


class CartesianPlot(QwtPlot):
    """Creates a coordinate system similar system
    http://en.wikipedia.org/wiki/Image:Cartesian-coordinate-system.svg"""
    def __init__(self, *args):
        QwtPlot.__init__(self, *args)
        self.setTitle('Cartesian Coordinate System Demo')
        # create a plot with a white canvas
        self.setCanvasBackground(Qt.white)
        # set plot layout
        self.plotLayout().setCanvasMargin(0)
        self.plotLayout().setAlignCanvasToScales(True)
        # attach a grid
        grid = QwtPlotGrid()
        grid.attach(self)
        grid.setPen(QPen(Qt.black, 0, Qt.DotLine))
        # attach a x-axis
        xaxis = CartesianAxis(QwtPlot.xBottom, QwtPlot.yLeft)
        xaxis.attach(self)
        self.enableAxis(QwtPlot.xBottom, False)
        # attach a y-axis
        yaxis = CartesianAxis(QwtPlot.yLeft, QwtPlot.xBottom)
        yaxis.attach(self)
        self.enableAxis(QwtPlot.yLeft, False)
        # calculate 3 NumPy arrays
        x = np.arange(-2*np.pi, 2*np.pi, 0.01)
        y = np.pi*np.sin(x)
        z = 4*np.pi*np.cos(x)*np.cos(x)*np.sin(x)
        # attach a curve
        curve = QwtPlotCurve('y = pi*sin(x)')
        curve.attach(self)
        curve.setPen(QPen(Qt.green, 2))
        curve.setData(x, y)
        # attach another curve
        curve = QwtPlotCurve('y = 4*pi*sin(x)*cos(x)**2')
        curve.attach(self)
        curve.setPen(QPen(Qt.black, 2))
        curve.setData(x, z)
        self.replot()


def make():
    demo = CartesianPlot()
    demo.resize(400, 300)
    demo.show()
    return demo



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
