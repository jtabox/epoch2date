# -*- coding: utf-8 -*-

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
import datetime
import re
import pyperclip

class HelloWorld(FlowLauncher):

    def query(self, query):
        # Depending on what the query is, return different results:
        if query == '':
            title = "..."
        elif query.isdigit():
            # It's a unix epoch timestamp, return the date
            title = datetime.datetime.fromtimestamp(int(query)).strftime('%Y-%m-%d %H:%M:%S')
        elif re.match(r'^\d{4}-\d{2}-\d{2}$', query):
            # It's a date, return the unix epoch timestamp for 00:00:00 of that day
            title = str(int(datetime.datetime.strptime(query, '%Y-%m-%d').timestamp()))
        elif re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', query):
            # It's a date with time, return the unix epoch timestamp
            title = str(int(datetime.datetime.strptime(query, '%Y-%m-%d %H:%M:%S').timestamp()))
        else:
            title = "..."
        return [
            {
                "Title": title,
                "SubTitle": "Enter a timestamp or a date (YYYY-MM-DD [HH:MM:SS])",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "copy_to_clipboard",
                    "parameters": [title]
                }
            }
        ]

    def copy_to_clipboard(self, text):
        pyperclip.copy(text)

if __name__ == "__main__":
    HelloWorld()
