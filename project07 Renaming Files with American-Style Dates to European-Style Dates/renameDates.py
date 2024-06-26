#! python3
# renameDates.py
# Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.
import shutil, os, re


# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)- # one or two digits for the month
    ((0|1|2|3)?\d)- # one or two digits for the day
    ((19|20)\d\d) # four digits for the year
    (.*?)$ # all text after the date
    """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    print('American filename : ', amerFilename)
    matchObj = datePattern.search(amerFilename)

    # Skip files without a date.
    if matchObj is None:
        continue

    # Get the different parts of the filename.
    beforePart = matchObj.group(1)
    monthPart = matchObj.group(2)
    dayPart = matchObj.group(4)
    yearPart = matchObj.group(6)
    afterPart = matchObj.group(8)

    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    print('Euro filename : ', euroFilename)

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...') #test output
    #shutil.move(amerFilename, euroFilename) # uncomment after testing