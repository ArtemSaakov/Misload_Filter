# misload bad-plot checker
# filter misloads to show non-mismatching work areas so
# as to more easily identify potential bad plots

import pandas as pd
from pathlib import Path

while True:
    try:
        # takes a file path with the assumption it will be dragged in
        path = input("Drag file into window ")
        # strips leftside whitespace and 
        path = path.lstrip(" &")
        if "'" in path:
            path = path.strip("'")
            path = path.strip('"')
        if '"' in path:
            path = path.strip('"')
            path = path.strip("'")
        filepath = Path(path)

        data = pd.read_excel(
            filepath,
            header=2,
        )

        indices = []

        for h, i in data.iterrows():
            workArea = str(i['WA#'])
            visionLabel = i["Vision Label"]
            if not isinstance(visionLabel, str) or workArea not in visionLabel[:4]:
                indices.append(h)
        data = data.drop(index=indices)
        try:
            data.to_excel(filepath)
            print("Open the original file to see the resulting data")
        except Exception as e:
            print(f'Error: {e}')
            response = input("The data was not able to be written to the file. Print it in this window? (y/n)")
            if response.lower() == "y":
                print(data)
        break
    except Exception as e:
        print("Something went wrong. Is there a space in the file name?")
        print(f'Error: {e}')
        break



