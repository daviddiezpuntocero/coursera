import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.junit.Ignore;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

public class InsertionTest {

    @Test
    public void testInsertionSort() 
    {
        Integer[] a = {
                       new Integer(11), new Integer(26),
                       new Integer(66), new Integer(71),
                       new Integer(72), new Integer(88),
                       new Integer(21), new Integer(45),
                       new Integer(87), new Integer(27)
        };
        Insertion.sort(a);
    }

    @Test
    public void testInsertionSort2() 
    {
        Integer[] a = {
                       new Integer(47), new Integer(64),
                       new Integer(67), new Integer(87),
                       new Integer(89), new Integer(59),
                       new Integer(62), new Integer(83),
                       new Integer(34), new Integer(91)
        };
        Insertion.sort(a);
    }
}
