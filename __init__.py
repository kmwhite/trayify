import gtk_icon
import qt_icon

class TrayifyError(Exception):
    ''' Exception Class for Trayify Errors '''
    def __init__(self, value):
        ''' Create a TrayifyError instance '''
        self.value = value
    def __repr__(self):
        ''' Define a textual representation of the Instance '''
        return "{0}: {1}".format( self.__class__.__name__ , self.value )

class InvalidUserInterfaceError(TrayifyError):
    ''' Exception: A bad UI type was passed to Trayify '''
    def __init__(self):
        ''' Create a new BadUserInterfaceType Exception '''
        super().__init__('Invalid UI Type')


def initialize(ui_type, *args, **kwargs):
    ''' Start-up Trayify '''

    if ui_type == 'gtk':
        return gtk_icon.NotificationIcon()
    elif ui_type == 'qt':
        return qt_icon.NotificationIcon()
    else:
        raise InvalidUserInterfaceError()
