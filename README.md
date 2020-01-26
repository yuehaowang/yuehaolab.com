# yuehaolab.com

A python-based simple web server.

Author: Yuehao Wang

## Usage

### Basic

Setup:

```bash
$ pip install -r requirements.txt
```

Start server:

```bash
$ sudo python ./main.py
```

### Optional Arguments

 - -h, --help: Show this help message and exit
 - --logfile LOGFILE: Path to the log file. Default: ''.
 - --port PORT: The port where the server works. Default: 9331.


## Dependencies

### Python

- Python: 3.5.3+
- Test passed on 3.5.3, 3.7.3

### Packages

- aiohttp
- aiohttp_jinja2
- markdown