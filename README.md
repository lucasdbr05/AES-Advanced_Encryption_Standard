# AES - Advanced Encryption Standard

This project implements the AES (Advanced Encryption Standard) algorithm in different modes of operation, as well as a simplified version called S-AES. It also includes functionalities for encryption and decryption in ECB mode using S-AES.

## How to Run

To install the dependencies and run the main program, use the following commands:

```shell
pip install pycryptodome numpy scipy
py main.py
```

## Features

1. **S-AES**:
   - Encryption and decryption using the S-AES algorithm.

2. **ECB Mode with S-AES**:
   - Encryption and decryption of text blocks in ECB mode using S-AES.

3. **AES in Different Modes of Operation**:
   - Implementation of operation modes: ECB, CBC, CFB, OFB, and CTR.
   - Approximate entropy calculation and execution time for each mode.

## Menu Options

- `T`: Change the input source to come from the user or default files.
- `0`: Exit the program.
- `1A`: Encrypt using S-AES.
- `1B`: Decrypt using S-AES.
- `2A`: Encrypt in ECB mode using S-AES.
- `2B`: Decrypt in ECB mode using S-AES.
- `2C`: Identic messages comparison with ECB mode using S-AES.
- `3`: Run AES in different modes of operation.

## Project Structure

- `main.py`: Main file that manages the menu and user interactions.
- `AES.py`: Implementation of AES with support for different modes of operation.
- `S_AES.py`: Implementation of the simplified S-AES algorithm.
- `ECB.py`: Functions for encryption and decryption in ECB mode using S-AES.
- `Logger.py`: Utility class for displaying formatted information in the console.

## Usage Example

### Encryption with S-AES
1. Select option `1A` in the menu.
2. Enter the key in hexadecimal format.
3. Enter the text to be encrypted.

### S-AES in Electronic Code Book Mode (ECB)
1. Select option `2A` in the menu.
2. Enter the key in hexadecimal format.
3. Enter the text to be encrypted.

### AES in Operation Modes
1. Select option `3` in the menu.
2. The program will display the results for each mode of operation, including execution time and entropy.

<h2>💻 Authors</h2>

<table>
  <tr>
    <td align="center"><a href="https://github.com/lucasdbr05" target="_blank"><img style="border-radius: 50%;" src="https://github.com/lucasdbr05.png" width="100px;" alt="Lucas Lima"/><br /><sub><b>Lucas Lima - 231003406</b></sub></a><br /></td>
</table>
