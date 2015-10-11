class Utils:
    
    @staticmethod    
    def tabs(num):
        if (num == 4):
            return "\t\t\t\t";
        elif (num == 3):
            return "\t\t\t";
        elif (num == 2):
            return "\t\t";
        elif (num == 1):
            return "\t";
        
    @staticmethod    
    def helpOutput():
        print("\n--projectName\t\tName of your new Project");
        print("--groupId\t\tA group id for your project");
        print("--directory\t\tthe location where you want the project to be created.\n")
        print("usage:\n");
        print("python run.py --projectName <PROJECT_NAME> --groupId <GROUP_ID> --directory <DIRECTORY_PATH>\n\n");
        print("example:\n");
        print("python run.py --projectName MyNewProject --groupId com.packagename --directory C:/devwork\n\n");