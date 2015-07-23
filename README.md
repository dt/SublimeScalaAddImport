Scala import manager for Sublime
====================
A tiny Sublime Text plugin that wraps many of the python tools Foursquare uses to work with and maintain tidy imports when working in Scala.

## Features

### Find and import selected symbol (`Cmd+Shift+i`)
Uses sublime's built-in symbol lookup to find definations, lets you pick which you want, and adds the import. Bonus points: if nothing is selected, will attempt to parse a sybol right before the cursor, so you can add-import right after typing a new symbol, without having to stop and select it first.

### Sort Imports (`Cmd+Shift+u`) (TODO)
Sort (and combine) imports. Will attempt to normalize imports of `a.b.x` and `a.b.y` into `a.b.{x, y}`, add line wrapping at configured widths, etc. Configured packages can also be sorted separately (eg some like to have stdlib imports separated).

### Remove Unused imports (`Cmd+Shift+j`) (TODO)
Remove imports of specific symbols that do not appear in the rest of the file. Does not remove wildcard (`a.b._`) imports or imports with a final component starting with a lowercase letter, as these are usually used implicitly, which cannot be determined via simple text search.

# Authors
- [dt](/dt)
- [benjyw](/benjyw)
