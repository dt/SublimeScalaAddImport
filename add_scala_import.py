import sublime, sublime_plugin

CLASSES = sublime.CLASS_WORD_START | sublime.CLASS_PUNCTUATION_START | sublime.CLASS_LINE_END

class ScalaAddImportLine(sublime_plugin.TextCommand):
  def run(self, edit, sym):
    end_of_imports = self.view.find_all('import .*\n\n')
    if len(end_of_imports) != 1:
      raise ValueError('where do i put this import?!')
    else:
      line = 'import {}\n'.format(sym)
      self.view.insert(edit, end_of_imports[-1].end() - 1, line)
      self.view.set_status('scalaimport', 'Imported ' + sym)


class ScalaFindAndImportSymbol(sublime_plugin.TextCommand):
  def run(self, edit):
    for s in self.view.sel():
      if len(s) == 0:
        s = self.view.expand_by_class(s.begin(), CLASSES, "[]{}()<>:.")
      sym = self.view.substr(s).strip()
      if sym:
        self.view.set_status('scalaimport', 'Searching for packages containing "{}"...'.format(sym))
        return self.find_and_import(sym)

  def find_and_import(self, sym):
    hits = self.view.window().lookup_symbol_in_index(sym)
    pkgs = []

    for hit in hits:
      with open(hit[0], 'r') as fp:
        for line in fp.readlines():
          if line.startswith('package '):
            pkgs.append(line[len('package '):].strip())

    if not pkgs:
      self.view.set_status('scalaimport', 'Could not find any packages containing "{}"'.format(sym))
    else:
      def picked(i):
        if picked != -1:
          chosen = pkgs[i] + '.' + sym
          self.view.run_command('scala_add_import_line', {'sym': chosen})

      self.view.window().show_quick_panel(pkgs, picked)
