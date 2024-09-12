import javax.swing.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private void solve() {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            int N = Integer.parseInt(br.readLine());            //수의 개수 N은 홀수
            int[] number = new int[N];
            int[] turn = new int[8001];
            List<Integer> list = new ArrayList<>();

            int first, second, third = 0, forth;
            double sum = 0;

            for (int i = 0; i < N; ++i) {
                int num = Integer.parseInt(br.readLine());
                number[i] = num;
                sum += num;

                turn[4000+num]++;
            }

            first = (int)(Math.round(sum/N));//첫번째 출력

            Arrays.sort(number);
            second = number[N/2];//두번째 출력

            int max = 0;
            boolean flag = false;

            for(int i = 0; i < turn.length; i++) {
                if(turn[i] > max) {
                    max = turn[i];
                    third = i - 4000;
                    flag = true;
                } else if(turn[i] == max && flag == true) {
                    third = i - 4000;
                    flag = false;
                }
            }

            forth = number[N-1] - number[0];

            System.out.println(first);
            System.out.println(second);
            System.out.println(third);
            System.out.println(forth);

        }catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args){
        new Main().solve();
    }
}