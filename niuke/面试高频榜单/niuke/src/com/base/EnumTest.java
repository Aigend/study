package com.base;
import java.lang.Enum;
enum SeasonEnum{
    Spring, SUMMER, FALL, WINTER;
}
class EnumTest {
    public void judge(SeasonEnum seasonEnum){
        switch (seasonEnum){
            case Spring:
                System.out.println("SPRING");
                break;
            case SUMMER:
                System.out.println("SUMMER");
        }
    }
    public static void main(String[] args) {
        SeasonEnum s = SeasonEnum.Spring;
        SeasonEnum t = SeasonEnum.SUMMER;
        System.out.println(s.compareTo(t));
        System.out.println(s.name());
        System.out.println(t.ordinal());
        System.out.println(t.toString());

        SeasonEnum q = SeasonEnum.valueOf(SeasonEnum.class, "Spring");
        System.out.println(q.compareTo(s));
    }
}
