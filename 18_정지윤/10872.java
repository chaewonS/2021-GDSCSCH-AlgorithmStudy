import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private void solve() {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            int N = Integer.parseInt(br.readLine());
            int sum = N;

            if (N == 0) {
                System.out.println(1);
            }
            else {
                for (int i = N - 1; i >= 1; --i) {
                    sum = sum * i;
                }
                System.out.println(sum);
            }
        }catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args){
        new Main().solve();
    }
}