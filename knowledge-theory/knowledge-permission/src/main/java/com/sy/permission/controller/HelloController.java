package com.sy.permission.controller;


import com.sy.permission.service.HelloService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author XiangChao
 * @date 2018/11/20
 */
@RestController
public class HelloController {
    final static Logger log = LoggerFactory.getLogger(HelloController.class);
    @Autowired
    HelloService helloService;
    @GetMapping("/hello")
    public void hello(@RequestParam(value = "name") String name){
        log.error(" 中文测试");
        System.out.println("nihaoaaaaa");
    }
    @GetMapping("/hello3")
    public String hello3(String name){
        return helloService.hello(name);
    }

}
