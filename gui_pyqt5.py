import sys
# import Adafruit_DHT
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QPushButton, QComboBox, QSpinBox, QMenuBar, QAction, QMainWindow, QLineEdit, QInputDialog, QFrame, QCheckBox, QTextEdit
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

class ControlPanel(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        # self.sensor = Adafruit_DHT.DHT22
        # self.pin = 4  # GPIO pin number where the sensor is connected
        # self.update_temperature()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        main_layout = QHBoxLayout(self.central_widget)

        control_layout = QVBoxLayout()

        # Set default font size
        default_font = self.font()
        default_font.setPointSize(11)
        self.setFont(default_font)

        # Menu bar
        menubar = self.menuBar()
        
        # Font size menu
        font_menu = menubar.addMenu('Font Size')
        set_font_size_action = QAction('Set Font Size', self)
        set_font_size_action.triggered.connect(self.set_font_size)
        font_menu.addAction(set_font_size_action)

        # Fan speed control
        fan_frame = QFrame(self)
        fan_frame.setFrameShape(QFrame.Box)
        fan_layout = QVBoxLayout(fan_frame)
        self.fan_control_label = QLabel('Fan Control', self)
        self.fan_speed_input = QSpinBox(self)
        self.fan_speed_input.setRange(0, 100)
        self.fan_speed_input.setSuffix(' %')
        self.fan_time_input = QSpinBox(self)
        self.fan_time_input.setRange(1, 60)
        self.fan_time_input.setSuffix(' min')
        fan_button_layout = QHBoxLayout()
        self.start_fan_button = QPushButton('Start Fan', self)
        self.start_fan_button.clicked.connect(self.start_fan)
        self.stop_fan_button = QPushButton('Stop Fan', self)
        self.stop_fan_button.clicked.connect(self.stop_fan)
        fan_button_layout.addWidget(self.start_fan_button)
        fan_button_layout.addWidget(self.stop_fan_button)
        fan_layout.addWidget(self.fan_control_label)
        fan_layout.addWidget(self.fan_speed_input)
        fan_layout.addWidget(self.fan_time_input)
        fan_layout.addLayout(fan_button_layout)
        control_layout.addWidget(fan_frame)

        # Temperature display
        temp_frame = QFrame(self)
        temp_frame.setFrameShape(QFrame.Box)
        temp_layout = QVBoxLayout(temp_frame)
        self.temp_label = QLabel('Temperature (°C)', self)
        self.temp_display = QLCDNumber(self)
        temp_layout.addWidget(self.temp_label)
        temp_layout.addWidget(self.temp_display)
        control_layout.addWidget(temp_frame)

        # Pump control
        pump_frame = QFrame(self)
        pump_frame.setFrameShape(QFrame.Box)
        pump_layout = QVBoxLayout(pump_frame)
        self.pump_label = QLabel('Pump Control (minutes)', self)
        self.pump_time_input = QSpinBox(self)
        self.pump_time_input.setRange(1, 60)
        self.pump_time_input.setSuffix(' min')
        pump_button_layout = QHBoxLayout()
        self.pump_button = QPushButton('Start Pump', self)
        self.pump_button.clicked.connect(self.start_pump)
        self.stop_pump_button = QPushButton('Stop Pump', self)
        self.stop_pump_button.clicked.connect(self.stop_pump)
        pump_button_layout.addWidget(self.pump_button)
        pump_button_layout.addWidget(self.stop_pump_button)
        pump_layout.addWidget(self.pump_label)
        pump_layout.addWidget(self.pump_time_input)
        pump_layout.addLayout(pump_button_layout)
        control_layout.addWidget(pump_frame)

        # LED control
        led_frame = QFrame(self)
        led_frame.setFrameShape(QFrame.Box)
        led_layout = QVBoxLayout(led_frame)
        self.led_label = QLabel('LED Light Control', self)
        self.led_circuit_1 = QCheckBox('Circuit 1', self)
        self.led_circuit_2 = QCheckBox('Circuit 2', self)
        self.led_circuit_3 = QCheckBox('Circuit 3', self)
        self.led_time_input = QSpinBox(self)
        self.led_time_input.setRange(1, 60)
        self.led_time_input.setSuffix(' min')
        led_button_layout = QHBoxLayout()
        self.start_led_button = QPushButton('Start LED', self)
        self.start_led_button.clicked.connect(self.start_led)
        self.stop_led_button = QPushButton('Stop LED', self)
        self.stop_led_button.clicked.connect(self.stop_led)
        led_button_layout.addWidget(self.start_led_button)
        led_button_layout.addWidget(self.stop_led_button)
        led_layout.addWidget(self.led_label)
        led_layout.addWidget(self.led_circuit_1)
        led_layout.addWidget(self.led_circuit_2)
        led_layout.addWidget(self.led_circuit_3)
        led_layout.addWidget(self.led_time_input)
        led_layout.addLayout(led_button_layout)
        control_layout.addWidget(led_frame)

        main_layout.addLayout(control_layout)

        # Message window
        self.message_window = QTextEdit(self)
        self.message_window.setReadOnly(True)
        main_layout.addWidget(self.message_window)

        self.setWindowTitle('Control Panel')

    def set_font_size(self):
        size, ok = QInputDialog.getInt(self, 'Set Font Size', 'Enter font size (8-72):', value=11, min=8, max=72)
        if ok:
            font = self.font()
            font.setPointSize(size)
            self.setFont(font)

    def set_fan_speed(self):
        value = self.fan_speed_input.value()
        # Add code here to control fan speed
        self.message_window.append(f'Set fan speed to {value}%')

    def start_fan(self):
        speed = self.fan_speed_input.value()
        time = self.fan_time_input.value()
        # Add code here to start the fan
        self.message_window.append(f'Fan started at {speed}% speed for {time} minutes')
        QTimer.singleShot(time * 60000, self.stop_fan)

    def stop_fan(self):
        # Add code here to stop the fan
        self.message_window.append('Fan stopped')

    def start_pump(self):
        time = self.pump_time_input.value()
        # Add code here to start the pump
        self.message_window.append(f'Pump started for {time} minutes')
        QTimer.singleShot(time * 60000, self.stop_pump)

    def stop_pump(self):
        # Add code here to stop the pump
        self.message_window.append('Pump stopped')

    def start_led(self):
        circuits = []
        if self.led_circuit_1.isChecked():
            circuits.append('Circuit 1')
        if self.led_circuit_2.isChecked():
            circuits.append('Circuit 2')
        if self.led_circuit_3.isChecked():
            circuits.append('Circuit 3')
        time = self.led_time_input.value()
        if circuits:
            # Add code here to start the selected LED circuits
            self.message_window.append(f'Started {", ".join(circuits)} for {time} minutes')
            QTimer.singleShot(time * 60000, self.stop_led)
        else:
            self.message_window.append('Error: No LED circuit selected')

    def stop_led(self):
        # Add code here to stop the LED circuits
        self.message_window.append('LED stopped')

    def update_temperature(self):
        pass
        # humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        # if temperature is not None:
        #     self.temp_display.display(temperature)
        #     self.message_window.append(f'Temperature updated: {temperature:.1f}°C')
        # else:
        #     self.message_window.append('Error: Failed to read temperature sensor')
        # QTimer.singleShot(2000, self.update_temperature)  # Update every 2 seconds

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ControlPanel()
    ex.show()
    sys.exit(app.exec_())
