package testHibernate;

import java.util.HashSet;
import java.util.Set;

import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.OneToMany;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Entity
public class Category {

	@Id
	@GeneratedValue
	private int id;
	
	private String name;
	
	// cascade=CascadeType.ALL : 연관된 객체까지 지우든 업데이트하든 같이 저장됨(persist, delete) -> product가 저장되면 연관된 Category도 자동 저장됨
	// mappedBy="category" : 필드 이름과 동일하게 넣으면 된다. 양방향 관계 설정시 관계의 주체가 되는 쪽에서 정의
	// fetch=FetchType.LAZY : Category 정보를 읽을 때 products의 모든 정보를 읽을 필요가 없다. 필요할 때만 읽는다. OneToMany, ManyToMany에선 default
	// fetch=FetchType.EAGER : Category 정보를 읽을 때 모든 product들의 정보를 읽는다. OneToOne, ManyToOne에선 default
	@OneToMany(mappedBy = "category", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
	private Set<Product> products = new HashSet<Product>();
	
}
