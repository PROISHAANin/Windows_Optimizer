"""
Temp File Cleaner Module
---------------------------
Cleans temporary files, prefetch cache, and Windows temp folders
to free up disk space.
"""

import os
import shutil
import tempfile

CLEAN_TARGETS = {
    "User Temp": tempfile.gettempdir(),
    "Windows Temp": r"C:\Windows\Temp",
    "Prefetch": r"C:\Windows\Prefetch",
}


def get_folder_size(path):
    total = 0
    if not os.path.exists(path):
        return 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                total += os.path.getsize(fp)
            except (OSError, FileNotFoundError):
                pass
    return total


def bytes_to_mb(b):
    return round(b / (1024 * 1024), 2)


def clean_folder(path):
    removed, failed = 0, 0
    if not os.path.exists(path):
        print(f"⚠️  Path not found: {path}")
        return removed, failed

    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        try:
            if os.path.isfile(full_path) or os.path.islink(full_path):
                os.unlink(full_path)
                removed += 1
            elif os.path.isdir(full_path):
                shutil.rmtree(full_path)
                removed += 1
        except (PermissionError, OSError):
            failed += 1  # file in use / access denied — normal, skip
    return removed, failed


def show_sizes():
    print("\n" + "=" * 70)
    print(" TEMP FILE CLEANER — Current Sizes")
    print("=" * 70)
    for idx, (name, path) in enumerate(CLEAN_TARGETS.items(), start=1):
        size_mb = bytes_to_mb(get_folder_size(path))
        print(f"[{idx}] {name:<20} {path:<30} ~{size_mb} MB")
    print("=" * 70)


def interactive_menu():
    show_sizes()
    print("\nEnter numbers to clean (comma-separated), 'all', or 'exit'.")
    choice = input("> ").strip().lower()

    if choice == "exit":
        return

    targets = list(CLEAN_TARGETS.items())
    if choice == "all":
        selected = targets
    else:
        try:
            indices = [int(x.strip()) - 1 for x in choice.split(",")]
            selected = [targets[i] for i in indices if 0 <= i < len(targets)]
        except (ValueError, IndexError):
            print("Invalid input.")
            return

    print("\nCleaning... (files in use will be safely skipped)\n")
    total_removed = 0
    for name, path in selected:
        removed, failed = clean_folder(path)
        total_removed += removed
        print(f"  {name}: {removed} items removed, {failed} skipped (in use)")

    print(f"\n✅ Done. {total_removed} total items removed.")


if __name__ == "__main__":
    interactive_menu()
