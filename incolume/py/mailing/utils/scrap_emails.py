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
    seq = False
    result = (
        []
        + get_email('../datas/mailing01.txt')
        + get_email('../datas/mailing02.txt')
        + get_email('../datas/mailing03.txt')
        + get_email('../datas/mailing04.txt')
    )
    result = [email.casefold() for email in result]
    result = sorted(list(set(result)))
    for i, email in enumerate(result, start=1):
        print(f'{i:3} {email}' if seq else email)


if __name__ == '__main__':
    run()
