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
 * Date:2018/11/22
 * Time:8:59
 */
@Data
@Entity
@Table(name = "language_pair")
public class LanguagePair {
    @Id
    @GeneratedValue
    private String id;
    private String chineseName;
    private String englishName;
    private Timestamp gmtCreate;
    private Timestamp gmtUpdate;
}
