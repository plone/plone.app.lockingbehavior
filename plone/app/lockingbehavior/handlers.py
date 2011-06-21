import AccessControl
from zExceptions import Redirect
from zope.component import getMultiAdapter


def protect_edit_form(obj, event):
    """If the object is locked for the current user, let's redirect to
    the view of the object, where the lockinfo viewlet usually is.
    """

    # Since locking does not work for anonymous users, so we disable the
    # redirect for them. This also makes widget traversal work, since the
    # widget traversal is always anonymous.
    nobody = AccessControl.SecurityManagement.SpecialUsers.nobody
    if AccessControl.getSecurityManager().getUser() == nobody:
        return

    info = getMultiAdapter((obj, obj.REQUEST),
                                name="plone_lock_info")

    if info.is_locked_for_current_user():
        raise Redirect(obj.absolute_url())
