from device.IAudioOutputDevice import IAudioOutputDevice
from device.BluetoothSpeakerAdaptor import BluetoothSpeakerAdaptor, BluetoothSpeakerAPI
from device.WiredSpeakerAdaptor import WiredSpeakerAdaptor, WiredSpeakerAPI
from device.HeadphonesAdaptor import HeadphonesAdaptor, HeadphoneAPI
from enums.DeviceType import DeviceType

class DeviceFactory:
    @staticmethod
    def create_device(device_type: DeviceType):
        if device_type == DeviceType.BLUETOOTH:
            return BluetoothSpeakerAdaptor(BluetoothSpeakerAPI())
        elif device_type == DeviceType.WIRED:
            return WiredSpeakerAdaptor(WiredSpeakerAPI())
        else:
            return HeadphonesAdaptor(HeadphoneAPI())