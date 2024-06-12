# Lock

## 낙관적 락 (Optimistic Lock)
데이터 충돌이 적을 때 사용. <br/>
데이터가 동시에 수정될 가능성이 낮은 경우 주로 사용 <br/>
데이터베이스에서 충돌이 발생할 가능성이 낮다고 가정하고, 실제로 충돌이 발생했을 때만 롤백을 수행 <br/>
주로 읽기 작업이 많고 쓰기 작업이 적은 도메인에 적합 <br/>
락을 걸지 않기 때문에 성능에 미치는 영향이 적음<br/>
병목현상이 적음<br/>
충돌이 발생하면 롤백 및 재시도가 필요하므로, 충돌이 자주 발생하면 오히려 성능이 저하될 수 있음<br/>
충돌을 처리하는 로직이 필요<br/>

### 예시 도메인
- 소셜 네트워크 서비스 (SNS) 게시물 <br/>
게시물 조회가 빈번하지만 수정은 적음. 조회는 빈번하지만 동일한 게시물을 동시에 수정하는 경우가 적음. <br/>

- 제품 카탈로그  <br/>
제품 정보 조회가 많고, 제품 정보 수정은 적음. 다수의 사용자가 제품을 검색하고 조회하는 경우가 많지만, 제품 정보 수정은 주로 관리자에 의해 이루어 짐으로 데이터가 동시에 수정될 가능성이 낮음.  <br/>

- 블로그 게시글  <br/>
게시글 조회는 많지만 수정은 적음. 작성된 블로그 게시글을 여러 사용자가 조회하는 경우가 많지만 동시에 수정하는 경우가 적음.  <br/>


## 비관적 락 (Pessimistic Lock)
데이터베이스 레벨에서 락을 걸어 동시성 문제를 방지<br/>
비관적 락은 데이터 충돌이 빈번하게 발생할 것으로 예상될 때 사용  <br/>
데이터가 동시에 수정될 가능성이 높은 경우 주로 사용  <br/>
데이터 일관성을 강하게 보장 <br/>
락을 걸기 때문에 성능에 영향을 미칠 수 있음<br/>
다른 트랜잭션이 해당 데이터에 접근하기 위해 대기해야 하므로 병목현상이 발생할 수 있음<br/>
주로 쓰기 작업이 많고 데이터 일관성이 중요한 도메인에 적합  <br/>


### 예시 도메인
- 은행 계좌 관리 시스템  <br/>
계좌 잔액을 조회하고 수정하는 작업이 동시에 발생할 수 있음. 하나의 계좌에 대해 여러 사용자가 동시에 입출금을 시도할 수 있기 때문에 데이터의 일관성을 유지하는 것이 중요.  <br/>

- 재고 관리 시스템  <br/>
재고 수량을 조회하고 수정하는 작업이 빈번하게 발생. 특히, 동시에 여러 주문이 들어올 수 있는 환경에서 문제 야기 <br/>

- 온라인 예약 시스템
동일한 자원(예: 항공편 좌석, 호텔 객실)을 여러 사용자가 동시에 예약하려고 시도할 수 있음. 따라서, 동일한 자원에 대한 중복 예약을 방지해야함 <br/>


## 분산 락(Distributed Lock)
분산 락은 여러 개의 노드로 구성된 분산 시스템에서 동시성 제어를 위해 사용되는 락 메커니즘. <br/>
여러 인스턴스가 동시에 동일한 자원에 접근하지 못하도록 하기 위해 사용. <br/>
분산 락은 일반적으로 `Redis`, `ZooKeeper`, `Etcd`와 같은 분산 시스템을 사용하여 구현. <br/>

### 분산 락의 특징

- 중앙 집중화된 락 관리 <br/>
락을 중앙에서 관리하여 여러 인스턴스가 동일한 락을 확인하고 사용할 수 있음. <br/>

- 동시성 제어 <br/>
여러 인스턴스가 동일한 자원에 동시에 접근하지 못하도록 막음. <br/>

- 신뢰성 <br/>
네트워크 문제나 서버 장애에도 락의 일관성을 유지. <br/>

- 타임아웃 <br/>
락이 너무 오래 유지되지 않도록 타임아웃을 설정하여 데드락(교착 상태)을 방지. <br/>

### redis를 활용한 분산락 처리
- Redisson <br/>
Redis를 사용하여 분산 락을 쉽게 구현할 수 있도록 돕는 라이브러리. <br/>
`pub/sub 방식`을 사용하며 Lock을 당장 획득할 수 없으면 대기하고, lock획득이 가능할 경우 redis에서 client로 lock 획득이 가능함을 알린다.<br/>
lock의 lease time이 설정 가능하여 lease time이 지난 경우 자동으로 lock 소유권을 회수하여 dead lock을 방지<br/>


- lectture <br/>
SETNX 명령을 활용한 스핀락 구현.<br/>
redis의 `SETNX`는 "SET if Not eXists" 명령으로 키가 존재하지 않을 때 값을 세팅하는 방법이다. 이를 통해 특정 키를 락으로 설정하고, 락이 이미 사용중이면 주기적으로 락을 획득하기 위해 요청하는 스핀락을 구현할 수 있다. <br/>
로직 실행 전에 lock을 걸고 로직 실행이 끝난 후 unlock을 수행<br/>
`스핀락`이란 Race Condition 상황에서 Lock이 반환될 때까지, 즉 Critical section(임계영역)에 진입 가능할 때까지 프로세스가 재시도하며 대기하는 상태. 쉽게 말해 `스레드가 락을 얻을 때까지 무한 루프를 돌며 확인하는 동기화 매커니즘`이다. <br/> <br/>
`Critical Section (임계 영역)`이란 여러 스레드 또는 프로세스가 공유 자원에 접근할 수 있는 코드 영역이다. 즉, 코드 상에서 Race condition (경쟁 상태)가 발생할 수 있는 곳으로, 둘 이상의 스레드가 동시에 접근하면 안되는 구역으로 아래의 코드에서는 count가 임계 영역이다.<br/>
```java
public class Counter {
	
  public int count; // 임계영역
  
  public synchronized void increase() {
    count++;
  }
  
  public synchronized void decrease() {
    count--;
  }
 
}
```

