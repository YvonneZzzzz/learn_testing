package test00;

public class Puppy{
    public Puppy(String name){
        // �������������һ�������� name
        System.out.println("С���������ǣ�"+ name);
    }
    // �޷�ִ�У��ᱨ��
    // String name;
    // public Puppy(){
    //     // �������������һ�������� name
    //     System.out.println("С���������ǣ�"+ name);
    // }
    public static void main(String []args){
        // �������佫����һ��Puppy����
        Puppy myPuppy = new Puppy("tommy");
    }
}