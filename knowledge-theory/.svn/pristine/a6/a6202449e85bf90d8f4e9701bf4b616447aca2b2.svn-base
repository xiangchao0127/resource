package com.sy.permission.service;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

/**
 * Created with IDEA
 * author:lhang
 * Date:2018/11/21
 * Time:15:36
 */
@FeignClient(value="knowledge-dictionary",path="/")
public interface HelloService {

    @GetMapping("/hello")
    String hello(@RequestParam(value="name",required = false)String name);
}
