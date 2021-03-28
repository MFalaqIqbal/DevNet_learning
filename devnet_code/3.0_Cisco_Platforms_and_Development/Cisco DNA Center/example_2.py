import json
from dnacentersdk import api
from pprint import pprint

DNAC = api.DNACenterAPI(
    username='devnetuser',
    password='C!3c0d$Y',
    base_url='https://devasc-dnacenter-1.cisco.com'
)


def main():
    list_of_all_devices = DNAC.devices.get_device_list()
    print(f'{"|Device Name":26} {"|Device Type":50} {"|Up Time"}')
    print('-' * 110)
    for value in list_of_all_devices.response:
        print(
            f'|{value["hostname"]:25} |{value["type"]:50} |{value["upTime"]}'
        )
    print('-' * 110)
    client_health = DNAC.clients.get_overall_client_health(timestamp="1566506489000")
    print(f'{"|Client Category":27} {"|Number of Clients":50} {"|Client Score"}')
    print('-' * 110)
    for value in client_health.response:
        for score in value.scoreDetail:
            print(
                f'|{score.scoreCategory.value:26} |{score.clientCount:50} |{score.scoreValue}'
            )
    return


if __name__ == "__main__":
    main()