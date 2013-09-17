public class Insertion {
    public static void sort(Comparable[] a) 
    {
        int N = a.length;
        int exchange = 0;
        for (int i = 0; i < N; i++) {
            for (int j = i; j > 0 ; j--) {
                if (less(a[j], a[j - 1])) {
                    exch(a, j, j - 1);
                    exchange++;
                    System.out.print("\n" + exchange + ": ");
                    for (int k = 0; k < N; k++) {
                        System.out.print(a[k] + " ");
                    }
                }
            }
        }
        System.out.println();
        for (int k = 0; k < N; k++) {
            System.out.print(a[k] + " ");
        }        
    }

    private static boolean less (Comparable v, Comparable w) 
    {
        return v.compareTo(w) < 0;
    }
    
    private static void exch(Comparable[] a, int i, int j) 
    {
        Comparable swap = a[i];
        a[i] = a[j];
        a[j] = swap;
    }

}
