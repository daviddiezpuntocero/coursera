public class Tube<T> {
    private T a;
    private T b;
    public Tube (T a, T b) {
        this.a = a;
        this.b = b;
    }

    public T getA() {
        return this.a;
    }

    public T getB() {
        return this.b;
    }
}
