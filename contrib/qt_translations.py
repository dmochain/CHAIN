#!/usr/bin/env python

# Helpful little script that spits out a comma-separated list of
# language codes for Qt icons that should be included
# in binary dmomint distributions

import glob
import os
import re
import sys

if len(sys.argv) != 3:
  sys.exit("Usage: %s $QTDIR/translations $DMOMINTDIR/src/qt/locale"%sys.argv[0])

d1 = sys.argv[1]
d2 = sys.argv[2]

l1 = set([ re.search(r'qt_(.*).qm', f).group(1) for f in glob.glob(os.path.join(d1, 'qt_*.qm')) ])
l2 = set([ re.search(r'dmomint_(.*).qm', f).group(1) for f in glob.glob(os.path.join(d2, 'dmomint_*.qm')) ])

print ",".join(sorted(l1.intersection(l2)))

