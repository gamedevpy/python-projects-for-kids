#!/usr/bin/env python3
import sys

sys.path.append('./lib')

# import Color.Helper
# color_helper = Color.Helper()


from Color.Helper import Helper
color_helper = Helper()


green = color_helper.getGreen()

print(green)