import subprocess

def run_command(command, shell=False):
    result = subprocess.run(command, shell=shell)
    if result.returncode != 0:
        return False
    return True

print("Installing Node.js dependencies...")

subprocess.run(['cd', 'Zero-Tool/nuke-bot'], shell=True)

if not run_command(['npm', 'install']):
    print("Failed to install Node.js dependencies. Pausing...")
    input("Press Enter to continue...")

