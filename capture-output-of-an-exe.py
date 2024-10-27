"""
Title: Capture Output of an Executable
Author: Shashank Kumar

This script runs a specified executable with given input parameters and captures its output.
"""

import subprocess

def capture_exe_output(exe_path, input_params):
    """
    Runs the specified executable with given input parameters and captures its output.

    :param exe_path: Path to the executable
    :param input_params: List of input parameters for the executable
    :return: A tuple containing the standard output and error
    """
    try:
        result = subprocess.run([exe_path] + input_params, capture_output=True, text=True)
        output = result.stdout
        error = result.stderr

        if result.returncode == 0:
            return output, None
        else:
            return None, error

    except Exception as e:
        return None, str(e)


if __name__ == "__main__":
    exe_path = 'your.exe'  # Adjust the path if necessary
    input_params = [    # Add input parameters as needed
        'param1',
        'param2',
        'param3'
    ]

    output, error = capture_exe_output(exe_path, input_params)

    if output:
        print("Output:", output)
    else:
        print("Error:", error)
