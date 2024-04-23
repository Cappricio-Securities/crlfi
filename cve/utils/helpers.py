#!/usr/bin/env python

"""
 * crlfi
 * crlfi Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */


"""
import getpass
username = getpass.getuser()


def display_help():
    help_banner = f"""

👋 Hey \033[96m{username}
   \033[92m                            v1.0
   __________  __    __________
  / ____/ __ \/ /   / ____/  _/
 / /   / /_/ / /   / /_   / /
/ /___/ _, _/ /___/ __/ _/ /
\____/_/ |_/_____/_/   /___/


                              \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1mcrlfi : Bug scanner for WebPentesters and Bugbounty Hunters

\x1b[31;1m$ \033[92mcrlfi\033[0m [option]

Usage: \033[92mcrlfi\033[0m [options]

Options:
  -u, --url     URL to scan                                crlfi -u https://target.com
  -i, --input   <filename> Read input from txt             crlfi -i target.txt
  -o, --output  <filename> Write output in txt file        crlfi -i target.txt -o output.txt
  -c, --chatid  Creating Telegram Notification             crlfi --chatid yourid
  -b, --blog    To Read about crlfi Bug           crlfi -b
  -h, --help    Help Menu
    """
    print(help_banner)


def banner():
    help_banner = f"""
    \033[94m
👋 Hey \033[96m{username}
      \033[92m                            v1.0
   __________  __    __________
  / ____/ __ \/ /   / ____/  _/
 / /   / /_/ / /   / /_   / /
/ /___/ _, _/ /___/ __/ _/ /
\____/_/ |_/_____/_/   /___/


                              \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1mcrlfi : Bug scanner for WebPentesters and Bugbounty Hunters

\033[0m"""
    print(help_banner)
