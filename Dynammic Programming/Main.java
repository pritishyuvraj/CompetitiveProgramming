// class Main {
//   public static void main(String[] args) {
//     System.out.println("Hello world!");
//   }
// }


class Main{
  public static void main(String[] args){
    long StartTime;
    long endTime;
    int n = 100;
    StartTime = System.nanoTime();
    System.out.println(Integer.toString(fibonacci_recursive(n)));
    endTime = System.nanoTime();
    // System.out.println("\nRecursive time -> " )
    System.out.printf("Recursive Time -> %d", (endTime - StartTime));
    
    StartTime = System.nanoTime();
    System.out.printf("\n\nDynammic Result %d", fibonacci_dynammic(n));
    endTime = System.nanoTime();
    System.out.printf("\nDynammic Time -> %d", endTime - StartTime);
    
    StartTime = System.nanoTime();
    System.out.printf("\n\nWithout loops -> %d", fibonacci_without_loops(n));
    endTime = System.nanoTime();
    System.out.printf("\nWithout Loops time -> %d", endTime - StartTime);
  }
  
  public static int fibonacci_without_loops(int n){
    int sum = 0;
    int a = 0;
    int b = 1; 
    
    if (n == 0){
      return 0;
    }
    if (n == 1){
      return 1;
    }
    for (int i = 2; i<= n; i++){
      sum = (a + b);
      // System.out.printf("\n %d,  %d -> %d", a, b, sum);
      a = b;
      b = sum;
    }
    return sum;
  }
  public static int fibonacci_recursive(int n){
    if (n == 0){
      return 0;
    }
    if (n == 1){
      return 1;
    }
    return  fibonacci_recursive(n-2)  + fibonacci_recursive(n - 1);
  }
  
  public static int fibonacci_dynammic(int n){
    int[] fibo = new int[n+1];
    fibo[0] = 0;
    fibo[1] = 1;
    for (int i = 2; i < fibo.length; i++){
      // System.out.printf("\nOutput -> %d", i);
      fibo[i] = fibo[i-1] + fibo[i - 2];
    }
    return fibo[n];
  }
}