import os
import subprocess
import sys
import platform
import shutil

def download_gitleaks():
    system = platform.system().lower()
    
    if system == 'linux':
        url = "https://github.com/gitleaks/gitleaks/releases/download/v8.18.4/gitleaks_8.18.4_linux_arm64.tar.gz"
        download_command = f"curl -LO {url}"
        download_file = "gitleaks_8.18.4_linux_arm64.tar.gz"
    elif system == 'windows':
        url = "https://github.com/gitleaks/gitleaks/releases/download/v8.18.4/gitleaks_8.18.4_windows_x64.zip"
        download_command = f"curl -LO {url}"
        download_file = "gitleaks_8.18.4_windows_x64.zip"
    else:
        raise OSError("Unsupported operating system")
    
    subprocess.run(download_command, shell=True, check=True)
    return download_file

def install_gitleaks():
    system = platform.system().lower()
    
    download_file = download_gitleaks()

    if system == 'linux':
        # Extract the tar.gz file
        extract_command = f"tar -xvf {download_file}"
        subprocess.run(extract_command, shell=True, check=True)
        
        binary_name = "gitleaks"
        extraction_dir = os.path.join(os.path.dirname(download_file), binary_name)
        install_path = os.path.expanduser(f"~/bin/{binary_name}")
        
        # Move the binary to ~/bin
        os.makedirs(os.path.dirname(install_path), exist_ok=True)
        shutil.move(extraction_dir, install_path)
        subprocess.run(["chmod", "+x", install_path])
        print(f"Gitleaks has been installed at {install_path}")

    elif system == 'windows':
        # Extract the ZIP file using PowerShell
        extraction_dir = os.path.join(os.path.dirname(download_file), "gitleaks")
        zip_command = f'powershell -command "Expand-Archive -Force -Path {download_file} -DestinationPath {extraction_dir}"'
        subprocess.run(zip_command, shell=True, check=True)
        
        binary_name = "gitleaks.exe"
        binary_path = os.path.join(extraction_dir, binary_name)
        install_path = os.path.expanduser(f"~/bin/{binary_name}")
        
        # Move the binary to ~/bin
        os.makedirs(os.path.dirname(install_path), exist_ok=True)
        shutil.move(binary_path, install_path)
        print(f"Gitleaks has been installed at {install_path}")
    
    else:
        raise OSError("Unsupported operating system")
    
    return install_path

def add_gitleaks_to_path(install_path):
    system = platform.system().lower()
    
    if system == 'linux':
        bashrc_path = os.path.expanduser("~/.bashrc")
        with open(bashrc_path, "a") as bashrc:
            bashrc.write(f"\nexport PATH=$PATH:{os.path.dirname(install_path)}\n")
        subprocess.run(["source", bashrc_path], shell=True)
        print("Gitleaks path has been added to your ~/.bashrc file.")
    elif system == 'windows':
        subprocess.run(f'setx PATH "%PATH%;{os.path.dirname(install_path)}"', shell=True)
        print("Gitleaks path has been added to your user PATH.")
    else:
        raise OSError("Unsupported operating system")

def main():
    install_path = install_gitleaks()
    add_gitleaks_to_path(install_path)
    print("Gitleaks installation complete.")

if __name__ == "__main__":
    main()
