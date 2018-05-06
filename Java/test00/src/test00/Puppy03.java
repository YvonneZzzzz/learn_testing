package test00;

public class Puppy03 {
	int puppyAge;
	public void setAge( int age) {
		puppyAge = age;
		System.out.println("这是" + puppyAge);
	}
	
	public static void main(String []args) {
//		创建对象
		Puppy03 myPuppy = new Puppy03();
		myPuppy.setAge(868);
		System.out.print("变量值：" + myPuppy.puppyAge);
//		System.out.println("static中的" + puppyAge);
	}
}
