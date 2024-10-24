import requests
import dns.resolver

# Default wordlists
default_dir_wordlist = ["admin", "login", "dashboard", "uploads"]
default_subdomain_wordlist = ["www", "mail", "ftp", "dev"]

def directory_enum(base_url, wordlist):
    """Perform directory enumeration."""
    results = []
    for dir in wordlist:
        url = f"{base_url}/{dir}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                results.append(f"[+] Found directory: {url}")
            else:
                results.append(f"[-] {url} not found.")
        except requests.exceptions.RequestException as e:
            results.append(f"[!] Error checking {url}: {str(e)}")
    return results

def subdomain_enum(domain, subdomain_list):
    """Perform subdomain enumeration."""
    results = []
    for subdomain in subdomain_list:
        sub = f"{subdomain}.{domain}"
        try:
            dns.resolver.resolve(sub)
            results.append(f"[+] Found subdomain: {sub}")
        except dns.resolver.NoAnswer:
            results.append(f"[-] Subdomain {sub} does not exist.")
        except Exception as e:
            results.append(f"[!] Error resolving {sub}: {str(e)}")
    return results

def cookie_tamper(url):
    """Test cookie tampering."""
    session = requests.Session()
    try:
        response = session.get(url)
        cookies = session.cookies.get_dict()
        results = [f"Initial Cookies: {cookies}"]
        
        for cookie_name in cookies:
            modified_cookie = {cookie_name: "tampered_value"}
            response = session.get(url, cookies=modified_cookie)
            results.append(f"Tampered {cookie_name}: Response {response.status_code}")
        return results
    except requests.exceptions.RequestException as e:
        return [f"[!] Error during cookie tampering: {str(e)}"]

def generate_report(directory_results, subdomain_results, cookie_results):
    """Generate a report from the results."""
    with open("pentest_report.txt", "w") as report:
        report.write("Site Scanner Analyzer - Pentest Report\n")
        report.write("===================================\n\n")
        
        report.write("Directory Enumeration Results:\n")
        report.write("\n".join(directory_results) + "\n\n")
        
        report.write("Subdomain Enumeration Results:\n")
        report.write("\n".join(subdomain_results) + "\n\n")
        
        report.write("Cookie Tampering Results:\n")
        report.write("\n".join(cookie_results) + "\n")
    
    print("Report saved as pentest_report.txt")

if __name__ == "__main__":
    # Decorative Welcome Message
    print("\n" + "\033[1;32m" + "*" * 43 + "\033[0m")
    print("\033[1;32m" + "*          Welcome to Site Scanner       *" + "\033[0m")
    print("\033[1;32m" + "*   A Website Security Analysis Tool v1.0 *" + "\033[0m")
    print("\033[1;32m" + "*          Developed by Deepanshu Deep   *" + "\033[0m")
    print("\033[1;32m" + "*" * 43 + "\033[0m" + "\n")

    print("\033[1;34m" + "This tool helps you scan websites for common security vulnerabilities." + "\033[0m")
    print("\033[1;34m" + "Version: 1.0" + "\033[0m")
    print("\033[1;31m" + "Use this tool responsibly and ensure you have permission to scan any website." + "\033[0m" + "\n")

    # Take user inputs
    base_url = input("Enter the target website URL (e.g., https://example.com): ").strip()

    # Directory enumeration wordlist
    use_custom_dir_wordlist = input("Do you want to use a custom directory wordlist? (y/n): ").lower()
    if use_custom_dir_wordlist == 'y':
        dir_wordlist_path = input("Enter the path to the directory wordlist file: ").strip()
        try:
            with open(dir_wordlist_path, 'r') as f:
                dir_wordlist = [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"[!] Error reading wordlist file: {str(e)}")
            dir_wordlist = default_dir_wordlist
            print(f"Using default directory wordlist: {dir_wordlist}")
    else:
        dir_wordlist = default_dir_wordlist
        print(f"Using default directory wordlist: {dir_wordlist}")
    
    # Subdomain enumeration wordlist
    use_custom_subdomain_wordlist = input("Do you want to use a custom subdomain wordlist? (y/n): ").lower()
    if use_custom_subdomain_wordlist == 'y':
        subdomain_wordlist_path = input("Enter the path to the subdomain wordlist file: ").strip()
        try:
            with open(subdomain_wordlist_path, 'r') as f:
                subdomain_wordlist = [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"[!] Error reading wordlist file: {str(e)}")
            subdomain_wordlist = default_subdomain_wordlist
            print(f"Using default subdomain wordlist: {subdomain_wordlist}")
    else:
        subdomain_wordlist = default_subdomain_wordlist
        print(f"Using default subdomain wordlist: {subdomain_wordlist}")
    
    # Perform tests
    print("\nStarting Directory Enumeration...")
    dir_results = directory_enum(base_url, dir_wordlist)
    
    print("\nStarting Subdomain Enumeration...")
    subdomain_results = subdomain_enum(base_url, subdomain_wordlist)
    
    print("\nStarting Cookie Tampering...")
    cookie_results = cookie_tamper(base_url)

    # Generate the report
    generate_report(dir_results, subdomain_results, cookie_results)
    print("Pentest report generated.")
print("Please check the report for more details.")