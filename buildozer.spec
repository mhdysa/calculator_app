[app]

# (str) Title of your application
title = ماشین حساب

# (str) Package name
package.name = calculatorapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (can be glob patterns)
source.include_exts = py,png,jpg,kv,atlas,ico,ttf

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*,fonts/*

# (list) Source files to exclude (can be glob patterns)
source.exclude_exts = spec

# (list) List of directory to exclude (can be glob patterns)
source.exclude_dirs = tests, bin, docs

# (list) List of additional files to include
source.include_files = a.ico

# (str) Application versioning (method 1)
version = 1.0.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
requirements = python3,kivy==2.2.1

# (str) Custom source folders for requirements
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = a.ico

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (bool) If True, the status bar will be hidden
# android.statusbar_hidden = False

# (bool) Indicate if the application should display a log on the screen
# log_enabled = True

# (str) Log level (debug, info, warning, error, critical)
# log_level = 2

# (bool) If True, the log will be redirected to a file
# log_to_file = True

# (str) The log file path
# log_file = /sdcard/%(package.name)s.log

# Android specific
[app@android]

# (int) Android API to use
android.api = 31

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version
android.sdk = 33

# (str) Android NDK version
android.ndk = 23b

# (str) Android NDK directory
# android.ndk_path =

# (str) Android SDK directory
# android.sdk_path =

# (str) Android ant directory
# android.ant_path =

# (str) Android Java directory
# android.java_path =

# (list) Permissions
android.permissions = INTERNET

# (list) Android meta-data to add
# android.meta_data =

# (list) Android features to add
# android.features =

# (str) Android addtional Java code to include
# android.add_src =

# (str) Android gradle dependencies to include
# android.gradle_dependencies =

# (str) Android manifest additions
# android.manifest_application = 
# android.manifest_activity =
# android.manifest =

# (str) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libs armeabi-v7a directory
# android.copy_libs = armeabi-v7a

# (bool) If True, the packaging will be in AAR mode
# android.aar = False

# (bool) If True, the packaging will be in AAB mode
# android.aab = False

# (bool) If True, the packaging will be in APK mode
# android.apk = True

# (bool) If True, the packaging will be in App Bundle mode
# android.app_bundle = False

# (str) Android debug mode (debug, release, or both)
# android.debug = debug

# (bool) If True, the application will be signed
# android.sign = False

# (str) Keystore file
# android.keystore =

# (str) Keystore password
# android.keystore_password =

# (str) Keystore alias
# android.keystore_alias =

# (str) Key password
# android.key_password =

# (bool) If True, the application will be zipaligned
# android.zipalign = True

# iOS specific
[app@ios]

# (str) iOS bundle identifier
# ios.bundle_identifier = org.example.calculatorapp

# (str) iOS version
# ios.version = 1.0.0

# (str) iOS icon
# ios.icon =

# (str) iOS framework
# ios.framework =

# (list) iOS plist items
# ios.plist_items =

# Buildozer spec
[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage
build_dir = ./build

# (str) Path to build output (i.e. .apk, .aab, .ipa)
bin_dir = ./bin

# (str) Path to buildozer's distfiles directory
# dist_dir = ./dist

# (str) Path to buildozer's cache directory
# cache_dir = ./cache

# (str) Path to buildozer's local data directory
# local_data_dir = ./local_data

# (str) Path to buildozer's global data directory
# global_data_dir = ~/.buildozer

# (str) Path to buildozer's log directory
# log_dir = ./logs

# (str) Name of the application distribution
# dist_name = calculatorapp

# (str) The android platform directory
# android.platform = android-31

# (str) The android NDK directory
# android.ndk = android-ndk-r23b

# (str) The android SDK directory
# android.sdk = android-sdk

# (str) The android ANT directory
# android.ant = apache-ant-1.9.4

# (str) The android python-for-android directory
# android.p4a = python-for-android
