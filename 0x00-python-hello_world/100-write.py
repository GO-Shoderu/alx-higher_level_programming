#!/usr/bin/python3
import sys
from datetime import datetime

date = datetime(2015, 10, 19)

sys.stderr.write(f"and that piece of art is useful - Dora \
Korpar, {date:%Y-%m-%d}\n")
sys.exit(1)
