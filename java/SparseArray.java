import java.util.*;



public class SparseArray {


    public static List<Integer> matchingList(List<String> strings, List<String> queries) {

        List<Integer> answers = new ArrayList<>();
        
        for (String query : queries) {
            int count = 0;
            for (String string : strings) {
                if (string.equals(query)) {
                    count++;
                }
            }
            answers.add(count);
        }
        return answers;

    
    }

    

    public static void main(String[] args){

        System.out.println("hello");
    }
}
