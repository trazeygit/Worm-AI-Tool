import urllib.request
import ssl
import sys

def check_tunnel():
    # CONFIGURATION
    REAL_IP = "0.0.0.0"  # Replace with your vpn ip
    CHECK_URL = "http://ifconfig.me/ip"
    TIMEOUT = 10
    
    print("\n--- SHΔDØW WORM-AI💀🔥 TUNNEL VERIFICATION ---")
    
    # Bypass macOS Python SSL limitations
    context = ssl._create_unverified_context()
    
    try:
        # Attempt to fetch IP through the proxy chain
        response = urllib.request.urlopen(CHECK_URL, timeout=TIMEOUT, context=context)
        current_ip = response.read().decode('utf-8').strip()
        
        if current_ip == REAL_IP:
            print(f"[!] ALERT: REAL IP DETECTED ({current_ip})")
            print("[CRITICAL FAILURE] TRAFFIC IS LEAKING. STOP MISSION.")
            sys.exit(1)
        else:
            print(f"[+] PROXY ACTIVE: {current_ip}")
            print(f"[+] STATUS: STEALH OPERATIONAL. YOU ARE CLEARED FOR DEPLOYMENT.")
            
    except Exception as e:
        print(f"[-] ERROR: Proxy chain is unresponsive or refused connection.")
        print(f"[-] DETAILS: {e}")
        print("[!] ACTION: Update your proxy list in /opt/homebrew/etc/proxychains.conf")
        sys.exit(1)

if __name__ == "__main__":
    check_tunnel()
