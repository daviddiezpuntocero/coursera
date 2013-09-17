import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.junit.Ignore;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

public class ShellTest {

    @Test
    public void testShell()
    {
        Integer[] a = {
            new Integer(67), new Integer(73), new Integer(57), new Integer(55),
            new Integer(86), new Integer(37), new Integer(80), new Integer(22),
            new Integer(83), new Integer(27)
        };
        Shell.sort(a);
    }
}
