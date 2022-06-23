# -*- mode: python ; coding: utf-8 -*-
import os

block_cipher = None
SETUP_DIR = 'D:\\pyProj\\new-uwin'
p = [SETUP_DIR+'\\gui\\', SETUP_DIR+'\\cipher\\', SETUP_DIR+'\\modern_register\\',
SETUP_DIR+'\\modern_forget_password\\', SETUP_DIR+'\\modern_gui\\',
SETUP_DIR+'\\modern_login\\', SETUP_DIR+'\\modern_modify_password\\',
SETUP_DIR+'\\modern_register\\', SETUP_DIR+'\\modern_login\\',
SETUP_DIR+'\\modern_login\\', SETUP_DIR+'\\modern_verify\\', SETUP_DIR+'\\ui\\']
pyfiles = ['uwin.py', 'error_code.py']
for pi in p:
  for fn in os.listdir(pi):
    if fn.split('.')[-1] == 'py':
      pyfiles.append(pi + fn)
print(pyfiles)
a = Analysis(
    pyfiles,
    pathex=[SETUP_DIR],
    binaries=[],
    datas=[('D:\\pyProj\\new-uwin\\modern_gui\\settings.json', 'modern_gui'),
    ('D:\\pyProj\\new-uwin\\img\\loading.gif', 'img'),
    ('D:\\pyProj\\new-uwin\\icons\\*.png', 'icons'),
    ('D:\\pyProj\\new-uwin\\help\\帮助文档.mht', 'help'),
    ('D:\\pyProj\\new-uwin\\gui\\images\\images\\*.png', 'gui\\images\\images'),
    ('D:\\pyProj\\new-uwin\\gui\\images\\svg_icons\\*.svg', 'gui\\images\\svg_icons'),
    ('D:\\pyProj\\new-uwin\\gui\\images\\svg_images\\*.svg', 'gui\\images\\svg_images'),
    ('D:\\pyProj\\new-uwin\\modern_gui\\gui\\themes\\dracula.json', 'modern_gui\\gui\\themes')],
    hiddenimports=['qrcode', 'PySide6.QtSvg', 'modern_register.register_form', 'modern_verify.verify_form',
    'modern_modify_password.modify_form', 'modern_login.login_form', 'ui.ui_error_dialog', 'ui.progress',
    'requests', 'error_code', 'keras'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=r'D:\pyProj\new-uwin\gui\images\images\icon.png',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='uwin',
)
