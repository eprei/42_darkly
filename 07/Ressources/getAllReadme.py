import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def get_all_readme(base_url, current_url, visited, output_file):
    if current_url in visited:
        return
    
    visited.add(current_url)
    
    try:
        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        if current_url.endswith('README'):
            print(f"Found README at: {current_url}")
            with open(output_file, 'a', encoding='utf-8') as f:
                f.write(response.text)
        else:
            for link in soup.find_all('a'):
                href = link.get('href')
                if href and not href.startswith(('http://', 'https://', '#')):
                    next_url = urljoin(current_url, href)
                    if next_url.startswith(base_url):
                        get_all_readme(base_url, next_url, visited, output_file)
    except Exception as e:
        print(f"Error crawling {current_url}: {e}")

def find_flag(file_path):
    flag_prefix = "Hey, here is your flag :"
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        if flag_prefix in content:
            flag_start = content.index(flag_prefix) + len(flag_prefix)
            flag = content[flag_start:].strip().split()[0]
            return flag
    return None

def main():
    base_url = input("Enter the base URL (e.g., http://example.com/.hidden/): ")
    output_file = 'readme_contents.txt'
    
    if os.path.exists(output_file):
        os.remove(output_file)
    
    visited = set()
    get_all_readme(base_url, base_url, visited, output_file)
    print(f"Crawling complete. README contents saved to {output_file}")
    
    flag = find_flag(output_file)
    if flag:
        print(f"Flag found: {flag}")
    else:
        print("No flag found in the README contents.")

if __name__ == "__main__":
    main()