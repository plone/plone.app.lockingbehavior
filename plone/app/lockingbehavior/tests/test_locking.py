# -*- coding: utf-8 -*-
import unittest
from plone.app.lockingbehavior.testing import LOCKING_FUNCTIONAL_TESTING
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_PASSWORD
from plone.app.testing import setRoles
from plone.dexterity.fti import DexterityFTI
from plone.testing import z2
import transaction


class TestLockingBehavior(unittest.TestCase):

    layer = LOCKING_FUNCTIONAL_TESTING

    def setUp(self):
        # add IShortName behavior to Page
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

        fti = DexterityFTI('LockableType',
                           factory='LockableType')
        fti.behaviors = ('plone.app.lockingbehavior.behaviors.ILocking', )
        fti.global_allow = True
        self.portal.portal_types._setObject('LockableType', fti)
        transaction.commit()

        # prepare two browsers
        self.foo_browser = z2.Browser(self.layer['app'])
        self.foo_browser.addHeader(
            'Authorization', 'Basic %s:%s'
            % (SITE_OWNER_NAME, SITE_OWNER_PASSWORD,)
        )
        self.foo_browser.open('http://nohost/plone')

        self.bar_browser = z2.Browser(self.layer['app'])
        self.bar_browser.addHeader(
            'Authorization', 'Basic %s:%s'
            % (TEST_USER_NAME, TEST_USER_PASSWORD,)
        )
        self.bar_browser.open('http://nohost/plone')

    def test_lockablebehavior(self):
        # Add a lockable item
        self.portal.invokeFactory(
            'LockableType', id='lockabletype', title='Lockable Type')
        obj = self.portal['lockabletype']
        transaction.commit()

        # Edit it with User1
        self.foo_browser.open(obj.absolute_url())
        self.assertEqual(
            self.foo_browser.url, 'http://nohost/plone/lockabletype')
        self.foo_browser.getLink('Edit').click()

        # Is locked for User2
        self.bar_browser.open(obj.absolute_url())
        self.assertIn('This item was locked', self.bar_browser.contents)

        # Clicking Edit will redirect to view for User2
        self.bar_browser.getLink('Edit').click()
        self.assertEqual(
            self.bar_browser.url, 'http://nohost/plone/lockabletype/@@view')
        self.assertIn('This item was locked', self.bar_browser.contents)

        # Unlock it
        self.foo_browser.getControl('Save').click()

        # Is now unlocked for User2
        self.bar_browser.open(obj.absolute_url())
        self.assertNotIn('This item was locked', self.bar_browser.contents)

        # Edit it with User2
        self.bar_browser.getLink('Edit').click()
        self.assertIn(
            'http://nohost/plone/lockabletype/edit', self.bar_browser.url)
        self.assertNotIn('This item was locked', self.bar_browser.contents)

        # Is locked for User1
        self.foo_browser.open(obj.absolute_url())
        self.assertIn('This item was locked', self.foo_browser.contents)

        # Releasing the lock by closing the window by User1 does not work
        self.bar_browser.open(obj.absolute_url())

        # The obj is still locked
        self.foo_browser.open(obj.absolute_url())
        self.assertIn('This item was locked', self.foo_browser.contents)

        # Instead you need to release it by saving
        self.bar_browser.getLink('Edit').click()
        self.bar_browser.getControl('Save').click()

        # Now it is unlocked
        self.foo_browser.open(obj.absolute_url())
        self.assertNotIn('This item was locked', self.foo_browser.contents)
