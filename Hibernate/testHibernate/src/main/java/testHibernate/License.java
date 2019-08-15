package testHibernate;

import java.util.Date;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToOne;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Entity
public class License {

	@Id
	@GeneratedValue
	@Column(name = "license_id")
	private int id;

	private String licenseNumber;

	private Date issueDate;

	@OneToOne
	@JoinColumn(name = "person_id")
	private Person person;

}
