import java.util.ArrayList;
import java.util.List;

interface FileSystemItem {
    public void ls(int indent);
    public void openAll(int indent);
    public int getSize();
    public FileSystemItem cd(String name);
    public String getName();
    public boolean isFolder();
}

class File implements FileSystemItem {
    private String name;
    private int size;

    public File(String name, int size) {
        this.name = name;
        this.size = size;
    }

    @Override
    public void ls(int indent) {
        String indentSpace = " ".repeat(indent);
        System.out.println(indentSpace + name);
    }

    @Override
    public void openAll(int indent) {
        String indentSpace = " ".repeat(indent);
        System.out.println(indentSpace + name);
    }
       

    @Override
    public int getSize() {
       return size;
    }

    @Override
    public FileSystemItem cd(String name) {
       return null;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public boolean isFolder() {
        return false;        
    }
}

class Folder implements FileSystemItem{
    private String folder;
    private List<FileSystemItem> children;

    public Folder(String folder){
        this.folder = folder;
        this.children = new ArrayList<>();
    }

    public void add(FileSystemItem item){
        children.add(item);
    }

    @Override
    public void ls(int indent) {
        String indentSpaces = " ".repeat(indent);

        for (FileSystemItem child: children){
            if(child.isFolder()){
                System.out.println(indentSpaces + "+ " + child.getName());
            } else {
                System.out.println(indentSpaces + child.getName());
            }
        }

    }

    @Override
    public void openAll(int indent) {
        String indentSpaces = " ".repeat(indent);
        System.out.println(indentSpaces + "+ " + folder);

        for (FileSystemItem child: children){
           child.openAll(indent + 4);
        }
    }

    @Override
    public int getSize() {
        int total = 0;

        for (FileSystemItem child: children){
            total += child.getSize();
        }
        return total; 
    }

    @Override
    public FileSystemItem cd(String name) {
        for (FileSystemItem child: children){
            if(child.isFolder() && child.getName() == name){
                return child;
            }
        }
        return null;
    }

    @Override
    public String getName() {
        return folder;
    }

    @Override
    public boolean isFolder() {
        return true;
    }
    
}



public class Composite {
    public static void main(String[] args) {
        Folder root = new Folder("root");
        root.add(new File("file1.txt", 20));
        root.add(new File("file2.txt", 30));
        Folder core = new Folder("core");

        core.add(new File("file3.txt", 40));
        core.add(new File("file4.txt", 1));

        root.add(core);

        Folder user = new Folder("user");

        user.add(new File("file5.txt", 100));
        root.add(user);
        
        FileSystemItem cwd = root;

        if(cwd != null){
            cwd.ls(0);
        }

    }
}
