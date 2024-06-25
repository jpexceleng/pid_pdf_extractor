# This script searches for tag numbers in piping plan and pid extracted text
# files.


def getDrawingNameFromPath(path):
    """
    Expected form of piping plan path is:
    "extracted/M51-10-01 - MECHANICAL-PROCESS PIPING PLAN-CA01-LEVEL 1 AREA 1.txt"
    OR
    "extracted/PID-1000 - WEIGHINGDISPENSING ROOM 1640.txt"
    """
    filename = path.split("/")
    name = filename[1].split(" - ")
    name = name[0].strip()
    return name


# enums for results list indices
INDEX_TAG = 0
INDEX_PID = 1
INDEX_MPPP = 2


# read tags from file and initialize results array
def initResultsList(tagsFilePath):
    results = []
    tagsFile = open(tagsFilePath, "r")
    for tag in tagsFile:
        tag = tag.strip()
        result = [tag, [], []]
        results.append(result)
    tagsFile.close()
    return results


def foundInPipingPlanFile(pipingPlanFilepath, tag):
    """
    Takes path to piping plan extracted text file and tag number. 
    
    Returns True if tag number is found in text file.
    Returns False otherwise.
    """
    foundFlag = False
    fh = open(pipingPlanFilepath, "r")
    for line in fh:
        if (tag in line):
            foundFlag = True
    fh.close()
    return foundFlag


def foundInPIDFile(pidFilepath, tag):
    """
    Takes path to piping plan extracted text file and tag number. 
    
    Returns True if tag number is found in text file.
    Returns False otherwise.
    """
    foundFlag = False
    fh = open(pidFilepath, "r")
    for line in fh:
        if (tag in line):
            foundFlag = True
    fh.close()
    return foundFlag


# read piping plan filenames from file into list
def getPipingPlanPaths(pipingPlanFilepathsFile):
    paths = []
    pipingPlanPathsFile = open(pipingPlanFilepathsFile, "r")
    for line in pipingPlanPathsFile:
        paths.append(line)
    pipingPlanPathsFile.close()
    return paths


# read pid filenames from file into list
def getPIDPaths(pidFilepathsFile):
    paths = []
    pidPathsFile = open(pidFilepathsFile, "r")
    for line in pidPathsFile:
        paths.append(line)
    pidPathsFile.close()
    return paths


def searchForTags(results, paths, index):
    """
    This function populates results list with drawing names found to contain
    a given tag number.

    results - list of form [<tag>, [<mppp_1, mppp_2, ...>], [<pid_1, pid2, ...>]]
    paths - list containing filepaths to search for tags.
    index - indicates where to store search result; possible values include: 
            INDEX_PID (1) and INDEX_MPPP (2).
    """
    for result in results:
        found = []
        for path in paths:
            path = path.strip()
            if (foundInPipingPlanFile(path, result[INDEX_TAG])):
                pipingPlan = getDrawingNameFromPath(path)
                found.append(pipingPlan)
                continue
        result[index] = found


# write results to file
def writeResultsToFile(resultsFilepath, results):
    resultsFile = open(resultsFilepath, "w")
    for result in results:
        line = result[INDEX_TAG]
        
        # append pids found
        if not result[INDEX_PID]:
            line = line + ', N/A'
        else:
            line = line + ','
            for pid in result[INDEX_PID]:
                line = line + ' ' + pid

        # append mechanical-process piping plans found
        if not result[INDEX_MPPP]:
            line = line + ', N/A'
        else:
            line = line + ','
            for pp in result[INDEX_MPPP]:
                line = line + ' ' + pp

        line = line + '\n'
        resultsFile.write(line)
    resultsFile.close()


def main():
    tagsFile = 'input/tags.txt'
    mpppFilepathsFile = 'input/mppp_filepaths.txt'
    pidFilepathsFile = 'input/pid_filepaths.txt'
    resultsFilepath = 'results/results.txt'

    results = initResultsList(tagsFile)

    pipingPlanPaths = getPipingPlanPaths(mpppFilepathsFile)
    searchForTags(results, pipingPlanPaths, INDEX_MPPP)
    
    pidPlanPaths = getPIDPaths(pidFilepathsFile)
    searchForTags(results, pidPlanPaths, INDEX_PID)

    writeResultsToFile(resultsFilepath, results)


main()