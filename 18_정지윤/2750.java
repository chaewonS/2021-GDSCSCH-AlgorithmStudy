import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    private void solve() {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            int N = Integer.parseInt(br.readLine());
            Integer[] num = new Integer[N];

            for (int i = 0; i < N; ++i) {
                num[i] = Integer.parseInt(br.readLine());
            }

            Arrays.sort(num);

            for (int i = 0; i < N; ++i) {
                System.out.println(num[i]);
            }

        }catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args){
        new Main().solve();
    }
}