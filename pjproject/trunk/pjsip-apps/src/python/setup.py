from distutils.core import setup, Extension
import os
import sys

VERSION = "0.9.0"

# Fill in pj_inc_dirs
pj_inc_dirs = []
f = os.popen("make -f helper.mak inc_dir")
for line in f:
	pj_inc_dirs.append(line.rstrip("\r\n"))
f.close()

# Fill in pj_lib_dirs
pj_lib_dirs = []
f = os.popen("make -f helper.mak lib_dir")
for line in f:
	pj_lib_dirs.append(line.rstrip("\r\n"))
f.close()

# Fill in pj_libs
pj_libs = []
f = os.popen("make -f helper.mak libs")
for line in f:
	pj_libs.append(line.rstrip("\r\n"))
f.close()

# Mac OS X depedencies
if sys.platform == 'darwin':
	extra_link_args = ["-framework", "CoreFoundation", 
			   "-framework", "AudioToolbox"]
else:
	extra_link_args = []


setup(name="_pjsua", version=VERSION,
	ext_modules = [
		Extension("_pjsua", 
			  ["_pjsua.c"], 
			  define_macros=[('PJ_AUTOCONF', '1'),],
			  include_dirs=pj_inc_dirs, 
			  library_dirs=pj_lib_dirs, 
			  libraries=pj_libs,
			  extra_link_args=extra_link_args),
	])

setup(name="pjsua", version=VERSION, py_modules=["pjsua"])


