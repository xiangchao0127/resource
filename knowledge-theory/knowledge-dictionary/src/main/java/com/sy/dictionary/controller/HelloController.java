package com.sy.dictionary.controller;

import com.sy.dictionary.dao.EsDao;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author XiangChao
 * @date 2018/11/20
 */
@RestController
public class HelloController {
    final static Logger log = LoggerFactory.getLogger(HelloController.class);

    @Autowired
    EsDao esDao;
    @GetMapping("/hello")
    public String hello(String name){
        log.error(" 中文测试");
        System.out.println(esDao.findById("testdb","userinfo","cLf5LmcB2jJVoNBwh3vX"));
        return "通信成功！"+esDao.findById("testdb","userinfo","cLf5LmcB2jJVoNBwh3vX")+"/n"+name;
    }
}
