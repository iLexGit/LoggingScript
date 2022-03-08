import re

regex = r"x[a-fA-F0-9]{2}(?<!\x22)"

str = r'''
"H\x00\x00\x00tj\xA8\x9E#D\x98+\xCA\xF0\xA7\xBBl\xC5\x19\xD7\x8D\xB6\x18\xEDJ\x1En\xC1\xF9xu[
l\xF0E\x1D-j\xEC\xD4xL\xC9r\xC9\x15\x10u\xE0%\x86Rtg\x05fv\x86]%\xCC\x80\x0C\xE8\xCF\xAE\x00\xB5\xC0f\xC8\x8DD\xC5
 '''
matches = re.finditer(regex, str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                        end=match.end(groupNum),
                                                                        group=match.group(groupNum)))