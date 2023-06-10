package annotation;

import com.sun.istack.internal.NotNull;

import java.lang.annotation.*;

@Target(ElementType.TYPE)
@Documented
@Retention(value = RetentionPolicy.RUNTIME)
@Inherited
public @interface MyAnnotation {
}

@Target(ElementType.FIELD)
@Documented
@Retention(RetentionPolicy.RUNTIME)
@interface MyFieldAnnoation{
    String name() default "zhangsan";
    int val() default  25;
}


@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
@interface Mytag{
    String name();
    int age();
}

@Target(ElementType.PARAMETER)
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@interface MyParameter{


}