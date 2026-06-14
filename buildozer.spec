[app]
title = اريد تطبيق بعداد يحسب المده ال
package.name = aiapp
package.domain = org.aibuilder
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,flet==0.24.1
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
[buildozer]
log_level = 2
warn_on_root = 1
