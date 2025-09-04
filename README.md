<h1>🔎 Port Scanner (Python)</h1>

<p>
A simple <b>command-line Port Scanner</b> built in Python, designed for 
<b>educational and ethical security testing</b>. <br>
This tool allows you to check for <b>open TCP ports</b> on a target host within a specified range.
</p>

<hr>

<h2>✨ Features</h2>
<ul>
  <li>🔍 Scan a range of ports on a target IP or hostname</li>
  <li>⚡ Fast and lightweight</li>
  <li>🧠 Written in Python </li>
  <li>⏱️ Customizable timeout per port</li>
  <li>💻 Cross-platform (Windows, macOS, Linux)</li>
</ul>

<hr>

<h2>🛠️ Requirements</h2>
<ul>
  <li>Python <b>3.x</b></li>
  <li>Internet/network access to the target host</li>
</ul>

<hr>

<h2>🚀 Usage</h2>

<p>Clone the repository:</p>
<pre>
git clone https://github.com/buddhi9785/Port-Scanner.git
cd Port-Scanner
</pre>

<p>Run the scanner:</p>
<pre>
python3 port_scanner.py
</pre>

<p>Follow the prompts:</p>
<pre>
Enter target IP or hostname: scanme.nmap.org
Enter starting port: 20
Enter ending port: 100
</pre>

<p>📸 <b>Sample Output</b></p>
<pre>
Scanning scanme.nmap.org from port 20 to 100...
✅ Port 22 is OPEN
✅ Port 80 is OPEN
</pre>

<hr>

<h2>⚠️ Legal Disclaimer</h2>
<p>
This tool is intended strictly for <b>educational purposes and authorized testing only</b>. <br>
❗ Do <b>not</b> use this tool to scan systems or networks you do not own or have explicit permission to test. <br>
Unauthorized scanning may be considered illegal or malicious activity.
</p>

<hr>

<h2>📁 File Structure</h2>
<pre>
port-scanner/
├── port_scanner.py
└── README.md
</pre>

<hr>

<h2>🧠 Future Enhancements</h2>
<ul>
  <li>[ ] Add multithreading for faster scans</li>
  <li>[ ] Add UDP scanning support</li>
  <li>[ ] Add service/version detection (like Nmap)</li>
  <li>[ ] Export results to a file</li>
</ul>

<hr>

<p>⚡ Built with Python | 💻 For ethical hacking & learning</p>
