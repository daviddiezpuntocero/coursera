import java.lang.Double;
import java.lang.Math;

public class TimeProgram {

    public Tube<Double> calculateLg(Tube<Double> tube) {
        return new Tube<Double>(Math.log(tube.getA()),
                                Math.log(tube.getB()));
    }

}
