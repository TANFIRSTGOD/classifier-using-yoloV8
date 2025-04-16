import os
from shutil import move

def join(*args):
    res = ""
    for i in args:
        res = os.path.join(res, i)
    return res

dataset = "C:\\Users\\tanta\\OneDrive\\Desktop\\CodingProjects\\classifier-using-yoloV8\\dataset2"

cloudyF = "C:\\Users\\tanta\\OneDrive\\Desktop\\CodingProjects\\classifier-using-yoloV8\\dataset2\\cloudy"
rainF = "C:\\Users\\tanta\\OneDrive\\Desktop\\CodingProjects\\classifier-using-yoloV8\\dataset2\\rain"
shineF = "C:\\Users\\tanta\\OneDrive\\Desktop\\CodingProjects\\classifier-using-yoloV8\\dataset2\\shine"
sunriseF = "C:\\Users\\tanta\\OneDrive\\Desktop\\CodingProjects\\classifier-using-yoloV8\\dataset2\\sunrise"

if os.path.exists(dataset):
    print(f"The path exists")
else:
    raise Exception("Path does not exist")

images = os.listdir(dataset)

for i in images:
    if os.path.exists(os.path.join(dataset, i)):
        if "cloudy" in i:
            move(join(dataset, i), cloudyF)
        elif "rain" in i:
            move(join(dataset, i), rainF)
        elif "shine" in i:
            move(join(dataset, i), shineF)
        elif "sunrise" in i:
            move(join(dataset, i), sunriseF)