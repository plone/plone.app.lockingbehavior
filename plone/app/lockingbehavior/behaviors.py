# -*- coding: utf-8 -*-
from plone.locking.interfaces import ITTWLockable


class ILocking(ITTWLockable):
    """Behavior interface for marking a dexterity content as lockable.
    """
