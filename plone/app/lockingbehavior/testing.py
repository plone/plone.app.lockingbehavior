from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer


class LockingLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import plone.app.lockingbehavior
        self.loadZCML(package=plone.app.lockingbehavior)


LOCKING_FIXTURE = LockingLayer()
LOCKING_INTEGRATION_TESTING = IntegrationTesting(
    bases=(LOCKING_FIXTURE,), name="PloneAppLockingbehavior:Integration")
LOCKING_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(LOCKING_FIXTURE,), name="PloneAppLockingbehavior:Functional")
