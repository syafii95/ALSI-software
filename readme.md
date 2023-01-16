# Auto Labeling Software
- Auto labeling software is used to assist the operations team in auto-tagging datasets using the existing training baby model, and it also includes features to sort out classes in the dataset.

#### **Requirement**
- Anaconda
- Visual Studio Code
- Source Code
- cudnn file
- Baby model file

#### **Installation**
- Clone repository or download the source code and extract to your pc.
![App Screenshot](https://dev.azure.com/TGDNA-IOT/da91e559-c955-477a-9c5a-07d367883329/_apis/git/repositories/dc2db265-2e5c-4848-8818-c25ded57e1c3/items?path=/AIVC/Auto%20Labelling/Screenshoot/1.JPG&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0)

- Then install Anaconda and run the Anaconda Navigator.
- Import the requirement.yaml file from your directory and rename the environment name for example "autoLabelEnv" to install the library and wait untill finish.
![App Screenshot](https://dev.azure.com/TGDNA-IOT/da91e559-c955-477a-9c5a-07d367883329/_apis/git/repositories/dc2db265-2e5c-4848-8818-c25ded57e1c3/items?path=/AIVC/Auto%20Labelling/Screenshoot/2.JPG&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0)

- After that, install Visual Studio Code until done and open the source code.
![App Screenshot](https://dev.azure.com/TGDNA-IOT/da91e559-c955-477a-9c5a-07d367883329/_apis/git/repositories/dc2db265-2e5c-4848-8818-c25ded57e1c3/items?path=/AIVC/Auto%20Labelling/Screenshoot/3.JPG&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0)


#### **Running the code**
- Click on AIVCtools.py then click on python version, new interpreter selector will popup. Select "autoLabelEnv" that you create just now to activate the environment.
![App Screenshot](https://dev.azure.com/TGDNA-IOT/da91e559-c955-477a-9c5a-07d367883329/_apis/git/repositories/dc2db265-2e5c-4848-8818-c25ded57e1c3/items?path=/AIVC/Auto%20Labelling/Screenshoot/4.PNG&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0)

- Select Command Prompt as running terminal.
![App Screenshot](https://dev.azure.com/TGDNA-IOT/da91e559-c955-477a-9c5a-07d367883329/_apis/git/repositories/dc2db265-2e5c-4848-8818-c25ded57e1c3/items?path=/AIVC/Auto%20Labelling/Screenshoot/5.JPG&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0)
![App Screenshot](https://dev.azure.com/TGDNA-IOT/da91e559-c955-477a-9c5a-07d367883329/_apis/git/repositories/dc2db265-2e5c-4848-8818-c25ded57e1c3/items?path=/AIVC/Auto%20Labelling/Screenshoot/6.JPG&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0)

- Download cudnn file from this [link](https://drive.google.com/file/d/1x5d5nMdUmCcnvAMlwT-M4ZEIhXwWBzz3/view?usp=share_link) and then extract into the auto labelling folder. 
- Make sure all file already inside this folder as well as baby model file. For yolov3.weight(baby model file), get the model from Meen.
![App Screenshot](https://dev.azure.com/TGDNA-IOT/da91e559-c955-477a-9c5a-07d367883329/_apis/git/repositories/dc2db265-2e5c-4848-8818-c25ded57e1c3/items?path=/AIVC/Auto%20Labelling/Screenshoot/7.JPG&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0)

- Run the source code.
![App Screenshot](https://dev.azure.com/TGDNA-IOT/da91e559-c955-477a-9c5a-07d367883329/_apis/git/repositories/dc2db265-2e5c-4848-8818-c25ded57e1c3/items?path=/AIVC/Auto%20Labelling/Screenshoot/8.JPG&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0)
