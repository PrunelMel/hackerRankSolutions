import java.util.Arrays;
import java.util.List;


class ArrayManip{

    public static long Result(int n, List<List<Integer>> queries){
        
        long [] arr = new long[n];//all values are 0 by default


        for(List<Integer> query : queries){

            System.out.println(query);

            for(int i=query.get(0); i <= query.get(1) && i >= query.get(0); i++){

                // System.out.println(query);
                
                arr[i - 1] += query.get(2);

            }

            System.out.println(Arrays.toString(arr));
        }

        return Arrays.stream(arr).max().getAsLong();
   
    }


    public static void main (String [] args){

        List<List<Integer>> queries = List.of(List.of(1,5,3), List.of(4,8,7), List.of(6,9,1));

        long res = Result(10, queries);

        System.err.println(res);
    }
}

