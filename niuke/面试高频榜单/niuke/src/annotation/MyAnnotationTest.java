package annotation;

import java.lang.annotation.Annotation;
import java.lang.reflect.Method;

@MyAnnotation
class MyAnnotationTest {

    @MyFieldAnnoation(name = "lisi")
    public String address;

    @Mytag(name = "dhs", age = 26)
    public void show(){
        System.out.println("**");
    }
    public static void main(String[] args) throws ClassNotFoundException, NoSuchMethodException {
        MyAnnotationTest myAnnotationTest = new MyAnnotationTest();
        System.out.println(myAnnotationTest.address);
        Annotation[] annotation = myAnnotationTest.getClass().getAnnotations();
        for(Annotation anno: annotation){
            System.out.println(anno);
        }
        Annotation annotation1 = Class.forName("annotation.MyAnnotationTest").getMethod("show").getAnnotation(Mytag.class);
        System.out.println(annotation1);
        Method method = Class.forName("annotation.MyAnnotationTest").getMethod("show");
        System.out.println(method.isAnnotationPresent(Mytag.class));
    }
}
