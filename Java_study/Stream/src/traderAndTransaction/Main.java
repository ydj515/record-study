package traderAndTransaction;

import java.util.*;
import java.util.stream.*;

public class Main {

	public static void main(String[] args) {

		Trader raoul = new Trader("Raoul", "Cambridge");
		Trader mario = new Trader("Mario", "Milan");
		Trader alan = new Trader("Alan", "Cambridge");
		Trader brian = new Trader("Brian", "Cambridge");

		List<Transaction> transactions = Arrays.asList(
				new Transaction(brian, 2011, 300),
				new Transaction(raoul, 2012, 1000),
				new Transaction(raoul, 2011, 400),
				new Transaction(mario, 2012, 710),
				new Transaction(mario, 2012, 700),
				new Transaction(alan, 2012, 950)
				);

		System.out.println("===========================Question1=============================");
		// Question 1 : 2011년에 일어난 모든 트랜잭션을 찾아 값을 오름차순으로 정리하시오.
		transactions.stream().filter(i -> (i.getYear() == 2011))
					.sorted(Comparator.comparing(Transaction::getValue))
					.collect(Collectors.toList()).forEach(i -> {
						System.out.println(i);
					});

		System.out.println("===========================Question2=============================");
		// Question 2 : 거래자가 근무하는 모든 도시를 중복 없이 나열하시오.
		// filter로는 불가능.
		// filter는 boolean을 비교해서 해야하기때문에 map을 사용해야함
		transactions.stream().map(i -> i.getTrader().getCity())
					.distinct().collect(Collectors.toList()).forEach(i -> {
						System.out.println(i);
					});

		System.out.println("===========================Question3===============================");
		// Question 3 : 케임브리지에서 근무하는 모든 거래자를 찾아서 이름순으로 정렬하시오.
		// filter로만i -> i.getTrader().getCity().equals("Cambridge")로 비교하면 sorted를 사용할 시에
		// Trader::getName을 사용할 수 없다.
		// 왜냐면 filter 걸러진 i는 Transaction 타입의 stream이기 때문이다.
		// 따라서 map으로 한번 걸르고 stream 타입을 Trader로 바꿔주고 filter를 걸어야한다.
		transactions.stream().map(i -> i.getTrader()).filter(j -> j.getCity().equals("Cambridge"))
					.sorted(Comparator.comparing(Trader::getName))
					.collect(Collectors.toList()).forEach(i -> {
						System.out.println(i);
					});

		System.out.println("===========================Question4===============================");
		// Question 4 : 모든 거래자의 이름을 알파벳순으로 정렬해서 반환하시오.
		// Transaction 타입을 map을 사용하여 Trader로 변환 후 sort
		transactions.stream().map(i -> i.getTrader()).sorted(Comparator.comparing(Trader::getName))
					.collect(Collectors.toList()).forEach(i -> {
						System.out.println(i);
					});

		System.out.println("===========================Question5===============================");
		// Question 5 : 밀라노에 거래자가 있는가?
		// anyMatch를 사용
		// boolean을 return
		boolean a = transactions.stream().map(i -> i.getTrader()).anyMatch(j -> j.getCity().equals("Milan"));
		System.out.println(a);

		System.out.println("===========================Question6===============================");
		// Question 6 : 케임브리지에 거주하는 거래자의 모든 트랜잭션값을 출력하시오.
		// map 후 filter를 걸면 이 map으로 Trader타입으로 바뀌었기 때문에 forEach로 i.get할 수가 없다.( 출력하는 트랜잭션 값은 Transaction 타입이기 때문)
		transactions.stream().filter(i -> i.getTrader().getCity().equals("Cambridge")).collect(Collectors.toList())
					.forEach(i -> {
						System.out.println(i.getValue());
					});

		System.out.println("===========================Question7===============================");
		// Question 7 : 전체 트랜잭션 중 최댓값은 얼마인가?
		// Intstream 사용하면 트랜잭션의 value 비교가 어려움
		// mapToInt를 사용!!
		OptionalInt maxValue = transactions.stream().mapToInt(i -> i.getValue()).max();
		System.out.println(maxValue.getAsInt()); // OptionalInt를 int로 형 변환
		
		int maxValue2 = transactions.stream().map(transaction -> transaction.getValue()).reduce(0, Integer::max);
		System.out.println(maxValue2);

		System.out.println("===========================Question8===============================");
		// Question 8 : 전체 트랜잭션 중 최솟값은 얼마인가?
		OptionalInt minValue = transactions.stream().mapToInt(i -> i.getValue()).min();
		System.out.println(minValue.getAsInt()); // OptionalInt를 int로 형 변환

		Optional<Transaction> minValue2 = transactions.stream().min(Comparator.comparing(Transaction::getValue));
		minValue2.ifPresent(System.out::println); // 이렇게도 쓸 수 잇다는 걸 알려주기 위해서 함 써봄
		System.out.println(minValue2.get().getValue());
		
	}

}
