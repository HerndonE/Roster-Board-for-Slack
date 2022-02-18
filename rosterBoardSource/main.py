#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

@author     : Ethan Herndon
@date       : 08 FEB 2022
@desc       : This program alerts Mighty Oak Medical employees every thursday when
              it is their turn to bring breakfast via Slack
"""

import numpy
import numpy as np
import requests


# Read names.txt and rotate position. When called by Crontab, alert user on Slack.

def nameSwitch():
    nameFileCurrent = open('names.txt', 'r')
    list_names = nameFileCurrent.read().splitlines()
    nameFileCurrent.close()

    with open('names.txt', 'w') as nameFileNew:
        name_array = np.array(list_names)
        nextPerson = name_array[0]
        print('User up on deck: ' + nextPerson)
        # print('Current names from file: ' + str(list_names))
        list_names = numpy.roll(list_names, -1)
        print(list_names[0] + list_names[1] + list_names[2])
        print('Next names from file: ' + str(list_names))

        employeeMemberID = {"Alice": "SLAKCMEMBERID",
                            "Bob": "SLAKCMEMBERID"
                            }

        getMemberID = " "
        for i, j in employeeMemberID.items():
            if i == nextPerson:
                getMemberID = j

        print(nextPerson + "'s member ID: " + getMemberID)

        memberID = str(getMemberID)
        message = '<@' + memberID + '>' + ' you are up for Breakfast tomorrow. Upcoming is: ' \
                  + '\n' + '1. ' + list_names[0]+ '\n' + '2. ' \
                  + list_names[1] + '\n' + '3. ' + list_names[2]


        #print(message)

        payload = '{"text": "%s"}' % message
        response = \
        requests.post('YOURSLACKAPPsWEBHOOK'
                          , data=payload)
        print(response)


        # Output back to file afterwards

        for name in list_names:
            nameFileNew.write(name + '\n')


if __name__ == '__main__':
    nameSwitch()
