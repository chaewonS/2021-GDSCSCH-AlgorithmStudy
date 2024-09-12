import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private void solve() {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            int N = Integer.parseInt(br.readLine());
            int sum = 0;
            for (int i = 1; i <= N; ++i) {
                sum = 0;
                if (i == 1000000) {
                    sum = 1000001;
                } else if (i >= 100000) {
                    sum += i;
                    sum += i / 100000;
                    sum += (i % 100000) / 10000;
                    sum += (i % 100000 % 10000) / 1000;
                    sum += (i % 100000 % 10000 % 1000) / 100;
                    sum += (i % 100000 % 10000 % 1000 % 100) / 10;
                    sum += (i % 100000 % 10000 % 1000 % 100) % 10;
                } else if (i >= 10000) {
                    sum += i;
                    sum += i / 10000;
                    sum += (i % 10000) / 1000;
                    sum += (i % 10000 % 1000) / 100;
                    sum += (i % 10000 % 1000 % 100) / 10;
                    sum += (i % 10000 % 1000 % 100) % 10;
                } else if (i >= 1000) {
                    sum += i;
                    sum += i / 1000;
                    sum += (i % 1000) / 100;
                    sum += (i % 1000 % 100) / 10;
                    sum += i % 1000 % 100 % 10;
                } else if (i >= 100) {
                    sum += i;
                    sum += i / 100;
                    sum += (i % 100) / 10;
                    sum += i % 100 % 10;
                } else if (i >= 10) {
                    sum += i;
                    sum += i / 10;
                    sum += i % 10;
                } else {
                    sum += (2*i);
                }

                if (sum == N) {
                    System.out.println(i);
                    return;
                }
            }
            System.out.println(0);

        }catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args){
        new Main().solve();
    }
}