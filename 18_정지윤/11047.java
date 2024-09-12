import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private void solve() {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            String[] s = br.readLine().split(" ");
            int N = Integer.parseInt(s[0]);
            int K = Integer.parseInt(s[1]);

            int[] money = new int[N];

            for (int i = 0;  i < N; ++i) {
                money[i] = Integer.parseInt(br.readLine());
            }

            N -= 1;
            int i = 0;

            for (i = 0; K != 0;) {
                if (K - money[N] >=0) {
                    K -= money[N];
                    ++i;
                } else {
                    N = N - 1;
                }
            }

            System.out.println(i);

        }catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args){
        new Main().solve();
    }
}