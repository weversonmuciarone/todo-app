import FreeSimpleGUI as sg
from zip_creator import make_archive


label1 = sg.Text("Choose a file to compress: ")
input1 = sg.Input()
button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select Destination Folder: ")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green")

layout = [[label1, input1, button1],
          [label2, input2, button2],
          [compress_button, output_label]]

window = sg.Window("File Compressor", layout=[[layout]])

while True:
    events, values = window.read()
    print(events)
    print(values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression Completed!")

window.close()