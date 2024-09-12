import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    int[] stack = new int[10000];
    int num = -1;

    void push(int X) {
        num++;
        stack[num] = X;
    }
    void pop() {
        if (num == -1) {
            System.out.println(-1);
        } else {
            int X = stack[num];
            num--;
            System.out.println(X);
        }
    }
    void size() {
        System.out.println(num + 1);
    }
    void empty() {
        if (num == -1) {
            System.out.println(1);
        } else{
            System.out.println(0);
        }
    }
    void top() {
        if (num == -1) {
            System.out.println(-1);
        } else {
            System.out.println(stack[num]);
        }
    }
    private void solve() {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
            int N = Integer.parseInt(br.readLine());
            String[] s;
            for (int i = 0; i < N; ++i) {
                s = br.readLine().split(" ");

                if (s[0].equals("push")) {
                    int X = Integer.parseInt(s[1]);
                    push(X);
                } else if (s[0].equals("pop")) {
                    pop();
                } else if (s[0].equals("size")) {
                    size();
                } else if (s[0].equals("empty")) {
                    empty();
                } else if (s[0].equals("top")){
                    top();
                }
            }
        }catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args){
        new Main().solve();
    }
}