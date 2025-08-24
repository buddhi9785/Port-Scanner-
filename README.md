# Port-Scanner-
A simple command-line Port Scanner built in Python, designed for educational and ethical security testing. This tool allows you to check for open TCP ports on a target host within a specified range.


Features
🔎 Scans a range of ports on a target IP or hostname
⚡ Fast and lightweight
🧠 Written in pure Python (no third-party libraries)
⏱️ Customizable timeout per port
💻 Works on Windows, Mac, and Linux

🛠️ Requirements
Python 3.x
Internet/network access to the target host


🚀 Usage
1. Clone the repository:
git clone https://github.com/buddhi9785/Port-Scanner-
cd port-scanner
2. Run the scanner:
python3 port_scanner.py
3. Follow the prompts:
Enter target IP or hostname: scanme.nmap.org
Enter starting port: 20
Enter ending port: 100
📸 Sample Output
Scanning scanme.nmap.org from port 20 to 100...

✅ Port 22 is OPEN
✅ Port 80 is OPEN

⚠️ Legal Disclaimer
This tool is intended strictly for educational purposes and authorized testing only.
❗ Do not use this tool to scan systems or networks that you do not own or do not have explicit permission to test. Unauthorized scanning may be considered illegal or malicious activity.

📁 File Structure
port-scanner/
├── port_scanner.py
└── README.md

🧠 To-Do / Future Enhancements
Add multithreading for faster scans
Add UDP scanning support
Add service/version detection (like Nmap)
Export results to a file
