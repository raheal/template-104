import os;
import sys;
from FileGenerator import FileGenerator;

class ProjectGenerator:
    
    def __init__ (self):
        print("OUT> Generating a project....");
        
    def createProject(self, dir, projectName, groupId):
        projectDir = dir+"/"+projectName;
        
        SOURCE_MAIN_JAVA = "src/main/java";
        SOURCE_MAIN_RESOURCES = "src/main/resources"
        SOURCE_TEST_JAVA = "src/test/java"
        SOURCE_TEST_RESOURCES = "src/test/resources";
        
        if not os.path.isdir(projectDir):
            os.mkdir(projectDir);
            # create the POM file
            FileGenerator.createPOMFile(projectName, groupId, projectDir);
        
            # create the project directories
        
            os.makedirs(projectDir+"/"+SOURCE_MAIN_JAVA);
            os.makedirs(projectDir+"/"+SOURCE_TEST_JAVA);
            os.makedirs(projectDir+"/"+SOURCE_MAIN_RESOURCES);
            os.makedirs(projectDir+"/"+SOURCE_TEST_RESOURCES);
            os.makedirs(projectDir+"/logs");
    
            packageFolderPathSrc = ProjectGenerator.createPackageFolder(self, projectDir, SOURCE_MAIN_JAVA, groupId);
            packageFolderPathTest = ProjectGenerator.createPackageFolder(self, projectDir, SOURCE_TEST_JAVA, groupId);
                
            #create the MainApplication.java file
            
            FileGenerator.createSourceEntryFile(packageFolderPathSrc, groupId)
            FileGenerator.createLogPropertiesFile(groupId, projectDir+"/"+SOURCE_MAIN_JAVA+"/log4j.properties");
    
    
        else:
            print("ERR> Folder : "+projectDir+" exists");
    
    @staticmethod
    def createPackageFolder(self, projectDir, mavenSourceFolder, groupId):
        packagefolders = groupId.split(".");
        packageFolderPath = projectDir+"/"+mavenSourceFolder;
        for d in packagefolders:
            packageFolderPath += "/"+d;
        packageFolderPath+="/app";
        os.makedirs(packageFolderPath);
        return packageFolderPath;
        
        