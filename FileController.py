class FileController:
    
    @staticmethod        
    def writeToFile(content, filepath):
        f = open(filepath, 'w');
        f.write(content);
        f.close();
        
        
    @staticmethod
    def readFile(filepath):
        f = open(filepath, 'r');
        content = f.read();
        f.close();
        return content;

    @staticmethod
    def readFileAndReturnLines(filepath):
        f = open(filepath);
        lines = f.readlines();
        return lines;