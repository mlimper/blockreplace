#!/usr/bin/python3

from argparse import ArgumentParser
from pathlib import Path


# #############################################################################
# argument parsing
# #############################################################################

parser = ArgumentParser()

parser.add_argument("-i", "--inputDirectory",  help="input directory",  default=".")
parser.add_argument("-o", "--outputDirectory", help="output directory", default="out")

pArgs    = parser.parse_args()
argsDict = vars(pArgs)

inputDirectory  = argsDict["inputDirectory"]
outputDirectory = argsDict["outputDirectory"]


# #############################################################################
# global variables and utility functions
# #############################################################################

BlockFileExt  = ".block"
BlockTagStart = "<blorp>"
BlockTagEnd   = "</blorp>"

def getBlockStr(blockName, blockFiles):
    for bf in blockFiles:
        if bf.stem == blockName:
            with open(bf) as blockFileHandle:
                return blockFileHandle.read()
   
    errorMsg = "ERROR: Could not replace block \"" + blockName + "\""
    print(errorMsg)    
    return "<strong>" + errorMsg + "</strong>"


# #############################################################################
# main script
# #############################################################################

htmlFiles  = list(Path(inputDirectory).glob('*.html'))
blockFiles = list(Path(inputDirectory).glob('*' + BlockFileExt))

for htmlFile in htmlFiles:

    with open(htmlFile) as htmlFileHandle:

        htmlFileContent    = htmlFileHandle.read()
        replacedBlockNames = []
        newHTMLFileContent = htmlFileContent
        
        blockIdx = htmlFileContent.find(BlockTagStart)        

        # parse blocks within the file and replace them
        while blockIdx != -1:
            blockEndIdx = htmlFileContent.find(BlockTagEnd, blockIdx + len(BlockTagStart))            

            # very basic error check
            if (blockEndIdx == -1):
                print("ERROR: Incomplete block. Must start with \"" + BlockTagStart +
                      "\" and end with \"" + BlockTagEnd + "\".")
                blockIdx = htmlFileContent.find(BlockTagStart, blockIdx + 1)
                continue

            # parse block name        
            blockName = htmlFileContent[blockIdx+len(BlockTagStart):blockEndIdx]

            if blockName in replacedBlockNames:
                blockIdx = htmlFileContent.find(BlockTagStart, blockIdx + 1)
                continue

            fullBlockNew = getBlockStr(blockName, blockFiles)

            # perform replacement for all instances
            fullBlockOld = htmlFileContent[blockIdx:blockEndIdx + len(BlockTagEnd)]
            newHTMLFileContent = newHTMLFileContent.replace(fullBlockOld, fullBlockNew)

            # remember that this block name has been processed for this HTML files
            replacedBlockNames.append(blockName)            
         
            blockIdx = htmlFileContent.find(BlockTagStart, blockIdx + 1)

        # write output file        
        outputFilePath = Path(outputDirectory).joinpath(htmlFile.name)

        with open(outputFilePath, "w") as htmlOutputFileHandle:
            htmlOutputFileHandle.write(newHTMLFileContent)
