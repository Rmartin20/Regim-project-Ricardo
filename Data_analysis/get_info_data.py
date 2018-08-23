import Imreg.RegistrationMethods as Reg
import os

GROUP = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
METRIC = "Correlation"
METHOD = 'Displacement'

NEW_DIRECTORY = './Data/Output/' + METRIC + '/' + METHOD
if not os.path.exists(NEW_DIRECTORY):
    os.makedirs(NEW_DIRECTORY)

print("==================================")
for i in GROUP:

    new_output = './Data/Output/' + METRIC + '/' + METHOD + '/' + i
    if not os.path.exists(new_output):
        os.makedirs(new_output)

    FIXED_IMAGE = 'Data/Input/' + i + '/input_1.png'
    MOVING_IMAGE = 'Data/Input/' + i + '/input_2.png'

    my_imreg = Reg.Imreg(FIXED_IMAGE, MOVING_IMAGE)

    # SELECT REGISTRATION METHOD
    result = my_imreg.image_registration_method_displacement()
    result.save(new_output + '/output.png')

    string = my_imreg.info_data
    metric = string.split(" Metric value:" + "\n")
    print(metric[1] + ",")
print("==================================")
