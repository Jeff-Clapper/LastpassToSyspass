import requests
import json
import csv



def get_account():
    """API call to server to get all account info"""
    url = "https://SERVER/api.php"

    payload = json.dumps({"jsonrpc": "2.0","method": "getAccountSearch","params": {"authToken": ""}, "id":1})
    headers = {
    'Content-Type': 'application/json'
    }

    # response = requests.request("GET", url=url, headers=headers, data=payload)
    response = requests.get(url=url,headers=headers,data=payload,verify=False)

    return response.text

def manipulate_file():
    """Takes in CSV file from LastPass and runs through it seperating Accounts and Notes in a list"""
    lastpass_data = []
    lastpass_nonpass_data = []
    with open('FILE PATH', newline='',encoding='utf-8') as csvfile:
        accounts = csv.reader(csvfile, delimiter = ',')
        account_data = list(accounts)

        for row in account_data:
            try:
                if lastpass_nonpass_data == []:
                    lastpass_nonpass_data.append(row)
                else:
                    if row[1] == "" or row[2] == "":
                        lastpass_nonpass_data.append(row)
                    else:
                        data = {
                            "name": row[5],
                            "url": row[0],
                            "username": row[1],
                            "password": row[2],
                            "notes": row[4]
                        }
                        lastpass_data.append(data)
            except:
                continue

    return [lastpass_data,lastpass_nonpass_data] 

def document_failed(data):
    """Takes in an array of non-account data extracted from LastPass CSV and sends the data to a new csv file
    Non-Account data is data that was in last pass but did not have username AND password
    One example of this was an excel attachment with phonenumbers"""
    
    with open('FILE PATH', 'w') as file:
        csv_writer = csv.writer(file, lineterminator="\n")
        header = data[0]
        file_data = data[1:]

        csv_writer.writerow(header)

        for ind in range(len(file_data)):
            try:
                csv_writer.writerow(file_data[ind])
            except:
                continue

results = manipulate_file()
successful = results[0]
unsuccessful = results[1]

document_failed(unsuccessful)



print(requests.get("https://SERVER/api.php", verify=False))
