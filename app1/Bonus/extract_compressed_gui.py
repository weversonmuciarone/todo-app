import FreeSimpleGUI as sg
from zip_extractor import extract_archive
import time

sg.theme('BrownBlue')
clock = sg.Text('', key='clock')

label = sg.Text("Select a zip folder to exract files:", size=(30, 1))
Input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="folder")

label2 = sg.Text("Select a destination folder:", size=(30, 1))
Input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="destination")

extract_button = sg.Button("Extract", key="extract", size=(10, 1))
exit_button = sg.Button("Exit", size=(10, 1))

window = sg.Window("File Extractor",
                   layout=[[clock],
                           [label, Input1, choose_button1],
                           [label2, Input2, choose_button2],
                           [extract_button, exit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    
    match event:
        case "extract":
            archivepath = values['folder']
            dest_path = values['destination']
            if archivepath and dest_path:
                extract_archive(archivepath, dest_path)
                sg.popup("Extraction completed!", font=("Helvetica", 20))
            else:
                sg.popup("Please select both source and destination folders.", font=("Helvetica", 20))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
