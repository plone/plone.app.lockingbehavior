Introduction
============

The ``plone.app.lockingbehavior`` package provides a ``plone.locking`` integration
for dexterity.

Usage
-----

Just use the behavior ``plone.app.lockingbehavior.behaviors.ILocking`` in
your dexterity content type. Also check the condition of the "edit" action
of your type, it should check if the object is locked.

In your *profiles/default/types/YOURTYPE.xml* add the behavior and the
edit action::

    <?xml version="1.0"?>
    <object name="example.conference.presenter" meta_type="Dexterity FTI"
            i18n:domain="example.conference" xmlns:i18n="http://xml.zope.org/namespaces/i18n">

        <!-- enabled behaviors -->
        <property name="behaviors">
            <element value="plone.app.lockingbehavior.behaviors.ILocking" />
        </property>

        <action action_id="edit"
                visible="True"
                title="Edit"
                category="object"
                url_expr="string:${object_url}/edit"
                condition_expr="not:object/@@plone_lock_info/is_locked_for_current_user|python:True">
            <permission value="Modify portal content"/>
        </action>

    </object>

The ILocking behavior enables locking support for your content type. This adds
the ``ITTWLockable`` interface from ``plone.locking``. The locking viewlet
from ``plone.app.layout`` is also working for the dexterity content type.


More Information
----------------

* http://pypi.python.org/pypi/plone.locking
