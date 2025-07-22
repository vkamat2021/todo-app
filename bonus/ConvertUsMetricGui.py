from bonus.convertUsMetric_func_convert import convert
import FreeSimpleGUI as sg

sg.theme("Black")
label_feet = sg.Text("Enter feet: ")
input_feet = sg.Input(key="feet")

label_inches = sg.Text("Enter inches: ")
input_inches = sg.Input(key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")
output_label = sg.Text("", key='output')

window = sg.Window("Convertor", layout=[[label_feet, input_feet],
                                        [label_inches, input_inches],
                                        [convert_button, exit_button, output_label]])

while True:
    try:
        event, values = window.read()
        match event:
            case "Exit":
                break
            case sg.WIN_CLOSED:
                break

        output = convert(float(values['feet']), float(values['inches']))
        result = f"{output}m"
        window['output'].update(value=result)
        print(output)
        print(event, values)
    except ValueError:
        sg.popup("Enter feet and inches values first.", font=("Helvetica",10))

window.close()
