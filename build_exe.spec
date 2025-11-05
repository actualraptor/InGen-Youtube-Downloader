# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec file for InGen YouTube Downloader

import sys
from pathlib import Path

block_cipher = None

# Collect all data files
added_files = [
    ('img\\*.*', 'img'),  # Include all files from img folder with T-Rex image
]

a = Analysis(
    ['youtube_downloader_gui.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[
        'yt_dlp',
        'PIL',
        'PIL.Image',
        'PIL.ImageTk',
        'tqdm',
        'tkinter',
    ],
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
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='InGen-YouTube-Downloader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Hide console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='img/trex.png' if Path('img/trex.png').exists() else None,
)

