# Install Modules Script

This Python script provides a simple way to install Python modules using pip.

## Usage

1. Clone or download this repository.
2. Navigate to the directory containing the script.
3. Run the script with the Python interpreter, providing the names of the modules you want to install as arguments:

   ```bash
   python install_modules.py requests numpy
  ```

Replace requests and numpy with the names of the modules you want to install.

## Notes
- Make sure your Python environment has access to pip.
- The script uses `subprocess` to call the `pip install` command for each module.
- If any installation errors occur, they will be displayed in the console.

Feel free to customize the script or integrate it into your project as needed.
