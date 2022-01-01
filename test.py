import requests
import json
import csv

def get_account():
    url = "URL HERE"

    payload = json.dumps({"jsonrpc": "2.0","method": "client/search","params": {"authToken": "CERT HERE"}, "id": 1})
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url=url, headers=headers, data=payload)

    print(response.text)

# def


# def manipulate_file():
#     lastpass_data = []
#     lastpass_nonpass_data = []
#     with open('FILE PATH HERE', newline='',encoding='utf-8') as csvfile:
#         accounts = csv.reader(csvfile, delimiter = ',')
#         account_data = list(accounts)

#         for row in account_data:
#             try:
#                 if lastpass_nonpass_data == []:
#                     lastpass_nonpass_data.append(row)
#                 else:
#                     if row[1] == "" or row[2] == "":
#                         lastpass_nonpass_data.append(row)
#                     else:
#                         data = {
#                             "name": row[5],
#                             "url": row[0],
#                             "username": row[1],
#                             "password": row[2],
#                             "notes": row[4]
#                         }
#                         lastpass_data.append(data)
#             except:
#                 continue

#     return [lastpass_data,lastpass_nonpass_data] 

# def document_failed(data):
#     with open('FILE PATH HERE', 'w') as file:
#         csv_writer = csv.writer(file, lineterminator="\n")
#         header = data[0]
#         file_data = data[1:]

#         csv_writer.writerow(header)

#         for ind in range(len(file_data)):
#             try:
#                 csv_writer.writerow(file_data[ind])
#             except:
#                 continue
# ud
# results = manipulate_fisle()
# successful = results[0]
# unsuccessful = results[1]

# document_failed(unsuccessful)



print(get_account())
