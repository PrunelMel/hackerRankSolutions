import java.util.*;
public class EqualStacks{

    public static int getStackSum(List<Integer> h){

        int sum = 0;

        for(int i: h){
            
            sum += i;

        }

        return sum;
    }


    public static int equalizer(List<Integer> h1, List<Integer> h2, List<Integer> h3 ){

        int sumH1 = getStackSum(h1);

        int sumH2 = getStackSum(h2);

        int sumH3 = getStackSum(h3);

        while(true){

            if (sumH1 == sumH2 && sumH2 == sumH3){

                break;
            }
            else{

                if(sumH1 > sumH2 && sumH1 > sumH2){

                    sumH1 -= h1.get(0);
                }
                else if(sumH2 > sumH1 && sumH2 > sumH3){

                    sumH2 -= h2.get(0);
                }
                else if(sumH3 > sumH1 && sumH3 > sumH2){

                    sumH3 -= h3.get(0);
                }
            }
        }

        return sumH1;
    }

    public static void main(String [] args){

        List<Integer> h1 = List.of(3, 2, 1, 1, 1);
        List<Integer> h2 = List.of(4, 3, 2);
        List<Integer> h3 = List.of(1, 1, 4, 1);

        System.out.println(equalizer(h1, h2, h3));
        
    }
}