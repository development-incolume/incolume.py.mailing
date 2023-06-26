import re
from pathlib import Path
import logging


def get_email(entrance_file: Path | str,
              regex=r'[\w.+-]+@[\w-]+\.[\w.-]+') -> list:
    """Get email list."""
    result = []
    entrance_file = Path(entrance_file)
    content = entrance_file.read_bytes().decode('utf-8')
    logging.debug(content)
    rule = re.compile(regex, re.I)
    for line in content.split('\n'):
        if '@' in line:
            logging.debug(line)
            result += rule.findall(line)
    logging.debug(result)
    return result


def run():
    for i in get_email('mailing01.txt'):
        print(i)


if __name__ == '__main__':
    run()
