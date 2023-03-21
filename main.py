from PIL import Image
from pytesseract import pytesseract
import os
import re
# assignment stuff
import quickstart
import datetime
import sheets_update_values

def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1

def topHundred():
    # this needs work for the readability.
    # Yisuki becomes Yisuld, Seyn becomes Sem, Tsuki becomes Teulkd?
    path_to_tesseract = r"C:\pytess\tesseract.exe"
    directory = 'C:\pytessimg'
    # Expired token, renew this.
    # service = quickstart.getService()
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            processtime = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
            img = Image.open(f)


            pytesseract.tesseract_cmd = path_to_tesseract


            text = pytesseract.image_to_string(img)
            str = text.split('\n')

            print(text)

def characterInfo():
    path_to_tesseract = r"C:\pytess\tesseract.exe"
    # image_path = r"C:\pytessimg\Pleione.png"
    directory = 'C:\pytessimg'
    service = quickstart.getService()

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            processtime = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
            # img object / open img
            img = Image.open(f)

            # give exe
            pytesseract.tesseract_cmd = path_to_tesseract

            # convert img to string
            text = pytesseract.image_to_string(img)
            str = text.split('\n')

            # Displaying the extracted text
            print(text)
            filename = filename[:-4]
            print(filename)
            # sheets_update_values.append_values('1VKNPvho4pqu3h2zglYxy6YdMQfik8zBqWi4FWDkC0MM','Sheet1!A:A','RAW',filename)

            # class
            charclass = str[:1]
            charclass = listToString(charclass)
            print(str[:1])
            print(charclass)
            # gearscore
            chargs = str[5:6]

            chargs = listToString(chargs)
            chargs = chargs.split(":")[1]

            print(str[5:6])
            print(chargs)
            # pvp honor
            charhonor = str[9:10]

            charhonor = listToString(charhonor)
            charhonor = charhonor.split(":")[1]

            print(str[9:10])
            print(charhonor)
            # player kills
            charkills = str[11:12]

            charkills = listToString(charkills)
            charkills = charkills.split(":")[1]

            print(str[11:12])
            print(charkills)

            values = [
                [filename, chargs, charclass, charkills, charhonor, processtime]
            ]
            body = {'values': values}
            result = service.spreadsheets().values().append(
                spreadsheetId="1VKNPvho4pqu3h2zglYxy6YdMQfik8zBqWi4FWDkC0MM", range="Sheet1!A1",
                valueInputOption="RAW", body=body).execute()

            # print(str)



#topHundred()
#characterInfo()