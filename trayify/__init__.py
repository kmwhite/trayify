import gtk_icon
import qt_icon


class TrayifyError(Exception):
    ''' Exception Class for Trayify Errors '''

    def __init__(self, value='No value provided'):
        ''' Create a TrayifyError instance '''
        self.value = value

    def __repr__(self):
        ''' Define a textual representation of the Instance '''
        return "{0}: {1}".format(self.__class__.__name__, self.value)


class InvalidUserInterfaceError(TrayifyError):
    ''' Exception: A bad UI type was passed to Trayify '''

    def __init__(self, message='Invalid UI Type'):
        ''' Create a new BadUserInterfaceType Exception '''
        super(InvalidUserInterfaceError, self).__init__(message)


def initialize(ui_type, *args, **kwargs):
    ''' Start-up Trayify '''

    if ui_type == 'gtk':
        return gtk_icon.NotificationIcon()
    elif ui_type == 'qt':
        return qt_icon.NotificationIcon()
    else:
        msg = "{0} is not a valid UI type".format(ui_type)
        raise InvalidUserInterfaceError(msg)
