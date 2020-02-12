import xadmin
from users.models import EmailVerifyRecord, UserProfile

class EmailVerifyRecordAdmin(object):
    pass
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)



