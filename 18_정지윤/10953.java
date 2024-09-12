import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private void solve() {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            int T = Integer.parseInt(br.readLine());

            for (int i = 0; i < T; ++i) {
                String[] s = br.readLine().split(",");
                System.out.println(Integer.parseInt(s[0]) + Integer.parseInt(s[1]));
            }

        }catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args){
        new Main().solve();
    }
}