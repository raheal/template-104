from FileController import FileController;
from Utils import Utils;

class FileGenerator:
    
    @staticmethod
    def createLogPropertiesFile(groupId, filepath):
        content = FileController.readFile("log.template");
        updatedContent = content.replace("{group.id}", groupId);
        FileController.writeToFile(updatedContent, filepath);
    
    @staticmethod
    def createSourceEntryFile(dir, groupId):
        content = FileController.readFile("java.template");
        res = content.replace("{package.name}", groupId+".app;")
        FileController.writeToFile(res, dir+"/MainApplication.java");
        
    @staticmethod
    def createPOMFile(projectName, groupId, projectDir):
        dict = {"{project.name}" : projectName, 
                "{artifact.id}": projectName,
                "{group.id}": groupId,
                "{version}": "1.0",
                "{list-dependencies}" : FileGenerator.readDependencyFile(),
                "{application.entrypoint}" : groupId+".app.MainApplication"};
    
        pomcontent = FileController.readFile("pom.template");
        print("CONTENT = "+pomcontent);
        str = pomcontent;
        for i, j in dict.items():
            str = str.replace(i, j);
        FileController.writeToFile(str, projectDir+"/pom.xml");
    
    @staticmethod    
    def readDependencyFile():
        lines = FileController.readFileAndReturnLines("dependencies.txt");
        dependencyString = "";
        for e in lines [1:]:
            dependencyString += "<dependency>\n"+Utils.tabs(3);
            record = e.split(",");
            dependencyString += "<artifactId>"+record[0]+"</artifactId>\n"+Utils.tabs(3);
            dependencyString += "<groupId>"+record[1]+"</groupId>\n"+Utils.tabs(3);
            dependencyString += "<version>"+record[2]+"</version>\n"+Utils.tabs(2);
            dependencyString += "</dependency>";
        return dependencyString;