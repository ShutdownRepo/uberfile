# Uberfile
  Uberfile is a simple command-line tool aimed to help pentesters quickly generate file downloader one-liners in multiple contexts (wget, curl, powershell, certutil...).
  This project code is based on my other similar project for one-liner reverseshell generation [Shellerator](https://github.com/ShutdownRepo/shellerator).

  This project is installed by default in the pentesting OS [Exegol](https://github.com/ShutdownRepo/Exegol)

  ![Example (with menus)](https://raw.githubusercontent.com/ShutdownRepo/uberfile/master/assets/example-menus.gif)

# Install
  The install is pretty simple, just clone this git and install the requirements.
  ```
  git clone https://github.com/ShutdownRepo/uberfile
  pip3 install --user -r requirements.txt
  ```

# Usage
  Usage is dead simple too.
  ```
  usage: uberfile.py [-h] [-lp LPORT] [-lh LHOST] [-t {windows,linux}] [-d TYPE] [-f INPUTFILE] [-o OUTPUTFILE] [-l]

  Generate a file downloader command

  optional arguments:
    -h, --help            show this help message and exit
    -lp LPORT, --lport LPORT
                          Server port
    -lh LHOST, --lhost LHOST
                          Server address
    -t {windows,linux}, --target-os {windows,linux}
                          Target machine operating system
    -d TYPE, --downloader TYPE
                          Downloader
    -f INPUTFILE, --input-file INPUTFILE
                          File to be downloaded
    -o OUTPUTFILE, --output-file OUTPUTFILE
                          File to write on the target machine
    -l, --list            Print all the commands UberFiles can generate
  ```
  If required options are not set, the tool will start in TUI (Terminal User Interface) with pretty menus but CLI works like a charm too.

  ![Example (without menus)](https://raw.githubusercontent.com/ShutdownRepo/uberfile/master/assets/example-no-menus.gif)

# Sources
  Some commands come from the following links
  - https://www.ired.team/
  - https://medium.com/@PenTest_duck/almost-all-the-ways-to-file-transfer-1bd6bf710d65
