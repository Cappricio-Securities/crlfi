#!/usr/bin/env python

"""
 * crlfi
 * crlfi Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */


"""
import click
from cve.utils import helpers
from cve.includes import scan
from cve.includes import filereader
from cve.utils import configure
from cve.utils import const
from cve.utils import status
import webbrowser
import os


def helpbanner(ctx, params, value):
    if value:
        helpers.display_help()
        ctx.exit()


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-u', '--url', type=str, help="URL to scan")
@click.option('-i', '--input', type=str, help="lost of input file")
@click.option('-o', '--output', type=str, help="output in text file")
@click.option('-c', '--chatid', type=str, help='Creating Telegram Notification')
@click.option('-b', '--blog', flag_value=True, help='Open Blog to read about Bug')
@click.option('-h', '--help', 'helpbanner', is_flag=True, expose_value=False, is_eager=True, callback=helpbanner, help="help menu")
def main(url, input, output, chatid, blog):
    if url:
        helpers.banner()
        scan.cvescan(url, output)

    if input:
        helpers.banner()
        filereader.reader(input, output)

    if chatid:
        helpers.banner()
        configure.new_chatid(chatid)

    if blog:
        helpers.banner()
        webbrowser.open(const.Data.blog)


if __name__ == "__main__":
    yaml_file_path = os.path.expanduser(const.Data.config_path)
    folder_path = os.path.dirname(yaml_file_path)
    os.makedirs(folder_path, exist_ok=True)
    if status.check_internet_connection():
        main()
    else:
        print("Check Internet Connection")
