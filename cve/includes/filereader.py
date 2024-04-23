#!/usr/bin/env python

"""
 * crlfi
 * crlfi Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */


"""
from cve.includes import scan


def reader(input, output):
    try:
        with open(input, 'r') as file:
            for line in file:
                scan.cvescan(line.strip(), output)
    except FileNotFoundError:
        print("File not found. Check the file path and name.")
