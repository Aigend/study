package com.base;

/**
 * @Author 徐志
 * @date 2020/9/4 12:42
 **/
interface BasicEnum<L,V> {
    /**
     * get name
     *
     * @return
     */
    L getName();
    /**
     * get value
     *
     * @return
     */
    V getValue();
}

/**
 * @Author 徐志
 * @date 2020/9/4 12:38
 **/
enum Color implements BasicEnum<String,Integer>{
    RED("a",0),
    GREEN("b",1),
    BLUE("c",2);
    private final String name;
    private final Integer value;
    Color(String name, Integer value) {
        this.name = name;
        this.value = value;
    }
    public String getName() {
        return this.name;
    }
    public Integer getValue() {
        return this.value;
    }
}

/**
 * @Author 徐志
 * @date 2020/9/4 12:46
 **/
public class EnumTest2 {

    public void test(){
        System.out.println(Color.valueOf("RED").getValue());
    }

    public static void main(String[] args) {
        EnumTest2 enumTest2 = new EnumTest2();
        enumTest2.test();
    }
}