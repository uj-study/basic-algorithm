package study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
	public static int a[];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		StringTokenizer s = new StringTokenizer(br.readLine());
		a = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = Integer.parseInt(s.nextToken());
		}
		Arrays.sort(a);
		int m = Integer.parseInt(br.readLine());
		int b[] = new int[m];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < m; i++) {
			b[i] = Integer.parseInt(st.nextToken());
		}

		for (int i = 0; i < m; i++) {
			// 찾고자 하는 값이 있을 경우 1, 없을 경우 0을 출력해야한다.
			if (binarySearch(b[i]) >= 0) {
				sb.append(1).append(' ');
			} else {
				sb.append(0).append(' ');
			}
		}
		System.out.println(sb);
	}

	/**
	 * @param key 찾으려는 값
	 * @return key와 일치하는 배열의 인덱스
	 */
	public static int binarySearch(int key) {

		int lo = 0; // 탐색 범위의 왼쪽 끝 인덱스
		int hi = a.length - 1; // 탐색 범위의 오른쪽 끝 인덱스

		// lo가 hi보다 커지기 전까지 반복한다.
		while (lo <= hi) {

			int mid = (lo + hi) / 2; // 중간위치를 구한다.

			// key값이 중간 위치의 값보다 작을 경우
			if (key < a[mid]) {
				hi = mid - 1;
			}
			// key값이 중간 위치의 값보다 클 경우
			else if (key > a[mid]) {
				lo = mid + 1;
			}
			// key값과 중간 위치의 값이 같을 경우
			else {
				return mid;
			}
		}

		// 찾고자 하는 값이 존재하지 않을 경우
		return -1;

	}

}
