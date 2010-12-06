import unittest2 as unittest
import doctest
from plone.testing import layered
from plone.app.lockingbehavior.testing import LOCKING_INTEGRATION_TESTING


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite('locking.txt'),
                layer=LOCKING_INTEGRATION_TESTING),
    ])
    return suite

