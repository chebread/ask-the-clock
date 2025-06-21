import argparse
from datetime import datetime
import sys
from colorama import init as colorama_init
from colorama import Fore, Style

def main():
    colorama_init()
    program_name = 'Ask The Clock'
    program_version = 1.0
    help_msg='Make decisions by entering one or more questions, or running this program empty for an instant choice.'
    parser = argparse.ArgumentParser(prog=program_name, description='Ask The Clock is a program that helps you make decisions.', add_help=False)
    parser.add_argument('question_arg', nargs='*', type=str, default='', help='your question') # 해당 값은 사용안 함
    parser.add_argument('-V', '--version', action='version', version=f'%(prog)s {program_version}')
    parser.add_argument('-h', '--help', action='store_true')
    args = parser.parse_args()
    if args.help:
        print(help_msg)
        sys.exit(0)
    now = datetime.now()
    x = int(str(now.microsecond)[-1])
    if x > 5:
        print(f"{Style.BRIGHT}{Fore.CYAN}Yes{Style.RESET_ALL}")
    else:
        print(f"{Style.BRIGHT}{Fore.RED}No{Style.RESET_ALL}")

if __name__ == '__main__':
    main()