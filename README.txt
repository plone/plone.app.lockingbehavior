Introduction
============

The ``plone.app.lockingbehavior`` package provides a ``plone.locking`` integration
for dexterity.

Usage
-----

Just use the behavior ``plone.app.lockingbehavior.behaviors.ILocking`` in
your dexterity content type.

In your *profiles/default/types/YOURTYPE.xml* add the behavior::

    <?xml version="1.0"?>
    <object name="example.conference.presenter" meta_type="Dexterity FTI"
       i18n:domain="example.conference" xmlns:i18n="http://xml.zope.org/namespaces/i18n">

     <!-- enabled behaviors -->
     <property name="behaviors">
         <element value="plone.app.lockingbehavior.behaviors.ILocking" />
     </property>

    </object>


The ILocking behavior enables locking support for your content type. This adds
the ``ITTWLockable`` interface from ``plone.locking``. The locking viewlet
from ``plone.app.layout`` is also working for the dexterity content type.


More Information
----------------

* http://pypi.python.org/pypi/plone.locking
