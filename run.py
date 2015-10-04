import sys;
import os;


def writePomFile(str, projectDir):
    f = open(projectDir+"/pom.xml", 'w');
    f.write(str);
    f.close();

def readDependencyFile():
    f = open("dependencies.txt");
    lines = f.readlines();
    dependencyString = "";
    for e in lines [1:]:
        dependencyString += "<dependency>\n"+tabs(3);
        record = e.split(",");
        dependencyString += "<artifactId>"+record[0]+"</artifactId>\n"+tabs(3);
        dependencyString += "<groupId>"+record[1]+"</groupId>\n"+tabs(3);
        dependencyString += "<version>"+record[2]+"</version>\n"+tabs(2);
        dependencyString += "</dependency>";
    return dependencyString;




def tabs(num):
    if (num == 4):
        return "\t\t\t\t";
    elif (num == 3):
        return "\t\t\t";
    elif (num == 2):
        return "\t\t";
    elif (num == 1):
        return "\t";
    

def readFile(projectName, groupId, projectDir):
    
    dict = {"{project.name}" : projectName, 
            "{artifact.id}": projectName,
            "{group.id}": groupId,
            "{version}": "1.0",
            "{list-dependencies}" : readDependencyFile(),
            "{application.entrypoint}" : groupId+".app.MainApplication"};
    
    print("Reading the file");
    f = open("pom.template");
    content = f.read();
    f.close();
    str = content;
    for i, j in dict.items():
        str = str.replace(i, j);
        
    print("contents of file:\n\n"+str);
    writePomFile(str, projectDir);



def createProject(dir, projectName, groupId):
    projectDir = dir+"/"+projectName;
    
    SOURCE_MAIN_JAVA = "src/main/java";
    SOURCE_MAIN_RESOURCES = "src/main/resources"
    SOURCE_TEST_JAVA = "src/test/java"
    SOURCE_TEST_RESOURCES = "src/test/resources";
    
    if not os.path.isdir(projectDir):
        os.mkdir(projectDir);
        # create the POM file
        readFile(projectName, groupId, projectDir);
    
        # create the project directories
    
        os.makedirs(projectDir+"/"+SOURCE_MAIN_JAVA);
        os.makedirs(projectDir+"/"+SOURCE_TEST_JAVA);
        os.makedirs(projectDir+"/"+SOURCE_MAIN_RESOURCES);
        os.makedirs(projectDir+"/"+SOURCE_TEST_RESOURCES);

        packageFolderPathSrc = createPackageFolder(projectDir, SOURCE_MAIN_JAVA, groupId);
        packageFolderPathTest = createPackageFolder(projectDir, SOURCE_TEST_JAVA, groupId);
            
        #create the MainApplication.java file
        
        createSourceEntryFile(packageFolderPathSrc, groupId)


    else:
        print("ERR> Folder : "+projectDir+" exists");
    




def createPackageFolder(projectDir, mavenSourceFolder, groupId):
    packagefolders = groupId.split(".");
    packageFolderPath = projectDir+"/"+mavenSourceFolder;
    for d in packagefolders:
        packageFolderPath += "/"+d;
        
    packageFolderPath+="/app";
    os.makedirs(packageFolderPath);
    return packageFolderPath;
    
def createSourceEntryFile(dir, groupId):
    f = open("java.template", 'r');
    content = f.read();
    f.close();
    res = content.replace("{package.name}", groupId+".app;")
    
    sourceFile = open(dir+"/MainApplication.java", 'w');
    sourceFile.write(res);
    sourceFile.close();

def main():
    projectName="";
    dir = "";
    groupId="";
    print("Running the main method");

    counter = 1;
    for arg in sys.argv [1:]:
        if (arg == "--projectName"):
            projectName = sys.argv[counter+1];
        elif (arg == "--groupId"):
            groupId = sys.argv[counter+1];
        elif (arg == "--directory"):
            dir = sys.argv[counter+1];
        counter+=1;

    print("projectName = "+projectName);
    print("groupId = "+groupId);
    print("projectDir = "+dir);
    #readFile(projectName, groupId, dir);
    createProject(dir, projectName, groupId);

main();