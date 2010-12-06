from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from zope.configuration import xmlconfig


class LockingLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import plone.app.lockingbehavior
        xmlconfig.file('configure.zcml', plone.app.lockingbehavior,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        pass


LOCKING_FIXTURE = LockingLayer()
LOCKING_INTEGRATION_TESTING = IntegrationTesting(
    bases=(LOCKING_FIXTURE,), name="PloneAppLockingbehavior:Integration")
LOCKING_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(LOCKING_FIXTURE,), name="PloneAppLockingbehavior:Functional")
