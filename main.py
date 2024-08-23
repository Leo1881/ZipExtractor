import FreeSimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("Black")

label_archive = sg.Text("Select archive")
input_archive = sg.InputText(tooltip="Select archive")
button_archive = sg.FilesBrowse("Choose", key="archive")

label_destination = sg.Text("Select destination")
input_destination = sg.InputText(tooltip="Select destination")
button_destination = sg.FolderBrowse("Choose", key="destination")

button_extract = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Archive Extractor", layout=[
                                                [label_archive, input_archive, button_archive],
                                                [label_destination, input_destination, button_destination],
                                                [button_extract, output_label]],
                                                font=["Helvetica", 16])

while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    dest_dir = values["destination"]
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction completed")

window.read()
window.close()