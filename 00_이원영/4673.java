public class Main {

	public static void main(String[] args) {
		
		boolean selfNum = true; // 셀프 넘버를 구분하는 변수 선언
		
		for(int i=1; i<=10000; i++) {
			
			// j가 10000까지 돌아가는 동안 10000을 초과하는 수가 나오기 때문에 비효율적
			for(int j=1; j<=10000; j++) {
				// 셀프 넘버가 아니면 false 값을 대입, 반복문 중지
				if(i == d(j)) {
					selfNum = false; break;
				}
			}
			if(selfNum == true) {
				System.out.println(i); // 셀프 넘버이면 출력
			}
			selfNum = true; // 셀프 넘버 구분 초기화
		}
	}
	
	static int d(int n) {
		
		String str = Integer.toString(n);
		
		for(int i=0; i<str.length(); i++) {
			n += Integer.parseInt(str.substring(i, i+1));
		}
		
		return n;
	}
}
