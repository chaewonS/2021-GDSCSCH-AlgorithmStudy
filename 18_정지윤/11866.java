import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    private void solve() {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
            String[] s = br.readLine().split(" ");
            int N = Integer.parseInt(s[0]);
            int K = Integer.parseInt(s[1]);

            Queue<Integer> queue = new LinkedList<>();

            for (int i = 1; i <=N; ++i) {
                queue.offer(i);
            }

            System.out.print("<");
            while (queue.size() != 1) {

                for (int i = 1; i < K; ++i) {
                    int n = queue.poll();
                    queue.offer(n);
                }
                System.out.print(queue.poll() +", ");
            }

            System.out.print(queue.poll()+">");


        }catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args){
        new Main().solve();
    }
}