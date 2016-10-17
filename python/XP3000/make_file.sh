#!/bin/bash
# Sun May 25 00:51:42 EEST 2014, nickkouk

tool="pyside-uic-2.7"

$tool Main_window.ui -o python_gui.py
$tool Settings.ui -o python_settings.py
$tool history_dialog.ui -o history_settings.py
$tool new_dev.ui -o device_configuration.py

