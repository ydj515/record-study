package kr.ac.hansung.cse.controller;

import java.util.ArrayList;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import kr.ac.hansung.cse.model.Customer;
import kr.ac.hansung.cse.repo.CustomerRepository;

@RestController
@RequestMapping("/api")
public class CustomerController {

	static Logger logger = LoggerFactory.getLogger(CustomerController.class);

	@Autowired
	CustomerRepository repository; // DAO

	// Get All
	@GetMapping(value = "/customers", produces = MediaType.APPLICATION_JSON_VALUE) // Response Body가 Json Format이다. client에서 accept라는 header가 Json이라고 되어 있어야함
	public ResponseEntity<List<Customer>> getAll() {

		logger.debug("Calling getAll( )");

		List<Customer> list = new ArrayList<>();
		Iterable<Customer> customers = repository.findAll(); // CrudRepository interface에 정의된 findAll()

		customers.forEach(list::add);

		return new ResponseEntity<List<Customer>>(list, HttpStatus.OK);

	}

	// Create
	@PostMapping(value = "/customers")
	public ResponseEntity<Void> postCustomer(@RequestBody Customer customer) {

		logger.debug("Calling postCustomer( )");

		String firstName = customer.getFirstName();
		String lastName = customer.getLastName();

		repository.save(new Customer(firstName, lastName)); // Id를 저장하진 않지만 자동적으로 할당이 된다.

		return new ResponseEntity<Void>(HttpStatus.CREATED);
	}

	// Get
	@GetMapping(value = "/customers/{lastName}", produces = MediaType.APPLICATION_JSON_VALUE) // Response Body가 Json Format이다
	public ResponseEntity<List<Customer>> findByLastName(@PathVariable String lastName) {

		logger.debug("Calling findByLastName( )");

		List<Customer> customers = repository.findByLastName(lastName);
		return new ResponseEntity<List<Customer>>(customers, HttpStatus.OK); // customers를 body 부분에 붙힌다
	}

	// Delete
	@DeleteMapping(value = "/customers/{id}")
	public ResponseEntity<Void> deleteCustomer(@PathVariable long id) {

		logger.debug("Calling deleteCustomer( )");
		repository.delete(id);

		return new ResponseEntity<Void>(HttpStatus.NO_CONTENT);
	}
}