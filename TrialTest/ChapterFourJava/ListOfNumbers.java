import java.util.Arrays;
public class ListOfNumbers {

public static int[] resultOfArray(int[] array, int number){
        int[] result = new int[array.length];
	
        for(int value = 0; value < array.length; value++){
            result[value] = array[value] * number;
            
        }
        return result;
    }
public static void main(String[] args) {

int[] numbers = {3, 4, 6, 7, 10};
int number = 4;
System.out.print(Arrays.toString(resultOfArray(numbers, number)));


}









}
