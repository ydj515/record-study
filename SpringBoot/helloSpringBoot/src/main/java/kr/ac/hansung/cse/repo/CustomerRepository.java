package kr.ac.hansung.cse.repo;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import kr.ac.hansung.cse.model.Customer;

public interface CustomerRepository extends CrudRepository<Customer, Long> { // interface로 구현해서 자동적으로 알아서 class(CRUD) 만들어줌

	List<Customer> findByLastName(String lastName);

}