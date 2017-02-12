Changelog
=========

1.0.5 (2017-02-12)
------------------

Bug fixes:

- Add coding header on python files.
 [gforcada]
- Unskip test for Zope 4, as isolation problems are already fixed.
  [thet]


1.0.4 (2016-05-02)
------------------

New:

- Add behavior short name.
  [jensens]


1.0.3 (2016-02-20)
------------------

Fixes:

- Use a functional layer to resolve test isolation problems.
  [gforcada]

- Refactor doctest to an integration test and skip it for Zope 4 due to isolation problems.
  [pbauer]

- Changed i18n_domain to "plone".
  Requires plone.app.locales 4.3.9 or higher.
  [claytonc]


1.0.2 (2015-09-09)
------------------

- Remove superfluous 'for'.
  [fulv]

- Fix tests: redirect was changed in commit e7367258.
  [jone]

- If the content is locked, the redirect points to the default view and
  not to the absolute_url of the object. It avoids image opening on redirect
  [parruc]


1.0.1 (2011-12-06)
------------------

- Fix version requirement of plone.dexterity: 1.1 is compatible.
  [jone]


1.0 (2011-11-27)
----------------

- Fixed problem: locks were not released when editing content and saving
  it without changing anything. Fixed by using new IEditFinishedEvent instead
  of IObjectModifiedEvent.
  [jbaumann]

- Fixed problem which caused widget traversal to fail.
  The edit form is now protected for non-anonymous user, since locking for
  anyonmous users does not work anyway.
  [jbaumann]

- Initial implementation
  [jbaumann]
