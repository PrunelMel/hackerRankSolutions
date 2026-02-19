import java.util.*;
public class MinMax {
    
    public void minMaxSum(List<Integer> arr){


        Collections.sort(arr); //we sort the List

        List<Long> longs = arr.stream()
                       .map(Integer::longValue)
                       .toList();

        long min;

        long max;

        List<Long> minList;

        List<Long> maxList;
        
        minList = longs.subList(0, arr.size() - 1);
        
        maxList = longs.subList(arr.size() - 4, arr.size());
        
        max = maxList.stream().mapToLong(Long::longValue).sum();

        min = minList.stream().mapToLong(Long::longValue).sum();

        System.out.println("minList " + minList);
        System.out.println("maxList " + maxList);

        System.out.println(min + " " + max);

    }

    public static void main(String[] args) {
        
        MinMax minMax = new MinMax();
        
        List<Integer> arr;
        
        // arr.add(1);
        // arr.add(2);
        // arr.add(3);
        // arr.add(4);
        // arr.add(5);

        arr = Arrays.asList(793810624, 895642170, 685903712, 623789054, 468592370);
        
        minMax.minMaxSum(arr);
    }
}

class Solution {

}