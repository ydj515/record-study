package testHibernate;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Entity
@Table(name = "Product") // table 이름 지정. 만약 안해주면 class 이름으로 table 생성
public class Product {

	@Id // record의 PK
	@GeneratedValue // 자동 생성
	@Column(name = "product_id") // column 이름 지정. 지정 안해줄 시 변수 이름과 동일하게 column 이름 생성
	private int id;

	private String name;
	private int price;
	private String description;

	@ManyToOne
	@JoinColumn(name = "category_id") // FK
	private Category category;

}
