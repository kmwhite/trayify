import gtk_icon
import qt_icon

# Trayify is covered by the 3-Clause BSD License:
LICENSE='''
 Copyright (c) 2012, Kristofer M White
 All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions are
 met:

 * Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
 * Neither the name of the software nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
 PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

class TrayifyError(Exception):
    ''' Exception Class for Trayify Errors '''

    def __init__(self, value='No value provided'):
        ''' Create a TrayifyError instance '''
        self.value = value

    def __str__(self):
        ''' Define a textual representation of the Instance '''
        return "{0}: {1}".format(self.__class__.__name__, self.value)


class InvalidUserInterfaceError(TrayifyError):
    ''' Exception: A bad UI type was passed to Trayify '''

    def __init__(self, message='Invalid UI Type'):
        ''' Create a new BadUserInterfaceType Exception '''
        super(InvalidUserInterfaceError, self).__init__(message)


def initialize(ui_type, *args, **kwargs):
    ''' Start-up Trayify '''

    if ui_type == 'appindicator':
        return gtk_icon.NotificationIcon('appindicator')
    elif ui_type == 'gtk':
        return gtk_icon.NotificationIcon()
    elif ui_type == 'qt':
        return qt_icon.NotificationIcon()
    else:
        msg = "{0} is not a valid UI type".format(ui_type)
        raise InvalidUserInterfaceError(msg)
