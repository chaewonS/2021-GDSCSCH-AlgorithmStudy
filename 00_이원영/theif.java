import java.util.*;

class Solution {
    public int solution(int[] money) {
        int[] arr0 = new int[money.length];
        int[] arr1 = new int[money.length];
        
        arr0[0] = arr0[1] = money[0];
        
        arr1[0] = 0;
        arr1[1] = money[1];
        
        for(int i=2; i<money.length-1; i++) {
            arr0[i] = Math.max(arr0[i-2]+money[i], arr0[i-1]);
            arr1[i] = Math.max(arr1[i-2]+money[i], arr1[i-1]);
        }
        
        
        int leng = money.length-1;
        arr1[leng] = Math.max(arr1[leng-2]+money[leng], arr1[leng-1]);
        
        return Math.max(arr0[leng-1], arr1[leng]);
    }
}
