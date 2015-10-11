from FileController import FileController;
from Utils import Utils;
from ScriptMonitor import ScriptMonitor;

class FileGenerator():
    
    @staticmethod
    def createLogPropertiesFile(groupId, filepath):
        ScriptMonitor.message("Creating the log4j file: log4j.properties");
        content = FileController.readFile("log.template");
        updatedContent = content.replace("{group.id}", groupId);
        FileController.writeToFile(updatedContent, filepath);
    
    @staticmethod
    def createSourceEntryFile(dir, groupId):
        ScriptMonitor.message("Creating sample java class: MainApplication.java");
        content = FileController.readFile("java.template");
        res = content.replace("{package.name}", groupId+".app;")
        FileController.writeToFile(res, dir+"/MainApplication.java");
        
    @staticmethod
    def createPOMFile(projectName, groupId, projectDir):
        ScriptMonitor.message("Creating the model file: pom.xml");
        dict = {"{project.name}" : projectName, 
                "{artifact.id}": projectName,
                "{group.id}": groupId,
                "{version}": "1.0",
                "{list-dependencies}" : FileGenerator.readDependencyFile(),
                "{application.entrypoint}" : groupId+".app.MainApplication"};
    
        pomcontent = FileController.readFile("pom.template");
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
            dependencyString += "<version>"+record[2].strip()+"</version>\n"+Utils.tabs(2);
            dependencyString += "</dependency>\n"+Utils.tabs(2);
        return dependencyString;