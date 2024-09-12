import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    class Node {
        int data;
        int index;

        Node(int data, int index) {
            this.data = data;
            this.index = index;
        }
    }
    private void solve() {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
            int T = Integer.parseInt(br.readLine());

            for (int t = 0; t < T; ++t) {
                String[] s = br.readLine().split(" ");
                int N = Integer.parseInt(s[0]);  //배열 인덱스
                int M = Integer.parseInt(s[1]);  //찾을 인덱스의 번호
                int turn = 0;
                Queue<Node> queue = new LinkedList<>();
                s = br.readLine().split(" ");

                for (int i = 0; i < N; ++i) {
                    queue.offer(new Node(Integer.parseInt(s[i]), i));
                }

                while (!queue.isEmpty()) {
                    Node node = queue.poll();
                    int size = queue.size();
                    int max = 0;

                    for (int i = 0; i < size; ++i) {
                        Node n = queue.poll();

                        if (max < n.data) {
                            max = n.data;
                        }

                        queue.offer(n);
                    }

                    if (max > node.data) {
                        queue.offer(node);
                    } else {
                        turn++;

                        if (node.index == M) {
                            System.out.println(turn);
                            queue.clear();
                        }
                    }

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