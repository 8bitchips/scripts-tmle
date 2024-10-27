"""
Author: Shashank Kumar
Date: 2023-10-05
Description: This script reads a file and pastes its content in chunks using clipboard and keyboard automation.
             It uses the pyautogui and pyperclip libraries to automate the process of copying and pasting text.
             The script is useful for scenarios where large amounts of text need to be pasted in smaller chunks
             with a delay between each paste operation.
"""


import pyautogui
import pyperclip
import time

def paste_code_in_chunks(file_path, chunk_size=200, delay=1):
    """
    Reads a file and pastes its content in chunks using clipboard and keyboard automation.

    Args:
        file_path (str): The path to the file to be read and pasted.
        chunk_size (int, optional): The number of lines to be included in each chunk. Default is 200.
        delay (int or float, optional): The delay in seconds between each paste operation. Default is 1 second.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file does not exist.
        Exception: If there is an error during file reading or pasting.

    Example:
        paste_code_in_chunks('/path/to/file.txt', chunk_size=100, delay=2)
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    total_lines = len(lines)
    for i in range(0, total_lines, chunk_size):
        chunk = lines[i:i + chunk_size]
        chunk_text = ''.join(chunk)
        pyperclip.copy(chunk_text)
        time.sleep(delay)  
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(delay)

if __name__ == '__main__':
    file_path = '/path/to/file.txt'  # Replace with your file path
    paste_code_in_chunks(file_path)
