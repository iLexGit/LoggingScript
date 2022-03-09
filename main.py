import re
import csv
import os
import json
from csv import reader


str = r'''2 logs from same IP 5.188.210.227 on 18/Feb/2022
[07:58:27] "\x05\x01\x00" 400 158 "-" "-" "-”
[07:58:27] "\x04\x01\x00P\x05\xBC\xD2\xE3\x00" 400 158 "-" "-" "-”
[07:59:30] "GET http://5.188.210.227/echo.php HTTP/1.1" 400 658 "https://www.google.com/" "Mozilla/5.0 (Windows NT 6.1) 
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36" "-" '''

with open('attackDB.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        matches = re.finditer(row[0], str, re.MULTILINE)
        if matches:
            for matchNum, match in enumerate(matches, start=1):
                print("\nMatch {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum,
                                                                                    start=match.start(),
                                                                                    end=match.end(),
                                                                                    match=match.group()))
                print("Attack Name:", row[1])
                print("CVE: ", row[2])
                if row[3] == "2":
                    print("Attack needs investigation")
                    with open('investage.json', 'w') as outfile:
                        outfile.write(str)
                if row[3] == "1":
                    print("Known attack")
                    with open('knownAttack.json', 'w') as outfile:
                        outfile.write(str)
                elif row[3] == "3":
                    print("discarded log")
                    fd = os.open('/dev/null', os.O_WRONLY)
                    os.dup2(fd, 2)
                    break

                for groupNum in range(0, len(match.groups())):
                    groupNum = groupNum + 1
                    print("\nGroup {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
                                                                                    start=match.start(groupNum),
                                                                                    end=match.end(groupNum),
                                                                                    group=match.group(groupNum)))
        else:
            print("Not Found in Attack DB")




