from bonus.convertUsMetric_func_convert import convert
import FreeSimpleGUI as sg

label_feet = sg.Text("Enter feet: ")
input_feet = sg.Input(key="feet")

label_inches = sg.Text("Enter inches: ")
input_inches = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text("", key='output')

window = sg.Window("Convertor", layout=[[label_feet, input_feet],
                                        [label_inches, input_inches],
                                        [convert_button, output_label]])

while True:
    event, values = window.read()
    output = convert(float(values['feet']), float(values['inches']))
    result = f"{output}m"
    window['output'].update(value=result)
    # print(output)
    # print(event, values)

window.close()
