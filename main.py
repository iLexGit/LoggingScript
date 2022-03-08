import re
import csv
from csv import reader


str = r'''185.254.196.223 - - [08/Mar/2022:11:09:51 +0000] "GET /.env HTTP/1.1" 301 169 "-" "Mozilla/5.0 (X11; Linux 
x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36" "-" '''

with open('attackDB.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        matches = re.finditer(row[0], str, re.MULTILINE)
        if matches:
            for matchNum, match in enumerate(matches, start=1):
                print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum,
                                                                                    start=match.start(),
                                                                                    end=match.end(),
                                                                                    match=match.group()))
                print("Attack Name:", row[1])
                print("CVE: ", row[2])
                if row[3] == "2":
                    print("\nAttack needs investigation")
                if row[3] == "1":
                    print("\nKnown attack")
                elif row[3] == "3":
                    print("\ndiscarded log")
                    break

                for groupNum in range(0, len(match.groups())):
                    groupNum = groupNum + 1
                    print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
                                                                                    start=match.start(groupNum),
                                                                                    end=match.end(groupNum),
                                                                                    group=match.group(groupNum)))


        else:
            print("Not Found in Attack DB")




