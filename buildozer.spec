[app]

# (str) Title of your application
title = Investment Assistant

# (str) Package name
package.name = investment_pro

# (str) Package domain (needed for android/ios packaging)
package.domain = org.investment

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,xlsx,json

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# 优化点 1: 去掉了 openssl (避免冲突)，保留 pandas 必须的 numpy
requirements = python3,kivy==2.3.0,requests,urllib3,pandas,numpy,openpyxl

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = False

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) The entry point of your application
# entrypoint = main.py

# 优化点 2: 显式指定只编译 arm64-v8a (减少 GitHub Actions 一半的压力)
# 现在的手机基本都是 64 位的，这足够用了
android.archs = arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
