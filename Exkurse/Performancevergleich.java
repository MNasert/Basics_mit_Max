public class Performancevergleich {
  
  public static void main(String[] args) {
    long start = System.currentTimeMillis();
    for (int i = 0; i < 100000; i++) {
      test(1000);
    }
    long end = System.currentTimeMillis();
    double runtime = (end-start);
    System.out.println(runtime/1E3);
  } // end of main
  
  
  
  public static int test(int x){
    int q = 0;
    int n = 0;
    for (int i = 0; i < x; i++) {
      q = q + i;
      n = n + q;
    }
    return q; 
    }
} // end of class Performancevergleich

