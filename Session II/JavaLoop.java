import java.util.Date;

class JavaLoop{
    public static void main(String args[])
    {
        int val = 0;
        Date d1 = new Date();
        for(int i=0; i<100000000; i++)
        {
            val += i;
        }
        Date d2 = new Date();
        System.out.println(d2.getTime()-d1.getTime()+" ms");
    }


}