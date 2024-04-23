#!/usr/bin/env python

"""
 * crlfi
 * crlfi Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */
"""
import requests
from cve.utils import const
from cve.utils import configure


def sendmessage(vul):

    data = {"Tname": "crlfi", "chatid": configure.get_chatid(), "data": vul,
            "Blog": const.Data.blog, "bugname": const.Data.bugname, "Priority": "Low"}

    headers = {
        "Content-Type": "application/json",
    }
    try:
        response = requests.put(const.Data.api, json=data, headers=headers)
    except:
        print("Bot Error")
