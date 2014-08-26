#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2012-2013, 2013 Scott Rice
# All rights reserved.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#

import sys, os
import unittest
import tempfile
import subprocess
import re

import steam_grid
from steam_shortcut_manager import SteamShortcutManager


def custom_image(grid_dir, filename):
  valid_custom_image_extensions = [".png", ".jpg", ".jpeg", ".tga"]
  for ext in valid_custom_image_extensions:
    image_location = os.path.join(grid_dir, filename+ext)
    if os.path.isfile(image_location):
      return image_location
  return None

def main(steam_install_dir):
  file_name = "shortcuts.vdf"
  grid_dir = os.path.join(steam_install_dir,"config","grid")
  if not os.path.exists(grid_dir):
    print os.makedirs(grid_dir)
  gridmanager = steam_grid.SteamGrid(steam_install_dir)

  shortcut_dir = os.path.join(steam_install_dir,"config")
  shortcut_path = os.path.join(shortcut_dir,file_name)
  shortcut_manager = SteamShortcutManager(shortcut_path)

  for shortcut in shortcut_manager.shortcuts:
    appname = shortcut.appname
    exe = shortcut.exe
    imagename = gridmanager.filename_for_shortcut(appname,exe)

    if re.match(".*[&!]+",appname):
      print "SKIPPED: "+appname
      continue
    customimage = custom_image(grid_dir,imagename)
    if customimage != None:
      #print "oblytile.exe" + "\""+appname+"\" "+exe+" \"\" \"" +customimage+"\" \"\" \"\" \""+customimage+"\" \"\" #2D8AEF #FFFFFF show admin no no no wide"+"\n"
      subprocess.call(["oblytile.exe", appname, exe,"", customimage, "", "", customimage, "", "#2D8AEF", "#FFFFFF", "show", "admin", "no", "no", "no", "wide"], shell=True)
    else:
      print "SKIPPED (Image \""+imagename+"\" not found): "+appname

if __name__ == "__main__":
  if len(sys.argv) != 2:
        print "Usage: windows_steamgrid.exe <USER FOLDER>"
        print "example: \"windows_steamgrid.exe C:\Program Files (x86)\Steam\userdata\\1234567\"   (replace 1234567 with your user id)"
        sys.exit(1)
  main(sys.argv[1])

