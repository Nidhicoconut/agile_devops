import pyautogui
import time
import subprocess
import sys

def automate_calculator_test():
    """
    Simple RPA script to automate running calculator tests and capture results
    """
    print("Starting automated test process...")
    
    # Open terminal (for macOS)
    if sys.platform == 'win32':
        subprocess.Popen(['cmd.exe'])
    elif sys.platform == 'darwin':  # macOS
        subprocess.Popen(['open', '-a', 'Terminal'])
    else:  # Linux
        subprocess.Popen(['gnome-terminal'])
    
    # Wait for terminal to open
    time.sleep(2)
    
    # Type commands to run tests
    pyautogui.write('cd ' + sys.path[0] + '/..')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('python -m unittest discover tests')
    pyautogui.press('enter')
    time.sleep(3)
    
    # Take screenshot of test results
    screenshot = pyautogui.screenshot()
    screenshot.save('test_results.png')
    print("Test automation completed. Results saved to test_results.png")


if __name__ == "__main__":
    # Wait 3 seconds before starting to give user time to prepare
    print("RPA will start in 3 seconds...")
    time.sleep(3)
    automate_calculator_test()
