import re

# load raw file
PATH_RAW = "preproinsulin-seq.txt"
with open(PATH_RAW, "r") as f:
    raw_data = f.read()
    
# remove "ORIGIN", "//", digit, and any extra whitespace. Ensure it lowercase
raw_data = re.sub(r"ORIGIN", "", raw_data)
raw_data = re.sub(r"//", "", raw_data)
raw_data = re.sub(r"[^A-Za-z]", "", raw_data)
raw_data = re.sub(r"\s+", "", raw_data)
raw_data = raw_data.lower()

# save cleaned data to a new file
PATH_CLEAN = "preproinsulin-seq-clean.txt"
cleaned_data = raw_data
with open(PATH_CLEAN, "w") as f:
    f.write(cleaned_data.lower())

# ensure it has 110 characters
with open(PATH_CLEAN, "r") as f:
    cleaned_data = f.read()
if len(cleaned_data) != 110:
    print("Error: {PATH_CLEAN} does not have 110 characters.")
else:
    print(f"Valid: {PATH_CLEAN} has {len(cleaned_data)} characters")

    # split the sequence into parts for each insulin component using slicing
    linsulin = {"name": "linsulin", "data": cleaned_data[0:24]}   # characters 1-24
    binsulin = {"name": "binsulin", "data": cleaned_data[24:54]}  # characters 25-54
    cinsulin = {"name": "cinsulin", "data": cleaned_data[54:89]}  # characters 55-89
    ainsulin = {"name": "ainsulin", "data": cleaned_data[90:110]} # characters 90-110

    for i in linsulin, binsulin, cinsulin, ainsulin:
        # save each part to its own file
        INSULIN_PARTS_FILE_NAMES = i["name"] + "-seq-clean.txt"
        with open(INSULIN_PARTS_FILE_NAMES, "w") as f:
            f.write(i["data"])
        print(f"Saved {INSULIN_PARTS_FILE_NAMES} with {len(i['data'])} characters")

print("DONE")