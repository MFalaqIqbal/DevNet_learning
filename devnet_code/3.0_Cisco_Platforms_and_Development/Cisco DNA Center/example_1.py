import requests
import json
from pprint import pprint
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


base_url = "https://devasc-dnacenter-1.cisco.com/dna"
auth_cred = ('devnetuser', 'C!3c0d$Y')
headers = {"Content-Type": "application/json"}
header = {
    "Authorization": "Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE=",
    "Content-Type": "application/json"
}


def get_auth_token(url):
    """Both base64 encoded and auth is supported"""
    url = url + '/system/api/v1/auth/token'
    auth_token = requests.post(url, auth=auth_cred, headers=headers, verify=False)
    return auth_token.json()['Token']


def get_data(uri, token):
    head = {"Content-Type": "application/json", "X-Auth-Token": token}
    response = requests.get(uri, headers=head, verify=False)
    return response.json()


def main():
    token = get_auth_token(base_url)
    list_of_all_devices = get_data(base_url+"/intent/api/v1/network-device", token)
    file_namespace = get_data(base_url+"/intent/api/v1/file/namespace", token)
    client_details = get_data(base_url+"/intent/api/v1/client-health", token)
    pprint(list_of_all_devices['response'])
    print('*' * 50)
    pprint(file_namespace['response'])
    print('*' * 50)
    pprint(client_details['response'])
    return


if __name__ == "__main__":
    main()
