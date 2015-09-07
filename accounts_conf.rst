Configuration
====================================

#. step 01
#. Append global settings file key with name your decorator 

TEMPLADO_DECORATOR_AUTH = 'accounts.views.must_login'

#. in settings file paste line

LOGIN_REDIRECT_URL = '/templado/'

#. step 02
#. in templado views and urls file paste line

from accounts.views import *

#. and now you could use decorator in urls templado file as

url(r'^help$', getNameDecorators(HelpView.as_view()), name='help'),
