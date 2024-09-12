import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	public static int N, M, answer;
	public static boolean[] visited;
	public static List<Integer>[] list;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		visited = new boolean[N];
		list = new ArrayList[N];
		
		for (int i = 0; i < N; ++i) {
			list[i] = new ArrayList<Integer>();
		}
		
		for (int i = 0; i < M; ++i) {
			st = new StringTokenizer(br.readLine());
			
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			
			list[from].add(to);
			list[to].add(from);
		}
		
		for (int i = 0; i < N; ++i) {
			go(i, 1);
			
			if (answer > 0) {
				break;
			}
		}
		
		System.out.println(answer);
	}
	
	public static void go(int cur, int cnt) {
		if (cnt == 5) {
			answer = 1;
			return;
		}
		
		visited[cur] = true;
		for (int next : list[cur]) {
			if (!visited[next]) {
				go(next, cnt + 1);
			}
		}
		visited[cur] = false;
	}
}
