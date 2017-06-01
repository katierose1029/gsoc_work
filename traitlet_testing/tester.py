import getpass
from traitlets import HasTraits, Unicode, default

class Identity(HasTraits):
    username = Unicode()

    @default('username')
    def _username_default(self):
        return getpass.getuser()


#id = Identity('krc1029')
#print id.username
