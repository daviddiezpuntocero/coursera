package unionfind;

import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.junit.Ignore;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

/**
 * Tests for {@link Foo}.
 *
 * @author user@example.com (John Doe)
 */
@RunWith(JUnit4.class)
public class QuickFindTest {

    @Test
    public void testUnion() {
        QuickFind quickFind = new QuickFind(10);
        quickFind.union(2, 5);
        quickFind.union(7, 1);
        quickFind.union(0, 3);
        quickFind.union(1, 9);
        quickFind.union(5, 4);
        quickFind.union(7, 8);
        int[] currentId = quickFind.getId();
        for(int i = 0; i < currentId.length; i++) {
            System.out.print(currentId[i] + " ");
        }
    }

}
