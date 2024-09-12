import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        //StringTokenizer st = new StringTokenizer(br.readLine(), " ", false);

        int N = Integer.parseInt(br.readLine());

        int[] A = new int[N];
        st = new StringTokenizer(br.readLine(), " ", false);
        for (int i = 0; i<N;i++)
        {
            A[i] = Integer.parseInt(st.nextToken());
        }

        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine(), " ", false);
        for (int i = 0; i<M;i++)
        {
            int num = Integer.parseInt(st.nextToken());
            Boolean flag = false;
            for(int j = 0; j<N;j++) // 사실 ArrayList가 훨씬 쉽지만 배열을 요구하는 것 같아 배열탐색으로 풀이
            {
                if(num == A[j]) {
                    flag = true;
                    break;
                }
            }
            if (flag) bw.write("1 \n");
            else bw.write("0 \n");
        }


        br.close();
        bw.close();
    }
}
