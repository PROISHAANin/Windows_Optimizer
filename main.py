"""
Windows Optimizer Toolkit — Main Menu
=======================================
A modular Windows debloating and optimization tool.

Run as Administrator for full functionality.
"""

import sys
import ctypes
from modules import debloat, telemetry, cleaner, startup, service_optimizer


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


def print_banner():
    print("=" * 70)
    print(" 🛠️   WINDOWS OPTIMIZER TOOLKIT")
    print("=" * 70)
    if is_admin():
        print(" Status: Running as Administrator ✅")
    else:
        print(" Status: NOT running as Administrator ⚠️  (some features limited)")
    print("=" * 70)


def main_menu():
    print_banner()
    options = {
        "1": ("Bloatware Remover", debloat.interactive_menu),
        "2": ("Telemetry Disabler", telemetry.interactive_menu),
        "3": ("Temp File Cleaner", cleaner.interactive_menu),
        "4": ("Startup App Manager", startup.interactive_menu),
        "5": ("Service Optimizer", service_optimizer.interactive_menu),
        "0": ("Exit", None),
    }

    while True:
        print("\nSelect a module:")
        for key, (label, _) in options.items():
            print(f"  [{key}] {label}")

        choice = input("\n> ").strip()

        if choice == "0":
            print("Goodbye!")
            sys.exit(0)
        elif choice in options:
            label, func = options[choice]
            print(f"\n--- {label} ---")
            func()
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    if sys.platform != "win32":
        print("❌ This tool only works on Windows.")
        sys.exit(1)
    main_menu()
