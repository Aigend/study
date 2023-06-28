package annotation;
//import java.lang.*;
class AnnotationTest implements Annota{

    @Deprecated
    @SuppressWarnings("uncheck")
    public void test(){
        System.out.println("test has deprecated");
    }
    public static void main(String[] args) {
        AnnotationTest annotationTest = new AnnotationTest();
        System.out.println(annotationTest);
        annotationTest.test();
    }

    @Override
    public void show() {
        System.out.println("Annotation test show execute .....");
    }
}
