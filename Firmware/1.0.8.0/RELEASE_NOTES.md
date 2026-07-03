# 🐼 PandaTouch Firmware Release v1.0.8.0

## 📖 Overview

This release is intended for all users, with major improvements to **system stability**, **OTA reliability**, **AMS support**, and the overall **UI/UX experience**.

### ✨ Highlights

- Redesigned the AMS interface with clearer slot layout and status display.
- Refactored the filament management interface and related filament management logic.
- Improved AMS2 / AMS-HT detection logic.
- Added printer / group list view modes.
- Optimized print wake behavior so the device stays awake while a print task is running.
- Added a screen saver mode during printing.
- Fixed crashes and repeated reboot issues caused by sleep / wake behavior.
- Refactored the file manager interface and improved file management logic and thumbnail display.
- Fixed a device reboot issue that could occur when logging in to a Bambu Lab cloud account.
- Improved Wi-Fi compatibility for WPA2 / WPA3 networks.
- Added validation to the OTA IMG update process and improved update stability.
- Updated HMS notification prompts and added new notification messages.

---

## 📋 Changelog

### 🔧 Bug Fixes

- Fixed repeated reboot issues caused by sleep / wake crashes.  
  [https://github.com/bigtreetech/PandaTouch/issues/260](https://github.com/bigtreetech/PandaTouch/issues/260)

- Fixed frequent short-cycle reboot issues and reboot loops after wake or print start.  
  [https://github.com/bigtreetech/PandaTouch/issues/328](https://github.com/bigtreetech/PandaTouch/issues/328)

- Added validation to the OTA IMG update process and improved update stability, reducing the probability of update failures during flashing.  
  [https://github.com/bigtreetech/PandaTouch/issues/327](https://github.com/bigtreetech/PandaTouch/issues/327)

- Fixed AMS2 / AMS-HT search and detection logic.  
  [https://github.com/bigtreetech/PandaTouch/issues/332](https://github.com/bigtreetech/PandaTouch/issues/332)

- Fixed external spool holder loading logic to ensure feed / unload operations work correctly.

- Fixed external spool refresh and AMS slot mapping issues to ensure slot status is displayed correctly.  
  [https://github.com/bigtreetech/PandaTouch/issues/313](https://github.com/bigtreetech/PandaTouch/issues/313)

- Improved WPA2 / WPA3 Wi-Fi compatibility.  
  [https://github.com/bigtreetech/PandaTouch/issues/331](https://github.com/bigtreetech/PandaTouch/issues/331)

- Fixed a device reboot issue that could occur when logging in to a Bambu Lab cloud account.

### 🚀 Functional Optimizations

- Optimized print wake behavior so the device stays awake while a print task is running.

![wake](https://raw.githubusercontent.com/bigtreetech/PandaTouch/master/Firmware/1.0.8.0/images/wake.png)

- Redesigned the firmware warning flow to make the recovery path clearer.  
  [https://github.com/bigtreetech/PandaTouch/issues/333](https://github.com/bigtreetech/PandaTouch/issues/333)

- Optimized warning prompts during firmware updates.

- Redesigned the AMS interface with clearer slot layout and status display.

![ams2](https://raw.githubusercontent.com/bigtreetech/PandaTouch/master/Firmware/1.0.8.0/images/ams2.png)

- Refactored the filament management interface and related filament management logic.

![ams-ext](https://raw.githubusercontent.com/bigtreetech/PandaTouch/master/Firmware/1.0.8.0/images/ams-ext.png)

- Added printer and group list view modes.  
  [https://github.com/bigtreetech/PandaTouch/issues/92](https://github.com/bigtreetech/PandaTouch/issues/92)

![List Mode](https://raw.githubusercontent.com/bigtreetech/PandaTouch/master/Firmware/1.0.8.0/images/List-Mode.png)

![homeListMode](https://raw.githubusercontent.com/bigtreetech/PandaTouch/master/Firmware/1.0.8.0/images/homeListMode.png)

- Optimized step prompts in the feed / unload operation flow.

- Optimized warning popups.

- Added a screen saver mode during printing to help prevent accidental operation while a print is running.

![pandatouch-screenshot](https://raw.githubusercontent.com/bigtreetech/PandaTouch/master/Firmware/1.0.8.0/images/pandatouch-screenshot.png)

- Refactored the file manager interface and improved file management logic and thumbnail display logic.  
  [https://github.com/bigtreetech/PandaTouch/issues/276](https://github.com/bigtreetech/PandaTouch/issues/276)

![File Manager List Mode](https://raw.githubusercontent.com/bigtreetech/PandaTouch/master/Firmware/1.0.8.0/images/File-Manager-List-Mode.png)

![File Manager View Mode](https://raw.githubusercontent.com/bigtreetech/PandaTouch/master/Firmware/1.0.8.0/images/File-Manager-View-Mode.png)

![USB Stick View Mode](https://raw.githubusercontent.com/bigtreetech/PandaTouch/master/Firmware/1.0.8.0/images/USB-stick-View-Mode.png)

- Updated notification prompts and added new notification message content.

---

## 🔄 Update Method

Firmware update guide:

- [https://global.bttwiki.com/PandaTouch.html#how-to-update-firmware](https://global.bttwiki.com/PandaTouch.html#how-to-update-firmware)
