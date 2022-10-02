#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

@author     : Ethan Herndon
@date       : 10 OCT 2022
@desc       : This program alerts members in a slack channel when it is their turn for 
			  breakfast.
"""

import numpy
import numpy as np
import requests


def printToConsole(msg):
	print(msg)


# Read names.txt and rotate position. When called by Crontab, alert user on Slack.
def nameSwitch():
    nameFileCurrent = open('names.txt', 'r')
    list_names = nameFileCurrent.read().splitlines()
    nameFileCurrent.close()

    with open('names.txt', 'w') as nameFileNew:
        name_array = np.array(list_names)
        nextPerson = name_array[0]
		printToConsole(f"User up on deck: {nextPerson}")
        list_names = numpy.roll(list_names, -1)
        printToConsole(f"{list_names[0]} {list_names[1]} {list_names[2]}")
        printToConsole(f"Next names from file: {list_names}")

        employeeMemberID = {"Alice": "SLAKCMEMBERID",
                            "Bob": "SLAKCMEMBERID"
                            }

        getMemberID = " "
        for i, j in employeeMemberID.items():
            if i == nextPerson:
                getMemberID = j

        printToConsole(f"{nextPerson}'s member ID: {getMemberID}")

        memberID = str(getMemberID)
        message = '<@' + memberID + '>' + ' you are up for Breakfast tomorrow. Upcoming is: ' \
                  + '\n' + '1. ' + list_names[0]+ '\n' + '2. ' \
                  + list_names[1] + '\n' + '3. ' + list_names[2]
		printToConsole(message)
        payload = '{"text": "%s"}' % message
        response = \
        requests.post('YOURSLACKAPPsWEBHOOK'
                          , data=payload)
        printToConsole(response)


        # Output back to file afterwards
        for name in list_names:
            nameFileNew.write(name + '\n')


if __name__ == '__main__':
    nameSwitch()
