import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    private void solve() {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            int N = Integer.parseInt(br.readLine());

            for (int i = 0; i < N; ++i) {
                String s[] = br.readLine().split(" ");
                StringBuilder sb = new StringBuilder();

                Stack<Character> stack = new Stack<>();

                for (int j = 0; j < s.length; ++j) {
                    for (int k = 0; k < s[j].length(); ++k) {
                        stack.push(s[j].charAt(k));
                    }

                    while (!stack.isEmpty()) {
                        sb.append(stack.pop());
                    }
                    sb.append(" ");
                }
                System.out.println(sb.toString());
            }

        }catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args){
        new Main().solve();
    }
}