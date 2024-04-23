#!/usr/bin/env python

"""
 * crlfi
 * crlfi Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */


"""
import os
import yaml
from cve.utils import const


def new_chatid(chatid):
    yaml_file_path = os.path.expanduser(
        const.Data.config_path)
    folder_path = os.path.dirname(yaml_file_path)
    os.makedirs(folder_path, exist_ok=True)

    if not os.path.exists(yaml_file_path):
        initial_content = {"config": {"chatid": chatid}}

        with open(yaml_file_path, "w") as file:
            yaml.dump(initial_content, file, default_flow_style=False)

        print(f"Config file created at: {yaml_file_path}")

    else:
        with open(yaml_file_path, "r") as file:
            data = yaml.safe_load(file)

        if "config" in data and "chatid" in data["config"]:
            print(f"chatid is already present: {data['config']['chatid']}")

        else:
            data.setdefault("config", {})
            data["config"]["chatid"] = chatid

            with open(yaml_file_path, "w") as file:
                yaml.dump(data, file, default_flow_style=False)

            print(f"chatid appended to YAML file: {yaml_file_path}")


def check_id():
    yaml_file_path = os.path.expanduser(const.Data.config_path)
    try:
        with open(yaml_file_path, "r") as file:
            data = yaml.safe_load(file)

        if "config" in data and "chatid" in data["config"]:
            return "Exist"

        else:
            return "Null"

    except:
        print()


def get_chatid():
    yaml_file_path = os.path.expanduser(const.Data.config_path)
    try:
        with open(yaml_file_path, "r") as file:
            data = yaml.safe_load(file)

        if "config" in data and "chatid" in data["config"]:
            chatid = data['config']['chatid']
            return chatid

        else:
            return "Null"

    except:
        print()
