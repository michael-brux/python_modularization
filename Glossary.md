# Glossary - Python Modularization
## Modul
A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Modules can be imported into other modules or into the main module. Using modules helps organize longer programs by splitting them into several files for easier maintenance.

Key aspects:

- Modules are files with the .py extension.
- They contain Python code, including definitions (functions, classes, ...) and statements.
- Modules provide encapsulation, organization, reusability, and namespace management.
- They are a basic organizational unit of Python code.
- The module's name is available as the global variable `__name__`.
- `__file__` indicates the pathname of the file from which the module was loaded (if loaded from a file)