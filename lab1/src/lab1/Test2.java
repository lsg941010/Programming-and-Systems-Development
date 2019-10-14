package lab1;
public class Test2 {
    int value;
    void Test(int i) {
        this.value = i;
    }
    public static void main(String[] args) {
        Test2 test = new Test2();
        test.Test(5);
        System.out.println(test.value);
    }
}