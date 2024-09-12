// 코테 준비 때문에 언어 변경 (python -> Java)

import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        int[] cnt = new int[26];

        for (int i = 0; i < str.length() ; i++) {
            int tmp = -1;
            tmp = str.charAt(i) <=90 ? str.charAt(i) - 65 : str.charAt(i) - 97;
            cnt[tmp] += 1;
        }

        boolean hasSameCnt = false;
        char alpa = 'A';
        int max = -1;
        for (int i  = 0; i<26;i++) {
            if (cnt[i] > max ) { 
                max = cnt[i];
                hasSameCnt = false;
                alpa = (char)(i+65);
            }
            else if (cnt[i] == max) hasSameCnt = true;
        }

        if (hasSameCnt) bw.write("?");
        else bw.write(alpa);
        bw.close();
    }
}
