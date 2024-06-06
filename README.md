# Keylogger with GUI

This repository contains a keylogger tool with a graphical user interface (GUI) as part of my Cyber Security Internship. The tool records and logs keystrokes to a file and displays them in real-time on the GUI.

## Contents

- `keylogger_gui.py`: A Python script that logs keystrokes to a file and displays them in a GUI.
- `README.md`: Documentation and details about the project.

## How to Use

1. **Run the Python Script**:
   - Execute the `keylogger_gui.py` script to launch the GUI application:
     ```bash
     python keylogger_gui.py
     ```

2. **Interact with the GUI**:
   - Click the "Start Keylogger" button to begin logging keystrokes.
   - The logged keystrokes will appear in the scrollable text area in real-time.
   - Click the "Stop Keylogger" button to stop logging keystrokes.

3. **Stop the Keylogger**:
   - The keylogger can also be stopped by pressing the `Esc` key.

4. **Check the Log File**:
   - The keystrokes will be logged to a file named `keylog.txt` in the same directory as the script.

## Ethical Considerations

- **Permissions**:
  - Always get explicit permission from the owner of the device before installing or running a keylogger.
  - Explain the purpose and functionality of the keylogger to the user.

- **Usage**:
  - Use keyloggers only for legitimate and ethical purposes, such as personal experiments on your own devices or for educational purposes in a controlled environment.

## Learning Outcomes

- Implemented a keylogger in Python with an enhanced GUI.
- Practiced using the `pynput` library to capture keyboard input.
- Emphasized ethical considerations in the development and use of keyloggers.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
