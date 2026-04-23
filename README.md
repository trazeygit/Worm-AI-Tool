# Worm-AI-Tool
.  💀 SHΔDØW WORM-AI: Deployment Guide This repository contains the SHΔDØW WORM-AI framework, a specialized tool for network reconnaissance and vulnerability assessment. 

🛠️ Step 1: Binary De-Protection (The macOS Bypass)
macOS "Hardened Runtime" prevents library injection into system binaries. We must create an "unlocked" Python binary to allow proxychains4 to hook the network stack.

Create the Mission Directory:
mkdir shadow_mission && cd shadow_mission
Clone and Unlock the Binary:

# Copy the real Python binary to the local folder
cp $(python3 -c "import sys; print(sys.executable)") ./mission_python

# Strip Apple security attributes and ad-hoc sign the binary
xattr -cr ./mission_python
codesign --force --deep --sign - ./mission_python

⚙️ Step 2: Proxy Configuration
Configure the tunnel gateway. WORM-AI requires a dynamic_chain to handle volatile public proxies.

Edit the Config:
sudo nano /opt/homebrew/etc/proxychains.conf

Enable these settings:
Uncheck dynamic_chain
Comment out strict_chain
Ensure proxy_dns is active.
Add Proxies at the bottom:

Plaintext
[ProxyList]
socks5 157.66.26.151 1080
# Add additional SOCKS5/HTTP proxies here

🧪 Step 3: SSL & Environment Setup
Python 3.14 on macOS requires manual certificate installation to prevent SSLCertVerificationError.
Install Certificates:
/Applications/Python\ 3.14/Install\ Certificates.command

Set the Worm Environment:
python3 -m venv worm_env
source worm_env/bin/activate
pip install requests  # or other requirements

🚀 Step 4: Verification & Deployment
Never launch the main mission without verifying the tunnel.

The Pre-Flight Check:
Run the verification script to ensure no IP leaks occur.

proxychains4 ./mission_python check_tunnel.py

Launch the Mission:
If the check returns STEALTH OPERATIONAL, deploy the main script:
proxychains4 ./mission_python Worm-AI.py

📂 Project Structure
mission_python: The unlocked execution engine (DO NOT GIT COMMIT THIS).
Worm-AI.py: The core automated reconnaissance logic.
check_tunnel.py: The safety kill-switch script.
proxychains.conf: External configuration for network routing.

⚠️ Operational Security (OPSEC) Warning
This framework is for authorized reconnaissance only. All traffic is routed through the proxy chain specified in proxychains.conf. If the terminal displays [proxychains] ... timeout, the script will automatically attempt the next proxy in the chain. If all proxies fail, the mission will abort to prevent IP exposure.
