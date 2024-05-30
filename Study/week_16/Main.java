import java.io.*;
import java.util.*;

public class Main {
    // 입력과 출력 설정
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws Exception {
        // 첫 번째 줄에서 N과 M을 입력받음
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());



        // 최종 결과 출력
        bw.write("" + "\n");

        // 입출력 닫기
        bw.flush();
        br.close();
        bw.close();
    }
}
