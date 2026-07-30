# Windows_Optimizer
A modular Python CLI tool to debloat, clean, and optimize Windows — remove bloatware, disable telemetry, manage startup apps, and tune background services.
# 🛠️ Windows Optimizer Toolkit

A modular, Python-based Windows debloating and optimization tool. Remove bloatware, disable telemetry, clean temp files, manage startup apps, and optimize background services — all from a simple CLI menu.

## ⚠️ Important Warnings

- **Run as Administrator** for full functionality (registry edits, service changes).
- **Create a System Restore Point before running any module.** Some changes (registry edits, service modifications) affect system behavior.
- This tool modifies your system. Use at your own risk. Always review what a module does before confirming changes.
- Tested on Windows 10/11.

## Features

| Module | What it does |
|---|---|
| 🗑️ Bloatware Remover | Uninstalls common pre-installed apps (Xbox, 3D Builder, etc.) |
| 📡 Telemetry Disabler | Disables data collection and tracking via registry |
| 🧹 Temp File Cleaner | Clears temp files, Windows temp, and prefetch cache |
| 🚀 Startup App Manager | Lists and disables apps launching at startup |
| ⚙️ Service Optimizer | Sets non-essential background services to manual start |

## Installation

\`\`\`bash
git clone https://github.com/PROISHAANin/Windows_Optimizer.git
cd windows-optimizer
\`\`\`

No external dependencies needed — pure Python standard library.

## Usage

Open **PowerShell or Command Prompt as Administrator**, then:

\`\`\`bash
python main.py
\`\`\`

Follow the on-screen menu to choose a module. Each module asks for confirmation before making any changes.

## Project Structure

\`\`\`
windows-optimizer/
├── main.py
├── modules/
│   ├── __init__.py
│   ├── debloat.py
│   ├── telemetry.py
│   ├── cleaner.py
│   ├── startup.py
│   └── service_optimizer.py
├── README.md
└── requirements.txt
\`\`\`

## Safety Design

- All destructive actions require explicit confirmation.
- Service optimizer uses "manual" start type, not full disable — reversible.
- Protected core services (RPC, DNS, Power, etc.) cannot be modified.
- No automatic/silent changes — everything is opt-in.

## Roadmap

- [ ] GUI version (Tkinter)
- [ ] "Restore defaults" function to undo changes
- [ ] Visual effects / performance mode tweaker
- [ ] Export/import optimization profiles

## Disclaimer

This tool is provided as-is for educational purposes. The author is not responsible for any system issues resulting from its use. Always back up your system before making changes.

## License

MIT License
