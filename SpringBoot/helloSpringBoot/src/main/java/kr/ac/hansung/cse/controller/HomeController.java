package kr.ac.hansung.cse.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

	static Logger logger = LoggerFactory.getLogger(HomeController.class);

	@GetMapping("/") // @RequestMapping(value="/", method = RequestMethod.GET)
	public String home(Model model) {

		logger.debug("Calling home( )");

		model.addAttribute("message", "hello world");
		return "index";

	}
}