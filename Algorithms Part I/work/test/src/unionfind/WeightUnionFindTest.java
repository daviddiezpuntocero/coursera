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
public class WeightUnionFindTest {

    @Test
    public void testUnion() {
        WeightedUnionFind wuf = new WeightedUnionFind(10);
        wuf.union(5, 4);
        wuf.union(7, 1);
        wuf.union(3, 2);
        wuf.union(1, 6);
        wuf.union(4, 3);
        wuf.union(8, 7);
        wuf.union(8, 3);
        wuf.union(0, 9);
        wuf.union(5, 9);
        int[] currentId = wuf.getId();
        for(int i = 0; i < currentId.length; i++) {
            System.out.print(currentId[i] + " ");
        }
    }

}
