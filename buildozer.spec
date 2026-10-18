[app]
title = Школьный помощник
package.name = schoolhelper
package.domain = org.schoolhelper
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.01.4

requirements = python3,kivy==2.3.0,kivymd==2.0.1.dev0,materialyoucolor,asynckivy,asyncgui,exceptiongroup,pillow,plyer,pyjnius,android

orientation = portrait
fullscreen = 0

android.permissions = POST_NOTIFICATIONS,VIBRATE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
