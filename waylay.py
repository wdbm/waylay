#!/usr/bin/env python3

'''
################################################################################
#                                                                              #
# waylay                                                                       #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program displays variables like a timestamp and a UUID4 for copy.       #
#                                                                              #
# copyright (C) 2025 Will Breaden Madden, wbm@protonmail.ch                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses>.                                               #
#                                                                              #
################################################################################
'''

import datetime
import tkinter as tk
import uuid

__version__ = "2025-07-28T0006Z"

def generate_UUID4T8():
    '''
    Generate an eight-character UUID4-based hex string which is required
    to contain at least one letter A–F.
    '''
    while True:
        code = uuid.uuid4().hex[:8]
        if any(char.isalpha() for char in code):
            return code

def main():
    root = tk.Tk()
    root.title("Waylay")
    root.resizable(False, False)

    timestamp_variable = tk.StringVar()
    UUID4T8_variable = tk.StringVar()

    timestamp_label = tk.Label(root, textvariable=timestamp_variable)
    UUID4T8_label = tk.Label(root, textvariable=UUID4T8_variable)
    timestamp_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    UUID4T8_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')

    def update_timestamp():
        '''
        Update the timestamp value once per second.
        '''
        current = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H%MZ")
        timestamp_variable.set(f"Timestamp: {current}")
        # Schedule next update in 1000 ms.
        root.after(1000, update_timestamp)

    def copy_timestamp():
        '''
        Copy the current timestamp to the clipboard.
        '''
        root.clipboard_clear()
        root.clipboard_append(timestamp_variable.get().split(': ', 1)[1])

    def copy_UUID4T8():
        '''
        Copy the current UUID4T8 code to the clipboard.
        '''
        root.clipboard_clear()
        root.clipboard_append(UUID4T8_variable.get().split(': ', 1)[1])

    def refresh_values():
        '''
        Regenerate UUID4T8 and refresh timestamp immediately.
        '''
        UUID4T8_variable.set(f"UUID4T8: {generate_UUID4T8()}")
        update_timestamp()

    button_width = 10
    copy_timestamp_button = tk.Button(
        root,
        text="Copy",
        width=button_width,
        command=copy_timestamp
    )
    copy_UUID4T8_button = tk.Button(
        root,
        text="Copy",
        width=button_width,
        command=copy_UUID4T8
    )
    copy_timestamp_button.grid(row=0, column=1, padx=5, sticky='w')
    copy_UUID4T8_button.grid(row=1, column=1, padx=5, sticky='w')

    refresh_button = tk.Button(root, text="Refresh", command=refresh_values)
    refresh_button.grid(row=2, column=0, columnspan=2, pady=8, sticky='w')

    UUID4T8_variable.set(f"UUID4T8: {generate_UUID4T8()}")
    update_timestamp()

    root.mainloop()

if __name__ == '__main__':
    main()
