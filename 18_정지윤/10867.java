import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private void solve() {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            int N = Integer.parseInt(br.readLine());
            String[] s = br.readLine().split(" ");

            ArrayList<Integer> num = new ArrayList<>();

            boolean[] flag = new boolean[2001];

            for (int i = 0; i < N; ++i) {
                int n = Integer.parseInt(s[i]);

                if (n < 0 && !flag[n + 1000]) {
                    num.add(n);
                    flag[n + 1000] = true;
                    continue;
                }

                if (n >= 0 && !flag[n + 1000]) {
                    num.add(n);
                    flag[n + 1000] = true;
                }
            }

            Collections.sort(num);

            for (int i = 0; i < num.size(); ++i) {
                System.out.print(num.get(i) + " ");
            }

        }catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args){
        new Main().solve();
    }
}