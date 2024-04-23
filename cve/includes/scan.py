#!/usr/bin/env python

"""
 * crlfi
 * crlfi Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */
 
"""
from cve.includes import bot
from cve.utils import configure
import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib.parse import quote
from cve.includes import writefile
from cve.utils import const
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



def cvescan(url, output):
    try:
        with requests.Session() as session:
            payreq = session.get(const.Data.payloadurl)
            for endpoint in payreq.text.splitlines():
                encode = quote(endpoint)
                if url.endswith('/'):
                    url = url[:-1]
                fullurl = f'{url}/{endpoint}'
                try:
                    response = session.get(
                        fullurl, verify=False, allow_redirects=False,timeout=5)
                    print(f'Checking ===> {fullurl}')
                    crlfhead = response.headers.get('crlfi',None)
                    crlfcook = response.headers.get('Set-Cookie', None)

                    if crlfhead or (crlfcook and "cappriciosec" in crlfcook):
                        outputprint = (
                            f"\n{const.Colors.RED}💸[Vulnerable]{const.Colors.RESET} ======> "
                            f"{const.Colors.BLUE}{url}{const.Colors.RESET} \n"
                            f"{const.Colors.MAGENTA}📸PoC-Url->{const.Colors.BLUE}${const.Colors.RESET} {fullurl}\n\n\n")
                        print(outputprint)
                        if configure.check_id() == "Exist":
                                bot.sendmessage(fullurl)
                        if output is not None:
                                writefile.writedata(
                                    output, str(f'{fullurl}\n'))
                        break
                except requests.exceptions.RequestException as e:
                    print(
                        f'{const.Colors.MAGENTA}Invalid Domain ->{const.Colors.BLUE}${const.Colors.RESET} {fullurl}: {e}')
    except requests.exceptions.RequestException as e:
        print(f"Check Network Connection: {e}")
