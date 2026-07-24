from DeviceParameters import DeviceParameters
from ControlLogic import ControlLogic
from SafetyChecks import SafetyChecks
d=DeviceParameters();print(d.rate);ControlLogic().run();SafetyChecks().check()
