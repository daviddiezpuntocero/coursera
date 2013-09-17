import java.util.Arrays;
import java.util.Random;

public class GrahamScan {
    public static void main(String[] args) {
        int N = 10;
        Point2D[] p = new Point2D[N];
        Random random = new Random();
        for (int i = 0; i < p.length; i++) {
            p[i] = new Point2D(random.nextDouble(), random.nextDouble());
        }

        Stack<Point2D> hull = new Stack<Point2D>();
        Arrays.sort(p, Point2D.Y_ORDER); //<--- p[0] is now point with lowest y-coordinate
        Arrays.sort(p, p[0].POLAR_ORDER); //<-- sort by polar angle with respect to p[0]

        hull.push(p[0]);  //<--- definitely on hull
        hull.push(p[1]);  //<--- definitely on hull
        
        for (int i = 0; i < N; i ++) {
            Point2D top = hull.pop();
            while (Point2D.ccw(hull.peek(), top, p[i]) <=0) {
                top = hull.pop(); //discard points that would create clockwise turn
            }
            hull.push(top);
            hull.push(p[i]); // <-- Add p[i] to putative hull.
        }
    }
}
