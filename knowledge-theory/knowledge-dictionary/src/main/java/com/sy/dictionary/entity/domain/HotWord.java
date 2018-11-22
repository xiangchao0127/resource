package com.sy.dictionary.entity.domain;

import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;
import java.sql.Timestamp;

/**
 * Created with IDEA
 * author:lhang
 * Date:2018/11/21
 * Time:18:08
 */
@Data
@Entity
@Table(name = "hot_word")
public class HotWord {
    @Id
    @GeneratedValue
    private Integer id;
    private String keyWord;
    private String dictName;
    private Integer count;
    private Timestamp gmtCreate;
}