### lettuce 활용 예시
- gradle
dependency 추가
```
dependencies {
  implementation 'org.springframework.boot:spring-boot-starter-data-redis'
}
```

- RedisLockRepository
redistemplate을 활용한 lock/unlock 구현
```java
@Component
public class RedisLockRepository {

    private RedisTemplate<String, String> redisTemplate;

    public RedisLockRepository(RedisTemplate<String, String> redisTemplate) {
        this.redisTemplate = redisTemplate;
    }

    public Boolean lock(Long key) {
        return redisTemplate
                .opsForValue()
                .setIfAbsent(generateKey(key), "lock", Duration.ofMillis(3_000)); //setnx
    }

    public Boolean unlock(Long key) {
        return redisTemplate.delete(generateKey(key));
    }

    private String generateKey(Long key) {
        return key.toString();
    }
}
```

- LettuceLockStockFacade
lock을 획득할때까지 재시도하고 로직을 실행 후 unlock을 실행
```java
@Component
@RequiredArgsConstructor
public class LettuceLockStockFacade {

    private final RedisLockRepository redisLockRepository;

    private final StockService stockService;

    public void decrease(Long key, Long quantity) throws InterruptedException {
        while (!redisLockRepository.lock(key)) { // lock 획득할때까지 재시도. redis의 부하를 줄이기 위해 loop
            Thread.sleep(100);
        }

        try {
            stockService.decrease(key, quantity);
        } finally {
            redisLockRepository.unlock(key);
        }
    }
}
```

- test
100개의 thread로 동시성 테스트 진행
```java
@SpringBootTest
class LettuceLockStockFacadeTest {

    @Autowired
    private LettuceLockStockFacade lettuceLockStockFacade;

    @Autowired
    private StockRepository stockRepository;

    @BeforeEach
    public void insert() {
        Stock stock = new Stock(1L, 100L);

        stockRepository.saveAndFlush(stock);
    }

    @AfterEach
    public void delete() {
        stockRepository.deleteAll();
    }

    @DisplayName("동시에 재고를 감소시킨다.")
    @Test
    public void test() throws InterruptedException {
        int threadCount = 100;
        ExecutorService executorService = Executors.newFixedThreadPool(32);
        CountDownLatch latch = new CountDownLatch(threadCount);

        for (int i = 0; i < threadCount; i++) {
            executorService.submit(() -> {
                try {
                    lettuceLockStockFacade.decrease(1L, 1L);
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                } finally {
                    latch.countDown();
                }
            });
        }

        latch.await();

        Stock stock = stockRepository.findById(1L).orElseThrow();

        // 100 - (100 * 1) = 0
        assertEquals(0, stock.getQuantity());
    }
}
```

### redisson 활용 예시
redisson에 이미 구현되어있어서 repository는 따로 구현하지 않아도 됨.

- gradle
dependency 추가
```
dependencies {
  implementation 'org.redisson:redisson-spring-boot-starter:3.17.4'
}
```

- LettuceLockStockFacade
lock을 획득할때까지 재시도하고 로직을 실행 후 unlock을 실행
```java
@Component
@RequiredArgsConstructor
public class RedissonLockStockFacade {

    private final RedissonClient redissonClient;

    private final StockService stockService;

    public void decrease(Long key, Long quantity) {
        RLock lock = redissonClient.getLock(key.toString());

        try {
            boolean available = lock.tryLock(10, 1, TimeUnit.SECONDS);

            if (!available) {
                System.out.println("lock 획득 실패");
                return;
            }

            stockService.decrease(key, quantity);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        } finally {
            lock.unlock();
        }
    }
}
```

- test
100개의 thread로 동시성 테스트 진행
```java
@SpringBootTest
class RedissonLockStockFacadeTest {

    @Autowired
    private RedissonLockStockFacade redissonLockStockFacade;

    @Autowired
    private StockRepository stockRepository;

    @BeforeEach
    public void insert() {
        Stock stock = new Stock(1L, 100L);

        stockRepository.saveAndFlush(stock);
    }

    @AfterEach
    public void delete() {
        stockRepository.deleteAll();
    }

    @Test
    @DisplayName("동시에 재고를 감소시킨다.")
    public void test() throws InterruptedException {
        int threadCount = 100;
        ExecutorService executorService = Executors.newFixedThreadPool(32);
        CountDownLatch latch = new CountDownLatch(threadCount);

        for (int i = 0; i < threadCount; i++) {
            executorService.submit(() -> {
                try {
                    redissonLockStockFacade.decrease(1L, 1L);
                } finally {
                    latch.countDown();
                }
            });
        }

        latch.await();

        Stock stock = stockRepository.findById(1L).orElseThrow();

        // 100 - (100 * 1) = 0
        assertEquals(0, stock.getQuantity());
    }
}
```