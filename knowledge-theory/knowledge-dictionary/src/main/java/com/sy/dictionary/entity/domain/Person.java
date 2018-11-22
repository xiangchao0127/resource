package com.sy.dictionary.entity.domain;

import lombok.Data;

import javax.persistence.*;

/**
 * @author XiangChao
 * @date 2018/11/20
 */
@Entity
@Data
public class Person {
    @Id
    @GeneratedValue
    private Long id;
    /**
     * 名字
     */
    private String name;
//    @OneToMany(cascade = {CascadeType.PERSIST,CascadeType.ALL},fetch = FetchType.LAZY)
    private Integer age;
}
