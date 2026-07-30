"""
Bloatware Remover Module
--------------------------
Removes common pre-installed Windows apps (bloatware) using PowerShell.
"""

import subprocess

# Common bloatware apps — safe to remove for most users
BLOAT_APPS = {
    "Microsoft.3DBuilder": "3D Builder",
    "Microsoft.BingWeather": "Weather App",
    "Microsoft.GetHelp": "Get Help",
    "Microsoft.Getstarted": "Tips",
    "Microsoft.MicrosoftOfficeHub": "Office Hub (promo tiles)",
    "Microsoft.MicrosoftSolitaireCollection": "Solitaire Collection",
    "Microsoft.MixedReality.Portal": "Mixed Reality Portal",
    "Microsoft.Office.OneNote": "OneNote (UWP version)",
    "Microsoft.People": "People App",
    "Microsoft.SkypeApp": "Skype (UWP version)",
    "Microsoft.Wallet": "Microsoft Wallet",
    "Microsoft.WindowsFeedbackHub": "Feedback Hub",
    "Microsoft.WindowsMaps": "Maps App",
    "Microsoft.Xbox.TCUI": "Xbox TCUI",
    "Microsoft.XboxApp": "Xbox App",
    "Microsoft.XboxGameOverlay": "Xbox Game Overlay",
    "Microsoft.XboxGamingOverlay": "Xbox Gaming Overlay",
    "Microsoft.XboxIdentityProvider": "Xbox Identity Provider",
    "Microsoft.XboxSpeechToTextOverlay": "Xbox Speech To Text",
    "Microsoft.YourPhone": "Phone Link",
    "Microsoft.ZuneMusic": "Groove Music",
    "Microsoft.ZuneVideo": "Movies & TV",
}


def run_ps(cmd):
    result = subprocess.run(["powershell", "-Command", cmd],
                             capture_output=True, text=True)
    return result.returncode == 0, result.stdout.strip() or result.stderr.strip()


def list_bloat_apps():
    print("\n" + "=" * 70)
    print(" BLOATWARE REMOVER — Available Apps")
    print("=" * 70)
    for idx, (pkg, name) in enumerate(BLOAT_APPS.items(), start=1):
        print(f"[{idx:2}] {name:<30} ({pkg})")
    print("=" * 70)


def remove_app(package_name):
    cmd = f"Get-AppxPackage *{package_name}* | Remove-AppxPackage"
    success, output = run_ps(cmd)
    if success:
        print(f"✅ Removed: {package_name}")
    else:
        print(f"⚠️  Could not remove {package_name}: {output}")
    return success


def interactive_menu():
    print("\n⚠️  WARNING: This will uninstall selected apps for the current user.")
    confirm = input("Continue? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Aborted.")
        return

    list_bloat_apps()
    print("\nEnter numbers to remove (comma-separated), 'all', or 'exit'.")
    choice = input("> ").strip().lower()

    if choice == "exit":
        return

    apps = list(BLOAT_APPS.keys())
    if choice == "all":
        selected = apps
    else:
        try:
            indices = [int(x.strip()) - 1 for x in choice.split(",")]
            selected = [apps[i] for i in indices if 0 <= i < len(apps)]
        except (ValueError, IndexError):
            print("Invalid input.")
            return

    for app in selected:
        remove_app(app)

    print("\n✅ Done.")


if __name__ == "__main__":
    interactive_menu()
