import requests
import json
import xmltodict
from pprint import pprint
from xml.dom.minidom import parseString, parse
from ucsmsdk.ucshandle import UcsHandle

HANDLE = UcsHandle("10.10.20.110", "ucspe", "ucspe")


def main():
    HANDLE.login()
    BLADES = HANDLE.query_classid("ComputeBlade")
    print('{0:23s}{1:8s}{2:12s}{3:14s}{4:6s}'.format(
        "DN",
        "SERIAL",
        "ADMIN STATE",
        "MODEL",
        "TOTAL MEMORY"))
    print('-' * 70)

    for BLADE in BLADES:
        print('{0:23s}{1:8s}{2:12s}{3:14s}{4:6s}'.format(
            BLADE.dn,
            BLADE.serial,
            BLADE.admin_state,
            BLADE.model,
            BLADE.total_memory))
    HANDLE.logout()

    return


if __name__ == "__main__":
    main()
