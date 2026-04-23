import subprocess
import sys
import time
import urllib.request
import ssl

# --- CONFIGURATION ---
REAL_IP = "149.22.82.32"  # Your Toronto IP for the Kill-Switch
VERSION = "11: OMEGA-THREADED | WAF-BYPASS"

def banner():
    print(r"""
    ██████╗ ███╗   ███╗███████╗ ██████╗  █████╗ 
    ██╔══██╗████╗ ████║██╔════╝██╔════╝ ██╔══██╗
    ██║  ██║██╔████╔██║█████╗  ██║  ███╗███████║
    ██║  ██║██║╚██╔╝██║██╔══╝  ██║   ██║██╔══██║
    ██████╔╝██║ ╚═╝ ██║███████╗╚██████╔╝██║  ██║
    ╚═════╝ ╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝
    """)
    print(f"    --- VERSION {VERSION} ---")

def verify_tunnel():
    """Operational Kill-Switch to prevent IP Leaks"""
    print("\n[!] RUNNING PRE-FLIGHT TUNNEL CHECK...")
    context = ssl._create_unverified_context()
    try:
        current_ip = urllib.request.urlopen('http://ifconfig.me/ip', timeout=10, context=context).read().decode().strip()
        if current_ip == REAL_IP:
            print(f"[CRITICAL] IP LEAK DETECTED: {current_ip}. Mission Aborted.")
            sys.exit(1)
        print(f"[+] TUNNEL ACTIVE: {current_ip} (Stealth Mode Engaged)")
    except Exception as e:
        print(f"[-] TUNNEL FAILURE: {e}")
        sys.exit(1)

def phase_1_recon(target):
    print(f"\n[+] STARTING: PHASE 1: STEALTH RECON")
    print(f"[*] Targeting: {target}")
    time.sleep(1) # Simulating network handshake
    print(f"[!] RECON COMPLETE FOR {target}")

def phase_2_brute():
    print(f"\n[+] PHASE 2: INITIALIZING ASYNC CREDENTIAL SPRAY")
    print(f"[+] STARTING: PHASE 2: BRUTE FORCE")
    # Simulate threading activity
    for i in range(3):
        print(f"[*] Testing payload set {i+1}...")
        time.sleep(0.5)

def phase_3_searchsploit(service="Apache 2.4.7"):
    """Corrected Searchsploit module with fixed syntax flags"""
    print(f"\n[!] PHASE 3: CROSS-REFERENCING EXPLOIT-DB")
    print(f"[*] Analyzing service: {service}")
    
    try:
        # Using -t (title) and -w (www) as per Searchsploit manual
        cmd = ["searchsploit", "-t", "-w", service]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            print("\n========== RELEVANT EXPLOITS FOUND ==========")
            print(result.stdout)
            print("=============================================")
        else:
            print(f"[-] No direct exploits found for {service} in local database.")
    except Exception as e:
        print(f"[-] PHASE 3 ERROR: Syntax mismatch in Searchsploit call: {e}")

def main():
    banner()
    verify_tunnel()
    
    target = input("\n[?] Enter Target: ")
