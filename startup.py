"""
Startup App Manager Module
-----------------------------
Lists and disables startup programs via the registry Run key
and Startup folder shortcuts.
"""

import winreg
import os

RUN_KEY_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"


def list_startup_registry():
    """List apps in HKCU Run key (per-user startup)."""
    apps = {}
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, RUN_KEY_PATH, 0, winreg.KEY_READ)
        i = 0
        while True:
            try:
                name, value, _ = winreg.EnumValue(key, i)
                apps[name] = value
                i += 1
            except OSError:
                break
        winreg.CloseKey(key)
    except FileNotFoundError:
        pass
    return apps


def disable_startup_app(name):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, RUN_KEY_PATH, 0, winreg.KEY_ALL_ACCESS)
        winreg.DeleteValue(key, name)
        winreg.CloseKey(key)
        print(f"✅ Disabled: {name}")
        return True
    except Exception as e:
        print(f"⚠️  Failed to disable {name}: {e}")
        return False


def interactive_menu():
    apps = list_startup_registry()

    if not apps:
        print("No startup apps found in the current-user Run key.")
        return

    print("\n" + "=" * 70)
    print(" STARTUP APP MANAGER")
    print("=" * 70)
    app_list = list(apps.items())
    for idx, (name, cmd) in enumerate(app_list, start=1):
        print(f"[{idx:2}] {name:<25} — {cmd}")
    print("=" * 70)

    print("\nEnter numbers to disable (comma-separated), or 'exit'.")
    choice = input("> ").strip().lower()

    if choice == "exit":
        return

    try:
        indices = [int(x.strip()) - 1 for x in choice.split(",")]
        selected = [app_list[i][0] for i in indices if 0 <= i < len(app_list)]
    except (ValueError, IndexError):
        print("Invalid input.")
        return

    for name in selected:
        disable_startup_app(name)

    print("\n✅ Done.")


if __name__ == "__main__":
    interactive_menu()
