import subprocess
import sys

def install_modules(*modules):
     """
     Installs the passed modules using pip.

     Options:
     *modules (str): Names of the modules to be installed.
     """
     try:
         for module in modules:
             subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
             print(f'Successfully installed {module}.')
     except subprocess.CalledProcessError as e:
         print(f'Error installing modules: {e}')

if __name__ == "__main__":
     # Usage example: python install_modules.py requests numpy
     if len(sys.argv) < 2:
         print("Usage: python install_modules.py module1 module2 ...")
         sys.exit(1)

     modules_to_install = sys.argv[1:]
     install_modules(*modules_to_install)
