import java.lang.Math;
class Knapsack_advanced {
  public static void display(int[] items){
    for(int item: items){
      System.out.println(item);
    }
  }
  
  public static void display2(int[][] array, int[] items, int[] weights, int total_weight){
    System.out.printf("\n\n %d %d\n\n", items.length, weights.length);
    for (int i = 0; i<=items.length; i++ ){
      for(int j = 0; j<=total_weight; j++){
        System.out.printf("%d", array[i][j]);
      }
      System.out.printf("\n");
    }
  }
  
  public static void dynammicProg(int[] items, int[] weights, int total_weight){
    System.out.println(weights.length);
    int[][] array = new int[weights.length+1][total_weight+1];
    // display2(array, items, weights, total_weight);
    for (int item = 0; item <= weights.length; item++){
      for (int weight = 0; weight <= total_weight; weight++){
        if ((item == 0) || (weight == 0)){
          array[item][weight] = 0;
        }
        else if(weight < weights[item - 1]){
          array[item][weight] = array[item - 1][weight];
        }
        else{
          array[item][weight] = Math.max(items[item-1] + array[item-1][weight - weights[item-1]], array[item-1][weight]);
        }
      }
    }
    display2(array, items, weights, total_weight);
  }
  
  public static void main(String[] args) {
    System.out.println("Hello world!");
    int[] items = {1, 4, 5, 7};
    int[] weights = {1, 3, 4, 5};
    int total_weight = 7;
    dynammicProg(items, weights, total_weight);
    // display(items);
  }
}