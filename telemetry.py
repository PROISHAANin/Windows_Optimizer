"""
Telemetry Disabler Module
---------------------------
Disables Windows telemetry/data collection via registry edits.
Requires Administrator privileges.
"""

import winreg
import ctypes
import sys

TELEMETRY_KEYS = [
    {
        "path": r"SOFTWARE\Policies\Microsoft\Windows\DataCollection",
        "name": "AllowTelemetry",
        "value": 0,
        "type": winreg.REG_DWORD,
        "hive": winreg.HKEY_LOCAL_MACHINE,
        "desc": "Disable telemetry data collection"
    },
    {
        "path": r"SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo",
        "name": "Enabled",
        "value": 0,
        "type": winreg.REG_DWORD,
        "hive": winreg.HKEY_CURRENT_USER,
        "desc": "Disable Advertising ID"
    },
    {
        "path": r"SOFTWARE\Microsoft\Windows\CurrentVersion\Privacy",
        "name": "TailoredExperiencesWithDiagnosticDataEnabled",
        "value": 0,
        "type": winreg.REG_DWORD,
        "hive": winreg.HKEY_CURRENT_USER,
        "desc": "Disable tailored experiences using diagnostic data"
    },
]


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


def apply_key(entry):
    try:
        key = winreg.CreateKeyEx(entry["hive"], entry["path"], 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, entry["name"], 0, entry["type"], entry["value"])
        winreg.CloseKey(key)
        print(f"✅ Applied: {entry['desc']}")
        return True
    except PermissionError:
        print(f"❌ Permission denied for: {entry['desc']} (run as Administrator)")
        return False
    except Exception as e:
        print(f"⚠️  Failed: {entry['desc']} — {e}")
        return False


def interactive_menu():
    if not is_admin():
        print("❌ This module requires Administrator privileges. Re-run as Admin.")
        sys.exit(1)

    print("\n⚠️  This will modify registry settings to disable telemetry.")
    print("Recommended: create a System Restore Point first.\n")

    for entry in TELEMETRY_KEYS:
        print(f"  - {entry['desc']}")

    confirm = input("\nApply all telemetry-disabling settings? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Aborted.")
        return

    for entry in TELEMETRY_KEYS:
        apply_key(entry)

    print("\n✅ Done. Restart recommended for full effect.")


if __name__ == "__main__":
    interactive_menu()
