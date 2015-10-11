#####################################################
# Maven Project Builder
# File: run.py
# Author: raheal
# Version: 1
#
#####################################################


import sys;
from ScriptMonitor import ScriptMonitor;
from ProjectGenerator import ProjectGenerator;
from Utils import Utils;

def main():
    projectName="";
    dir = "";
    groupId="";
    counter = 1;

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--help"):
            Utils.helpOutput();
            exit(0);
    else:
        for arg in sys.argv [1:]:
            if (arg == "--projectName"):
                projectName = sys.argv[counter+1];
            elif (arg == "--groupId"):
                groupId = sys.argv[counter+1];
            elif (arg == "--directory"):
                dir = sys.argv[counter+1];
            counter+=1;

    ScriptMonitor.message("********************************************");
    ScriptMonitor.message("Maven Project Builder")
    ScriptMonitor.message("********************************************");
    ScriptMonitor.message("projectName = "+projectName);
    ScriptMonitor.message("groupId = "+groupId);
    ScriptMonitor.message("projectDir = "+dir);
    projectGenerator = ProjectGenerator();
    projectGenerator.createProject(dir, projectName, groupId);

main();