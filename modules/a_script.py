#!/usr/bin/env python3

import a_module	 # import module
import dir_a.b_module  # module is in dir_a (with dot notation)
from dir_b import c_module  # alternative: from dir_b

a_module.hello()  # call function in module
dir_a.b_module.hello() # ... and in sub directory
c_module.hello() # ... from other sub directory
